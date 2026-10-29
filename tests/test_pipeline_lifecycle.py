import importlib.util
from contextlib import nullcontext
from pathlib import Path
import sys
import socket
from types import SimpleNamespace
from unittest.mock import Mock

import pytest


@pytest.fixture
def pipeline():
    spec = importlib.util.spec_from_file_location("pipeline_subject", Path(__file__).parents[1] / "run_pipeline.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_unavailable_accelerators_fall_back_to_cpu(pipeline, monkeypatch):
    monkeypatch.setattr(pipeline.sys, "platform", "darwin")
    fake = SimpleNamespace(cuda=SimpleNamespace(is_available=lambda: False),
                           backends=SimpleNamespace(mps=SimpleNamespace(is_available=lambda: False)))
    monkeypatch.setitem(sys.modules, "torch", fake)
    assert pipeline.detect_device() == "cpu"


def test_open_socket_is_not_a_health_check(pipeline, monkeypatch):
    monkeypatch.setattr(pipeline.urllib.request, "urlopen", Mock(side_effect=OSError("wrong service")))
    monkeypatch.setattr(socket, "create_connection", Mock(return_value=nullcontext(object())))
    assert not pipeline.is_server_ready()


def test_failed_startup_stops_owned_process(pipeline, monkeypatch):
    child = Mock()
    child.poll.return_value = None
    monkeypatch.setattr(pipeline, "is_server_ready", lambda: False)
    monkeypatch.setattr(pipeline, "detect_device", lambda: "cpu")
    monkeypatch.setattr(pipeline.time, "sleep", lambda seconds: None)
    monkeypatch.setattr(pipeline.subprocess, "Popen", Mock(return_value=child))
    with pytest.raises(RuntimeError, match="ready"):
        pipeline.start_hybrid_server()
    child.terminate.assert_called_once()
    child.wait.assert_called_once()


def test_cli_failure_stops_only_owned_server(pipeline, monkeypatch):
    child = Mock()
    child.poll.return_value = None
    monkeypatch.setattr(pipeline, "start_hybrid_server", lambda: child)
    monkeypatch.setattr(pipeline, "run_conversion", Mock(side_effect=ValueError("conversion failed")))
    with pytest.raises(ValueError, match="conversion failed"):
        pipeline.main([])
    child.terminate.assert_called_once()


def test_cli_keeps_preexisting_server(pipeline, monkeypatch):
    monkeypatch.setattr(pipeline, "start_hybrid_server", lambda: None)
    convert = Mock()
    monkeypatch.setattr(pipeline, "run_conversion", convert)
    pipeline.main(["input", "output"])
    convert.assert_called_once_with("input", "output")
