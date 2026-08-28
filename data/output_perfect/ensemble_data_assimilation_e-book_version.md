# Ensemble Data Assimilation Applied to Geological Reservoir Models

Alexandre A. Emerick

![](<ensemble_data_assimilation_e-book_version_images/imageFile1.png>)

# Ensemble Data Assimilation Applied to Geological Reservoir Models

Alexandre A. Emerick

![](<ensemble_data_assimilation_e-book_version_images/imageFile2.png>)

# On the cover

Alexandre A. Emerick

# Cover design

María Julia Gouffier - Firjan-SENAI

First edition | 2025

© 2025 Alexandre A. Emerick

![](<ensemble_data_assimilation_e-book_version_images/imageFile1.png>)

This work is licensed under a Creative Commons Attribution–

NonCommercial 4.0 International License (CC BY-NC 4.0) ( https://creativecommons.org/licenses/by-nc/4.0 ). You are free to share (copy and redistribute the material in any medium or format) and adapt (transform and build upon the material), provided that you give appropriate credit, include a link to the license, and indicate if changes were made. Commercial use of the material is not permitted. Commercial reproduction of this work, including printed editions for sale, is reserved by the author. For commercial uses or permissions beyond the scope of this license, please contact: emerick@petrobras.com.br .

Calatogação na fonte Esther Rocha de Souza – CBR-7 6909  

# E53 Emerick, Alexandre A.

Ensemble data assimilation applied to geological reservoir models / Alexandre A. Emerick – Rio de Janeiro: PETROBRAS, 2025

420 p. : il. color. [recurso eletrônico].

Inclui bibliografias. ISBN 978-65-88763-29-2.

1. Modelos de reservatórios geológicos. 2. Assimilação de dados. 3. Dados dinâmicos. I. Emerick, Alexandre A. II. Título

CDD 550.285

After years of business and technological achievements, Petrobras has accumulated invaluable and unique knowledge. Part of this knowledge has been generated, transformed, and transmitted by our employees, who, throughout their professional careers, acquire specific and valuable technical expertise.

Recognizing the contributions and unique skills of our employees is essential. Retaining and disseminating acquired knowledge is equally important. This is the inspiration behind the Textbook Publishing Program ( Programa de Editoração de Livros Didáticos – PELD), which creates value for new employees, the market, and the academic community. We have published several titles, including both physical books and e-books.

Through PELD, Universidade Petrobras sponsors the entire publishing process, including printing a limited number of copies. This ensures that the published work can be used internally in training programs for new employees and continuous education while also allowing the author to distribute it in the publishing market. We are confident that this initiative enhances employee leadership and strengthens Petrobras as a generator and promoter of knowledge.

We hope that the publication in your hands, a product of PELD, contributes to your learning and continues driving the energy industry forward, delivering even more value to society. Join us on this journey!

![](<ensemble_data_assimilation_e-book_version_images/imageFile2.png>)

Ensemble Data Assimilation Applied to Geological Reservoir Models offers an in-depth examination of ensemble-based data assimilation methods for numerical modeling of geological reservoirs. Grounded in a Bayesian framework, the book emphasizes the integration of prior geological knowledge with dynamic data to enhance model predictions. A central focus is on iterative ensemble smoothers, particularly the Ensemble Smoother with Multiple Data Assimilation (ES-MDA), which has demonstrated effectiveness in real-world applications. The methods are presented with a balance of theoretical rigor and practical insights, featuring pseudo-codes and case studies to bridge theory and practice. This book is intended for researchers, students, and practitioners involved in reservoir characterization and management in diverse applications, including hydrocarbon production, groundwater hydrology, carbon capture and storage, and geothermal energy.

![](<ensemble_data_assimilation_e-book_version_images/imageFile3.png>)

Alexandre A. Emerick is a Senior Advisor at the Petrobras Research Center (CENPES) in Rio de Janeiro, with over 20 years of experience in applied research in reservoir engineering. His expertise includes reservoir simulation, data assimilation, uncertainty quantification, and optimization. Dr. Emerick has extensive experience in research, software development, training, and the application of ensemble data assimilation to petroleum reservoirs. He has authored numerous peer-reviewed papers on data assimilation and holds a Ph.D. in Petroleum Engineering from The University of Tulsa.

To Tatiana, my loving wife, whose unwavering support and belief in me have been my greatest source of strength. To Rafael and Gabriel, my dear sons, whose curiosity and joy inspire me every day. This book is for you.

# Foreword

Approximately fifteen years ago, Albert Reynolds, Ning Liu, and I published a book on the application of Bayesian inverse theory to history matching. We emphasized the benefits of highly parameterized reservoir models to reduce the effect of model error and better quantify uncertainty. As a consequence of the large number of model variables, minimization of the data mismatch was relatively difficult and typically required the solution of an adjoint system for gradient computation.

The book that Alex Emerick has written has the same general objective of parameter estimation and uncertainty quantification, but the methodology is generally much more computationally efficient and easier to implement. So, while much of the background material in the earlier book is still relevant today, ensemble-Kalman methods have revolutionized the practice of history matching, allowing practitioners to use highly parameterized models without the need for computing gradients. Dr Emerick describes in detail the evolution of the ensemble methods from the early attempts at direct application of the ensemble Kalman filter through the development of ensemble smoothers and iterative ensemble smoothers.

Despite the power of the methodology, there are many reasons that an application of an ensemble-based data assimilation to real-field history matching might fail to properly match data or quantify uncertainty, including omission of important parameters, inappropriate characterization of prior uncertainty, and failure to localize the updates. For practitioners whose only experience is with types of history matching that emphasize the need for parsimony, the importance of getting these aspects right may not be obvious. In this book, Dr Emerick explains thoroughly the “why” and then illustrates the “how” of each critical technique. By “how” I refer to things like the choice of important history-matching variables and the region of localization for updates. Making appropriate choices requires some insight into the physics of the problem, an understanding of the algorithms, and an understanding of the relationship between observations and reservoir model parameters. As the developer of the most popular algorithm for ensemble-based history

Bergen, Norway, November 2024

Dean S. Oliver

# Preface

I began my journey with ensemble methods during my PhD program at the University of Tulsa in 2008. I was fortunate to encounter these methods at a time when reservoir applications were still in their infancy. It was a period of intensive investigation and testing, during which the strengths and weaknesses of these approaches were gradually being understood. I’m proud to have contributed to the field and even prouder to have helped bridge the gap between academia and operational applications upon returning to Petrobras after completing my studies. At Petrobras, I had the unique opportunity to write ensemble-based codes, conduct initial field applications, deliver numerous training courses, and contribute to the gradual adoption of these methods within the company. After a decade of hands-on experience—working with reservoir engineers, geoscientists, graduate students, data scientists, and data assimilation experts, while also contributing through technical publications—I realized the need to document this journey, which ultimately led to this book.

Writing this book has been one of the most challenging yet rewarding experiences of my career. We often hear the saying, “ If you love what you do, you’ll never work a day in your life .” I’m not so sure about that. While I genuinely enjoyed writing this book, I can certainly attest that it required considerable effort! I’ve always aspired to create something that would benefit students, researchers, and practitioners. My goal was to strike a balance between theory and practice, ensuring the content is academically rigorous and applicable to real-world scenarios. I’m not sure I fully achieved that, but I certainly gave it my best effort!

It took me a few years to complete this book. I began by writing Chapters 4 and 5, which cover the EnKF and ES-MDA methods. While the EnKF is the most influential ensemble data assimilation technique, ES-MDA was specifically designed in the context of reservoir problems. After completing these chapters, I moved on to Chapter 7, which focuses on localization—a crucial component for ensuring the process works.

After completing the initial chapters, I began working on multiple sections simultaneously, trying to fill gaps and give the book a sense of completeness. Chapter 2, which provides the essential background needed to understand the developments throughout the book, was one of the last chapters I wrote, yet it became fundamental. Chapter 3 departs somewhat from ensemble methods, focusing on more traditional optimization-based data assimilation techniques. Initially, this chapter was intended to be an appendix, solely discussing classical methods based on derivative information. My goal in this discussion was to connect ensemble methods with Gauss-Newton. However, as the chapter expanded, I decided to include additional topics, such as proxy models and reduced parameterizations. Overall, I believe it nicely complements the scope of the book. Chapter 6 discusses other iterative ensemble smoothers. Along with ES-MDA, these methods represent the state of the art in reservoir data assimilation. Chapter 9 was particularly challenging to write. My goal was to discuss practical aspects and provide guidelines for the effective use of ensemble smoothers, something I believe is lacking in the current literature.

Additionally, the book includes four appendices that provide review material, making it easier for readers to follow the main text.

The book focuses on reservoir data assimilation, but I have aimed to keep the discussion broad enough to be useful for readers interested in ensemble methods beyond their application to geological reservoirs. That said, the examples throughout the book are drawn primarily from petroleum reservoirs, as this is my area of expertise. In other words, these are the examples I could provide most effectively based on my background.

This book is deeply influenced by the works of Professors Dean Oliver and Albert Reynolds. I have extensively studied Professor Oliver’s publications and regard him as the foremost authority in reservoir data assimilation. His thoughtful review of this book, along with his invaluable recommendations for improvement, significantly refined its content. I’m profoundly honored that he also wrote the foreword. Professor Reynolds, my PhD advisor, played a pivotal role in shaping my understanding of data assimilation while instilling the principles of effective research. Working with him was not only a distinct honor and privilege, but also an immense amount of fun.

I must also acknowledge the significant influence of Dr. Geir Evensen, the inventor of the EnKF, whose contributions have profoundly shaped the field. Additionally, I would like to recognize my colleagues from NORCE—Andreas Stordal, Geir Nævdal, Kristian Fossum, Patrick Raanes, Randi Valestrand, Rolf Lorentzen, Trond Mannseth, Xiaodong Luo, Yan Chen (TotalEnergies), and Remus Hanea (Equinor)—whose contributions and insights have greatly influenced my understanding of ensemble methods.

I would also like to acknowledge the invaluable contributions of my colleagues at Petrobras. Given the many individuals involved, it would be difficult to name everyone without risking unintentional omissions. However, I must express my deep gratitude to four dear friends: Euripedes Barsanulpho, Henrique Cotrim, Vinícius Silva, and Gilson Neto (now at Equinor).

Euripedes, Henrique, and Vinícius were instrumental in introducing ensemble methods at Petrobras. They not only supported me during the early applications but also believed in the potential of these methods at a time when skepticism prevailed. Gilson, one of the brightest individuals I have worked with, made critical contributions, particularly in the integration of 4D seismic data. I sincerely thank Daniel Miranda, Henrique Cotrim, José Roberto Rodrigues, and Marcos Vitor Machado for reviewing the book and granting their recommendation for its publication.

Finally, I must thank Petrobras for investing in my education and granting me permission to publish this work. I’m truly grateful to work at an organization that values both knowledge and its people.

Rio de Janeiro, Brazil, December 2024

Alexandre A. Emerick

# Contents

<table>
  <tr>
    &lt;th colspan="3"&gt;1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Geological Reservoirs . . . . . . . . . . . . . . . . . . . . . .</th>
    &lt;th&gt;. . . . . . . . . . . . 1 . . . . . . . . . . . . 1</th>
  </tr>
  <tr>
    &lt;td&gt;1.1.1</td>
    &lt;td&gt;Reservoir Models . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 2</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;. . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 4</td>
  </tr>
  <tr>
    &lt;td&gt;1.2 Uncertainty 1.3 Forward</td>
    &lt;td&gt;Problem . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 5</td>
  </tr>
  <tr>
    &lt;td&gt;1.4 Inverse</td>
    &lt;td&gt;Problem . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 8</td>
  </tr>
  <tr>
    &lt;td&gt;1.4.1 Data</td>
    &lt;td&gt;Assimilation . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 10</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Geostatistics . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 11</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Viewpoint . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 13</td>
  </tr>
  <tr>
    &lt;td&gt;1.5 Bayesian 1.6 Ensembles</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 14</td>
  </tr>
  <tr>
    &lt;td&gt;1.6.1</td>
    &lt;td&gt;Ensemble-Based Methods</td>
    &lt;td&gt;. . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 15</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Organization . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 16</td>
  </tr>
  <tr>
    &lt;td&gt;1.7 Book</td>
    &lt;td&gt;Book . . . . . . .</td>
    &lt;td&gt;Organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;16</td>
  </tr>
  <tr>
    &lt;td&gt;2 Bayesian</td>
    &lt;td&gt;Formulation of the</td>
    &lt;td&gt;Data Assimilation</td>
    &lt;td&gt;Problem . 19</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 19</td>
  </tr>
  <tr>
    &lt;td&gt;2.1 Introduction 2.2 Model</td>
    &lt;td colspan="2"&gt;Likelihood . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 20</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Maximum Likelihood</td>
    &lt;td&gt;Estimate . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 21</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Data and Model Errors</td>
    &lt;td&gt;I . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 22</td>
  </tr>
  <tr>
    &lt;td&gt;2.2.2 2.2.3 Linear</td>
    &lt;td&gt;Case. . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;a Posteriori . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 25 . . . . . . . . . . . . 26</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Linear Case. . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 28</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Nonlinear Case . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 35</td>
  </tr>
  <tr>
    &lt;td&gt;2.3.2 2.3.3 Data</td>
    &lt;td&gt;and Model Errors</td>
    &lt;td&gt;II . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 37</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Assimilation as a Sampling Problem . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 39</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Sampling in the Linear</td>
    &lt;td&gt;Case . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 40</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Sampling in the Nonlinear</td>
    &lt;td&gt;Case . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 47</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Markov Chain Monte</td>
    &lt;td&gt;Carlo . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 48</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Randomized Maximum</td>
    &lt;td&gt;Likelihood . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 50</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Examples . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 51</td>
  </tr>
  <tr>
    &lt;td&gt;2.5 Normalized</td>
    &lt;td colspan="2"&gt;Objective Function . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 56</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th colspan="3"&gt;3 Optimization Methods for Data Assimilation 3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</th>
    &lt;th&gt;. . . . . . . . . . . . 61 . . . . . . . . . . . . 61</th>
  </tr>
  <tr>
    &lt;td&gt;3.2 Derivative-Based</td>
    &lt;td colspan="2"&gt;Methods . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 62</td>
  </tr>
  <tr>
    &lt;td&gt;3.2.1</td>
    &lt;td colspan="2"&gt;Steepest Descent Method . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 62</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Nonlinear Conjugate</td>
    &lt;td&gt;Gradient Method .</td>
    &lt;td&gt;. . . . . . . . . . . . 64</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Newton’s Method . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 65</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Gauss-Newton . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 66</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Levenberg-Marquardt</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 67</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Quasi-Newton. . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 68</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Scaling . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 70</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Comments on Line</td>
    &lt;td&gt;Search . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 71</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Comments on Gradient</td>
    &lt;td&gt;and Sensitivity</td>
    &lt;td&gt;Calculation . . 71</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Optimization</td>
    &lt;td&gt;Methods . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 73</td>
  </tr>
  <tr>
    &lt;td&gt;3.3 Stochastic 3.3.1</td>
    &lt;td colspan="2"&gt;Evolutionary Algorithms . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 74</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Particle Swarm</td>
    &lt;td&gt;Optimization . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 76</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Simulated Annealing .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 77</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Derivative-Free</td>
    &lt;td&gt;Optimization Methods .</td>
    &lt;td&gt;. . . . . . . . . . . . 78</td>
  </tr>
  <tr>
    &lt;td&gt;3.4 Other 3.5 Methods</td>
    &lt;td colspan="2"&gt;Based on Proxy Modeling . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 79</td>
  </tr>
  <tr>
    &lt;td&gt;3.5.1</td>
    &lt;td colspan="2"&gt;Design of Experiments . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 79</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Standard Proxy Models</td>
    &lt;td&gt;. . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 80</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Other Frequently-Adopted</td>
    &lt;td&gt;Proxy Models</td>
    &lt;td&gt;. . . . . . . . . . . 86</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Analysis . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 87</td>
  </tr>
  <tr>
    &lt;td&gt;3.6.1</td>
    &lt;td colspan="2"&gt;Sensitivity Analysis Based on Monte Carlo</td>
    &lt;td&gt;Simulations 88</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Parametrization . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 91</td>
  </tr>
  <tr>
    &lt;td&gt;3.7.1</td>
    &lt;td colspan="2"&gt;Zonation . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 93</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Pilot Point . . . . . . . . . Gradual Deformation</td>
    &lt;td&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 94 . . . . . . . . . . . . 95</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Parametrizations Based</td>
    &lt;td&gt;on PCA . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 96</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Parametrizations Based</td>
    &lt;td&gt;on Data Sensitivity</td>
    &lt;td&gt;. . . . . . . . . 99</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Parametrizations for</td>
    &lt;td&gt;Facies . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 100</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Parametrizations for</td>
    &lt;td&gt;Complex Geological</td>
    &lt;td&gt;Models . . . . 101</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Big-Loop Parametrization</td>
    &lt;td&gt;. . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 101</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;3.7.7</td>
    &lt;td&gt;Parametrizations for Complex Geological Models . . .</td>
    &lt;td&gt;101</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Kalman Filter . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 103</td>
  </tr>
  <tr>
    &lt;td colspan="3"&gt;4 Ensemble 4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 103</td>
  </tr>
  <tr>
    &lt;td&gt;4.2 Kalman</td>
    &lt;td colspan="2"&gt;Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 104</td>
  </tr>
  <tr>
    &lt;td&gt;4.2.1</td>
    &lt;td colspan="2"&gt;Kalman Filter as a Minimum Variance</td>
    &lt;td&gt;Estimator . . . . 106</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Kalman Filter as a</td>
    &lt;td&gt;Bayesian Estimator .</td>
    &lt;td&gt;. . . . . . . . . . . . 114</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Sequential Data</td>
    &lt;td&gt;Assimilation . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 119</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Kalman Filter . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 121</td>
  </tr>
  <tr>
    &lt;td&gt;4.3 Ensemble 4.3.1</td>
    &lt;td colspan="2"&gt;Perturbed Observations . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 125</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Ensemble-Based</td>
    &lt;td&gt;Covariance. . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 127</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Parameters-State</td>
    &lt;td&gt;Consistency . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 131</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Coupling EnKF with</td>
    &lt;td&gt;a Reservoir Simulator</td>
    &lt;td&gt;. . . . . . . . . 132</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Filter Divergence . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 135</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Ensemble Square Root</td>
    &lt;td&gt;Filters . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 136</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;5 Ensemble 5.1 Introduction</th>
    &lt;th colspan="3"&gt;Smoother with Multiple Data Assimilation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</th>
    &lt;th&gt;. . . . 139 . . . . . . . . 139</th>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="3"&gt;Ensemble Smoother . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 140</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="3"&gt;Ensemble Smoother with Multiple Data Assimilation.</td>
    &lt;td&gt;. . . . . . 142</td>
  </tr>
  <tr>
    &lt;td&gt;5.3 5.3.1</td>
    &lt;td colspan="3"&gt;MDA for the Linear Case . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 143</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;MDA from</td>
    &lt;td&gt;Bayes’ Rule . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 147</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;MDA from</td>
    &lt;td&gt; </td>
    &lt;td&gt;Nonlinear Least-Squares.</td>
    &lt;td&gt;. . . . 150</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Examples . . .</td>
    &lt;td&gt;Regularized . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 152</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;How Many Data</td>
    &lt;td&gt;Assimilations?</td>
    &lt;td&gt;. . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 156</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Deterministic</td>
    &lt;td&gt; </td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 168</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;5.3.6</td>
    &lt;td&gt; </td>
    &lt;td&gt;Deterministic ES-MDA. . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;168</td>
  </tr>
  <tr>
    &lt;td&gt;6 Iterative</td>
    &lt;td colspan="3"&gt;Ensemble Smoothers . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 175</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="3"&gt;Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 175</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Ensemble Randomized LM-EnRML .</td>
    &lt;td colspan="2"&gt;Maximum Likelihood . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 175 . . . . . . . . 178</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Ensemble Smoother . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 182</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Subspace Iterative</td>
    &lt;td colspan="2"&gt;Subspace Iterative Ensemble Smoother . .</td>
    &lt;td&gt;182</td>
  </tr>
  <tr>
    &lt;td&gt;7 Sampling</td>
    &lt;td colspan="3"&gt;Errors and Rank Deficiency . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 187</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Introduction . . . . . . .</td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 187</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Deficiency . . . .</td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 188</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Porosity and Permeability of a Rock</td>
    &lt;td&gt;Sample 189</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Example: Spurious Correlations</td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 190</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt;Porosity and</td>
    &lt;td&gt;Permeability of a Rock</td>
    &lt;td&gt;Sample 190</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt;Porosity Distribution</td>
    &lt;td&gt;in a Core</td>
    &lt;td&gt;Sample . . . . 194</td>
  </tr>
  <tr>
    &lt;td&gt;7.3.2 7.4 Covariance</td>
    &lt;td colspan="3"&gt;Example: Inflation . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 194</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Localization . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 196</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt;Correlation . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 197</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Degrees of</td>
    &lt;td&gt; </td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 198</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt;Localization Dependent</td>
    &lt;td&gt;. . . . . . . . . . . . . . Localization . . . . . .</td>
    &lt;td&gt;. . . . . . . . 200 . . . . . . . . 207</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt;Localization . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 214</td>
  </tr>
  <tr>
    &lt;td&gt;7.5.5</td>
    &lt;td colspan="3"&gt;Domain</td>
    &lt;td&gt;217</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="3"&gt;Implementation of the Analysis . .</td>
    &lt;td&gt;. . . . . . . . 217</td>
  </tr>
  <tr>
    &lt;td&gt;8 Computational 8.1 Introduction</td>
    &lt;td colspan="3"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 217</td>
  </tr>
  <tr>
    &lt;td&gt;8.2 Analysis</td>
    &lt;td colspan="3"&gt;in Matrix Form . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 218</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="3"&gt;Inversion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="3"&gt;Pseudoinverse . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 219 . . . . . . . . 220</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Subspace</td>
    &lt;td&gt;Inversion . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 221</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;8.3.3</td>
    &lt;td&gt; </td>
    &lt;td&gt;Pseudoinverse</td>
    &lt;td&gt;. . . . . . . . 224</td>
  </tr>
  <tr>
    &lt;td&gt;8.3.3 8.3.4</td>
    &lt;td&gt; </td>
    &lt;td&gt;Sherman-Morrison-Woodbury of Singular Values</td>
    &lt;td&gt;. . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . 225</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt;. . . . . . . . . . .</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Example: Parallelization of the</td>
    &lt;td&gt;Analysis . . . .</td>
    &lt;td&gt;. . . . . . . . 229</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th colspan="3"&gt;9 Practical Aspects and Field Examples . . . . .</th>
    &lt;th&gt;231</th>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Aspects and Field Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 231 . . . . . . . . . . . . 231</td>
  </tr>
  <tr>
    &lt;td&gt;9.1 Introduction 9.2 Parametrization</td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 231</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Realizations versus</td>
    &lt;td&gt;Scenarios to Describe</td>
    &lt;td&gt;Uncertainty 232</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Integrated Workflows</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 234</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Main Types of Reservoir</td>
    &lt;td&gt;Parameters . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 234</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Structural Parameters</td>
    &lt;td&gt;. . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 243</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Data . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 243</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Production Data . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 243</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;4D Seismic Data . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 252</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Other Data . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 255</td>
  </tr>
  <tr>
    &lt;td&gt;9.3.3 9.4 Results</td>
    &lt;td colspan="2"&gt;Evaluation. . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 259</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Example: Non-Representative</td>
    &lt;td&gt;Priors . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 260</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Prior Observation</td>
    &lt;td&gt;Coverage and Mean</td>
    &lt;td&gt;Squared Error 261</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Plausibility of the</td>
    &lt;td&gt;Posterior Realizations</td>
    &lt;td&gt;. . . . . . . . . . . 265</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Data-Mismatch Objective</td>
    &lt;td&gt;Function . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 269</td>
  </tr>
  <tr>
    &lt;td&gt;9.5 Field 9.5.1 Field</td>
    &lt;td&gt;Examples . . . . . . . . . . . 1 . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 270 . . . . . . . . . . . . 271</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Field 2 . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 275</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Field 3 . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 282</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Models . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 287</td>
  </tr>
  <tr>
    &lt;td&gt;9.6 Representative</td>
    &lt;td&gt; </td>
    &lt;td&gt;Representative Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;287</td>
  </tr>
  <tr>
    &lt;td&gt;A Elements of</td>
    &lt;td colspan="2"&gt;Linear Algebra . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 289</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 289</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 290</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;and Matrix Calculus . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 294</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Value Decomposition . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 297</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 298</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Range, Null Space and Rank . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 299</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Poor Conditioning . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 300</td>
  </tr>
  <tr>
    &lt;td&gt;A.6 Square</td>
    &lt;td colspan="2"&gt;Root of a Matrix . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 300</td>
  </tr>
  <tr>
    &lt;td&gt;B Elements of</td>
    &lt;td colspan="2"&gt;Linear Inverse Problems . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 303</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Linear Problems . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 303</td>
  </tr>
  <tr>
    &lt;td&gt;B.1 Discrete B.2 Ill-Posed</td>
    &lt;td colspan="2"&gt;Problems . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 304</td>
  </tr>
  <tr>
    &lt;td&gt;B.3 Classification</td>
    &lt;td colspan="2"&gt;of Linear Inverse Problems . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 304</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;for Discrete Linear Inverse Problems</td>
    &lt;td&gt;. . . . . . . . . . . . 305</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Least Squares . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 305</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Weighted Least Squares</td>
    &lt;td&gt;. . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 306</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Constrained Least</td>
    &lt;td&gt;Squares . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 307</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Regularized Least</td>
    &lt;td&gt;Squares . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 308</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Tikhonov Regularization</td>
    &lt;td&gt;. . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 309</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;SVD Solution . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 310</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th colspan="3"&gt;C Elements of Probability and Geostatistics . . . . C.1 Basic Concepts . . . . . . . . . . . . . . . . . . . . . . . . . . . .</th>
    &lt;th&gt;. . . . . . . . . . . . 315 . . . . . . . . . . . . 315</th>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Random Variables . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 315</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Probability Mass</td>
    &lt;td&gt;Function . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 315</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Probability Density</td>
    &lt;td&gt;Function . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 316</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Cumulative Density</td>
    &lt;td&gt;Function . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 316</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Joint Probability . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 316</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Marginal PDF . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 317</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Conditional PDF . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 317</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;The Chain Rule of</td>
    &lt;td&gt;Conditional Probabilities</td>
    &lt;td&gt;. . . . . . . . 317</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt;. . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 318</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Expected Value . . . Independent Random</td>
    &lt;td&gt;Variables . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 318</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Variance . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 319</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Covariance . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 320</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Correlation Coefficient . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 320</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Covariance Matrix . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 320</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Ensemble Estimators . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 321</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 322</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Mean Square Error . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 322</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Typical Distributions . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 323</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 329</td>
  </tr>
  <tr>
    &lt;td&gt;C.2 Likelihood C.2.1</td>
    &lt;td colspan="2"&gt;Maximum Likelihood Estimation . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 329</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Rule . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 329</td>
  </tr>
  <tr>
    &lt;td&gt;C.3 Bayes’ C.4 Geostatistics</td>
    &lt;td&gt; </td>
    &lt;td&gt;. . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 331</td>
  </tr>
  <tr>
    &lt;td&gt;C.4.1</td>
    &lt;td&gt; </td>
    &lt;td&gt;. . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 331</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Stationarity . . . . . . Transformation of</td>
    &lt;td&gt;Variables . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 331</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Variogram . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 333</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Kriging . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 334</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Geostatistical Simulation</td>
    &lt;td&gt;. . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 335</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Geostatistical Simulation</td>
    &lt;td&gt;of Facies . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 335</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;Beyond Covariance-Based</td>
    &lt;td&gt;Models . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 336</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;C.4.7</td>
    &lt;td&gt;Beyond Covariance-Based Models . . . . . . . . .</td>
    &lt;td&gt;336</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt;. . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;D Brief Literature D.1 Introduction</td>
    &lt;td colspan="2"&gt;Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 339 . . . . . . . . . . . . 339</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;and Its Variants . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 339</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;EnKF to Iterative ES .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 341</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 343</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Errors . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 345</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 346</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Data Assimilation . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 347</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Inversion . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 348</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Kalman Inversion . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 349</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Optimization . . . . . . . . . . . . . . .</td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Methods in Multimodal</td>
    &lt;td&gt;. . . . . . . . . . . . 349 Distributions . . . . . 350</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Applications . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 351</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td colspan="2"&gt;Petroleum Reservoirs . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . 351</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;D.12.2 Groundwater Hydrology</th>
    &lt;th&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . 352</th>
  </tr>
  <tr>
    &lt;td&gt;D.12.3 Geological Carbon D.12.4 Geothermal Energy . .</td>
    &lt;td&gt;Storage. . . . . . . . . . . . . . . . . . . . . . . . 354 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354</td>
  </tr>
  <tr>
    &lt;td&gt;D.12.5 Seismic Inversion . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . 355</td>
  </tr>
  <tr>
    &lt;td&gt;D.12.5 Seismic Inversion . . . . . . . . .</td>
    &lt;td&gt;355</td>
  </tr>
  <tr>
    &lt;td&gt;References . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . 357</td>
  </tr>
  <tr>
    &lt;td&gt;Index . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
    &lt;td&gt;. . . . . . . . . . . . . . . . . . . . . . . . . . . . 397</td>
  </tr>
</table>


# Symbols

# Integers

<table>
  <tr>
    &lt;th&gt;N d Number of data Number of data</th>
    &lt;th&gt;points points at time step</th>
  </tr>
  <tr>
    &lt;td&gt;N n Number of model</td>
    &lt;td&gt;t n parameters</td>
  </tr>
  <tr>
    &lt;td&gt;N m Number of scalar</td>
    &lt;td&gt;model parameters</td>
  </tr>
  <tr>
    &lt;td&gt;N m,s Number of ensemble</td>
    &lt;td&gt;members (ensemble size)</td>
  </tr>
  <tr>
    &lt;td&gt;N e Number of retained</td>
    &lt;td&gt;singular values</td>
  </tr>
  <tr>
    &lt;td&gt;N r Number of samples</td>
    &lt;td&gt;Number of retained singular values</td>
  </tr>
  <tr>
    &lt;td&gt;N s Number of time</td>
    &lt;td&gt;steps</td>
  </tr>
  <tr>
    &lt;td&gt;N t</td>
    &lt;td&gt;Number of time steps</td>
  </tr>
</table>


# Scalars

<table>
  <tr>
    &lt;th&gt;c Compressibility, or normalizing c Coefficient of the wetting</th>
    &lt;th&gt;constant, or covariance value phase for capillary pressure calculation</th>
  </tr>
  <tr>
    &lt;td&gt;1 c 2 Coefficient of the non-wetting</td>
    &lt;td&gt;phase for capillary pressure calcu-</td>
  </tr>
  <tr>
    &lt;td&gt;lation</td>
    &lt;td&gt;Coefficient of the non-wetting phase for capillary pressure calcu- lation</td>
  </tr>
  <tr>
    &lt;td&gt;e i Corey exponent for relative</td>
    &lt;td&gt;permeability calculation of phase i</td>
  </tr>
  <tr>
    &lt;td&gt;e p1 Wetting phase exponent for</td>
    &lt;td&gt;capillary pressure calculation</td>
  </tr>
  <tr>
    &lt;td&gt;e p2 Non-wetting phase exponent</td>
    &lt;td&gt;for capillary pressure calculation</td>
  </tr>
  <tr>
    &lt;td&gt;E i LET parameter for relative</td>
    &lt;td&gt;permeability calculation of phase i</td>
  </tr>
  <tr>
    &lt;td&gt;g Acceleration due to gravity</td>
    &lt;td&gt;Acceleration due to gravity</td>
  </tr>
  <tr>
    &lt;td&gt;h Distance</td>
    &lt;td&gt;Distance</td>
  </tr>
  <tr>
    &lt;td&gt;L Correlation or critical length</td>
    &lt;td&gt;Correlation or critical length</td>
  </tr>
  <tr>
    &lt;td&gt;L i LET parameter for relative</td>
    &lt;td&gt;permeability calculation of phase i</td>
  </tr>
  <tr>
    &lt;td&gt;t Time</td>
    &lt;td&gt;Time</td>
  </tr>
  <tr>
    &lt;td&gt;p Pressure</td>
    &lt;td&gt;Pressure</td>
  </tr>
  <tr>
    &lt;td&gt;p c Capillary pressure</td>
    &lt;td&gt;Capillary pressure</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;q Source or sink term of mass r Localization coefficient</th>
    &lt;th&gt;Source or sink term of mass</th>
  </tr>
  <tr>
    &lt;td&gt;s Fluid saturation</td>
    &lt;td&gt;Localization coefficient</td>
  </tr>
  <tr>
    &lt;td&gt;s n i Normalized saturation for</td>
    &lt;td&gt;phase i</td>
  </tr>
  <tr>
    &lt;td&gt;s w,con Connate water saturation</td>
    &lt;td&gt;Normalized saturation for phase i</td>
  </tr>
  <tr>
    &lt;td&gt;s w,cr Critical water saturation Residual oil saturation at</td>
    &lt;td&gt;oil-water table</td>
  </tr>
  <tr>
    &lt;td&gt;s o,rw T Temperature parameter in</td>
    &lt;td&gt;simulated annealing</td>
  </tr>
  <tr>
    &lt;td&gt;T i LET parameter for relative</td>
    &lt;td&gt;permeability calculation of phase i</td>
  </tr>
  <tr>
    &lt;td&gt;w Weight</td>
    &lt;td&gt;LET parameter for relative permeability calculation of phase i</td>
  </tr>
  <tr>
    &lt;td&gt;α ES-MDA inflation coefficient</td>
    &lt;td&gt;or regularization coefficient in an</td>
  </tr>
  <tr>
    &lt;td&gt;inverse problem Step size in derivative-based</td>
    &lt;td&gt;methods, or sum of the inverse in-</td>
  </tr>
  <tr>
    &lt;td&gt;β flation coefficients in ES-MDA</td>
    &lt;td&gt;Step size in derivative-based methods, or sum of the inverse in- flation coefficients in ES-MDA</td>
  </tr>
  <tr>
    &lt;td&gt;γ Correction coefficient (varies</td>
    &lt;td&gt;depending on the context)</td>
  </tr>
  <tr>
    &lt;td&gt;κ Permeability</td>
    &lt;td&gt;Permeability</td>
  </tr>
  <tr>
    &lt;td&gt;κ r i Relative permeability of phase</td>
    &lt;td&gt;i</td>
  </tr>
  <tr>
    &lt;td&gt;κ r i, max Maximum relative permeability λ Eigenvalue, Levenberg-Marquadt</td>
    &lt;td&gt;of phase i parameter, or Lagrange multi-</td>
  </tr>
  <tr>
    &lt;td&gt;pliers</td>
    &lt;td&gt;Viscosity</td>
  </tr>
  <tr>
    &lt;td&gt;µ Viscosity</td>
    &lt;td&gt;Gradual deformation parameter</td>
  </tr>
  <tr>
    &lt;td&gt;ν Gradual deformation parameter</td>
    &lt;td&gt;Retained singular value energy</td>
  </tr>
  <tr>
    &lt;td&gt;ξ Retained singular value energy</td>
    &lt;td&gt;Fluid density or correlation coefficient</td>
  </tr>
  <tr>
    &lt;td&gt;ρ Fluid density or correlation σ Singular value or standard</td>
    &lt;td&gt;coefficient deviation</td>
  </tr>
  <tr>
    &lt;td&gt;σ e Data-error standard deviation</td>
    &lt;td&gt;Data-error standard deviation</td>
  </tr>
  <tr>
    &lt;td&gt;σ pr Prior standard deviation</td>
    &lt;td&gt;Prior standard deviation</td>
  </tr>
  <tr>
    &lt;td&gt;σ post Posterior standard deviation</td>
    &lt;td&gt;Posterior standard deviation</td>
  </tr>
  <tr>
    &lt;td&gt;τ Localization threshold Optimal hard threshold of</td>
    &lt;td&gt;singular values</td>
  </tr>
  <tr>
    &lt;td&gt;τ ∗ υ BFGS coefficient</td>
    &lt;td&gt;Optimal hard threshold of singular values</td>
  </tr>
  <tr>
    &lt;td&gt;φ Porosity</td>
    &lt;td&gt;BFGS coefficient</td>
  </tr>
  <tr>
    &lt;td&gt;ω Coefficient to compute the</td>
    &lt;td&gt;optimal hard threshold of singular</td>
  </tr>
  <tr>
    &lt;td&gt;values</td>
    &lt;td&gt;Coefficient to compute the optimal hard threshold of singular values</td>
  </tr>
</table>


# Vectors

<table>
  <tr>
    &lt;th&gt;d Predicted data d Observed data</th>
    &lt;th&gt;(dimension N d ) (dimension )</th>
  </tr>
  <tr>
    &lt;td&gt;obs d Noiseless data</td>
    &lt;td&gt;N d (dimension )</td>
  </tr>
  <tr>
    &lt;td&gt;true e Data error</td>
    &lt;td&gt;N d (dimension )</td>
  </tr>
  <tr>
    &lt;td&gt;e Measurement</td>
    &lt;td&gt;N d error (dimension )</td>
  </tr>
  <tr>
    &lt;td&gt;d e Model error</td>
    &lt;td&gt;N d (dimension )</td>
  </tr>
  <tr>
    &lt;td&gt;g</td>
    &lt;td&gt;N d</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;e y Model error in the state m Model parameters (dimension</th>
    &lt;th&gt;(dimension N y ) N )</th>
  </tr>
  <tr>
    &lt;td&gt;m c Conditional (posterior) model</td>
    &lt;td&gt;m parameters (dimension N m )</td>
  </tr>
  <tr>
    &lt;td&gt;m ml Maximum likelihood estimate</td>
    &lt;td&gt;(dimension N m )</td>
  </tr>
  <tr>
    &lt;td&gt;m map MAP estimate (dimension m Prior estimate (dimension</td>
    &lt;td&gt;N m ) )</td>
  </tr>
  <tr>
    &lt;td&gt;pr m true Ground truth for the vector</td>
    &lt;td&gt;N m of the model parameters (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N m )</td>
    &lt;td&gt;Prior estimate (dimension N m )</td>
  </tr>
  <tr>
    &lt;td&gt;p Gradient change for BFGS</td>
    &lt;td&gt;(dimension N m )</td>
  </tr>
  <tr>
    &lt;td&gt;q Model change for BFGS s Search direction (derivative-based</td>
    &lt;td&gt;(dimension N m ) methods)</td>
  </tr>
  <tr>
    &lt;td&gt;u Model controls, left singular</td>
    &lt;td&gt;vector, or coordinate position (in</td>
  </tr>
  <tr>
    &lt;td&gt;Geostatistics)</td>
    &lt;td&gt;Search direction (derivative-based methods)</td>
  </tr>
  <tr>
    &lt;td&gt;u h Historical (past) controls  </td>
    &lt;td&gt;Model controls, left singular vector, or coordinate position (in Geostatistics)</td>
  </tr>
  <tr>
    &lt;td&gt;u Optimal set of controls v Phase velocity or right singular</td>
    &lt;td&gt;vector</td>
  </tr>
  <tr>
    &lt;td&gt;w Weights for LS-SVR or SIES</td>
    &lt;td&gt;methods</td>
  </tr>
  <tr>
    &lt;td&gt;x State vector for Kalman filter</td>
    &lt;td&gt;and EnKF</td>
  </tr>
  <tr>
    &lt;td&gt;y Combined parameter-state</td>
    &lt;td&gt;vector for Kalman filter and EnKF</td>
  </tr>
  <tr>
    &lt;td&gt;(dimension N y ) z Random normal deviates or</td>
    &lt;td&gt;model reparametrization vector (di-</td>
  </tr>
  <tr>
    &lt;td&gt;mension N z )</td>
    &lt;td&gt;Random normal deviates or model reparametrization vector (di- mension N z )</td>
  </tr>
  <tr>
    &lt;td&gt;δ d Innovation vector (dimension</td>
    &lt;td&gt;N d )</td>
  </tr>
  <tr>
    &lt;td&gt;δ y State vector error (difference</td>
    &lt;td&gt;between true and predicted state)</td>
  </tr>
  <tr>
    &lt;td&gt;(dimension N y ) δ z Random normal deviates</td>
    &lt;td&gt;with reduced variance</td>
  </tr>
  <tr>
    &lt;td&gt;η Data mismatch tolerances</td>
    &lt;td&gt;(dimension N d )</td>
  </tr>
  <tr>
    &lt;td&gt;0 Zero or null vector (all entries</td>
    &lt;td&gt;equals to zero)</td>
  </tr>
  <tr>
    &lt;td&gt;1 Unity vector (all entries</td>
    &lt;td&gt;equals to one)</td>
  </tr>
</table>


# Matrices

<table>
  <tr>
    &lt;th&gt;A Centering matrix (dimension B Hessian matrix (dimension</th>
    &lt;th&gt;N e × N e ) N N )</th>
  </tr>
  <tr>
    &lt;td&gt;C e Data-error covariance matrix</td>
    &lt;td&gt;m × m (dimension N N )</td>
  </tr>
  <tr>
    &lt;td&gt;C e Covariance matrix of</td>
    &lt;td&gt;d × d measurement errors (dimension N d N d )</td>
  </tr>
  <tr>
    &lt;td&gt;d C e g Covariance matrix of model</td>
    &lt;td&gt;× errors (dimension N d × N d )</td>
  </tr>
  <tr>
    &lt;td&gt;C m Prior covariance of model</td>
    &lt;td&gt;parameters (dimension N m × N m )</td>
  </tr>
  <tr>
    &lt;td&gt;C m c Posterior covariance of model</td>
    &lt;td&gt;parameters (dimension N m × N m )</td>
  </tr>
  <tr>
    &lt;td&gt;C md Covariance matrix between</td>
    &lt;td&gt;model parameters and predicted data</td>
  </tr>
  <tr>
    &lt;td&gt;(dimension N m × N d )</td>
    &lt;td&gt;Covariance matrix between model parameters and predicted data (dimension N m × N d )</td>
  </tr>
  <tr>
    &lt;td&gt;C dd Covariance matrix of predicted</td>
    &lt;td&gt;data (dimension N d × N d )</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;C f y Forecast covariance matrix )</th>
    &lt;th&gt;of the state vector (dimension N y ×</th>
  </tr>
  <tr>
    &lt;td&gt;N y C a y Analysed covariance matrix</td>
    &lt;td&gt;of the state vector (dimension N y</td>
  </tr>
  <tr>
    &lt;td&gt;N y )</td>
    &lt;td&gt;×</td>
  </tr>
  <tr>
    &lt;td&gt;D Ensemble of predicted data</td>
    &lt;td&gt;(dimension N d × N e )</td>
  </tr>
  <tr>
    &lt;td&gt;E Ensemble data errors (dimension F Linear forward model in</td>
    &lt;td&gt;N d × N e ) Kalman filter (dimension N N )</td>
  </tr>
  <tr>
    &lt;td&gt;G Jacobian or sensitivity matrix</td>
    &lt;td&gt;y × y (dimension N d × N m )</td>
  </tr>
  <tr>
    &lt;td&gt;G d Dimensionless sensitivity</td>
    &lt;td&gt;matrix (dimension N d × N m )</td>
  </tr>
  <tr>
    &lt;td&gt;H Observation matrix in Kalman )</td>
    &lt;td&gt;filter and EnKF (dimension N n ×</td>
  </tr>
  <tr>
    &lt;td&gt;N y I Identity matrix</td>
    &lt;td&gt;Identity matrix</td>
  </tr>
  <tr>
    &lt;td&gt;J Innovation matrix (dimension</td>
    &lt;td&gt;N d × N e )</td>
  </tr>
  <tr>
    &lt;td&gt;K Kalman gain (dimension N</td>
    &lt;td&gt;m × N d or N y × N n )</td>
  </tr>
  <tr>
    &lt;td&gt;K Permeability tensor (dimension L Lower triangular matrix</td>
    &lt;td&gt;3 × 3) obtained with the Cholesky decomposi-</td>
  </tr>
  <tr>
    &lt;td&gt;tion, or Tikhonov matrix</td>
    &lt;td&gt;Lower triangular matrix obtained with the Cholesky decomposi- tion, or Tikhonov matrix</td>
  </tr>
  <tr>
    &lt;td&gt;M Ensemble of model parameters</td>
    &lt;td&gt;(dimension N m × N e )</td>
  </tr>
  <tr>
    &lt;td&gt;O Zero or null matrix (all entries P Reparamerization matrix</td>
    &lt;td&gt;equals to zero) (dimension )</td>
  </tr>
  <tr>
    &lt;td&gt;Q BFGS matrix (dimension N</td>
    &lt;td&gt;N m × N z m N m )</td>
  </tr>
  <tr>
    &lt;td&gt;R Localization matrix</td>
    &lt;td&gt;×</td>
  </tr>
  <tr>
    &lt;td&gt;R md Localization matrix for the</td>
    &lt;td&gt;Kalman gain or for the matrix C md</td>
  </tr>
  <tr>
    &lt;td&gt;(dimension N m × N d ) R Localization matrix for C</td>
    &lt;td&gt;(dimension N N )</td>
  </tr>
  <tr>
    &lt;td&gt;dd dd R 1 Random diagonal matrix</td>
    &lt;td&gt;d × d with element drawn from U [0 , 1] for</td>
  </tr>
  <tr>
    &lt;td&gt;PSO method</td>
    &lt;td&gt;Random diagonal matrix with element drawn from U [0 , 1] for PSO method</td>
  </tr>
  <tr>
    &lt;td&gt;R 2 Random diagonal matrix PSO method</td>
    &lt;td&gt;with element drawn from U [0 , 1] for</td>
  </tr>
  <tr>
    &lt;td&gt;S Diagonal matrix with data-error</td>
    &lt;td&gt;standard deviations (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N d × N d )</td>
    &lt;td&gt;Right-square root transform matrix (dimension N e × N e</td>
  </tr>
  <tr>
    &lt;td&gt;T R Right-square root transform</td>
    &lt;td&gt;matrix (dimension N e × N e )</td>
  </tr>
  <tr>
    &lt;td&gt;T L Left-square root transform U Left singular vectors</td>
    &lt;td&gt;matrix (dimension N y × N y )</td>
  </tr>
  <tr>
    &lt;td&gt;V Right singular vectors</td>
    &lt;td&gt;Right singular vectors</td>
  </tr>
  <tr>
    &lt;td&gt;W Ensemble of weight parameters</td>
    &lt;td&gt;for SIES method (dimension N e ×</td>
  </tr>
  <tr>
    &lt;td&gt;N e ) X Ensemble of model states</td>
    &lt;td&gt;(dimension )</td>
  </tr>
  <tr>
    &lt;td&gt;Y Ensemble of combined</td>
    &lt;td&gt;N x × N e parameters-states (dimension N y N e )</td>
  </tr>
  <tr>
    &lt;td&gt;∆ M Ensemble anomalies of model</td>
    &lt;td&gt;× parameters (dimension N m × N e )</td>
  </tr>
  <tr>
    &lt;td&gt;∆ D Ensemble anomalies of</td>
    &lt;td&gt;predicted data (dimension N d × N e )</td>
  </tr>
  <tr>
    &lt;td&gt;∆ X Ensemble anomalies of model ∆ Y Ensemble anomalies of</td>
    &lt;td&gt;states (dimension N x × N e ) combined parameters-states (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N x × N e )</td>
    &lt;td&gt;Ensemble anomalies of combined parameters-states (dimension N x × N e )</td>
  </tr>
  <tr>
    &lt;td&gt;Σ Singular values</td>
    &lt;td&gt;Singular values</td>
  </tr>
  <tr>
    &lt;td&gt;Λ Eigenvalue values</td>
    &lt;td&gt;Eigenvalue values</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;Θ Auxiliary matrix used in Γ Matrix with eigenvalues of</th>
    &lt;th&gt;subspace inversion (dimension N r × N r ) Θ used in subspace inversion (dimen-</th>
  </tr>
  <tr>
    &lt;td&gt;sion N r × N r ) Ψ Matrix with eigenvectors of</td>
    &lt;td&gt;Θ used in subspace inversion (dimen-</td>
  </tr>
  <tr>
    &lt;td&gt;sion N r × N r ), or feature Φ Auxiliary matrix for</td>
    &lt;td&gt;matrix for LS-SVR (dimension N s × N s ) implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N d × N r ) Υ Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N r × N r ) Ξ Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N r × N r ) Ω Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N d × N r ) Ω 1 Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N r × N d ) Ω 2 Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N r × N d ) Ω 3 Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N d × N e ) Ω 4 Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N e × N e ) Ω 5 Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;N m × N d ) Ω Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;6 N e × N d ) Ω Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;7 N e × N d ) Ω Auxiliary matrix for</td>
    &lt;td&gt;implementation of the analysis (dimension</td>
  </tr>
  <tr>
    &lt;td&gt;8 N m × N e )</td>
    &lt;td&gt;Auxiliary matrix for implementation of the analysis (dimension N m × N e )</td>
  </tr>
</table>


# Functions

g ( · ) Predicted datum from a forward model

p ( · ) Probability density function

P ( · ) Cumulative density function  

- p ( · ) Target probability density function
- q ( · ) Proposal probability density function
- r ( · ) Correlation function for localization


OF ( · ) Weighted least-squares data mismatch objective function

- B ( · , · ) Beta function
- C ( · ) Covariance function
- D ( · ) Mahalanobis distance


I z ( · , · ) Incomplete beta function

<table>
  <tr>
    &lt;th&gt;O d ( · ) Data-mismatch or ( ) Model-mismatch or</th>
    &lt;th&gt;likelihood objective function prior objective function</th>
  </tr>
  <tr>
    &lt;td&gt;O m · ( ) Total objective</td>
    &lt;td&gt;function</td>
  </tr>
  <tr>
    &lt;td&gt;O · ( ) RML objective</td>
    &lt;td&gt;function</td>
  </tr>
  <tr>
    &lt;td&gt;O r · ( ) Normalized objective</td>
    &lt;td&gt;function</td>
  </tr>
  <tr>
    &lt;td&gt;O N · ( ) Normalized</td>
    &lt;td&gt;data-mismatch objective function</td>
  </tr>
  <tr>
    &lt;td&gt;O N,d · ( ) Likelihood function</td>
    &lt;td&gt;Normalized data-mismatch objective function</td>
  </tr>
  <tr>
    &lt;td&gt;L · ( ) Gamma function</td>
    &lt;td&gt;Likelihood function</td>
  </tr>
  <tr>
    &lt;td&gt;Γ · ( ) Incomplete gamma</td>
    &lt;td&gt;function</td>
  </tr>
  <tr>
    &lt;td&gt;γ · , · ( ) Quadratic function</td>
    &lt;td&gt;Incomplete gamma function</td>
  </tr>
  <tr>
    &lt;td&gt;Q · ( ) Quantity of interest</td>
    &lt;td&gt;(proxy modeling)</td>
  </tr>
  <tr>
    &lt;td&gt;F · ( ) Kriging model</td>
    &lt;td&gt;Quantity of interest (proxy modeling)</td>
  </tr>
  <tr>
    &lt;td&gt;Z · ( ) Kernel function</td>
    &lt;td&gt;Kriging model</td>
  </tr>
  <tr>
    &lt;td&gt;K · , ·</td>
    &lt;td&gt;Kernel function</td>
  </tr>
</table>


# Vector functions

<table>
  <tr>
    &lt;th&gt;f ( · , · ) Forward model g ( ) Predicted data from a forward</th>
    &lt;th&gt;model (dimension )</th>
  </tr>
  <tr>
    &lt;td&gt;· h ( ) Nonlinear relationship</td>
    &lt;td&gt;N d between state and data (dimension )</td>
  </tr>
  <tr>
    &lt;td&gt;· ( ) Nonlinear mapping to a</td>
    &lt;td&gt;N d feature space</td>
  </tr>
  <tr>
    &lt;td&gt;ϕ · ( ) Augmented Lagrangian</td>
    &lt;td&gt;function</td>
  </tr>
  <tr>
    &lt;td&gt;L ·</td>
    &lt;td&gt;Augmented Lagrangian function</td>
  </tr>
</table>


# Vector spaces

<table>
  <tr>
    &lt;th&gt;V Vector R N</th>
    &lt;th&gt;space -dimensional real space</th>
  </tr>
  <tr>
    &lt;td&gt;N ( ) Null space</td>
    &lt;td&gt;N -dimensional real space</td>
  </tr>
  <tr>
    &lt;td&gt;N · ( ) Range</td>
    &lt;td&gt;Null space</td>
  </tr>
  <tr>
    &lt;td&gt;R ·</td>
    &lt;td&gt;Range</td>
  </tr>
</table>


# Statistical operators

<table>
  <tr>
    &lt;th&gt;B [ · ] Bias [ ]</th>
    &lt;th&gt;Expected value</th>
  </tr>
  <tr>
    &lt;td&gt;E · [ ]</td>
    &lt;td&gt;Variance</td>
  </tr>
  <tr>
    &lt;td&gt;V · [ ]</td>
    &lt;td&gt;Covariance</td>
  </tr>
  <tr>
    &lt;td&gt;C ·</td>
    &lt;td&gt;Covariance</td>
  </tr>
</table>


# Probability distributions

χ 2 ( · )

Chi-squared

N ( · , · )

Normal (Gaussian)

U ( · , · ) Uniform

# Acronyms

<table>
  <tr>
    &lt;th&gt;AHM Assisted History Matching AVO Amplitude Variation</th>
    &lt;th&gt;with Offset</th>
  </tr>
  <tr>
    &lt;td&gt;BLUE Best Linear Unbiased</td>
    &lt;td&gt;Estimate</td>
  </tr>
  <tr>
    &lt;td&gt;BFGS Broyden-Fletcher-Goldfarb-Shanno</td>
    &lt;td&gt;Best Linear Unbiased Estimate</td>
  </tr>
  <tr>
    &lt;td&gt;CCS Carbon Capture and</td>
    &lt;td&gt;Storage</td>
  </tr>
  <tr>
    &lt;td&gt;CCUS Carbon Capture,</td>
    &lt;td&gt;Utilization, and Storage</td>
  </tr>
  <tr>
    &lt;td&gt;CDF Cumulative Density</td>
    &lt;td&gt;Function</td>
  </tr>
  <tr>
    &lt;td&gt;CMA-ES Covariance Matrix</td>
    &lt;td&gt;Adaptation Evolution Strategy</td>
  </tr>
  <tr>
    &lt;td&gt;CMC Canadian Meteorological</td>
    &lt;td&gt;Centre</td>
  </tr>
  <tr>
    &lt;td&gt;CPU Central Processing Unit</td>
    &lt;td&gt;Canadian Meteorological Centre</td>
  </tr>
  <tr>
    &lt;td&gt;CS Cosine Similarity</td>
    &lt;td&gt;Central Processing Unit</td>
  </tr>
  <tr>
    &lt;td&gt;CUDA Compute Unified Device</td>
    &lt;td&gt;Architecture</td>
  </tr>
  <tr>
    &lt;td&gt;DES-MDA Deterministic Ensemble</td>
    &lt;td&gt;Smoother with Multiple Data As-</td>
  </tr>
  <tr>
    &lt;td&gt;similation</td>
    &lt;td&gt;Deterministic Ensemble Smoother with Multiple Data As- similation</td>
  </tr>
  <tr>
    &lt;td&gt;DFO Derivative-Free Optimization</td>
    &lt;td&gt;Derivative-Free Optimization</td>
  </tr>
  <tr>
    &lt;td&gt;DNAPL Dense Nonaqueous Phase</td>
    &lt;td&gt;Liquid</td>
  </tr>
  <tr>
    &lt;td&gt;DSI Data-Space inversion</td>
    &lt;td&gt;Data-Space inversion</td>
  </tr>
  <tr>
    &lt;td&gt;EA Evolutionary Algorithms</td>
    &lt;td&gt;Evolutionary Algorithms</td>
  </tr>
  <tr>
    &lt;td&gt;EKF Extended Kalman Filter</td>
    &lt;td&gt;Extended Kalman Filter</td>
  </tr>
  <tr>
    &lt;td&gt;EnKF Ensemble Kalman Filter</td>
    &lt;td&gt;Ensemble Kalman Filter</td>
  </tr>
  <tr>
    &lt;td&gt;EKI Ensemble Kalman</td>
    &lt;td&gt;Inversion</td>
  </tr>
  <tr>
    &lt;td&gt;EnOpt Ensemble-Based</td>
    &lt;td&gt;Optimization</td>
  </tr>
  <tr>
    &lt;td&gt;EnRML Ensemble Randomized</td>
    &lt;td&gt;Maximum Likelihood</td>
  </tr>
  <tr>
    &lt;td&gt;EnSRF Ensemble Square Root</td>
    &lt;td&gt;Filters</td>
  </tr>
  <tr>
    &lt;td&gt;ERT Ensemble Reservoir Tool</td>
    &lt;td&gt;Ensemble Reservoir Tool</td>
  </tr>
  <tr>
    &lt;td&gt;ES Ensemble Smoother</td>
    &lt;td&gt;Ensemble Smoother</td>
  </tr>
  <tr>
    &lt;td&gt;ES-MDA Ensemble Smoother</td>
    &lt;td&gt;with Multiple Data Assimilation</td>
  </tr>
  <tr>
    &lt;td&gt;FOC Facies Overlap Coefficient</td>
    &lt;td&gt;Facies Overlap Coefficient</td>
  </tr>
  <tr>
    &lt;td&gt;FMU Fast Model Update</td>
    &lt;td&gt;Fast Model Update</td>
  </tr>
  <tr>
    &lt;td&gt;FWI Full Waveform Inversion</td>
    &lt;td&gt;Full Waveform Inversion</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;FZI Flow Zone Indicator GOR Gas-Oil Ratio</th>
    &lt;th&gt;Flow Zone Indicator</th>
  </tr>
  <tr>
    &lt;td&gt;GN Gauss-Newton</td>
    &lt;td&gt;Gas-Oil Ratio</td>
  </tr>
  <tr>
    &lt;td&gt;GA Genetic Algorithms</td>
    &lt;td&gt;Gauss-Newton</td>
  </tr>
  <tr>
    &lt;td&gt;GCS Geological Carbon Storage</td>
    &lt;td&gt;Genetic Algorithms</td>
  </tr>
  <tr>
    &lt;td&gt;GPL General Public License</td>
    &lt;td&gt;Geological Carbon Storage</td>
  </tr>
  <tr>
    &lt;td&gt;GPU Graphics Processing</td>
    &lt;td&gt;Unit</td>
  </tr>
  <tr>
    &lt;td&gt;GRACE Gravity Recovery and</td>
    &lt;td&gt;Climate Experiment</td>
  </tr>
  <tr>
    &lt;td&gt;IAGS Iterative Adaptive</td>
    &lt;td&gt;Gaussian Mixture Smoother</td>
  </tr>
  <tr>
    &lt;td&gt;ILUES Iterative Local Updating</td>
    &lt;td&gt;Ensemble Smoother</td>
  </tr>
  <tr>
    &lt;td&gt;KF Kalman Filter</td>
    &lt;td&gt;Iterative Local Updating Ensemble Smoother</td>
  </tr>
  <tr>
    &lt;td&gt;LETKF Local Ensemble Transform</td>
    &lt;td&gt;Kalman Filter</td>
  </tr>
  <tr>
    &lt;td&gt;LHS Latin Hypercube Sampling</td>
    &lt;td&gt;Local Ensemble Transform Kalman Filter</td>
  </tr>
  <tr>
    &lt;td&gt;LM Levenberg-Marquadt</td>
    &lt;td&gt;Latin Hypercube Sampling</td>
  </tr>
  <tr>
    &lt;td&gt;LM-EnRML Levenberg-Marquadt</td>
    &lt;td&gt;Ensemble Randomized Maximum Like-</td>
  </tr>
  <tr>
    &lt;td&gt;lihood</td>
    &lt;td&gt;Levenberg-Marquadt Ensemble Randomized Maximum Like- lihood</td>
  </tr>
  <tr>
    &lt;td&gt;LS-SVR Least-Squares Support</td>
    &lt;td&gt;Vector Regression</td>
  </tr>
  <tr>
    &lt;td&gt;LVA Locally Varying Anisotropy</td>
    &lt;td&gt;Locally Varying Anisotropy</td>
  </tr>
  <tr>
    &lt;td&gt;MAD Median Absolute Deviation</td>
    &lt;td&gt;Median Absolute Deviation</td>
  </tr>
  <tr>
    &lt;td&gt;MAP Maximum a Posteriori</td>
    &lt;td&gt;Maximum a Posteriori</td>
  </tr>
  <tr>
    &lt;td&gt;MCMC Markov Chain Monte</td>
    &lt;td&gt;Carlo</td>
  </tr>
  <tr>
    &lt;td&gt;MDA Multiple Data Assimilation</td>
    &lt;td&gt;Multiple Data Assimilation</td>
  </tr>
  <tr>
    &lt;td&gt;MDP Morozov’s Discrepancy</td>
    &lt;td&gt;Principle</td>
  </tr>
  <tr>
    &lt;td&gt;ML Maximum Likelihood</td>
    &lt;td&gt;Maximum Likelihood</td>
  </tr>
  <tr>
    &lt;td&gt;MSE Mean Squared Error</td>
    &lt;td&gt;Mean Squared Error</td>
  </tr>
  <tr>
    &lt;td&gt;NERSC Nansen Environmental</td>
    &lt;td&gt;and Remote Sensing Centre</td>
  </tr>
  <tr>
    &lt;td&gt;NCG Nonlinear Conjugate</td>
    &lt;td&gt;Gradient</td>
  </tr>
  <tr>
    &lt;td&gt;NICE Noise‐Informed Covariance</td>
    &lt;td&gt;Estimation</td>
  </tr>
  <tr>
    &lt;td&gt;NMC Normalized Model Change</td>
    &lt;td&gt;Normalized Model Change</td>
  </tr>
  <tr>
    &lt;td&gt;NTG Net-to-Gross Ratio</td>
    &lt;td&gt;Net-to-Gross Ratio</td>
  </tr>
  <tr>
    &lt;td&gt;NV Normalized Variance</td>
    &lt;td&gt;Normalized Variance</td>
  </tr>
  <tr>
    &lt;td&gt;NPV Net Present Value</td>
    &lt;td&gt;Net Present Value</td>
  </tr>
  <tr>
    &lt;td&gt;NRMS Normalized Root Mean</td>
    &lt;td&gt;Squared</td>
  </tr>
  <tr>
    &lt;td&gt;NWP Numerical Weather</td>
    &lt;td&gt;Prediction</td>
  </tr>
  <tr>
    &lt;td&gt;OAS Orthogonal Array</td>
    &lt;td&gt;Sampling</td>
  </tr>
  <tr>
    &lt;td&gt;OBN Ocean Bottom Nodes</td>
    &lt;td&gt;Ocean Bottom Nodes</td>
  </tr>
  <tr>
    &lt;td&gt;OC Observation Coverage</td>
    &lt;td&gt;Observation Coverage</td>
  </tr>
  <tr>
    &lt;td&gt;OHT Optimal Hard Thresholding</td>
    &lt;td&gt;Optimal Hard Thresholding</td>
  </tr>
  <tr>
    &lt;td&gt;OIP Oil in Place</td>
    &lt;td&gt;Oil in Place</td>
  </tr>
  <tr>
    &lt;td&gt;PCA Principal Component PDF Probability Density</td>
    &lt;td&gt;Analysis Function</td>
  </tr>
  <tr>
    &lt;td&gt;PDG Permanent Downhole</td>
    &lt;td&gt;Gauges</td>
  </tr>
  <tr>
    &lt;td&gt;PEM Petroelastic Model</td>
    &lt;td&gt;Permanent Downhole Gauges</td>
  </tr>
  <tr>
    &lt;td&gt;PLT Production-Logging Tool</td>
    &lt;td&gt;Petroelastic Model</td>
  </tr>
  <tr>
    &lt;td&gt;PMF Probability Mass Function</td>
    &lt;td&gt;Production-Logging Tool</td>
  </tr>
  <tr>
    &lt;td&gt;PSO Particle Swarm Optimization</td>
    &lt;td&gt;Probability Mass Function</td>
  </tr>
  <tr>
    &lt;td&gt;PSO</td>
    &lt;td&gt;Particle Swarm Optimization</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;PTA Pressure Transient RFT Repeat Formation Testers</th>
    &lt;th&gt;Analysis</th>
  </tr>
  <tr>
    &lt;td&gt;RLM-MAC Regularized</td>
    &lt;td&gt;Levenberg-Marquardt for Minimum-Average-</td>
  </tr>
  <tr>
    &lt;td&gt;Cost</td>
    &lt;td&gt;Regularized Levenberg-Marquardt for Minimum-Average- Cost</td>
  </tr>
  <tr>
    &lt;td&gt;RML Randomized Maximum</td>
    &lt;td&gt;Likelihood</td>
  </tr>
  <tr>
    &lt;td&gt;SA Sensitivity Analysis</td>
    &lt;td&gt;Sensitivity Analysis</td>
  </tr>
  <tr>
    &lt;td&gt;SDA Sequential Data</td>
    &lt;td&gt;Assimilation</td>
  </tr>
  <tr>
    &lt;td&gt;SGS Sequential Gaussian</td>
    &lt;td&gt;Simulation</td>
  </tr>
  <tr>
    &lt;td&gt;StoSAG Stochastic Simplex</td>
    &lt;td&gt;Approximate Gradient</td>
  </tr>
  <tr>
    &lt;td&gt;SIES Subspace Iterative</td>
    &lt;td&gt;Ensemble Smoother</td>
  </tr>
  <tr>
    &lt;td&gt;SIS Sequential Indicator</td>
    &lt;td&gt;Simulation</td>
  </tr>
  <tr>
    &lt;td&gt;SVR Support Vector Regression</td>
    &lt;td&gt;Support Vector Regression</td>
  </tr>
  <tr>
    &lt;td&gt;SVD Singular Value</td>
    &lt;td&gt;Decomposition</td>
  </tr>
  <tr>
    &lt;td&gt;TPG Truncated Plurigaussian</td>
    &lt;td&gt;Truncated Plurigaussian</td>
  </tr>
  <tr>
    &lt;td&gt;TSVD Truncated Singular WAG Water-Alternating-Gas</td>
    &lt;td&gt;Value Decomposition</td>
  </tr>
  <tr>
    &lt;td&gt;WAG</td>
    &lt;td&gt;Water-Alternating-Gas</td>
  </tr>
</table>


![](<ensemble_data_assimilation_e-book_version_images/imageFile6.png>)

1

# Introduction

Abstract: This chapter reviews key concepts explored throughout the book to contextualize the reservoir data assimilation problem. It briefly introduces elements such as geological reservoirs, reservoir models, uncertainty, forward and inverse problems, data assimilation, Bayesian formulation, and ensembles. Additionally, this chapter outlines the organization of the book .

# 1.1 Geological Reservoirs

Geological reservoirs are subsurface formations capable of storing and transmitting fluids, such as hydrocarbons (oil and gas), water, hydrogen (H 2 ), carbon dioxide (CO 2 ), and waste materials from industrial processes. These reservoirs comprise porous and permeable rocks, such as sandstones, limestones, or fractured igneous and metamorphic rocks, allowing for fluid accumulation and movement within their pore spaces and fractures.

Geological reservoirs result from complex natural processes with varied types and characteristics. However, three key components are always present. First, there must be a rock with sufficient porosity and permeability. Porosity refers to the percentage of the rock’s volume made up of pore spaces that can store fluids, with higher porosity indicating greater storage capacity. Permeability describes the ability of the rock to transmit fluids through its pore network, with higher permeability allowing fluids to flow more quickly through the rock, making extraction and injection processes more efficient.

The second component is the presence of a trap and seal. Geological reservoirs are associated with structural or stratigraphic traps that prevent fluids from escaping. A seal, typically a layer of impermeable rock such as shale or salt, overlies the formation and ensures the containment of the fluids within the reservoir.

The third component is the fluid itself, which can be extracted for use, injected for permanent disposal, or stored temporarily. The type, composi-

Geological reservoirs serve several critical functions across various industries, with their primary applications encompassing the extraction and storage of natural resources. The main applications of geological reservoirs include:

- 1. Hydrocarbon production: This is the most known application. Geological reservoirs store and allow the extraction of hydrocarbons like oil and gas.
- 2. Natural gas storage: Geological reservoirs, particularly salt caverns, saline aquifers, and depleted oil and gas fields, can be used for temporary storage of natural gas, helping to balance the supply and demand of energy resources.
- 3. Carbon capture and storage (CCS): Geological reservoirs are increasingly being utilized for the storage of CO 2 to mitigate the impacts of climate change. In CCS processes, CO 2 is captured from industrial sources or directly from the air and injected into deep geological formations for permanent storage.
- 4. Geothermal energy production: Some geological reservoirs contain hot water or steam that can be explored for geothermal energy production, providing a low-carbon alternative to fossil fuels.
- 5. Water supply and management: Aquifers are essential freshwater sources. They provide water for drinking, irrigation, and industrial use.
- 6. Underground waste disposal: Certain geological reservoirs are used to dispose of hazardous and non-hazardous waste from industrial processes, particularly those related to energy production. Deep geological formations provide a secure environment for the long-term containment of waste materials, reducing the risk of surface contamination and environmental impact.
- 7. Underground hydrogen storage: Geological reservoirs present a promising solution for large-scale hydrogen storage, offering a cost-effective alternative to traditional methods such as compressed or liquefied hydrogen storage. Although the technology is still in the developmental phase, ongoing research and advancements continue to enhance its feasibility and potential for widespread adoption.


# 1.1.1 Reservoir Models

Understanding and managing geological reservoirs are essential for optimizing resource extraction while maintaining economic and environmental sustainability. Effective development and management involve constructing detailed numerical models that provide insights into fluid flow dynamics and simulate reservoir performance under various operational scenarios. These

models are essential for predicting reservoir behavior, making informed decisions, and enhancing overall efficiency and sustainability in resource utilization.

The construction of a reservoir model is a multidisciplinary process that integrates expertise from various fields to create a comprehensive representation of the subsurface. Fig. 1.1 provides a schematic representation of this process, highlighting some of its main components. In this process, geophysicists use seismic data to map the reservoir’s geometry and identify key subsurface features, while geologists interpret the depositional environment and characterize the reservoir’s structural and stratigraphic framework. Petrophysicists assess rock properties, such as porosity and permeability, using well-log data and rock samples, and study rock-fluid interactions through laboratory experiments. Geologists and geostatisticians work together to integrate diverse data sources, generating plausible distributions of rock properties. Engineers—including those specializing in reservoirs, production, and drilling—provide essential data on fluid dynamics, well performance, and operational constraints. Reservoir engineers are responsible for building reservoir simulation models and assimilating data acquired during field operations to reduce uncertainties and improve model accuracy.

Structural modeling

![](<ensemble_data_assimilation_e-book_version_images/imageFile4.png>)

κ

Petrophysics

φ

Facies modeling

Seismic interpretation

k r

P c

S

‘

S

Well

Rock-fluid

completions

properties

Property modeling

Upscaling

P

Forecast

Data assimilation

Reservoir simulation

T

Fluid properties

Fig. 1.1: Schematic representation of the reservoir model construction process, highlighting the main steps involved, from geological characterization to simulation and data assimilation.

Reservoir models are inherently complex and uncertain due to several interrelated factors. The heterogeneity of reservoir rocks is a primary challenge, as geological reservoirs consist of various rock types with differing properties such as porosity, permeability, and mineral composition. These properties can vary significantly over short distances, resulting in intricate spatial distributions that are difficult to predict accurately.

Parameter uncertainty further complicates reservoir modeling. Many input parameters, including multiphase relative permeability, capillary pressure, and fluid properties, are not directly measurable and must be estimated, often with substantial uncertainty. This uncertainty is compounded by the reservoirs’ dynamic nature, where fluid flow, pressure changes, and chemical interactions evolve over time. Modeling these dynamic processes requires solving complex partial differential equations that account for multiphase flow, heat transfer, geomechanics, and geochemical reactions, each adding layers of complexity and potential sources of uncertainty.

The initial conditions of a reservoir also introduce uncertainty. The initial distribution and composition of fluids, as well as pressure conditions, are often imprecisely known. This uncertainty in initial conditions propagates through the model, affecting predictions of future reservoir behavior. Additionally, the data available for reservoir models are often limited and sparse, typically derived from well logs, core samples, seismic surveys, and dynamic measurements such as flow rates and pressure readings. These data provide only indirect and incomplete information about the reservoir, and the sparse coverage compared to the reservoir’s size requires interpolation or extrapolation, introducing further uncertainty.

Measurement errors are another significant source of uncertainty. All measurements used to construct and calibrate reservoir models are subject to some degree of error, stemming from limitations in measurement techniques, instrument precision, and data interpretation. The challenge of integrating data collected at various scales—from microscopic pore-scale observations to large-scale seismic surveys—adds to the complexity of creating a coherent model. Finally, despite advances in computational power, there are still limitations in the resolution and complexity that can be feasibly modeled. Simplifications and assumptions are always necessary, which introduce additional uncertainty.

# 1.2 Uncertainty

Nearly all problems involving physical systems require decision-making under uncertainty. Uncertainty sources can be classified into three primary types:

1. Stochasticity in the dynamical system: Some systems exhibit instability, where small changes in initial conditions lead to divergent solutions

and chaotic dynamics. Consequently, models for these systems have limited predictive capabilities over extended time horizons. A classic example is numerical weather forecast.

- 2. Incomplete observability: The system’s outcomes may appear stochastic to the modeler because they cannot observe or accurately determine all the parameters that influence the system’s behavior.
- 3. Incomplete modeling: The system’s outcomes may also seem stochastic due to the model’s inability to capture all the relevant physical processes present in the real system.


Unlike atmospheric models, reservoir models are generally stable, making stochasticity in the dynamical system a less significant source of uncertainty. However, the other two sources—incomplete observability and modelingare always present.

Ultimately, the goal of a reservoir model is to support informed decisionmaking in investments and management of natural resources. However, due to inherent uncertainties in model construction, predictions are also uncertain. Therefore, it is essential to quantify this uncertainty in the model’s outcomes to manage the potential consequences of different actions.

In this context, uncertainty quantification can be approached from two perspectives: forward propagation of uncertainty and inverse assessment of model uncertainty. Forward propagation involves carrying various sources of uncertainty through the forward model to predict the overall uncertainty in the system’s response. In contrast, inverse assessment involves estimating the uncertainty in model input parameters based on measurements from the reservoir. The first perspective—forward modeling—represents the primary goal of reservoir simulation: predicting the future. The second perspectiveinverse modeling—is generally more challenging but of great relevance. During inverse modeling, data assimilation occurs, reducing uncertainty in the model parameters and, consequently, improving confidence in the model forecasts.

# 1.3 Forward Problem

This book centers on data assimilation, particularly emphasizing the inverse modeling perspective of uncertainty quantification. However, before delving into inverse problems, it is helpful first to outline the forward problem addressed in this book.

If the mathematical model is sufficiently simple, it may have an analytical solution. For instance, a one-dimensional, two-phase incompressible flow in a homogeneous reservoir, describing an immiscible displacement process such as oil being displaced by water, has a well-known analytical solution derived by Buckley and Leverett [50]. However, for most reservoir problems, analytical solutions are not available, necessitating the use of numerical models, commonly referred to as reservoir simulators.

For example, the mathematical equations that describe an isothermal twophase flow represent one of the simplest yet common problems in reservoir simulation. In this scenario, fluid flow can be described by the following set of equations:

-  Conservation of mass:

$$
∇· ( ρ i v i ) + ∂ ( ρ i s i φ ) ∂t = q i . (1.1)
$$

-  Darcy’s law:

$$
v i = - κ r i µ i K ( ∇ p i - ρ i g ∇ z ) . (1.2)
$$

-  Equation of state:

$$
c i = 1 ρ i ∂ρ i ∂p i ∣ ∣ ∣ ∣ T = const . (1.3)
$$

-  Saturation:

$$
s 1 + s 2 = 1 . (1.4)
$$

-  Capillary pressure:


$$
p 2 - p 1 = p c ( s 1 ) . (1.5)
$$

In the equations above, the subscript i denotes the phase number, for example, water and oil. Eq. (1.1) represents the conservation of mass, stating that the difference between the mass flux entering and exiting a medium equals the change in the amount accumulated within that medium. The divergence term ∇· ( ρ i v i ) represents the net flux within the medium, where ρ i is the phase density and v i is the phase velocity. ∂ ( ρ i s i φ ) ∂t represents the rate of accumulation of mass, where s i is the saturation of phase i and φ is the porosity of the medium. q i is a source (or sink) term of mass. Eq. (1.2) represents Darcy’s law, which is a statement of momentum con-

servation and relates phase velocity to the pressure gradient ∇ p i . Here, K is the permeability tensor, and κ r ,i = κ r ,i ( s i ) denotes the relative permeability of phase i , modeled as a function of s i . µ i = µ i ( p i ) represents the phase viscosity, typically a function of pressure, and ρ i g ∇ z accounts for gravitational effects, where g is the acceleration due to gravity and ∇ z is the depth gradient.

Eq. (1.3) represents an isothermal equation of state that relates fluid density variation to changes in pressure. It provides a straightforward description of phase compressibility, c i , and assumes no mass transfer between

phases. Eq. (1.4) states that the medium is fully saturated with the two phases, while Eq. (1.5) writes the capillary pressure, p c , as the difference between the pressure in the non-wetting phase, p 2 , and the pressure in the wetting phase, p 1 . p c is modeled as a function of the saturation of the wetting phase, s 1 . Typically, reservoir simulators solve the fluid flow equations using finite

difference or finite volume methods. In these approaches, the reservoir is discretized into gridblocks, resulting in a system of nonlinear equations that are solved using an iterative process for the primary variables (dynamical state) of the reservoir at a sequence of times. In the example of two-phase flow described by Eqs. (1.1)–(1.5), the primary variables are pressure and phase saturations. This model has several parameters representing physical properties that must be specified in advance. In the two-phase flow example, φ , K , κ r i ( s i ), ρ i ( p i ), µ i ( p i ), c i and p c ( s 2 ) are model parameters. Following the notation used in Tarantola [428] and Oliver et al. [334], in this book, we reserve m to denote the vector containing the model parameters. Fig. 1.2 shows an example of a reservoir model of an oilfield in the Campos Basin, illustrating the values of permeability, which represent the model parameters and the corresponding predicted water saturation at a specific time, representing the dynamical state of the system.

![](<ensemble_data_assimilation_e-book_version_images/imageFile5.png>)

mD

10 3

10 2

10 2

10 0

INTERNA

(a)

Permeability

1

0

(b)

Water saturation

Fig. 1.2: Reservoir simulation model of an oilfield in the Campos Basin. Panel (a) illustrates the permeability distribution, while panel (b) shows the predicted water saturation after 15 years of field operations. The black lines represent oil-producing wells, and the blue lines indicate water injection wells.

Wells play a crucial role in this process, serving as the communication link between the reservoir and the surface. However, they introduce complexities to the overall modeling because the flow within the wellbore differs fundamentally from the flow through porous media. To address this, coupling equations are necessary to model the interaction between these elements accurately. Additionally, wells function as control components in the dynamical system, acting as boundary conditions that must be specified during simulations. Consequently, reservoir simulation predictions are functions of both the model parameters and well controls. We use g ( m , u ) to denote a prediction of a reservoir model, where u represents a set of controls of the system. For example, u may include the schedule of fluid injection rates, operational pressure constraints for individual wells, and total fluid processing capacity.

The primary objectives of reservoir simulation are to predict the behavior and performance of a reservoir under various development and operational scenarios. These simulations help optimize recovery strategies and evaluate the economic viability of various operational approaches. In this context, reservoir simulation can be used to predict the optimal set of controls, u   , while accounting for uncertainties in the parameters, m .

Numerous commercial and open-source reservoir simulators are available, offering a diverse array of formulations and numerical schemes. Prominent open-source examples include MRST [261], OPM-Flow [359], open-DARTS [455], PFLOTRAN-OGS [337], JutulDarcy.jl [311], and GEOS [177], among others. A detailed discussion of the formulations and methods employed by these simulators is beyond the scope of this book. The literature on this topic is extensive and continually evolving; for further reading, see, e.g., [21, 84, 30, 261].

# 1.4 Inverse Problem

In the forward problem, we are interested in predicting

$$
d = g ( m , u ) (1.6)
$$

for different combinations of ( m , u ). In contrast, the inverse problem involves solving

$$
g ( m | u h ) = d obs (1.7)
$$

for m , given a set of measurements d obs . Here, u h denotes the historical (past) controls used in the field. Since these controls are fixed during the

However, a fundamental flaw exists in attempting to find a solution for (1.7): data contain errors, and models are imperfect representations of reality. Therefore, finding m such that g ( m ) = d obs is exactly satisfied may not be possible nor desirable. The solution must account for data uncertainties and limitations in the forward modeling.

One naive attempt to circumvent this issue would be to search for a model such that the distance between the vectors g ( m ) and d obs is within some tolerance. For example, one might set an algorithm to look for a model such that

$$
‖ g ( m ) - d obs ‖ ≤ ‖ η ‖ , (1.8)
$$

where η represents a vector of data mismatch tolerances. However, several challenges remain. First, although condition (1.8) is less stringent than Eq. (1.7), it may still lead to model overfitting data. Hence, it is necessary to formulate the problem in a more robust manner. Second, since the number of unknown model parameters is usually much larger than the number of observations, multiple or even infinite combinations of model parameters can fit the data within some tolerance. In the context of inverse problems, this constitutes an ill-posed problem 2 . Third, there are always additional sources of information about the model that are not captured by the vector d obs . This a priori information must be combined with the data contained in d obs to better constrain the solution of the inverse problem. Eq. (1.8) does not specify a procedure for integrating different sources of information.

The a priori information is a critical aspect of inverse problems in reservoir modeling. Reservoir models result from geological modeling efforts that synthesize various sources of information, observations, and hypotheses. For example, geologists often study the depositional environment that formed the reservoir to build a prior expectation about the structures and values of the rock properties.

Fig. 1.3 illustrates a simplified version of this process, where a conceptual model of channelized turbidite deposits is used to classify the expected distribution of rock properties in a reservoir. Fig. 1.3b shows a schematic cross-section with stacked turbidite channels. The yellow areas represent regions rich in sand sediments associated with high reservoir quality, while the green areas indicate regions rich in mud sediments. As one moves away from the central axis of the turbidite channels, a decline in reservoir quality is expected. This conceptual model was used to generate a reservoir model for an oilfield in the Campos Basin, classifying the spatial distribution of

1 Even past controls can have some level of uncertainty, which might need consideration during the solution of the inverse problem. 2

Practical inverse problems are often ill-posed, meaning they typically fail to meet at least one of the following conditions: existence of a solution, uniqueness of the solution, or stability; see Appendix B (Section B.2).

FLOW

OVERBANK NON-RESERVOIR

NON-RESERVOIR

AXIS

OFF-AXIS

MARGIN

Lower reservoir quality

OVERBANK

(a)

Conceptual turbidite system INTERNA

INTERNA

(b)

Schematic cross-section

INTERNA

![](<ensemble_data_assimilation_e-book_version_images/imageFile6.png>)

AXIS

OFF-AXIS

MARGIN

NON-RES

(c)

Model

Fig. 1.3: Illustration of prior information used to develop a model for a turbidite reservoir. Panel (a) depicts the conceptual model of amalgamated turbidite channels. Panel (b) presents a schematic cross-section showing the increasing intercalation of sand and mud deposits. Panel (c) displays the model of an actual oilfield, where the rock type distribution follows the classification outlined in (b).

# 1.4.1 Data Assimilation

Data assimilation involves integrating observed data into numerical models to improve their predictive capabilities. Therefore, it can be viewed as a type of inverse problem. In the context of geological reservoirs, data assimilation

In the literature, data assimilation is known by many names, including data integration, model calibration, parameter or state estimation, and history matching. The term “history matching” is particularly prevalent in the petroleum and groundwater hydrology fields. However, this book adopts the term “reservoir data assimilation.”

This book focuses on the assimilation of dynamic data collected during reservoir operations through drilled wells or geophysical techniques such as seismic and electromagnetic methods. These data include flow rate measurements, which indicate the volume of fluid produced or injected; pressure measurements, which reflect reservoir pressure distribution and temporal variations; rock property measurements from well logging and core sampling; fluid composition data obtained from downhole sampling tools, production logging instruments, and surface analysis techniques; temperature measurements from downhole sensors, providing insights into water or gas influx and geothermal gradients; tracer injection data, which track injected tracers to understand fluid movement within the reservoir; and 4D (time-lapse) seismic data, which capture changes in subsurface properties over time.

Fig. 1.4 illustrates some of these data alongside model predictions for an oilfield in the Campos Basin, highlighting discrepancies between observed data and model outputs. The objective of data assimilation is to minimize these discrepancies while accounting for data noise and model limitations.

# 1.4.2 Geostatistics

At this point, it is convenient to introduce a fundamental element of reservoir modeling: geostatistics. Geostatistics is a specialized branch of statistics that focuses on the analysis and interpretation of spatially or spatiotemporally correlated data. It has become a crucial tool in various fields for predicting the spatial distribution of natural resources and environmental variables.

Originally, geostatistics was closely associated with interpolation methods, particularly with the development of kriging. However, modern geostatistics extends far beyond simple interpolation problems. It has revolutionized the understanding and modeling of geological reservoirs and their uncertainties. This transformation has been driven by the development of advanced algorithms for estimating and simulating reservoir models. Instead of relying on a single “best” estimate, geologists use geostatistics to generate multiple model realizations, embracing a much greater degree of heterogeneity representation and assessment of uncertainty.

Geostatistics is closely tied to inverse problems and can be considered a form of data assimilation, as it seeks to infer the underlying properties of

 

    DWHUFXW  

���

���

���









��

M

   3UHVVXUH M3D 

��

��

��









����

����

  7 PH GD V 

(a)

Water cut









����

����



 

 



 

 

  7 PH GD V 

![](<ensemble_data_assimilation_e-book_version_images/imageFile7.png>)

(b)

Pressure

0.08

INTERNA

0

-0.08

Observed

(c)

4D seismic

Predicted

Fig. 1.4: Examples of actual data and predictions from a model of an oilfield in the Campos Basin. Panels (a) and (b) show the observed values of water cut and pressure (red dots), while the gray lines represent predictions from 200 different versions (realizations) of the model. Panel (c) shows the observed and predicted 4D seismic data for this field. In this image, blue colors indicate a relative increase in impedance in the reservoir, typically associated with the injection of water, which is denser than the original oil. The red regions indicate a decrease in impedance, generally associated with an increase in pore pressure.

Fig. 1.5 illustrates this concept. In this example, porosity measurements from well logs (Fig. 1.5a) and an image of acoustic impedance from seismic data (Fig. 1.5b) were used in a geostatistical method to estimate the porosity distribution for a petroleum reservoir in the Campos Basin (Fig. 1.5c). Here, both data sources—well logs and seismic data—are assumed to be linearly related to the property of interest, which is porosity.

Introduction

0.3

![](<ensemble_data_assimilation_e-book_version_images/imageFile8.png>)

0.2

0.1

0

(a)

Well porosity data

INTERNA

INTERNA

10 6 kg/m 2 s

8

7

6

5

(b)

Seismic data (acoustic impedance) INTERNA

INTERNA

0.3

0.2

0.1

0

(c)

Porosity

Fig. 1.5: Porosity model of an oilfield in the Campos Basin. Panel (a) illustrates the porosity data at well locations, (b) shows a 3D seismic image (acoustic impedance) used as correlated data to build the porosity model presented in (c).

Geostatistics, however, has specialized in generating complex (non-Gaussian) distributions of model properties by integrating multiple data sources with prior information. In reservoir modeling, and particularly in the data assimilation problems discussed in this book, geostatistics is almost always employed to construct the prior model realizations.

# 1.5 Bayesian Viewpoint

A practical consequence of inverse problems in reservoir modeling is that we often have multiple solutions consistent with the data, requiring us to

Probability theory has its roots in the analysis of the frequency of events, a concept most intuitive when applied to repeatable events. When we say that an event has a probability P of occurring, it means that if we were to repeat the event an infinite number of times, P would represent the proportion of occurrences. For example, the probability of rolling an odd number with a single die is 50%. With enough rolls, the frequency of odd numbers will eventually converge to 50%.

However, the frequency interpretation of probability does not apply directly to non-repeatable events. For instance, if a doctor says that a patient has a 90% chance of having a particular disease, he or she is not dealing with an infinite number of identical patients with the same symptoms but different underlying conditions. In this case, probability represents a degree of belief rather than a frequency of occurrence.

This use of probability to express relative levels of uncertainty is known as Bayesian probability. An interesting (and sometimes controversial 3 ) consequence is that we assign probabilities to events that are not inherently random. For example, we use probabilities to describe the distribution of rock properties in a reservoir, even though the physical laws governing these properties are deterministic. The reservoir, a result of complex geological processes, is modeled as a random event drawn from a probability distribution.

Bayesian probability theory provides mathematical tools for integrating a priori information with observed data. In this framework, the solution to an inverse problem is represented by the a posteriori probability distribution 4 .

# 1.6 Ensembles

Bayesian probability is one of the foundations for the methods discussed in this book. Bayes’ rule describes how to update probability density functions (PDFs) in light of new data. However, the actual PDFs are of little practical interest in reservoir modeling. First, these PDFs can be extremely high-

3 Sharon McGrayne’s book, The Theory that Would Not Die: How Bayes’ Rule Cracked the Enigma Code, Hunted Down Russian Submarines, and Emerged Triumphant from Two Centuries of Controversy [299], offers a compelling account of the evolution of Bayesian statistics, highlighting its tumultuous journey before ultimately gaining widespread acceptance. 4

It is important to note that the terms a priori and a posteriori should not be interpreted literally as “before” and “after.” They do not imply any temporal causality. Instead, these terms refer to the state of understanding of the system. The prior represents our initial knowledge or assumptions about the structure of the model parameters we want to estimate. The combination of this prior knowledge with field measurements results in the posterior.

A significant complication in this process is that executing the forward model can be computationally expensive and time-consuming, limiting the number of samples that can be evaluated. As a practical consequence, naive trial-and-error strategies or even rigorous sampling methods like Markov chain Monte Carlo can become computationally prohibitive despite the impressive advances in computational power over the last decades. This means we are constrained to approximate solutions, as we are particularly interested in methods that scale well with the number of parameters and data points.

# 1.6.1 Ensemble-Based Methods

Ensemble-based methods encompass a range of data assimilation techniques grounded in Monte Carlo formulations of the Kalman filter [228, 229]. The ensemble Kalman filter (EnKF), introduced by Evensen [136], was the pioneering approach in this field. EnKF and its numerous variations have achieved notable success across various domains, including oceanography [34], atmospheric modeling [464], and numerical weather prediction [201, 338].

The introduction of EnKF as a reservoir data assimilation method by Nævdal et al. [313] sparked significant research activity, leading to the publication of numerous studies in subsequent years; see, e.g., [3, 331] and references therein. In its standard form, EnKF uses an ensemble of states of the dynamical system to represent the mean and covariance, which are updated sequentially over time.

While the sequential data assimilation scheme is a key advantage in oceanography and weather prediction applications, it presents challenges when applied to reservoir data assimilation. Specifically, frequent restarts of the reservoir simulations are required, substantially increasing the overall computational cost of the process.

An alternative approach is to apply the EnKF equations to update the entire history of observations simultaneously, a process known as the ensemble

# 1.7 Book Organization

The book is structured into nine chapters and four appendices, designed to provide a comprehensive understanding of ensemble data assimilation techniques and their applications to geological reservoir models. The methods are presented looking for a balance between mathematical formulation and practical applicability. Each method is accompanied by “pseudo-codes,” which are not intended for direct computational implementation but rather offer a concise overview of the procedural steps involved. Additionally, the book includes practical examples of reservoir data assimilation, primarily drawn from petroleum reservoirs, the author’s area of expertise.

The book is organized as follows: Chapter 2 delves into the Bayesian formulation of the data assimilation problem, offering a statistical framework for updating reservoir models using observational data. Chapter 3 covers optimization methods employed in reservoir data assimilation and includes a discussion of parametrization strategies commonly used in this field. Chapter 4 focuses on the EnKF method, beginning with the derivation of the standard Kalman filter, followed by the introduction of the ensemble component. This chapter also covers topics such as sequential data assimilation, ensemble covariances, parameter-state consistency, and square root formulations. Chapter 5 introduces the ES and ES-MDA methods, emphasizing their advantages in reservoir modeling. Chapter 6 reviews two widely used iterative versions of the ES: ensemble randomized maximum likelihood (EnRML) and subspace iterative ensemble smoother (SIES). Chapter 7 addresses the challenges posed by limited-sized ensembles, namely sampling errors and limited degrees of freedom, and explores strategies to mitigate their negative effects, with a focus on the method known as localization. Chapter 8 provides an overview of the computational implementation of ES-MDA, focusing on the matrix operations essential for efficiently performing the analysis step. Chapter 9 discusses practical aspects and field examples, showcasing real-

This page is intentionally left blank. (Paradox alert!)

![](<ensemble_data_assimilation_e-book_version_images/imageFile12.png>)

2

# Bayesian Formulation of the Data Assimilation Problem

Abstract: This chapter frames data assimilation within the framework of Bayesian inference. It establishes both the likelihood and prior distribution and leverages Bayes’ rule to derive the posterior distribution. The analytical solutions for the linear-Gaussian case are presented, forming the foundational basis for subsequent discussions on techniques such as randomized maximum likelihood and ensemble smoother. Additionally, this chapter introduces the primary notation components used throughout the book. Therefore, a solid understanding of the content in this chapter is essential for comprehending the remaining chapters of the book.

# 2.1 Introduction

Bayesian inference and Monte Carlo sampling are the cornerstones of modern data assimilation methods. Bayes’ rule establishes a mechanism to combine prior information about the reservoir with data, while Monte Carlo sampling provides a strategy for practical applications.

This chapter reviews fundamental elements of Bayesian inference, presenting both likelihood and prior distributions and leveraging Bayes’ rule to derive the posterior distribution. It also discusses analytical solutions for the linear-Gaussian case, providing the foundational basis for subsequent techniques such as randomized maximum likelihood and ensemble smoother.

While there are excellent books on this subject, particularly the seminal works of Tarantola [428] and Oliver et al. [334], the objective here is to summarize the indispensable elements necessary for the development of the

# 2.2 Model Likelihood

Let m ∈ R N m be the random vector of model parameters, which means that m contains a stochastic realization of the uncertain parameters required to construct a plausible representation of the reservoir of interest. Let g ( m ) ∈ R N d to denote the predicted data obtained running the forward model g ( · ) given the realization m . Finally, let d obs ∈ R N d be the vector of observed data, which is assumed to be corrupted with an unknown additive random error such that

$$
d obs = d true + e d , (2.1)
$$

where d true represents the true (noiseless) data, and e d denotes the dataerror vector associated with measurement errors.

For now, assume that the forward model is perfect, which means that if we were able to provide the ground truth for the vector of the model parameters 1 , it would return the observation true values

$$
g ( m true ) = d true . (2.2)
$$

From (2.1) and (2.2), we have

$$
d obs = g ( m true ) + e d . (2.3)
$$

Note that because e d is a random vector, d obs is also a random vector. Assume that e d is a sample from a multivariate Gaussian (normal) distribution with zero mean and covariance C e d , which is represented by the notation e d ∼ N ( 0 , C e d ). In this case, the probability density function (PDF) of e d has the form

$$
p ( e d ) = 1 [(2 π ) N d det C e d ] 1/2 exp { - 1 2 e ⊤ d C - 1 e d e d } . (2.4)
$$

The expectation of d obs is

$$
E [ d obs ] = E [ g ( m true ) + e d ] = g ( m true ) , (2.5)
$$

and the covariance is

$$
C [ d obs ] = E [ ( d obs - E [ d obs ]) ( d obs - E [ d obs ]) ⊤ ] = E [ ( d obs - g ( m true )) ( d obs - g ( m true )) ⊤ ] = E [ e d e ⊤ d ] = C [ e d ] = C e d . (2.6)
$$

Thus, d obs ∼ N ( g ( m true ) , C e d ) and the PDF for d obs given m true is

$$
p ( d obs | m true ) = 1 [(2 π ) N d det C e d ] 1/2 × exp { - 1 2 ( d obs - g ( m true )) ⊤ C - 1 e d ( d obs - g ( m true )) } . (2.7)
$$

Instead of p ( d obs | m true ), we can speculate about the likelihood of a model m for a given set of actual measurements, d obs . In this case, we write

$$
L ( m ) = L ( m | d obs ) ≡ p ( d obs | m ) = 1 [(2 π ) N d det C e d ] 1/2 × exp { - 1 2 ( d obs - g ( m )) ⊤ C - 1 e d ( d obs - g ( m )) } . (2.8)
$$

Eq. (2.8) represents the likelihood function 2 of m given d obs . This function measures how well a model explains the data [428].

# 2.2.1 Maximum Likelihood Estimate

The vector m that maximizes L ( m ) is called the maximum likelihood (ML) estimate. Note that maximizing L ( m ) defined in Eq. (2.8) is equivalent to solving the following minimization problem

$$
m ml = arg min m O d ( m ) , (2.9)
$$

$$
O d ( m ) = 1 2 ( d obs - g ( m )) ⊤ C - 1 e d ( d obs - g ( m )) . (2.10)
$$

We refer to O d ( m ) as the data-mismatch or likelihood objective function.

In the petroleum history matching literature a very common assumption for production data is that the measurement errors are uncorrelated in time and space. In this case, the matrix C e d becomes diagonal

$$
C e d = ⎡ ⎢ ⎢ ⎢ ⎣ σ 2 e, 1 0 · · · 0 0 σ 2 e, 2 · · · 0 0 0 . . . 0 0 0 · · · σ 2 e,N d ⎤ ⎥ ⎥ ⎥ ⎦ , (2.11)
$$

where σ 2 e,i is the variance of the measurement error of the i th datum. In case of uncorrelated measurement errors, O d ( m ) reduces to

$$
O d ( m ) = 1 2 N d ∑ i =1 ( d obs ,i - g i ( m )) 2 σ 2 e,i . (2.12)
$$

In commercial assisted history matching (AHM) packages, the objective function is typically defined as a sum of weighted squares, i.e.,

$$
OF ( m ) = N d ∑ i =1 w i ( g i ( m ) - d obs ,i ) 2 , (2.13)
$$

where w i is the weight of the i th datum. Comparing these objective functions, we conclude that in order to obtain the ML estimate, we should use 1

$$
w i = 1 2 σ 2 e,i , (2.14)
$$

which means that the weight of each datum in OF ( m ) should reflect the confidence level we have in the particular datum.

# 2.2.2 Data and Model Errors I

The vector e d was defined as the random vector representing the noise due to measurement errors present in the data. A critical assumption made to derive the likelihood function in Eq. (2.8) is e d ∼ N ( 0 , C e d ), which implies the following:

-  There are no biases in the observed data vector, meaning there are no systematic errors in the measurements.
-  The noise follows a Gaussian distribution with a known covariance.
-  The forward model is perfect.


Clearly, these assumptions do not hold in practice. In fact, the uncertainty attributed to the measurements strongly impacts the data assimilation as they define the accuracy required for data matching. Unfortunately, how to appraise data uncertainty is not always evident because more than just random noise may contaminate the observations. Often, there are systematic errors in the data acquisition, which are challenging to characterize and frequently unknown to practitioners. A poor representation of the uncertainty in the measurements deteriorates the data assimilation results. Underestimation leads to overly strong updates in model parameters, while overestimation hinders the utilization of all available information in the data.

Moreover, models inherently contain imperfections and deviations from reality; thus, model errors are a persistent factor in practical applications. Perhaps one of the first works to formally incorporate model errors within the Bayesian uncertainty quantification framework was presented by Kennedy and O’Hagan [235]. They define model errors as “ discrepancies between model predictions and the actual physical processes, even in the absence of uncertainty in the model input parameters. ” Model errors also appear in the literature with other names such as model inadequacy, model discrepancy, model bias, or structural uncertainty [49]. These errors typically arise from simplifications made in the formulation of the physical process of interest or numerical approximations (discretization errors) resulting from the solution of the differential equations. Another important source of model errors is the fact that it is almost inevitable that some parameters that have an influence on the predicted data are neglected during data assimilation. In this situation, the parameters used in the data assimilation will have to compensate for the missing ones. As a result, we may observe some of these parameter values outside of the expected range.

In practice, however, estimating the effects of model errors is difficult. Model errors and observation biases typically have similar consequences in data assimilation, making it challenging to separate these effects without additional information.

Examples of sources of model errors in reservoir data assimilation include:

-  Under-parametrization (missing parameters with a significant effect on predicted data).
-  Discretization errors (excessive coarseness).
-  Well constraint specification (control the simulation forcing to honor noisy rate data).
-  Fluid modeling (use of black-oil formulation to approximate compositional).
-  Simplified well model (neglect long-term loss of performance due to local effects).


Examples of sources of observation biases:

-  Allocation of production/injection rates based on infrequent well tests.
-  Extrapolation of buildup pressures.
-  Incorrect time-to-depth conversion for 4D seismic.


A common remedy for compensating for neglecting model errors and observation bias is inflating the data error covariance. This procedure does not resolve the problem but alleviates its negative consequences. This procedure can be justified by assuming additive model errors, denoted as e g ,

$$
g ( m true ) = d true + e g , (2.15)
$$

in which case the observation vector can be written as

$$
d obs = d true + e d = g ( m true ) - e g + e d . (2.16)
$$

Assuming independence between e g and e d 3 and disregarding model bias leads to

$$
E [ d obs ] = g ( m true ) (2.17)
$$

and

$$
C [ d obs ] = E [ ( - e g + e d ) ( - e g + e d ) ⊤ ] = E [ e g e ⊤ g ] + E [ e d e ⊤ d ] - E [ e g e ⊤ d ] - E [ e d e ⊤ g ] = C [ e g ] + C [ e d ] = C e g + C e d ≡ C e . (2.18)
$$

This means that the likelihood expression in Eq. (2.8) remains valid, replacing C e d by a total data-error covariance, C e , which represents the sum of the covariance matrix of the measurement and model errors. Unlike measurement errors, which can often be assumed to be independent in time and space, model errors are almost always correlated.

# 2.2.3 Linear Case

Assume that the predicted data are linearly related to m , i.e.,

$$
g ( m ) = Gm , (2.19)
$$

where G is an N d × N m matrix. The entry in the i th row and j th column of G is given by ( m )

$$
G ij = ∂g i ( m ) ∂m j , (2.20)
$$

which means that G ij is the sensitivity of the i th datum with respect to the j th model parameter. We refer to the matrix G as the Jacobian or sensitivity matrix.

For the linear case, the ML estimate can be found by minimizing

$$
O d ( m ) = 1 2 ( d obs - Gm ) ⊤ C - 1 e ( d obs - Gm ) (2.21)
$$

analytically. This can be achieved by setting the gradient of O d ( m ) to zero 4 and solving for m ,

$$
0 = ∇O d ( m ) = G ⊤ C - 1 e ( d obs - Gm ) = G ⊤ C - 1 e d obs - G ⊤ C - 1 e Gm , (2.22)
$$

which leads to

$$
G ⊤ C - 1 e Gm = G ⊤ C - 1 e d obs . (2.23)
$$

The matrix G   C − 1 e G is at least positive semidefinite, but there is no guarantee that this matrix has an inverse. In case the inverse does not exist, we may have none or an infinite number of solutions. Nevertheless, we can

# 2.3 Maximum a Posteriori

The ML estimate focuses solely on maximizing the likelihood function based on the observed data without considering any prior information about the problem. Fortunately, Bayes’ rule provides a way to combine information from the data with prior beliefs about the distribution of model parameters.

Let p ( m , d obs ) denote the joint distribution of m and d obs . Recall from Bayes’ rule (Appendix C, Section C.3):

$$
p ( m | d obs ) = p ( m , d obs ) p ( d obs ) = p ( d obs | m ) p ( m ) p ( d obs ) = L ( m ) p ( m ) p ( d obs ) = L ( m ) p ( m ) ∫ L ( m ) p ( m ) d m (2.24)
$$

or

$$
p ( m | d obs ) = const ×L ( m ) p ( m ) . (2.25)
$$

Now, let the prior PDF of m be a multivariate Gaussian, p ( m ) = N ( m pr , C m ). In this case, p ( m ) assumes the form

$$
p ( m ) = 1 [(2 π ) N m det C m ] 1/2 exp { - 1 2 ( m - m pr ) ⊤ C - 1 m ( m - m pr ) } , (2.26)
$$

where m pr is the prior mean and C m is the prior covariance of m . Using the expressions obtained for ( m ) (2.8) and ( m ) (2.26) in

L p (2.25) results in

$$
p ( m | d obs ) = const × exp { - 1 2 ( d obs - g ( m )) ⊤ C - 1 e ( d obs - g ( m )) } × exp { - 1 2 ( m - m pr ) ⊤ C - 1 m ( m - m pr ) } = const × exp { - 1 2 ( d obs - g ( m )) ⊤ C - 1 e ( d obs - g ( m )) - 1 2 ( m - m pr ) ⊤ C - 1 m ( m - m pr ) } = const × exp {-O ( m ) } . (2.27)
$$

In this expression, O ( m ) is the total objective function defined as

$$
O ( m ) ≡ O d ( m ) + O m ( m ) (2.28)
$$

with

and

$$
O d ( m ) = 1 2 ( d obs - g ( m )) ⊤ C - 1 e ( d obs - g ( m )) (2.29)
$$

$$
O m ( m ) = 1 2 ( m - m pr ) ⊤ C - 1 m ( m - m pr ) . (2.30)
$$

The maximum a posteriori (MAP) estimate is defined as the model m that maximizes p ( m | d obs ). This is equivalent to minimizing O ( m ), i.e.,

$$
m map = arg min m O ( m ) . (2.31)
$$

# Remark 2.3: Objective Function

- 1. The functional O ( m ) defined in Eq. (2.28) includes two components: O d ( m ), representing the data-mismatch part, and O m ( m ), representing the model-mismatch part. Therefore, minimizing O ( m ) seeks a compromise between adjusting m to match the data while maintaining its proximity to m pr . In essence, it aims for the smallest changes in m required to assimilate the observations.
- 2. In reservoir data assimilation problems, typically, the number of model parameters greatly exceeds the number of observations ( N m   N d ). This makes the problem of minimizing the mismatch between predicted and observed data ill-posed, and some regularization is often needed. Fortunately, O ( m ), which was obtained from a direct application of Bayes’ rule, already contains a built-in regularization term: O m ( m ) (see Appendix B, Section B.4 for a short discussion on regularization methods).


# 2.3.1 Linear Case

For the linear case, we have g ( m ) = Gm and the objective function becomes

$$
O ( m ) = 1 2 ( d obs - Gm ) ⊤ C - 1 e ( d obs - Gm ) + 1 2 ( m - m pr ) ⊤ C - 1 m ( m - m pr ) , (2.32)
$$

whose minimum can be computed analytically. Setting the gradient of O ( m ) to zero leads to

$$
0 = ∇O ( m ) (2.33) = - G ⊤ C - 1 e ( d obs - Gm ) + C - 1 m ( m - m pr ) = - G ⊤ C - 1 e ( d obs - Gm + Gm pr - Gm pr ) + C - 1 m ( m - m pr ) = - G ⊤ C - 1 e ( d obs - Gm pr ) + ( C - 1 m + G ⊤ C - 1 e G ) ( m - m pr ) .
$$

Hence,

$$
( G ⊤ C - 1 e G + C - 1 m ) ( m - m pr ) = G ⊤ C - 1 e ( d obs - Gm pr ) . (2.34)
$$

Let

then Eq. (2.34) becomes

$$
B ≡ G ⊤ C - 1 e G + C - 1 m , (2.35)
$$

$$
B ( m - m pr ) = G ⊤ C - 1 e ( d obs - Gm pr ) . (2.36)
$$

Note that B is positive definite because C − 1 m is positive definite and G   C − 1 e G is at least positive semidefinite. Therefore, we can solve for m . Calling this result as m map results in

$$
m map = m pr + B - 1 G ⊤ C - 1 e ( d obs - Gm pr ) . (2.37)
$$

The MAP estimate in Eq. (2.37) assumes a Gaussian prior PDF, p ( m ), and a linear relationship between data and model, g ( m ) = Gm . Under these assumptions, the posterior PDF, p ( m | d obs ), is also Gaussian [428]. To demonstrate this, it suffices to write the second-order Taylor series expansion of O ( m ) around m map :

$$
O ( m ) = O ( m map ) + [ ∇O ( m )] ⊤ m map ( m - m map ) + 1 2 ( m - m map ) ⊤ ∇ { [ ∇O ( m )] ⊤ m map } ( m - m map ) , (2.38)
$$

and note that

$$
∇ [ O ( m )] = 0 .
$$

$$
m map (2.39)
$$

The Hessian ∇   [ ∇O ( m )]     is given by

$$
∇ { [ ∇O ( m )] ⊤ } = ∇ { [ - G ⊤ C - 1 e ( d obs - Gm ) + C - 1 m ( m - m pr ) ] ⊤ } = ∇ { - ( d obs - Gm ) ⊤ C - 1 e G +( m - m pr ) ⊤ C - 1 m } = ∇ { - ( d obs - Gm ) ⊤ C - 1 e G } + ∇ { ( m - m pr ) ⊤ C - 1 m } = ∇ { m ⊤ G ⊤ C - 1 e G } + ∇ { m ⊤ C - 1 m } = ∇ m ⊤ ( G ⊤ C - 1 e G ) + ∇ ( G ⊤ C - 1 e G ) ⊤ m + ∇ m ⊤ C - 1 m + ∇ ( C - 1 m ) ⊤ m = G ⊤ C - 1 e G + C - 1 m = B . (2.40)
$$

We used the fact that C m is symmetric positive definite, which means that C − 1 m = C −  m to obtain Eq. (2.40). This result shows that the Hessian matrix is equal to B defined in Eq. (2.35), which is constant (independent of m ). Hence, there are no higher-order terms in the Taylor series and the quadratic form

$$
O ( m ) = O ( m map ) + 1 2 ( m - m map ) ⊤ B ( m - m map ) (2.41)
$$

is exact. Recall that

Hence

$$
p ( m | d obs ) = const × exp {-O ( m ) } . (2.42)
$$

$$
p ( m | d obs ) = const × exp { -O ( m map ) - 1 2 ( m - m map ) ⊤ B ( m - m map ) } = const × exp {-O ( m map ) } × exp { - 1 2 ( m - m map ) ⊤ B ( m - m map ) } = const × exp { - 1 2 ( m - m map ) ⊤ B ( m - m map ) } . (2.43)
$$

The last result shows that p ( m | d obs ) is Gaussian with mean equals to m map and covariance given by

$$
C m c = B - 1 = ( G ⊤ C - 1 e G + C - 1 m ) - 1 . (2.44)
$$

We use the subscript c to denote that C m c is the covariance for the conditional ( a posteriori ) vector of model parameters.

The formulas derived for the MAP estimate and the posterior covariance involve the inversion of a N m × N m matrix. We can rewrite these expressions in a more convenient way using the Sherman-Morrison-Woodbury (A.9) 5 formula as

and

$$
m map = m pr + ( C - 1 m + G ⊤ C - 1 e G ) - 1 G ⊤ C - 1 e ( d obs - Gm pr ) = m pr + C m G ⊤ ( C e + GC m G ⊤ ) - 1 ( d obs - Gm pr ) (2.45)
$$

$$
C m c = ( G ⊤ C - 1 e G + C - 1 m ) - 1 = C m - C m G ⊤ ( C e + GC m G ⊤ ) - 1 GC m . (2.46)
$$

The second line in Eqs. (2.45) and (2.46) involve the inversion of N d × N d matrices. Therefore, these forms are preferable when N d &lt; N m , which is the typical case in reservoir data assimilation applications.

# 2.3.1.1 Example: Porosity of a Rock Sample

Consider the problem of estimating the porosity of a rock sample combining a prior information that φ ∼ N ( φ pr ,σ 2 pr ) and a measurement d obs ∼ N ( φ obs ,σ 2 e ). In this case, the posterior distribution of the porosity corresponds to the Gaussian distribution

$$
p ( φ | φ obs ) = N ( φ map , σ 2 post ) . (2.47)
$$

φ map and σ 2 post can be obtained by the direct application of the expressions developed for m map (2.45) and C m c (2.46):

and

$$
φ map = φ pr + σ 2 pr σ 2 e + σ 2 pr ( φ obs - φ pr ) (2.48)
$$

$$
σ 2 post = σ 2 pr - σ 4 pr σ 2 e + σ 2 pr . (2.49)
$$

5 See, for example, Oliver et al. [334, Chap. 7] for the algebraic steps to obtain (2.45) and (2.46).

Sometimes, we use the ratio between the posterior and prior variances (normalized variance) as an approximate measure of the uncertainty reduction [334]. From (2.49), the normalized variance, NV, is

$$
NV = σ 2 post σ 2 pr = 1 - σ 2 pr σ 2 pr + σ 2 e < 1 , (2.50)
$$

which means that we observe an uncertainty reduction due to the assimilation of φ obs . Also note that if we have a perfect (noiseless) measurement, i.e., σ e = 0, the normalized variance collapses to zero. Conversely, if we assume an infinitely noisy observation, i.e., σ e → ∞ , we obtain φ post → φ pr and NV → 1, which means that there is no uncertainty reduction assimilating a non-informative datum.

# 2.3.1.2 Example: Porosity of a Rock Sample Effect of Non-Diagonal Data-Error Covariance

Consider the same problem but with two measurements of porosity. For the sake of this illustration, assume that both measurements gave the same observed value φ obs . Moreover, assume that the data-error covariance matrix has the form 2 2

$$
C e = [ σ 2 e ρσ 2 e ρσ 2 e σ 2 e ] , (2.51)
$$

where ρ is the correlation coefficient between the errors of the two observations. In this case, we obtain the following expressions for the posterior mean and NV

$$
φ post ( ρ ) = φ pr + 2 σ 2 pr 2 σ 2 pr + σ 2 e (1 + ρ ) ( φ obs - φ pr ) , (2.52)
$$

$$
NV ( ρ ) = 1 - 2 σ 2 pr 2 σ 2 pr + σ 2 e (1 + ρ ) . (2.53)
$$

For ρ = 1, i.e., the errors in the two observations are perfectly correlated, we have

and

$$
φ post ( ρ = 1) = φ pr + σ 2 pr σ 2 pr + σ 2 e ( φ obs - φ pr ) (2.54)
$$

$$
NV ( ρ = 1) = 1 - σ 2 pr σ 2 pr + σ 2 e , (2.55)
$$

which are the same results for the assimilation of a single measurement. To provide a more concrete example, let us consider the following numerical values: φ pr = 0 . 20, σ 2 pr = 0 . 0025, φ obs = 0 . 30, and σ 2 e = 0 . 0025. Fig. 2.1

shows the plots of φ post and NV as a function of ρ . The figure clearly shows that increasing ρ leads to an increase in NV, indicating a reduction in the weight of the measurements. When ρ approaches 1, the problem becomes equivalent to assimilating a single measurement.

0.268

0.550

![](<ensemble_data_assimilation_e-book_version_images/imageFile13.png>)

0.267

0.500

0.264

0.500

Nomralized variance

Posterior mean

0.260

0.450

0.256

0.400

0.252

0.350

0.333

0.250

0.248 0

0.300 1

0

0.2

0.4

0.6

0.8

1

Correlation coefficient

Fig. 2.1: Posterior mean and normalized variance as a function of the correlation coefficient between the observation error of two measurements. Example 2.3.1.2. Reproduced from Emerick and Neto [124] with permission from Elsevier.

# 2.3.1.3 Example: Porosity and Permeability of a Rock Sample

Consider the same rock sample problem, but with the goal of estimating the porosity and the logarithm of permeability simultaneously, m = [ φ ln κ ]   , from a single measurement of porosity. Assume the prior mean and covariance have the forms

$$
m pr = [ φ pr (ln κ ) pr ] (2.56)
$$

and

$$
C m = [ σ 2 φ ρσ φ σ ln κ ρσ φ σ ln κ σ 2 ln κ ] = [ c 11 c 12 c 21 c 22 ] . (2.57)
$$

Because there is only a porosity measurement, the sensitivity matrix is

$$
G = [ 1 0 ] . (2.58)
$$

The MAP estimate becomes

$$
m map = m pr + C m G ⊤ ( C e + GC m G ⊤ ) - 1 ( d obs - Gm pr ) = [ φ pr (ln κ ) pr ] + [ c 11 c 12 c 21 c 22 ][ 1 0 ]( σ 2 e + [ 1 0 ] [ c 11 c 12 c 21 c 22 ][ 1 0 ]) - 1 × ( φ obs - [ 1 0 ] [ φ pr (ln κ ) pr ]) = ⎡ ⎢ ⎣ φ pr + σ 2 φ σ 2 e + σ 2 φ ( φ obs - φ pr ) (ln κ ) pr + ρσ φ σ ln κ σ 2 e + σ 2 φ ( φ obs - φ pr ) ⎤ ⎥ ⎦ . (2.59)
$$

The posterior covariance becomes

$$
C m c = C m - C m G ⊤ ( C e + GC m G ⊤ ) - 1 GC m = ⎡ ⎢ ⎣ σ 2 φ ( 1 - σ 2 φ σ 2 e + σ 2 φ ) ρσ φ σ ln κ ( 1 - σ 2 φ σ 2 e + σ 2 φ ) ρσ φ σ ln κ ( 1 - σ 2 φ σ 2 e + σ 2 φ ) σ 2 ln κ ( 1 - ρ 2 σ 2 φ σ 2 e + σ 2 φ ) ⎤ ⎥ ⎦ . (2.60)
$$

It is interesting to analyze some particular cases:

# Case 1: uncorrelated porosity and log-permeability

In this case, the prior correlation coefficient between φ and ln κ is ρ = 0. The MAP estimate and the posterior covariance become

$$
m map = [ φ pr + σ 2 φ σ 2 e + σ 2 φ ( φ obs - φ pr ) (ln κ ) pr ] (2.61)
$$

and

$$
C m c = [ σ 2 φ ( 1 - σ 2 φ σ 2 e + σ 2 φ ) 0 0 σ 2 ln κ ] , (2.62)
$$

which means that the assimilation of φ obs does not reduce the uncertainty in ln κ .

Case 2: perfect correlation between porosity and log-permeability If ρ = 1, the posterior covariance become

$$
C m c = ( 1 - σ 2 φ σ 2 e + σ 2 φ ) [ σ 2 φ σ φ σ ln κ σ φ σ ln κ σ 2 ln κ ] = a C m . (2.63)
$$

Hence, for ρ = 1 all elements of C m are updated by the same amount, a . Note that the determinant of C m c is

$$
det C m c = a [ σ 2 φ σ 2 ln κ - ( σ φ σ ln κ ) ( σ φ σ ln κ ) ] = 0 , (2.64)
$$

which means that C m c is singular. This result shows that there was only one degree of freedom as the observation of porosity resolves porosity and permeability simultaneously.

# Case 3: infinitely noisy data

If σ e → ∞ , we have m map → m pr and C m c → C m . Thus, p ( m | d obs ) → p ( m ), which means that there is no reduction in uncertainty.

# Case 4: perfect (noiseless) data

If σ e = 0 the posterior covariance reduces to

$$
C m c = [ 0 0 0 σ 2 ln κ ( 1 - ρ 2 ) ] , (2.65)
$$

which is singular. Therefore, it is no longer possible to assimilate another observation of porosity because there is no uncertainty left and

$$
m map = [ φ obs (ln κ ) pr - ρσ ln κ σ φ ( φ obs - φ pr ) ] . (2.66)
$$

# 2.3.1.4 Example: Porosity Distribution in a Core Sample

In the previous examples, we considered the estimation of a single value of porosity for a rock sample based on a measurement and prior information. Now, consider a similar situation, but for a core sample discretized in 50 (equally sized) gridblocks. Assume the prior mean is constant for all gridblocks with value m pr ,i = 0 . 25. Moreover, assume that the prior covariance can be modeled with a spherical covariance function with constant prior variance σ pr = 0 . 0025 and range of L = 10 gridblocks.

$$
C ( h ) = σ 2 pr { 1 - 3 h 2 L + h 3 2 L 3 for 0 ≤ h ≤ L 0 for h > L (2.67)
$$

For this example, assume that we have ten equally spaced porosity measurements with σ e = 0 . 005. Fig. 2.2a shows the prior mean, the mean ± three prior standard deviations, and the porosity measurements. The ground truth of porosity is also presented in this figure. Using Eqs. (2.45) and (2.46), we can compute the values of the MAP estimate and posterior variances (Fig. 2.2b). This figure shows that the MAP estimate, which represents the posterior mean, is very smooth compared to the ground truth. This is a consequence of the minimization of Eq. (2.28), which results in a compromise between data matches and changes in m from the prior, which is smooth. Fig. 2.2b also demonstrates that the posterior uncertainty in the porosity estimate is minimal at the measurement locations and maximal between them.





![](<ensemble_data_assimilation_e-book_version_images/imageFile14.png>)





























 

 

�











�











 U GE RF 

 U GE RF 

(a)

Prior

(b)

MAP

Fig. 2.2: Prior and MAP estimate of porosity in a core sample. The solid red line is the ground truth. The red circles are the observations. The dashed lines are the prior mean in (a) and MAP estimate in (b). The dotted lines correspond to the mean or MAP ± three standard deviations. Example 2.3.1.4.

# 2.3.2 Nonlinear Case

When the forward model, g ( m ), exhibits nonlinearity with respect to the parameter vector m , the posterior PDF deviates from a Gaussian distribution. In this situation, the posterior may manifest multiple modes, with each mode corresponding to a distinct local minimum of the objective function O ( m ). Furthermore, O ( m ) can possess several global minima, thereby giving rise to multiple MAP estimates.

In the context of nonlinearity, computing the MAP estimate entails solving a nonlinear minimization problem. In practical applications, the effectiveness of this process is greatly influenced by the performance of the optimization algorithm. For instance, in cases where local minima exist, relying solely on a derivative-based algorithm may not guarantee convergence to an actual MAP estimate.

# 2.3.2.1 Example: Permeability in a Single Phase Flow

Consider the one-dimensional horizontal reservoir with single-phase flow introduced in [128]. The reservoir model is discretized into 300 gridblocks with a single production well situated at the 300th gridblock. Observations consist of pressure measurements taken over a sequence of drawdown and build-up periods. The model parameters under consideration are the log-permeabilities assigned to each gridblock. The prior value for logpermeability is 5 ln-mD for all gridblocks.

Fig. 2.3 shows the prior mean and the MAP estimate obtained by the minimization of Eq. (2.28) using a quasi-Newton [350] method and adjoint

 

![](<ensemble_data_assimilation_e-book_version_images/imageFile15.png>)



   R SHUPHDE   W 

�

�



 

�





  U GE RF 







���������

Fig. 2.3: True, prior, and MAP estimate of log-permeability in a single-phase flow. The red line represents the ground truth, the dashed line represents the MAP estimate, and the solid gray line represents the prior mean. Example 2.3.2.1. Reproduced from Emerick and Reynolds [128] with permission from Springer Nature.

# 2.3.2.2 Example: Permeability in a Two-Phase Flow

Consider a data assimilation problem on a single-layer reservoir model with a two-phase (oil-water) flow. Fig. 2.4a shows the ground truth for the values of log-permeability. This figure also indicates the position of four production and two water injection wells. The prior mean corresponds to a constant value of log-permeability of 5 ln-mD. The ML and MAP estimates were obtained for this problem minimizing Eqs. (2.10) and (2.28), respectively using a quasi-Newton [350] method and adjoint gradients [259].

Fig. 2.4b shows that the lack of regularization resulted in a completely unrealistic permeability field for a ML estimate, although the model is consistent with data as illustrated in Fig. 2.5. The regularization introduced by the term O m ( m ) ensured a smooth MAP estimate (Fig. 2.4c).

6 Chapter 3 presents an overview of optimization methods used in the context of reservoir data assimilation.

(a)

True

8.00

![](<ensemble_data_assimilation_e-book_version_images/imageFile9.png>)

7.00

6.00

5.00

4.00

3.00

2.00

1.00

(b)

ML

8.00

7.00

6.00

5.00

4.00

3.00

2.00

1.00

(c)

MAP

8.00

8.00

7.00

7.00

6.00

6.00

5.00

5.00

4.00

4.00

3.00

3.00

2.00

2.00

1.00

1.00

Fig. 2.4: True, ML, and MAP estimates of log-permeability in a two-phase flow. Black circles corresponds to the position of oil producing wells and blue circles the position of water injection wells. Example 2.3.2.2.

![](<ensemble_data_assimilation_e-book_version_images/imageFile17.png>)

800

Water Rate (bbl/day)

600

400

200

0

0

500

1000

1500

2000

Time (days)

Fig. 2.5: Water production rate in one of the wells of the two-phase flow example. White circles are the observations, solid black curve corresponds to the MAP estimate, gray curve corresponds to ML estimate, and dashed line corresponds to the prior model. Example 2.3.2.2.

# 2.3.3 Data and Model Errors II

Section 2.2.2 examined the case where data and model errors are additive with zero mean. In this scenario, the equations derived for the ML and MAP estimate can be used with C e representing the total data-error covariance, i.e.,

$$
C e = C e g + C e d . (2.68)
$$

This section considers a less restrictive assumption following Evensen [141]. Rather than assuming an additive model error, we assume that the predicted data vector, d , takes the form

$$
d = g ( m , e g ) . (2.69)
$$

This condition is a more general representation of model errors because the predicted data are nonlinear functions of m and e g . Such scenarios are not uncommon in practical applications. For instance, Evensen and Eikrem [143] points out a typical situation in petroleum reservoir simulation where observed liquid rates are imposed to control the wells during the historical period. In this case, the measurement errors in liquid rates introduce nonlinear perturbations in the predicted data.

Assuming that the prior PDFs of m and e g are independent,

the joint PDF becomes

$$
p ( m , e g ) = p ( m ) p ( e g ) , (2.70)
$$

$$
p ( d , m , e g ) = δ ( d - g ( m , e g )) p ( m ) p ( e g ) , (2.71)
$$

where δ ( d − g ( m , e g )) is the Dirac delta function. The likelihood function for the observations given

the predictions is

$$
L ( d ) = p ( d obs | d ) . (2.72)
$$

Thus, the joint posterior PDF becomes

$$
p ( d , m , e g | d obs ) ∝ p ( d obs | d ) δ ( d - g ( m , e g )) p ( m ) p ( e g ) . (2.73)
$$

Because d is a function of m and e g , we can compute the marginal PDF

$$
p ( m , e g | d obs ) ∝ ∫ p ( d obs | d ) δ ( d - g ( m , e g )) p ( m ) p ( e g ) d d = p ( d obs | g ( m , e g )) p ( m ) p ( e g ) . (2.74)
$$

Eq. (2.74) gives the posterior joint PDF of m and e g given the observations. Assuming Gaussian priors

and

leads to

$$
p ( m ) = N ( m pr , C m ) , (2.75)
$$

$$
p ( e g ) = N ( e g, pr , C e g ) , (2.76)
$$

$$
p ( d obs | g ( m , e g )) = N ( g ( m , e g ) - d obs , C e d ) (2.77)
$$

$$
p ( m , e g | d obs ) ∝ exp { - 1 2 ( m - m pr ) ⊤ C - 1 m ( m - m pr ) - 1 2 ( e g - e g, pr ) ⊤ C - 1 e g ( e g - e g, pr ) - 1 2 ( g ( m , e g ) - d obs ) ⊤ C - 1 e d ( g ( m , e g ) - d obs ) } . (2.78)
$$

Eq. (2.78) assumed that m and e g are independent. This condition can be relaxed defining an augmented vector y   =   m   e   g   and writing the covariance as C C

$$
C y = [ C m C m , e g C e g , m C e g ] . (2.79)
$$

Hence

$$
p ( y | d obs ) ∝ exp { - 1 2 ( y - y pr ) ⊤ C - 1 y ( y - y pr ) - 1 2 ( g ( y ) - d obs ) ⊤ C - 1 e d ( g ( y ) - d obs ) } . (2.80)
$$

This expression represents the joint posterior, which can be used to compute the MAP estimate, y map , or to generate samples with the methods discussed in the sequence of this book. In this formulation, we estimate simultaneously the model parameters m and model errors e g . However, because e g varies with time, the estimated values are valid only for the historical period. They cannot be directly applied to the forecast period.

# 2.4 Data Assimilation as a Sampling Problem

Data assimilation is frequently characterized as an ill-posed inverse problem due to the fact that the quantity of independent data accessible is substantially less than the number of uncertain parameters. Consequently, there exists an infinite number of combinations of these parameters capable of generating models that can match the observations within a tolerance range. Furthermore, the available data are always inaccurate and occasionally inconsistent. As a result, reservoir models are built under conditions of significant uncertainty, leading to inherently uncertain predictions.

Bayesian statistics offers a straightforward framework for handling uncertainty. Bayes’ rule enables us to establish the posterior PDF for model parameters based on field measurements. Despite our ability to formulate these PDF expressions, they often have limited practical utility. Practitioners truly seek access to models conditioned on observations, allowing them to make performance predictions under various operational conditions and informed decisions.

The MAP estimate represents a mode of this distribution. However, a single model is insufficient for a useful characterization of uncertainty. Consequently, sampling the PDF emerges as the practical solution for quantifying uncertainty. If a collection of realizations for the model parameter vector serves as a set of samples drawn from the posterior PDF, then an accurate evaluation of uncertainty in specific outcomes of model predictions can be achieved by generating predictions with each model and constructing statistics for the resulting set of outcomes.

For example, consider the problem of computing the expectation of g ( m ). By definition ∞

$$
E [ g ( m )] = ∫ ∞ -∞ g ( m ) p ( m ) d m , (2.81)
$$

where p ( m ) is the PDF of m . Monte Carlo methods evaluate E [ g ( m )] by drawing N e samples from p ( m ) and approximating the integral as

$$
E [ g ( m )] ≈ 1 N e N e ∑ j =1 g ( m j ) . (2.82)
$$

If the samples { m j } are independent, the Law of Large Numbers 7 ensures that the approximation converges as N e → ∞ (we control the accuracy of our estimate by increasing N e ). It is required, however, that { m j } are generated from a process that draws samples from p ( m ) in the correct proportions 8 .

# 2.4.1 Sampling in the Linear Case

Let’s first analyze the problem of sampling from a multivariate prior Gaussian distribution and the posterior for the case where the predicted data are linearly related to the model 9 .

# 2.4.1.1 Sampling the Prior PDF

Let the prior PDF of m be a multivaraite Gaussian, i.e., p ( m ) = N ( m pr , C m ), in which case we can write

7 The law of large numbers is a fundamental theorem in probability and statistics that states that as the size of a sample increases, the sample mean converges to the expected value of the underlying distribution. 8

Note that the samples don’t need to be “equiprobable.” The requirement is that they are samples drawn from p ( m ). 9

Practical data assimilation is typically nonlinear. However, the solutions for linear problems serve as the basis for developing methods for the nonlinear.

$$
p ( m ) = const × exp { - 1 2 ( m - m pr ) ⊤ C - 1 m ( m - m pr ) } . (2.83)
$$

There are various methods available to sample this PDF. The simplest procedure is based on the square root of C m . In this case, a sample from p ( m ) is given by

$$
m j = m pr + C 1/2 m z j , (2.84)
$$

where, z j ∼ N ( 0 , I ), i.e., z j is a vector of random normal deviates. C 1/2 m is a square root of C m (see Appendix A, Section A.6). In order to show that m generated with Eq. (2.84) is a sample from

j N ( m pr , C m ), suffices to show that E [ m j ] = m pr and C [ m j ] = C m . These results follow directly from the definitions of expectation and covariance

$$
E [ m j ] = E [ m pr + C 1/2 m z j ] = E [ m pr ] + C 1/2 m E [ z j ] = m pr (2.85)
$$

$$
C [ m j ] = E [ ( m j - E [ m j ]) ( m j - E [ m j ]) ⊤ ] = E [ ( m j - m pr ) ( m j - m pr ) ⊤ ] = E [ ( C 1/2 m z j )( C 1/2 m z j ) ⊤ ] = E [ C 1/2 m z j z ⊤ j C ⊤ / 2 m ] = C 1/2 m E [ z j z ⊤ j ] C ⊤ / 2 m = C 1/2 m C ⊤ / 2 m = C m . (2.86)
$$

Any valid square root of C m can be used in Eq. (2.84). Often, the Cholesky decomposition is employed, in which case we write

$$
C m = LL ⊤ , (2.87)
$$

where L is a lower triangular matrix and C 1/2 m = L .

Unfortunately, for large models, the factorization of C m becomes unfeasible. There are more efficient alternatives [454]. However, in reservoir modeling, we typically resort to geostatistical methods, in which case the most common is the sequential Gaussian simulation (SGS) method [171, 104].

# 2.4.1.2 Example: Cross-covariances

Often there are prior correlations between properties, e.g., porosity and logpermeability. In this case, we have non-zero cross-covariance terms in C m , i.e.,

$$
C m = [ C φ C φ, ln κ C ln κ,φ C ln κ ] , (2.88)
$$

where C φ, ln κ = C   ln κ,φ . One problem is ensuring

that the cross-covariance matrix is positivedefinite. A fairly simple way to do this is to use the screening hypothesis [471], in which case the entries of the cross-covariance matrices are computed as

$$
C [ φ i , ln κ j ] = C [ln κ j , φ i ] = ρσ φ i σ ln κ j C [ln κ j ] = ρσ ln κ j σ φ i C [ φ i ] . (2.89)
$$

Consider the following prior information about the porosity and logpermeability of a rock sample:

-  p ( φ ) = N (0 . 2 , 0 . 05 2 ). 2
-  p (ln κ ) = N (1 , 0 . 5 ).
-  ρ = 0 . 8.


Let m = [ φ ln κ ]   . The prior covariance of m is

$$
C m = [ σ 2 φ ρσ φ σ ln κ ρσ φ σ ln κ σ 2 ln κ ] = [ 0 . 05 2 0 . 8 × 0 . 05 × 0 . 5 0 . 8 × 0 . 05 × 0 . 5 0 . 5 2 ] = [ 0 . 0025 0 . 02 0 . 02 0 . 25 ] . (2.90)
$$

Because φ and ln κ are correlated, we need to compute C 1/2 m to drawn samples from p ( φ, ln κ ). This can be done using the Cholesky decomposition. The Cholesky of a 2 × 2 is trivial to compute. First, we write

$$
C m = LL ⊤ = [ a 0 b c ][ a b 0 c ] = [ a 2 ab ab b 2 + c 2 ] = [ 0 . 0025 0 . 02 0 . 02 0 . 25 ] . (2.91)
$$

Hence a = 0 . 05, b = 0 . 4 and c = 0 . 3.

Now we can drawn samples using

$$
m = m pr + C 1/2 m z , (2.92)
$$

where m pr = [0 . 2 1]   and z ∼ N ( 0 , I ). Fig. 2.6 shows a cross-plot between φ and ln κ obtained using Eq. (2.92) illustrating that the resulting samples are correlated.

2.5

![](<ensemble_data_assimilation_e-book_version_images/imageFile18.png>)

2

Log-permeability

1.5

1

0.5



= 0.805

0

-0.5

0.05

0.1

0.15

0.2

0.25

0.3

0.35

Porosity

Fig. 2.6: Cross-plot between porosity and log-permeability obtained with 100 correlated samples. Example 2.4.1.2.

# 2.4.1.3 Example: Porosity Realizations

Fig. 2.7 shows two samples from a multivariate Gaussian distribution used to model the spatial distribution of porosity in a 2D uniform grid with 100 × 100 gridblocks. These samples were generated using the Cholesky decomposition. The prior mean is assumed to be constant and equal to 0.2, and the prior standard deviation is 0.05. The covariance was computed using a spherical model (see Appendix C, Section C.4.3) with and without anisotropy.

# 2.4.1.4 Sampling the Posterior PDF

As discussed before, if the prior model is Gaussian and the relationship between model and data is linear, then the posterior PDF is also Gaussian with the form

$$
p ( m | d obs ) = const × exp { - 1 2 ( m - m map ) ⊤ C - 1 m c ( m - m map ) } . (2.93)
$$

We can use the same procedure described to sample the prior and compute the square root of C m c to generate samples from p ( m | d obs ). Nevertheless,

(a)

Isotropic

(b)

Anisotropic

0.30 0.30

0.30

0.25 0.25

����





0.20 0.20



����

0.15 0.15

���

 

0.10 

0.10



���

���

0.05 0.05





0.00 0.00

0.00







 3RURV W 







��������

0.30 0.30

![](<ensemble_data_assimilation_e-book_version_images/imageFile10.png>)

0.30

0.25 0.25

����

 

����

0.20 0.20



����

���

0.15 0.15

 



0.10 0.10



���

���

0.05 0.05





0.00 0.00

0.00





 3RURV W 







��������

Fig. 2.7: Porosity models sampled from a multivariate Gaussian using Cholesky decomposition of the prior covariance matrix. The isotropic case uses a covariance matrix with range corresponding to 30 gridblocks. The anisotropic case uses a major range of 40 and a minor of 20 gridblocks, rotated by 45 o . Example 2.4.1.3.

this approach is only practical when dealing with a low-dimensional model. Fortunately, there is an alternative method for generating conditional samples m c ,j ∼ N ( m map , C m c ) by solving the following optimization problem:

$$
m c ,j = arg min m O r ( m ) , (2.94)
$$

where O r ( m ) is a modified (randomized) objective function given by

$$
O r ( m ) = 1 2 ( d obs ,j - Gm ) ⊤ C - 1 e ( d obs ,j - Gm ) + 1 2 ( m - m j ) ⊤ C - 1 m ( m - m j ) . (2.95)
$$

Note the differences between the original O ( m ) and O r ( m ). In Eq. (2.95), we replaced d obs by a random sample d obs ,j ∼ N ( d obs , C e ) and m pr by a prior sample m j ∼ N ( m pr , C m ). The minimum of ( m ) can be obtained with the same procedure used

O r to derive m map . The resulting expressions are similar to the ones obtained

$$
m c ,j = ( C - 1 m + G ⊤ C - 1 e G ) - 1 ( C - 1 m m j + G ⊤ C - 1 e d obs ,j ) = m j + ( C - 1 m + G ⊤ C - 1 e G ) - 1 G ⊤ C - 1 e ( d obs ,j - Gm j ) = m j + C m G ⊤ ( C e + GC m G ⊤ ) - 1 ( d obs ,j - Gm j ) , (2.96)
$$

where m c ,j is a sample from the posterior. This procedure in known as randomized maximum likelihood (RML) [332].

In order to show that m c ,j ∼ N ( m map , C m c ), suffices to show that E [ m c ,j ] = m map and C [ m c ,j ] = C m c . For the expectation follows that

$$
E [ m c ,j ] = E [ ( C - 1 m + G ⊤ C - 1 e G ) - 1 ( C - 1 m m j + G ⊤ C - 1 e d obs ,j ) ] = E [ C m c ( C - 1 m m j + G ⊤ C - 1 e d obs ,j )] = C m c { C - 1 m E [ m j ] + G ⊤ C - 1 e E [ d obs ,j ] } = C m c { C - 1 m m pr + G ⊤ C - 1 e d obs } = m map . (2.97)
$$

The calculation of the covariance requires more steps, but it is relatively straightforward starting from the definition of covariances

$$
C [ m c ,j ] = E [ ( m c ,j - E [ m c ,j ]) ( m c ,j - E [ m c ,j ]) ⊤ ] = E [ ( m c ,j - m map ) ( m c ,j - m map ) ⊤ ] . (2.98)
$$

Let’s first develop an expression for m c ,j − m map :

$$
m c ,j - m map = C m c {( C - 1 m m j + G ⊤ C - 1 e d obs ,j ) - ( C - 1 m m pr + G ⊤ C - 1 e d obs )} = C m c { C - 1 m ( m j - m pr ) + G ⊤ C - 1 e ( d obs ,j - d obs ) } = C m c { C - 1 m C 1/2 m z m ,j + G ⊤ C - 1 e C 1/2 e z d ,j } .
$$

$$
(2.99)
$$

In (2.99), we used

$$
m j = m pr + C 1/2 m z m ,j (2.100)
$$

$$
d obs ,j = d obs + C 1/2 e z d ,j , (2.101)
$$

where both z m ,j and z d ,j are random vectors sampled from N ( 0 , I ). Now, we compute the cross product

Now, we compute the cross product

$$
( m c ,j - m map ) ( m c ,j - m map ) ⊤ = (2.102) = C m c { C - 1 m C 1/2 m z m ,j + G ⊤ C - 1 e C 1/2 e z d ,j } × { z ⊤ m ,j C ⊤ / 2 m C - 1 m + z ⊤ d ,j C ⊤ / 2 e C - 1 e G } C m c = C m c { C - 1 m C 1/2 m z m ,j z ⊤ m ,j C ⊤ / 2 m C - 1 m + C - 1 m C 1/2 m z m ,j z ⊤ d ,j C ⊤ / 2 e C - 1 e G + G ⊤ C - 1 e C 1/2 e z d ,j z ⊤ m ,j C ⊤ / 2 m C - 1 m + G ⊤ C - 1 e C 1/2 e z d ,j z ⊤ d ,j C ⊤ / 2 e C - 1 e G } C m c .
$$

Finally, we note that E   z m ,j z   m ,j   = I , E   z d ,j z   d ,j   = I and E   z m ,j z   d ,j   = E   z d ,j z   m ,j   = O (null matrix) because z m ,j and z d ,j are independent. The covariance becomes

$$
C [ m c ,j ] = E [ ( m c ,j - m map ) ( m c ,j - m map ) ⊤ ] = C m c { C - 1 m + G ⊤ C - 1 e G } C m c = C m c C - 1 m c C m c = C m c , (2.103)
$$

which completes the demonstration that m c ,j ∼ N ( m map , C m c ).

# 2.4.1.5 Example: Porosity Distribution in a Core Sample

Consider the same problem of Example 2.3.1.4. Instead of the MAP estimate, we can generate 100 samples of the prior using the square root method (Fig. 2.8a). For each prior realization, we applied Eq. (2.96) to obtain a posterior sample (Fig. 2.8b). Note that all posterior realizations are consistent with the observed data points. The average of the posterior realizations is an approximation of the MAP estimate (compare Figs 2.2 and 2.8b) 10 .

10 The average converges to the MAP as we increase the number of samples.





![](<ensemble_data_assimilation_e-book_version_images/imageFile20.png>)





























 

 

�











�











 U GE RF 

 U GE RF 

(a)

Prior

(b)

Posterior

Fig. 2.8: Prior and posterior realizations of porosity in a core sample. The solid red line is the ground truth. The red circles are the observations. The gray lines are samples from the prior (a) and posterior (b). The dashed lines are the average computed over the 100 samples. Example 2.4.1.5.

# Remark 2.4: Relation to Geostatistics

Geostatistics, as a statistical discipline, primarily focuses on analyzing spatial and temporal datasets. Its roots can be traced back to the early days when it was closely associated with interpolation techniques, particularly in the development of kriging methods [242, 295]. However, contemporary geostatistics has expanded well beyond the realms of basic interpolation. Modern geostatistics embraces a Bayesian framework, with its core objective being the generation of samples from complex, high-dimensional probability distributions. Notably, traditional geostatistical techniques like simple kriging and SGS find direct parallels in the linear-Gaussian context: simple kriging corresponds to the posterior mean a estimate, while models generated using SGS are akin to samples drawn from the posterior distribution.

a One important difference between kriging and the MAP estimate is the fact that in kriging, we typically assume that data are perfect. This is the so-called “hard data assumption.”

# 2.4.2 Sampling in the Nonlinear Case

In the nonlinear case, estimators such as mean and covariance are not enough to fully characterize the PDF, and there are no general analytical solutions. Moreover, apart from problems with low dimensionality, a “brutal force” exploratory sampling is unfeasible. This happens because high-dimensional

To illustrate this issue, consider the example of sampling from a multivariate Gaussian distribution m ∼ p ( m ) = N ( 0 , I ). In this standard Gaussian distribution, the mode is centered at the origin, suggesting that a significant portion of the probability mass should concentrate near this point. However, this expectation holds only in cases of very low dimensions. To quantify this behavior, we can compute the probability of a random vector m being within a distance of 1 from the origin, denoted as P ( m   m ≤ 1). We note that:

$$
m ⊤ m = N m ∑ i =1 m 2 i = x, (2.104)
$$

where x follows a chi-squared distribution with N m degrees of freedom (see Appendix C, Section C.1.18.4), i.e., x ∼ χ 2 ( N m ). Therefore, we can compute the probability P ( x = m   m ≤ 1) using the cumulative density function of χ 2 ( N m )

$$
P ( x ≤ 1) = 1 Γ ( N m 2 ) γ ( N m 2 , x 2 ) , (2.105)
$$

where Γ ( · ) represents the gamma function, and γ ( · , · ) denotes the incomplete gamma function. As illustrated in Fig. 2.9, we observe that the probability mass around the origin in a multivariate Gaussian distribution diminishes rapidly as we increase the dimensionality N m . For instance, with N m = 10, less than 10 − 3 of the probability mass lies within a radius of 1 from the origin. For N m = 20, this probability is on the order of 10 − 10 . For this reason, sampling high-dimensional PDFs can be very challenging.

In the context of reservoir data assimilation, we are interested in sampling the posterior PDF of model parameters given a set of measurements. However, the number of parameters can be extremely high; we may have problems with 10 7 parameters or even more. The number of observations is also high, often more than 10 3 data points. This means that the probability of getting a model consistent with the observation with a naive acceptancerejection algorithm is extremely low.

# 2.4.3 Markov Chain Monte Carlo

There are general sampling methods that can be used to sample p ( m | d obs ) in the nonlinear case. Among these methods, Markov chain Monte Carlo (MCMC) is perhaps the best known. In MCMC, a sequence of “states” is generated by simulating a Markov chain, where the probability of transition-

11 The term “curse of dimensionality” was originally coined by the mathematician Richard E. Bellman within the context of dynamic programming [33].

![](<ensemble_data_assimilation_e-book_version_images/imageFile21.png>)

 



   3UREDE   W 



 

  



 ' PHQV RQ





���������

Fig. 2.9: Probability of a random vector be at a distance less than one in a standard multivariate Gaussian distribution.

# 2.4.3.1 Metropolis-Hastings Algorithm

The foundation of many MCMC implementations rests upon the seminal work from Metropolis et al. [302] 13 , which introduced the concept of defining transition probabilities. In the Metropolis algorithm, the probability of transitioning from a state m to   m is computed as the product of the probability of proposing this transition, denoted as q ( m ,   m ), and the probability of accepting the proposal. Hastings [187] expanded the Metropolis algorithm, giving rise to what is now one of the most widely adopted MCMC techniques – the Metropolis-Hastings algorithm.  

Consider p ( m ) as the target PDF we aim to sample, and let q ( · , · ) represent a proposal PDF easy to sample from. As long as the proposal mechanism allows for reaching any state with p   ( m )   = 0 within a finite number of transitions, the states in the chain generated by the Metropolis-Hastings algorithm will eventually represent samples from p   ( m ), regardless of the initial state m 0 . Computing the acceptance probability, denoted as P ( m   ,   m   +1 ), only requires the evaluation of the target PDF up to its normalization constant.

̸

12 The body of literature dedicated to MCMC methods is extensive and wide-ranging. A good introduction discussion on MCMC methods is presented in [166]. 13

The Metropolis algorithm was selected as one of the ten algorithms that have had the greatest influence on the development and practice of science and engineering in the 20th Century – Cipra, B.A., The Best of the 20th Century: Editors Name Top 10 Algorithms , SIAM News (2000) [88].

The main challenge in MCMC, especially for high-dimensional problems, is the slow convergence. The selection of the proposal distribution is crucial, as a well-chosen proposal can greatly influence the acceptance rate of new states within the chain, thereby reducing the number of iterations needed to converge to the target distribution.

Pseudo-code 2.1 provides a concise summary of the Metropolis-Hastings MCMC algorithm.

# Pseudo-code 2.1: MCMC - Metropolis-Hastings

- 1. Set   = 0 (iteration index) and m   = m 0 (initial state).   +1     +1
- 2. Propose a new state   m from q ( m ,   m ). 3. Compute the probability of accepting the


proposed state

$$
P ( m ℓ , ̂ m ℓ +1 ) = min { 1 , q ( ̂ m ℓ +1 , m ℓ ) p ⋆ ( ̂ m ℓ +1 ) q ( m ℓ , ̂ m ℓ +1 ) p ⋆ ( m ℓ ) } . (2.106)
$$

  4. Sample u ∼ U [0 , 1]. If u ≤ P ( m   ,   m   +1 ), accept the new state, m   +1 =   m   +1 . Otherwise, repeat the old state, m   +1 = m   . Then add 1 to   and return to step 2.

In data assimilation, the target is the posterior PDF, p   ( m ) ≡ p ( m | d obs ). Therefore, evaluation of p   ( m ) requires the evaluation of the forward model, which can render the sampling process computationally prohibitive unless (1) the forward model is extremely fast, or (2) there is very few model parameters and/or few data points.

In practical reservoir data assimilation scenarios, MCMC techniques are frequently employed in conjunction with the substitution of the original forward model with a surrogate (proxy) model. In such cases, the quality of the sampling hinges on the surrogate’s capacity to replicate the nonlinearity inherent in the original forward model. However, the generation of reliable proxies can be very challenging for high-dimensional problems 14 .

# 2.4.4 Randomized Maximum Likelihood

RML was independently introduced by Kitanidis [239] and Oliver et al. [332] 15 as an approximate sampling method for nonlinear problems. Orig-

14 Chapter 3, Section 3.5 discusses the use of proxies in the context of reservoir data assimilation. 15

In a more recent publication, Bardsley et al. [28] proposed the “Randomize-ThenOptimize” method for sampling posterior distributions. This method is essentially identical to RML.

Pseudo-code 2.2 summarizes the RML process. Each sample obtained through RML requires the solution of an optimization problem. In theory, any optimization technique can be employed, provided it converges to a minimum of O r ( m ). However, practical experience suggests that an efficient implementation of RML requires highly efficient optimization methods, such as the ones based on derivatives (Chapter 3, Section 3.2).

Upon inspecting O r ( m ), it becomes evident that each RML sample tends to remain close to the prior realization unless the likelihood demands significant adjustments to the parameter values. This characteristic stands out as a distinctive advantage of the method, particularly when the prior realizations are derived from a rigorous geomodeling process. In this sense, the objective is to make the smallest changes in the model to honor the observations [328].

# Pseudo-code 2.2: RML

1. Sample m j ∼ N ( m pr , C m ). 2. Sample d ( d C ).

obs ,j ∼ N obs , e 3. Compute

Compute

$$
m c ,j = arg min m O r ( m ) , (2.107)
$$

where

$$
O r ( m ) = 1 2 ( d obs ,j - g ( m )) ⊤ C - 1 e ( d obs ,j - g ( m )) + 1 2 ( m - m j ) ⊤ C - 1 m ( m - m j ) . (2.108)
$$

# 2.4.5 Examples

# 2.4.5.1 Example: Linear Model

Consider a linear-Gaussian problem with three measurements and N m = 20 model parameters. Fig. 2.10a shows five prior samples along with the three

16 For linear-Gaussian problems, RML results in a correct sampling (as discussed in Section 2.4.1.4).

![](<ensemble_data_assimilation_e-book_version_images/imageFile22.png>)

3

3

1.5

1.5

0

0

-1.5

-1.5

-3 0

-3 0

0

5

10

15

20

0

5

10

15

20

(a)

Prior

(b)

MCMC

INTERNA

INTERNA

INTERNA

INTERNA

Fig. 2.10: Five prior and MCMC samples for a simple linear problem. The red circles are the observations and the lines are samples. Example. 2.4.5.1.

Using MCMC to sample the posterior can be computationally very expensive. However, sampling the prior tends to be relatively straightforward. This observation motivates the adoption of a procedure that goes beyond mere acceptance or rejection of proposals; instead, it corrects the proposals. This rationale underlies the concept of RML. Fig. 2.11a shows one realization from the prior and a hypothetical naive correction to this sample in order to match the observations. While this naive correction achieves the goal of matching the data, it compromises the notion of model plausibility. Furthermore, it offers no enhancements in predicting values at other locations. In contrast, RML produces smooth corrections to the prior realization that are consistent with the expected distribution of the property (Fig. 2.11b)

# 2.4.5.2 Example: Nonlinear Univariate Problem

Consider a single-parameter model with time evolution defined as

$$
g ( m,t ) = 1 - 9 2 ( m - 2 π 3 ) 2 +( t - 1) sin( m ) . (2.109)
$$

This problem is an extension of the synthetic problem tested in [332]. Assume a Gaussian prior PDF N (2 . 4 , 0 . 1) and five measurements corrupted with random error e ∼ N (0 , 0 . 01). The posterior PDF has the form

![](<ensemble_data_assimilation_e-book_version_images/imageFile23.png>)

3

3

1.5

1.5

0

0

-1.5

-1.5

-3 0

-3 0

0

5

10

15

20

0

5

10

15

20

(a)

Implausible

(b)

RML

INTERNA

INTERNA

INTERNA

INTERNA

Fig. 2.11: Implausible and RML corrections to a prior sample for a simple linear problem. The red circles are the observations. The black line is the prior and the gray line is the corresponding realization after corrections. Example. 2.4.5.1.

$$
p ( m | d obs ) = b exp ( - 1 2 ( m ℓ - 2 . 4 ) 2 0 . 1 - 1 2 N t ∑ t =1 ( d obs ,t - g ( m ℓ , t )) 2 0 . 01 ) , (2.110)
$$

where N t is the number of time steps. Fig. 2.12 presents histograms of the

model parameters obtained through the sampling of both the prior PDF and the posterior using MCMC and RML. Each plot also includes the actual posterior distribution for reference. It is worth noting that the posterior exhibits a bi-modal behavior, particularly pronounced after the assimilation of the first datum. As more data points are incorporated, one of the modes becomes more prominent. Just as a reference, the true value of m is 1.884, which is closer to the first mode of the posterior. The prior distribution was intentionally chosen with a mean closer to the second mode of the posterior.

MCMC utilized 50,000 proposals from the prior, resulting in a nearperfect sampling of the PDFs. The acceptance rates for the chains were 0.274 and 0.06 for the posteriors with one and five data points, respectively. In contrast, for RML, we obtained the samples by generating 3,000 realizations while minimizing the objective function (2.108). In this example, the minimization problem was solved using Brent’s method [350, Chap. 8]. For the first datum, RML was successful in capturing both modes of the posterior distribution, although not in the exact proportions. Notably, the region between the modes was under-sampled. After the fifth datum, RML over-sampled the mode of the distribution closer to the prior mean.

# 2.4.5.3 Example: Permeability in a Two-Phase Linear Flow

Emerick and Reynolds [131] proposed a benchmark problem to compare the sampling performance of ensemble-based methods. This problem entails es-

 

 

 

![](<ensemble_data_assimilation_e-book_version_images/imageFile24.png>)

 

 

 





































 





���







 

���

 







 

���

 









(a)

Prior 1st datum

(b)

MCMC 1st datum

(c)

RML 1st datum







 

 

 



















 





���







 

���

 







 

���

 









(d)

Prior 5th datum

(e)

MCMC 5th datum

(f)

RML 5th datum

Fig. 2.12: Prior, MCMC and RML sampling for a nonlinear univariate problem. The black curve in each plot corresponds to the correct posterior distribution. Example 2.4.5.2.

$$
̂ m ℓ +1 = m ℓ + C 1/2 m δ z , (2.111)
$$

  where δ z ∼ N ( 0 ,γ 2 I ), with γ = 0 . 05 representing the scaling factor. This proposal scheme resulted in an acceptance rate of 23%.

Fig. 2.13 presents the percentiles (p2, p25, p50, p75, and p98) of the resulting marginal posterior distributions of log-permeability obtained with MCMC and RML. Fig. 2.14 shows the corresponding distributions obtained for a forecasted water production rate. For RML, the optimizations were solved using a quasi-Newton method with adjoint gradients to generate 100 conditional realizations; more details can be found in the original publication. These figures show that MCMC and RML yield remarkably similar samplings of the posterior PDF.

![](<ensemble_data_assimilation_e-book_version_images/imageFile25.png>)

8

8

7

7

3 4 5 6 Log-permeability

3 4 5 6 Log-permeability

6

6

5

5

4

4

3

3

2 1

2 1

1

6

11

16 Gridblock

21

26

31

1

6

11

16 Gridblock

21

26

31

Gridblock

Gridblock

(a)

MCMC

(b)

RML

NTERNA

NTERNA

Fig. 2.13: Marginal log-permeability distributions for a two-phase linear flow. The red line represents the ground truth, the dashed line denotes the median, and the solid black lines correspond to the 25th and 75th percentiles. The outer bounding lines encompass the 2nd and 98th percentiles. Example 2.4.5.3. Reproduced from Emerick and Reynolds [131] with permission from Springer Nature.

![](<ensemble_data_assimilation_e-book_version_images/imageFile26.png>)

70

70

Water Rate (bbl/day)

Water Rate (bbl/day)

60

60

50

50

40

40

30

30

20

20

10

10

0 0

0 0

0

200

400

600

800

0

200

400

600

800

Time (days)

Time (days)

(a)

MCMC

(b)

RML

NTERNA

NTERNA

Fig. 2.14: Predicted water production rate. The red line represents the ground truth, the dashed line denotes the median, and the solid black lines correspond to the 25th and 75th percentiles. The outer bounding lines encompass the 2nd and 98th percentiles. Example 2.4.5.3. Reproduced from Emerick and Reynolds [131] with permission from Springer Nature.

# 2.4.5.4 Example: Two-Phase Flow in 2D Model

Consider a two-phase flow (oil and water) in a small 2D model discretized into 15 × 30 gridblocks. In this model, there are six producers and two water injection wells arranged in five-spot patterns, as illustrated in Fig. 2.15. The ground truth of log-permeability and the prior realizations were generated by sampling a multivariate Gaussian distribution with a constant mean of 5 ln-mD and a constant variance of 1 (ln-mD) 2 using the Cholesky decomposition method. The prior covariance was constructed using an exponential covariance function with ranges corresponding to 60 gridblocks in the major direction and five gridblocks in the minor direction, rotated by

The experiment involves the assimilation of oil and water production data for a period of 3900 days, with measurements every 150 days. The synthetic observations were obtained perturbing the data predicted by the model with the true log-permeability distribution (Fig. 2.15a) with random uncorrelated noise with standard deviation corresponding to 5% of the data values.

Starting from a constant prior mean, we obtained the MAP estimate by minimizing Eq. (2.28) using a quasi-Newton method and adjoint gradients. This process successfully recovered the high-permeability streak connecting one injector to two producers in the upper part of the model, as indicated in Fig. 2.15b. Figs. 2.15c–2.15e show three prior realizations while Figs. 2.15f–2.15h show the corresponding posteriors obtained with RML. The posterior realizations exhibit the expected structure with long-range permeability corridors.

Fig. 2.16 shows the predicted water production rate for three wells in the model, including a forecast period with an additional 3900 days of production. Each plot displays the observed data points, the predicted data obtained with the true log-permeability distribution, the MAP estimate, 100 prior realizations, and the corresponding 100 posterior realizations obtained with RML. Notably, there is significant variability in the predicted water breakthrough with the prior realizations. This occurs because these realizations were generated without any conditioning data at well locations, resulting in high-permeability channels appearing in different locations. This feature makes the data assimilation problem highly nonlinear despite the model’s simplicity. It is also noteworthy that the predicted water production obtained with the MAP estimate deviates significantly from the ground truth during the forecast period, especially for the first well. However, the range of predictions from the posterior realizations obtained with RML encompasses the true prediction.

# 2.5 Normalized Objective Function

A recurring question posed by data assimilation practitioners pertains to the criteria for determining the success of a data assimilation procedure. Evidently, the response to this question encompasses various facets of the process, including considerations related to model plausibility, proper quantification of uncertainty, and the quality of data matches. In fact, defining strict criteria for acceptance of a data assimilation study can be challenging (and often controversial). Experienced practitioners consistently emphasize the importance of aligning the study’s objectives with the criteria for evaluating its acceptability.

![](<ensemble_data_assimilation_e-book_version_images/imageFile27.png>)

7.00

7.00

7.00

7.00

6.56

6.56

6.56

6.56

6.11

6.11

6.11

6.11

5.67

5.67

5.67

5.67

5.22

5.22

5.22

5.22

4.78

4.78

4.78

4.78

4.33

4.33

4.33

4.33

3.89

3.89

3.89

3.89

3.44

3.44

3.44

3.44

3.00

3.00

3.00

3.00

(a)

True

(b)

MAP

(c)

Prior 1

(d)

Prior 2

7.00

7.00

7.00

7.00

6.56

6.56

6.56

6.56

6.11

6.11

6.11

6.11

5.67

5.67

5.67

5.67

5.22

5.22

5.22

5.22

4.78

4.78

4.78

4.78

4.33

4.33

4.33

4.33

3.89

3.89

3.89

3.89

3.44

3.44

3.44

3.44

3.00

3.00

3.00

3.00

(e)

Prior 3

(f)

RML 1

(g)

RML 2

(h)

RML 3

3.00

3.44

3.89

4.33

4.78

5.22

5.67

6.11

6.56

7.00

Fig. 2.15: True, MAP, and three prior and posterior realizations of log-permeability for a 2D model under two-phase flow. The posterior realizations were obtained with RML. Black circles indicate the position of producers and black triangles indicate the position of water injection wells. Example 2.4.5.4.

Among these aspects, the quality of data matches is perhaps the easiest to quantify, as it directly relates to the definition of the objective function minimized during data assimilation. However, a crucial question arises: What should be the acceptable value of the objective function following a successful data assimilation? Oliver et al. [334] observe that in the linear-Gaussian case, the value of 2 O ( m ) when evaluated at the MAP estimate follows a χ 2 distribution with N d degrees of freedom [428]. For large N d , the χ 2 distribution can be approximated by a Gaussian distribution with a mean of N d and a variance of 2 N d . Consequently, it is convenient to define a normalized objective function as





![](<ensemble_data_assimilation_e-book_version_images/imageFile28.png>)



���

       DWHUUDWH EE GD  

      DWHUUDWH EE GD  

          DWHUUDWH EE GD  

���

���

���

���

���

��

���

���

��

��

���

��

��

���

��

��

 

 

 

�







����

����



 

 

�







����

����



 

 

�







����

����



 

 

  7 PH GD V 

  7 PH GD V 

  7 PH GD V 

(a)

Well 1

(b)

Well 2

(c)

Well 3

Fig. 2.16: Water production rate in bbl/day for three wells. Red circles are the observations, red line the prediction with the true log-permeability distribution, black line the prediction from the MAP estimate. The gray and blue lines show the predictions from 100 prior and posterior realizations, respectively. The posterior realizations were obtained with RML. Example 2.4.5.4.

$$
O N ( m ) = O ( m c ) N d . (2.112)
$$

Based on the arguments presented in [334], the expected value of O N ( m map ) should be 1/2. For samples of the posterior, Oliver et al. [334] drop the multiplication by two and defined the following acceptance criteria

$$
O N ( m c ,j ) = O ( m c ,j ) N d ≤ 1 + 5 √ 2 N d . (2.113)
$$

The reason for dropping the multiplication by two comes from the fact that when sampling the posterior with RML, we replace m pr and d obs by m j and d obs ,j [334]. The criterion of Eq. (2.113) is strictly valid only for linear problems, but

Oliver et al. [334] argues that it should approximately hold for nonlinear problems. However, for practical data assimilation applications, the computation of O ( m ) is expensive because it includes the inverse of C m . In these cases, it is common to consider only the data mismatch part of the objective function with the justification that this part typically dominates the magnitude of the total objective function. Hence, we define the normalized data-mismatch objective function

$$
O N,d ( m ) ≡ O d ( m ) N d . (2.114)
$$

However, even considering only the data mismatch, the experience with real-life applications indicates that the criterion of Eq. (2.113) is rarely satisfied. This level of agreement is typically only observed in controlled synthetic problems, where model and data uncertainties are fully characterized and

Perhaps one useful interpretation for the values of O N,d ( m ) is how large is the average mismatch compared to the data error standard deviation. If we neglect the off-diagonal terms of C e , Eq. (2.114) reduces to

$$
O N,d ( m ) = 1 2 N d N d ∑ i =1 ( d obs ,i - g i ( m ) σ e,i ) 2 . (2.115)
$$

Therefore, if the absolute difference | d obs ,i − g i ( m ) | in Eq. (2.115) is exactly equals to σ e,i for all data points, we obtain O N,d ( m ) = 0 . 5. Similarly, allowing mismatches of 2 σ e,i or 3 σ e,i correspond to O N,d ( m ) = 2 and O N,d ( m ) = 4 . 5, respectively, as illustrated in Fig. 2.17. These numbers serve as a reference for analyzing the results of the data assimilation. For example, O N,d ( m ) &gt; 4 . 5 may indicate that the validity of the model should be reconsidered. It also may indicate that the data-error covariance has been underestimated. Note that in the definition of C e we should consider both measurement and model errors.

Data

![](<ensemble_data_assimilation_e-book_version_images/imageFile11.png>)

INTERNA

Time

Fig. 2.17: Hypothetical model predictions with corresponding values of normalized data mismatch objective function.

This page has no content, but it has plenty of potential.

![](<ensemble_data_assimilation_e-book_version_images/imageFile30.png>)

# Optimization Methods for Data Assimilation

Abstract: This chapter provides a concise overview of key optimization methods employed in reservoir data assimilation. The goal is to introduce these techniques and guide readers toward more detailed references for further study. The chapter concludes with a discussion of parametrization strategies commonly used in reservoir data assimilation.

# 3.1 Introduction

A substantial portion of the literature on reservoir data assimilation is devoted to proposing efficient optimization strategies to minimize the distance between observed and predicted data vectors. The range of methods explored in this context is vast and diverse.

This book adopts the fundamental principle that reservoir data assimilation is better described as a sampling problem rather than an optimization problem. According to this principle, the goal is to explore the uncertainty space while searching for solutions (samples) that are consistent with geological information and capable of reproducing the observations within their confidence levels. Even in this context, however, optimization methods can be useful as components for building efficient sampling strategies, with the most prominent example being the RML method. In fact, as we will discuss in the following chapters, even ensemble methods, particularly the iterative forms of the ensemble smoother, have roots grounded in optimization.

This chapter presents a concise (and superficial) review of some optimization methods used in reservoir data assimilation. The objective is to provide an overview of these methods and direct readers to relevant references. The final section of this chapter discusses some parametrization strategies used in reservoir data assimilation.

# 3.2 Derivative-Based Methods

Derivative-based optimization methods were among the earliest techniques to emerge in the data assimilation literature in the context of petroleum reservoirs [331] and groundwater hydrology [473]. Most current developments in this area are grounded in the foundational works of Gavalas et al. [164] and Shah et al. [390]. These methods typically exhibit high convergence rates. In practical applications, however, the crux of the problem lies in computing the derivatives, as this factor heavily influences the overall performance of the process.

Pseudo-code 3.1 presents the general iterative process for minimizing O ( m ). Each iteration of this process requires the selection of a downhill direction followed by the solution of a line-search problem 1 . Fig. 3.1 illustrates the process described in Pseudo-code 3.1.

# Pseudo-code 3.1: Derivative-Based Methods

- 1. At the   th iteration, find a downhill direction, s   .
- 2. Find an approximate solution for the line-search problem, i.e., find β   such that arg min m   + s   (3.1)

$$
β ℓ ≈ arg min β O ( m ℓ + β s ℓ ) . (3.1)
$$

- 3. Update the model estimate using


$$
m ℓ +1 = m ℓ + β ℓ s ℓ = m ℓ + δ m ℓ +1 . (3.2)
$$

# 3.2.1 Steepest Descent Method

The direction with the fastest decrease in O   m     is the opposite of the gradient of O ( m   ). Therefore, the steepest descent method corresponds to set the search direction s   in Pseudo-code 3.1 as

$$
s ℓ = -∇O ( m ℓ ) . (3.3)
$$

Note, however, that the name “steepest descent direction” does not mean that s   = −∇O ( m   ) is the direction which will necessarily lead to the minimum of O ( m ) with the smallest number of iterations. Actually, any direction

1 Derivative-based optimization strategies are typically divided into line-search and trust-region methods. In this book, we limit our discussion to optimization schemes based on line search. There are several excellent references on derivative-based optimization methods. For example, Nocedal and Wright [325] presents a didactic discussion of both line-search and trust-region methods.

ℓ

(a)

Current point

m  

INTERNA

ℓ

(b)

Set a search direction s

 

INTERNA

![](<ensemble_data_assimilation_e-book_version_images/imageFile12.png>)

(c)

Compute

β  

ℓ

INTERNA

+1

+1

(d)

Move to

m  

(e)

Continue the process

INTERNA Fig. 3.1: Illustration of the general derivative-based optimization process based on linesearch.

s   such that   −∇O ( m   )     s   &gt; 0

$$
is downhill. Note that [
$$

$$
-∇O ( m ℓ ) ] ⊤ s ℓ = ‖ - ∇O ( m ℓ ) ‖‖ s ℓ ‖ cos θ, (3.4)
$$

where θ is the angle between −∇O ( m   ) and s   . Therefore, any s   such that − π/ 2 &lt; θ &lt; π/ 2 is a downhill direction. Fig. 3.2a illustrates the steepest descent direction pointing in the opposite direction to the gradient of O ( m   ). Note that the alternate direction s   in Fig. 3.2b is also downhill and points directly towards the optimum m   . In this case, s   would require a single iteration to converge. In fact, for poorly scaled problems, the steepest descent method may present a poor performance, requiring several iterations to converge to an optimum.

INTERNA

![](<ensemble_data_assimilation_e-book_version_images/imageFile13.png>)

(a)

Steeped descent direction

direction

(b)

Alternate downhill direction s  

ℓ

direction

s

INTERNA

INTERNA Fig. 3.2: Illustration of the steepest descent search direction.

# 3.2.2 Nonlinear Conjugate Gradient Method

The conjugate gradient method is an iterative technique for solving symmetric systems of linear equations or, equivalently, for minimizing convex quadratic functions. This method was extended to minimize general nonlinear functions by Fletcher and Reeves [149]. Pseudo-code 3.2 presents a standard version of the nonlinear conjugate gradient (NCG). The minimization process is similar to the steepest descent method; in fact, the first iteration of both methods is identical. However, unlike the steepest descent, NCG uses information from the previous iteration’s search direction to compute the current search direction. Pseudo-code 3.2 utilizes the formula proposed in [149] to update the search direction, but other formulas also exist; see Nocedal and Wright [325] for further details. Similar to the steepest descent

# Pseudo-code 3.2: Nonlinear Conjugate Gradient Method

- 1. Set   = 0 and initialize with the steepest descent search direction, s 0 = −∇O   m 0   .
- 2. Find an approximate solution for the line-search problem

$$
β ℓ ≈ arg min β O ( m ℓ + β s ℓ ) . (3.5)
$$

- 3. Update the model estimate

$$
m ℓ +1 = m ℓ + β ℓ s ℓ . (3.6)
$$

- 4. Check the termination criteria.
- 5. If not terminated then:


-  Compute

$$
γ ℓ +1 = [ ∇O ( m ℓ +1 )] ⊤ ∇O ( m ℓ +1 ) [ ∇O ( m ℓ )] ⊤ ∇O ( m ℓ ) . (3.7)
$$

-  If γ   +1 &lt;   , set γ   +1 = 0 (typically   ≤ 0 . 1). • Update the search direction


Update the search direction

$$
s ℓ +1 = -∇O ( m ℓ +1 ) + γ ℓ +1 s ℓ . (3.8)
$$

• Set   =   + 1 and return to step 2.

# 3.2.3 Newton's Method

Newton’s method define the search direction by computing a quadratic function around the current estimate m   as

$$
Q ( m ) = O ( m ℓ ) + ( ∇O ( m ℓ ) ) ⊤ ( m - m ℓ ) + 1 2 ( m - m ℓ ) ⊤ B ℓ ( m - m ℓ ) . (3.9)
$$

Q ( m ) has a unique minimum if the Hessian matrix B   = ∇     ∇O ( m   )       is positive definite. In this case, to find the minimum of the quadratic, it suffices to compute the gradient ∇Q ( m ) and set the resulting expression to zero:

$$
∇Q ( m ) = ∇O ( m ℓ ) + B ℓ ( m - m ℓ ) = 0 . (3.10)
$$

Solving for   m − m     and denoting the result as δ m   +1 leads to the Newton’s search direction:

$$
s ℓ = δ m ℓ +1 = - B - 1 ℓ ∇O ( m ℓ ) . (3.11)
$$

The original Newton’s method uses a full step ( β   = 1), in which case there is no need for a line search. This condition is required for proving the quadratic convergence of the method [325]. In practice, however, it may be beneficial to restrict the step size, especially in the early iterations [334].

# 3.2.4 Gauss-Newton

Newton’s method requires second-order derivatives to compute the Hessian. The Gauss-Newton (GN) method relaxes this requirement for least-squares problems by approximating the Hessian using only first-order derivatives. 2

Recall the objective function for finding the MAP

$$
O ( m ) = 1 2 ( d obs - g ( m )) ⊤ C - 1 e ( d obs - g ( m )) + 1 2 ( m - m pr ) ⊤ C - 1 m ( m - m pr ) . (3.12)
$$

The gradient of O ( m ) has the form

$$
∇O ( m ) = G ⊤ C - 1 e ( g ( m ) - d obs ) + C - 1 m ( m - m pr ) , (3.13)
$$

and the Hessian of O ( m ) is

$$
B = ∇ [ ( ∇O ( m )) ⊤ ] = G ⊤ C - 1 e G + ∇ G ⊤ C - 1 e ( g ( m ) - d obs ) + C - 1 m . (3.14)
$$

G is the sensitivity (Jacobian) matrix, which contains the partial derivatives of data with respect to parameters

$$
G ij = ∂g i ( m ) ∂m j , for i = 1 , . . . , N d and j = 1 , . . . , N m . (3.15)
$$

2 Here, we present the equations for finding the MAP. However, the equations are essentially the same for finding posterior realizations with RML, in which case it suffices to replace m pr by m j and d obs by d obs ,j .

$$
B GN = G ⊤ C - 1 e G + C - 1 m . (3.16)
$$

The GN Hessian is positive definite. This means that the GN search direction is always downhill, whereas this may not be true for Newton’s method. The GN search direction for computation of the MAP estimate at the   th iteration becomes

$$
s ℓ = - B - 1 GN ,ℓ ∇O ( m ℓ ) = - ( G ⊤ ℓ C - 1 e G ℓ + C - 1 m ) - 1 × [ G ⊤ ℓ C - 1 e ( g ( m ℓ ) - d obs ) + C - 1 m ( m ℓ - m pr )] . (3.17)
$$

Eq. (3.17) involves the inverse of N m × N m matrices. For N d   N m , it is convenient to use the Sherman-Morrison-Woodbury formula (A.9) to rewrite the search direction as

$$
s ℓ = m pr - m ℓ - C m G ⊤ ℓ ( C e + G ℓ C m G ⊤ ℓ ) - 1 × [ g ( m ℓ ) - d obs - G ℓ ( m ℓ - m pr )] . (3.18)
$$

If both N m and N d are large, the GN method may not be computationally feasible. In such case, we may use the steepest descent, NCG, or quasiNewton methods.

# 3.2.5 Levenberg-Marquardt

The GN method tends to be very efficient when the objective function is well approximated by a quadratic. However, especially at the beginning of the minimization process, when the estimate is far from the optimum, a quadratic can result in a poor estimate of the objective function. In these cases, the steepest descent method can move faster toward the solution than GN. Fortunately, the Levenberg-Marquardt (LM) algorithm incorporates characteristics of both methods: it behaves like the steepest descent when the objective function is more complex than a quadratic and inherits the good convergence rate of GN when the quadratic becomes a good approximation.

The most basic form of the LM algorithm is obtained by modifying the Hessian as follows:

$$
B LM = λ I + B , (3.19)
$$

where λ &gt; 0 is known as the LM parameter. Note that B LM is always positive definite, even if the Hessian is not. Typically, we use the GN Hessian, in which case the LM parameter has a favorable effect on improving the condition number of the matrix. LM does not require a line search to define

# Pseudo-code 3.3: Levenberg-Marquardt

1. Set   = 0 and choose λ 0 (typically λ 0 = O ( m 0 ) /N d ). 2. Solve

Solve

$$
( λ ℓ I + B ℓ ) δ m ℓ +1 = -∇O ( m ℓ ) , (3.20)
$$

and set

$$
m ℓ +1 = m ℓ + δ m ℓ +1 . (3.21)
$$

3. If O   m   +1   ≥ O   m     then

$$
λ ℓ = γλ ℓ , where γ > 1 ( typically 4 ≤ γ ≤ 10) (3.22)
$$

and redo step 2.

Else check the termination criteria.

If not terminated then

$$
λ ℓ +1 = λ ℓ /γ, where γ > 1 . (3.23)
$$

Set   =   + 1 and return to step 2.

# 3.2.6 Quasi-Newton

For large-scale problems, the construction of the Hessian may not be feasible. Even the computation of individual components of G may become problematic. In these cases, one alternative is the use of quasi-Newton methods. These methods are based on recursive formulas to construct an estimate of B − 1 during the iterations of the optimization.

The basic condition for quasi-Newton methods is that

$$
˜ B - 1 ℓ +1 [ ∇O ( m ℓ +1 ) -∇O ( m ℓ )] = m ℓ +1 - m ℓ . (3.24)
$$

The Broyden-Fletcher-Goldfarb-Shanno (BFGS) method [325, 350] stands out as one of the most efficient quasi-Newton methods. BFGS uses information on the descent directions and gradients at previous iterations to construct an approximate inverse Hessian,   B − 1 . In the pure quadratic case, the BFGS algorithm can eventually converge to the true inverse Hessian [325].   +1     +1  

Calling p   = ∇O   m   − ∇O   m   and q   = m − m in Eq. (3.24) leads to

$$
˜ B - 1 ℓ +1 p ℓ = q ℓ . (3.25)
$$

$$
˜ B - 1 ℓ +1 = Q ⊤ ℓ ˜ B - 1 ℓ Q ℓ + υ ℓ q ℓ q ⊤ ℓ , (3.26)
$$

    where υ   = 1 / ( p     q   ) and Q   = I − υ   p   q     . The theory behind BFGS is beyond the scope of this book 3 . Pseudo-code 3.4 summarizes the BFGS method.

# Pseudo-code 3.4: BFGS

- 1. Set   = 0. Choose an initial symmetric positive definite inverse Hessian,   B − 1 0 .   1  
- 2. Compute the search direction s = −   B −   ∇O ( m ). 3. Find an approximate solution for the line-search


problem

$$
β ℓ ≈ arg min β O ( m ℓ + β s ℓ ) . (3.27)
$$

- 4. Update the estimate

$$
m ℓ +1 = m ℓ + β ℓ s ℓ .
$$

- 5. Check the termination criteria.


If not terminated then compute:

$$
p ℓ = ∇O ( m ℓ +1 ) -∇O ( m ℓ ) , (3.28)
$$

$$
q ℓ = m ℓ +1 - m ℓ , (3.29)
$$

$$
˜ B - 1 ℓ +1 = Q ⊤ ℓ ˜ B - 1 ℓ Q ℓ + υ ℓ q ℓ q ⊤ ℓ . (3.30)
$$

    Set   =   + 1 and go to step 2.

The BFGS algorithm requires only the gradient of the objective function. A good initial guess for the inverse Hessian is   B − 1 0 = C m whenever computing and storing C m is feasible. Alternatively, a reasonable choice is to initialize   B − 1 0 = diag ( C m ). However, the BFGS approximation of   B − 1   is usually dense [325], which can make manipulating this matrix prohibitive for large-scale problems. In this case, the alternative is to use the limitedmemory BFGS (L-BFGS) algorithm [324], which stores only a subset of pairs of the vectors p   and q   . Gao and Reynolds [158] presents a series of procedures to enhance the performance of an L-BFGS implementation in the context of reservoir data assimilation.

3 A good theoretical description of BFGS can be found in [325].

# Remark 3.1: Termination Criteria

Oliver et al. [334] present three termination criteria for the iterative optimization process in the context of reservoir data assimilation:

- 1. The algorithm is terminated if

$$
‖∇O ( m ℓ +1 ) ‖ max {‖ m ℓ +1 ‖ 2 , 1 } < 10 - 8 . (3.31)
$$

- 2. If both of the following two conditions are satisfied, we also terminate the algorithm:


$$
|O ( m ℓ ) -O ( m ℓ +1 ) | max {O ( m ℓ +1 ) , 1 } < 10 - 4 , (3.32)
$$

and

$$
max 1 ≤ i ≤ N m { | m ℓ +1 i - m ℓ i | max { | m ℓ +1 i | , | typ ( m i ) | } } < 10 - 3 . (3.33)
$$

where typ( m i ) is a typical value for m i but nonzero. We also terminate the process if the number of iterations

3. exceeds a predefined value.

# 3.2.7 Scaling

The vector of model parameters may include properties with very different magnitudes. Therefore, it is good practice to re-scale m before applying an optimization procedure. One way to re-scale m is to write

$$
̂ m = C - 1/2 m ( m - m pr ) , (3.34)
$$

  and the predicted data vector as

$$
̂ d = C - 1/2 e ( g ( m ) - d obs ) . (3.35)
$$

In this case, the objective function reduces to

$$
O ( ̂ m ) = 1 2 ̂ m ⊤ ̂ m + 1 2 ̂ d ⊤ ̂ d . (3.36)
$$

The gradient with respect to   m becomes

$$
∇ m O ( ̂ m ) = ̂ m + G ⊤ d ̂ d , (3.37)
$$

  m

and the Hessian becomes

$$
̂ B = ∇ ̂ m [ ( ∇ ̂ m O ( ̂ m ) ) ⊤ ] = I + G ⊤ d G d . (3.38)
$$

    In these expressions, G d is referred to as dimensionless sensitivity matrix [478], which is defined as

$$
G d = ( ∇ ̂ m ̂ d ⊤ ) ⊤ = ( ∇ m ̂ d ⊤ ) ⊤ ( ∇ ̂ m m ⊤ ) ⊤ = C - 1/2 e GC 1/2 m . (3.39)
$$

# 3.2.8 Comments on Line Search

The line-search problem is formulated as the finding β   such that

$$
β ℓ ≈ arg min β O ( m ℓ + β s ℓ ) . (3.40)
$$

Eq. (3.40) corresponds to a single-variable optimization problem. Numerous methods are readily available in the literature; see, e.g., [350, Chap. 10] for some classical algorithms. However, it is worth noting that each iteration of the line-search problem entails the evaluation of the forward model, and considering that the overall process may require multiple line searches, it is advisable to limit the number of steps for each line search. Remarkably, it is not necessary to employ an exact line search. In fact, there are theoretical results showing that an approximate line search suffices to establish convergence toward a local minimum (assuming it exists) [325]. Oliver et al. [334] presents a detailed discussion on quadratic and cubic line-search procedures for reservoir data assimilation.

# 3.2.9 Comments on Gradient and Sensitivity Calculation

Different optimization methods require different levels of derivative information. For instance, a complete implementation of Newton’s method may yield a quadratic convergence rate, but it demands the computation of the Hessian matrix. In contrast, GN and LM methods alleviate this demand by only requiring the sensitivity matrix involving first-order derivatives. Steepest descent, NCG, and quasi-Newton methods, on the other hand, require only the gradient of the objective function.

The literature on reservoir data assimilation shows that various strategies for computing derivative information have been used, including finite-

Finite difference, being the simplest approach, requires an additional execution of the forward model for each model parameter to estimate its corresponding derivative. Therefore, a problem with N m parameters requires N m +1 evaluations of the forward model to compute the gradient vector. As a result, this method is viable only for problems featuring a limited number of parameters. The forward method computes the entire sensitivity matrix by solving an extra system of linear equations for each model parameter at each time step. The full sensitivity matrix allows the use of methods such as GN and LM, which exhibit high convergence rates, often rivaling Newton’s method [334]. The primary drawback here is the added computational expense required to obtain the sensitivity matrix if the number of parameters is large.

The adjoint method provides the sensitivity matrix at the cost of solving a linear system for each data point in reverse chronological order. Typically, the number of data points is significantly less than the number of model parameters, rendering the adjoint method a preferred choice. Furthermore, the adjoint method can compute the gradient vector with the cost of solving a single linear system for each time step, regardless of the number of model parameters or data points [367]. This information suffices for using the steepest descent, NCG, or quasi-Newton methods. In fact, combining adjoint gradients with quasi-Newton methods results in a highly efficient data assimilation strategy [158]. However, unlike finite differences, the adjoint method demands substantial effort for implementation and maintenance, in addition to requiring integration within the source code of the forward model. In this context, the use of automatic differentiation (AD) strategies can be an alternative to simplify coding by eliminating the implementation of derivative calculations to construct the Jacobian matrix required in the forward simulations [260, 243]. AD can be used to calculate the partial derivatives required to construct the adjoint problem for sensitivity or gradient calculation [437].

Another gradient computation strategy explored in reservoir data assimilation literature is the SPSA method. In SPSA, the gradient vector is determined through simultaneous random perturbations of all model parameters. This approach yields a stochastic approximation of the gradient, which, under mild conditions, can be demonstrated to be downhill and have an expectation equal to the true gradient [159]. However, it is important to note that this method typically requires a higher number of iterations to converge. Nevertheless, it has the advantage of being relatively easy to implement and seamlessly integrate with complex forward models.

Streamline simulation presents another alternative for approximating sensitivities. In this approach, analytical derivatives of water-cut, gas-oil ratio, and even well-flowing pressures are derived. This method can be applied to

# Remark 3.2: Derivative-Based Methods and Sampling

Derivative-based optimization methods are well-known for their tendency to converge toward local minima. This fact has always been a cause of concern in data assimilation applications. Typically, a premature convergence to a local minimum is quickly spotted because it corresponds to a model with poor data match. One potential remedy is to initiate the optimization from a different starting point. However, it is important to recall that the goal is to sample the posterior distribution. If we use RML, the sampling requires solving several independent minimization problems, some of which may not converge to acceptable estimates. Therefore, the use of an efficient optimization method is mandatory, in which case, the derivative-based methods become a natural choice.

# 3.3 Stochastic Optimization Methods

Stochastic optimization methods have been frequently used as data assimilation techniques, especially in the context of petroleum reservoirs. Among these techniques, prominent options include evolutionary algorithms [195], particle swarm optimization [234], and simulated annealing [238], among others. These methods offer some attractive features, including their ability to generate multiple solutions, robustness, simplicity of implementation, and seamless integration with the forward model, which is used as a “black box.” However, a primary drawback associated with these methods is their relatively slow convergence, which may constrain their applicability to problems featuring only a small number of uncertain parameters.

Stochastic optimization methods are well-known to be less prone to converge to local minima as they explore different parts of the search space. For this reason, these methods are sometimes used as sampling strategies, providing multiple solutions for data assimilation. Nevertheless, despite the inherently exploratory nature of stochastic methods in contrast to their derivative-based counterparts, there exists no formal assurance that they yield a judicious and unbiased sampling of the parameter space’s uncertainty. In his seminal work on Inverse Problems, Tarantola [428] aptly notes that “ genetic algorithms lack the fundamental theorem of the Metropolis algorithm: if you follow certain steps, you will produce samples from the distribution, precisely and in a technical sense. ” While Tarantola explicitly mentions genetic algorithms, the same assertion holds true for various other

stochastic optimization methods. It is worth noting, however, that none of the methods currently operational in reservoir data assimilation applications can guarantee an exact sampling, and a degree of approximation invariably persists.

# 3.3.1 Evolutionary Algorithms

Evolutionary algorithms (EA) are stochastic optimization methods inspired by Darwin’s Evolution Theory and Natural Selection 4 There are several variants, but the methods follow the base idea described in Pseudo-code 3.5.

# Pseudo-code 3.5: Evolutionary Algorithms

- 1. Initialize the population.
- 2. Evaluate individuals.
- 3. While termination criteria are not met do:


-  Select individuals.
-  Recombine individuals.
-  Mutate individuals.
-  Evaluate individuals.


Genetic algorithms (GA) are among the most used variants of EA. In GA, each member of the population serves as a potential solution for the data assimilation problem. Various parametrization methods exist for individuals within GA. Traditional GA implementations employ binary arrays to represent individuals. However, floating-point representations of individuals can be used, particularly for describing real-valued parameters. Pseudo-code 3.6 provides a summarized outline of the main steps involved in employing GA to update models within a data assimilation process.

4 There are several good books about EA; for example, [90] is good reference.

# Pseudo-code 3.6: Main Step of GA for Data Assimilation

For a predefined number of generations, repeat the following steps:

1. Selection of individuals:

• The probability of selecting an individual of the population is proportional to its fitness value, i.e.,

$$
P i = f i ∑ N s j =1 f j , (3.41)
$$

where the fitness is typically defined as f i = 1 / O d ( m i ). Therefore, models with better data matches have a higher

• probability of being selected for the recombination.

# 2. Recombination:

-  Individuals of the current generation (parents) are combined to generate new individuals (offsprings).
-  There are several forms of recombination (crossover). For example, we can use a random linear combination of two models:


where u ∼ U [0 , 1].

# 3. Mutation:

$$
̂ m = u m 1 +(1 - u ) m 2 , (3.42)
$$

• Random perturbation in some individuals. For example, we can use a Gaussian perturbation

$$
̂ m = m + γ C 1/2 m z , (3.43)
$$

  where z ∼ N ( 0 , I ), and γ ∈ (0 , 1] is a mutation factor.

# 4. Elitism:

• Preserve the best individuals of a generation to the next one (to ensure that the best-so-far solutions are not lost).

Several other algorithms belong to the EA class, among which the covariance matrix adaptation evolution strategy (CMA-ES) [186] is considered state-of-the-art [402]. However, its application to reservoir data assimilation remains limited. CMA-ES employs a mutation strategy based on Gaussian perturbations of the current solution, with a covariance matrix that is iteratively updated to adapt to the local structure of the objective function, thereby enhancing optimization efficiency.

# 3.3.2 Particle Swarm Optimization

Similar to GA, particle swarm optimization (PSO) [234] is a populationbased method inspired by the collective behavior of animal groups, such as birds and fish. PSO operates by generating random solutions, with each solution represented as a particle forming a swarm. Within this swarm, each particle navigates the parameter space. At each step, the position and velocity of these particles are updated based on the best individual and global solutions from the previous step. This iterative process continues until the particles converge to the global optimum.

Pseudo-code 3.7 presents the basic PSO procedure. In this procedure, m   j is the previous best position for the j th particle, while m   is the overall best position for all particles (sometimes computed as the best position in the neighborhood of the j th particle). The inertia parameter w controls the exploratory ability of the search: large values promote a more global search, while small values encourage local search. Typically, w is selected between 0.4 and 1. However, it may be beneficial to start with a higher value, such as 1.4, and reduce it during the iterations. The parameter c 1 defines the confidence that the particle has in its previous trajectory (the “cognitive” component) and is usually chosen between 1 and 2. The parameter c 2 defines the confidence in the swarm (the “social” component) and is also typically selected between 1 and 2. R 1 and R 2 are diagonal matrices with elements drawn from U [0 , 1].

# Pseudo-code 3.7: Basic PSO for Data Assimilation

1. Initialize the particles, { m 0 j } , and the corresponding velocities,   v 0 j   , for j = 1 ,...,N s . Set   = 0 (iteration index). 2. Update the position of each particle using

Update the position of each particle using

$$
m ℓ +1 j = m ℓ j + v ℓ j ∆ t, for j = 1 , . . . , N s (3.44)
$$

where ∆ t = 1.

- 3. Evaluate the objective function for each particle.
- 4. Update the velocity of each particle using

$$
v ℓ +1 j = w v ℓ j + c 1 ∆ t R ℓ +1 1 ( m ⋆ j - m ℓ j ) + c 2 ∆ t R ℓ +1 2 ( m ⋆ - m ℓ j ) . (3.45)
$$

- 5. Set   =   + 1.
- 6. If maximum number of iterations, then stop. Otherwise, go to step 2.


Before optimization, it is recommended to scale the parameters in the range [ − 1 , 1]. Babin et al. [22] presents the following set of rules to ensure the parameter values to be within the range [ − 1 , 1] during the optimization:

-  Set m   ij = − 2 − m   ij if m   ij ≤ − 1.      
-  Set m ij = 2 − m ij if m ij ≥ 1.      
-  Set v ij = − v ij if   m ij   ≥ 1.    
-  Set v ij = v max if   v ij   &gt; v max .


where m   ij and v   ij denote the i th component of m   j and v   j , respectively. v max ∈ (0 , 2] is the maximum allowed velocity.

# 3.3.3 Simulated Annealing

Simulated Annealing [238] is a stochastic optimization algorithm inspired by the annealing process in metallurgy, where a material is heated and gradually cooled to reduce defects and attain a stable state. The algorithm iteratively explores the solution space by applying small random perturbations to the current solution. To avoid premature convergence, it accepts worse solutions with a probability that decreases over time. This mechanism helps the algorithm to escape local minima and enhance exploration.

The acceptance probability of a worse solution is governed by the Metropolis criterion:

$$
P ( m , ̂ m ) = exp ( - ∆ O ( ̂ m ) T ) , (3.46)
$$

where ∆ O (   m ) = O (   m ) − O ( m ) denotes the change in the objective function from the proposed solution   m to the current solution m . In simulated annealing, O (   m ) is interpreted as the system’s energy function, and T is the annealing parameter (temperature), which decreases throughout the optimization process, progressively reducing the probability of accepting worse solutions.

Pseudo-code 3.3.3 outlines the basic simulated annealing procedure for data assimilation.

# Pseudo-code 3.3.3: Basic Simulated Annealing for Data Assimilation

- 1. Initialize the process with an initial solution m , initial temperature T , cooling rate β ∈ (0 , 1), e.g., β = 0 . 95, and stopping temperature T min .  
- 2. Keep the overall best solution m = m .
- 3. While T &gt; T min :


• Propose a new solution   m with, for example, a Gaussian perturbation around the current solution m :

$$
̂ m = m + γ C 1/2 m z , (3.47)
$$

  where z ∼ N ( 0 , I ), and γ ∈ (0 , 1] is a perturbation factor.

-  Compute the change in thre objective function:

$$
∆ O ( ̂ m ) = O ( ̂ m ) -O ( m ) . (3.48)
$$

-    • If ∆ O (   m ) &lt; 0 accept the proposal: – Set m = m .


Set m = m .

  – If O ( m ) − O ( m   ) &lt; 0, set m   = m .

Else:

-  Sample u ∼ U [0 , 1].
-  Compute:

$$
P ( m , ̂ m ) = exp ( - ∆ O ( ̂ m ) T ) . (3.49)
$$

-  If u &lt; P ( m ,   m ), accept the worse solution and set m =   m . Reduce the temperature T = βT .


•

# 3.4 Other Derivative-Free Optimization Methods

There are numerous methods available for solving complex nonlinear optimization problems that do not rely on derivative information. The variety of derivative-free optimization (DFO) methods proposed in the literature is extensive 5 . Notable examples of DFO methods include the Nelder-Mead method [317], pattern search methods [442], Powell’s conjugate direction method [348], and NEWUOA [349].

DFO methods provide a flexible alternative by relying exclusively on function evaluations to navigate the search for optimal solutions. This charac-

5 It is worth noting that stochastic methods, discussed in the previous section, could also be included in this category. However, for clarity and to emphasize their significance as data assimilation methods, we have chosen to address them separately.

# 3.5 Methods Based on Proxy Modeling

Another important group of methods used in the context of reservoir data assimilation is based on the combination of optimization and sampling methods with proxies of the forward model. The basic idea is to replace executions of a computationally intensive forward model with a faster substitute. Proxy modeling often appears with different names in the literature, including meta-models, surrogate, and response surface modeling.

The successful application of proxy modeling for reservoir data assimilation depends on two key factors: (1) the number of experiments (sample points) required for constructing or training the proxy, and (2) the proxy’s capability to replicate the nonlinear behavior of the forward model.

# 3.5.1 Design of Experiments

In the context of proxy modeling, the objective of the design of experiments is to acquire the maximum information about the behavior of the dynamical system using the minimum possible number of executions of the forward model. Increasing the number of experiments typically results in improvements in the quality of the proxy; however, it diminishes the advantage of using proxies compared to using the full-featured forward model. Therefore, the selection of a proper set of experiments has a major impact on the performance of the process.

Bahrami et al. [23] divide the strategies for sampling experimental points into two broad classes: stationary and sequential (adaptive). In the stationary strategy, a predefined number of experiments is obtained and used to build the proxy. In the sequential strategy, a limited set of experiments is used to construct an initial proxy model, which is then refined through the selection of additional experimental points based on the progress of the optimization or sampling process.

Factorial and Plackett-Burman designs are among the most commonly used methods in the context of stationary sampling. In these cases, each

Fractional factorial designs are a subset of full factorials, where the number of experiments is determined by L N m − p &gt; N m , with p indicating the degree of reduction. When constructing such designs, it is crucial to maintain balance and orthogonality. In a balanced design, each level of a particular parameter must be used an equal number of times, while orthogonality aims to eliminate correlations between main effects and interaction terms.

Other commonly employed methods for selecting experimental points to construct proxies include random Monte Carlo sampling, Latin hypercube sampling (LHS) [301], and orthogonal array sampling (OAS) [340]. LHS is a stratified sampling method that divides the parameter space into a predefined number of intervals with the same probability value. OAS, on the other hand, is an extension of LHS that uniformly distributes sample points in the dimensional projection of the parameter domain. A recent review of the main methods used for experimental design is presented by Garud et al. [161].

# 3.5.2 Standard Proxy Models

The number of proxy models developed in the context of reservoir data assimilation is quite extensive, with numerous publications in this area, including a few recent review papers [211, 23, 309]. This topic is too broad to be covered as a section in a book on ensemble methods. Nevertheless, in the following section, we discuss the formulation of three commonly used proxies and provide references to other popular methods.

# 3.5.2.1 Quadratic Polynomials

Quadratic polynomials were among the first proxies used in the context of reservoir data assimilation [96] and are still employed in various commercial software for data assimilation and uncertainty quantification. A quadratic polynomial, denoted as Q ( m ), can be expressed as follows:

$$
Q ( m ) = a + b ⊤ m + m ⊤ Cm = a + N m ∑ i =1 b i m i + N m ∑ i =1 N m ∑ j =1 c ij m i m j , (3.50)
$$

where c ij = c ji . Q ( m ) is used to replace a quantity of interest, F ( m ), obtained through the execution of the forward model. For example, F ( m ) may represent the data mismatch objective function, F ( m ) = O d ( m ). Alternatively, F ( m ) may correspond to a specific datum predicted by the forward model, in which case we may have F i ( m ) = g i ( m ) for i = 1 ,...,N d . In this situation, we can fit a set of quadratics Q i ( m ) ≈ g i ( m ) and use these proxies to compute O d ( m ). To fully determine all coefficients of ( m ), it is necessary to conduct

Q ( N m + 1)( N m + 2) / 2 experiments. Consequently, when dealing with many model parameters, the computational demand becomes impractical. For example, N m = 10 requires 66 experiments while N m = 100 necessitates 5151 experiments. If we have more than ( N m +1)( N m +2) / 2 experiments, we have an overdetermined problem (see Appendix B, Section B.3). In such cases, we can compute a least-squares solution to determine the coefficients of the polynomial.

Sometimes, a simplified version of Q ( m ) omitting the interaction terms is adopted to reduce the number of experiments. In this scenario, only the diagonal elements of C are computed, and the quadratic reduces to:

$$
˜ Q ( m ) = a + N m ∑ i =1 b i m i + N m ∑ i =1 c ii m 2 i . (3.51)
$$

This simplified version requires only 2 N m + 1 experiments.

# 3.5.2.2 Kriging

Variations of kriging, or more generically Gaussian processes, are very common techniques used in proxy modeling. Here, we assume that the quantity of interest, F ( m ), can be modeled as

$$
F ( m ) ≈ Q ( m ) + Z ( m ) , (3.52)
$$

where Q ( m ) is a quadratic model and Z ( m ) is a kriging model. This formulation uses Q ( m ) to predict the trend and Z ( m ) to predict the fluctuations of the quantity F ( m ).

The goal is to construct Z ( m ) using a collection of samples, z i = Z ( m i ) for i = 1 ,...,N s . In kriging, the value at an unsampled location, denoted as z 0 = Z ( m 0 ), is estimated as a linear weighted sum of the N s sample points, i.e.,

$$
z 0 = N s ∑ i =1 w i z i = w ⊤ z , (3.53)
$$

where z i is treated as a random variable. Here we assume that E [ z i ] = 0 6 for i = 0 , 1 ,...,N s , where i = 0 means the unsampled location. We also assume stationary covariance

$$
C [ z ] = E [ zz ⊤ ] = C z . (3.54)
$$

The goal is to compute an estimate of z 0 that minimizes the expected squared error

$$
σ 2 K = E [ ( z 0 - w ⊤ z ) 2 ] = E [ z 2 0 ] - 2 w ⊤ E [ z 0 z ] ︸ ︷︷ ︸ c 0 + w ⊤ E [ zz ⊤ ] ︸ ︷︷ ︸ C z w = σ 2 z - 2 w ⊤ c 0 + w ⊤ C z w , (3.55)
$$

in which case suffices to compute ∇ σ 2 K = 0

$$
∇ σ 2 K = - 2 c 0 +2 C z w = 0 , (3.56)
$$

and solve for w . This procedure leads to

$$
w = C - 1 z c 0 . (3.57)
$$

The kriging error variance becomes

$$
σ 2 K = σ 2 z - 2 w ⊤ c 0 + w ⊤ C z w = σ 2 z - 2 c ⊤ 0 C z c 0 . (3.58)
$$

Note that the kriging estimate depends on the choice of a covariance structure. The typical assumption is that C z is a function of the distance between pairs of the vectors m i and m j . Therefore

$$
C z = ⎡ ⎢ ⎣ C ( m 1 , m 1 ) · · · C ( m 1 , m N s ) . . . . . . . . . C ( m N s , m 1 ) · · · C ( m N s , m N s ) ⎤ ⎥ ⎦ (3.59)
$$

$$
c 0 = ⎡ ⎢ ⎣ C ( m 0 , m 1 ) . . . C ( m 0 , m N s ) ⎤ ⎥ ⎦ , (3.60)
$$

where C ( m i , m j ) is a covariance function typically selected as

$$
C ( m i , m j ) = σ 2 z exp [ - ( ‖ m i - m j ‖ L ) p ] . (3.61)
$$

The covariance function (3.61) has three parameters: σ z &gt; 0, L &gt; 0, and p ∈ [1 , 2]. The exponent p is typically selected as p = 2 to ensure a smooth estimate. The standard deviation σ z can be estimated from the set { z i } N s i =1 or other information about the behavior of F ( m ). The correlation range L can also be estimated from the set. For example, one can use a cross-validation scheme to test the ability of the kriging to predict z i . Note that   m i − m j   represents the distance between models m i and m j . However, because the components of m may represent reservoir properties of different orders of magnitude, it is recommended to normalize the components before building the proxy.

# 3.5.2.3 Support Vector Regression

Support vector regression (SVR) is a particular type of support vector machine (SVM) [45] specialized in nonlinear regression analysis. Both SVR and SVM are methods that belong to a broader class of machine learning methods. Here, we present a particular version called least-squares SVR (LSSVR) introduced by Suykens and Vandewalle [423] and applied in reservoir data assimilation by Guo et al. [181] 7 .

LS-SVR approximates the quantity of interest as

$$
F ( m ) ≈ w ⊤ ϕ ( m ) + b, (3.62)
$$

where w is a vector of weights, ϕ ( m ) is a nonlinear mapping to a so-called “feature space,” and b is a bias term. w and b are obtained by solving a regularized least-squares problem based on a training set with N s experiments

$$
min w ,b 1 2 w ⊤ w + 1 2 γ N s ∑ i =1 e 2 i (3.63) s.t. e i = y i - w ⊤ ϕ ( m i ) - b, for i = 1 , . . . , N s .
$$

This constrained problem can be solved using Lagrange multipliers by defining the function

$$
L ( w , b, e , λ ) = 1 2 w ⊤ w + 1 2 γ N s ∑ i =1 e 2 i - N s ∑ i =1 λ i ( w ⊤ ϕ ( m i ) + b + e i - d i ) , (3.64)
$$

where d i = F ( m i ) denotes the predicted quantity of interest obtained with the training point m i . Setting ∇ L ( w ,b, e , λ ) = 0 and solving the resulting expression for w , b , e , and λ leads to

and

$$
∇ w L ( w , b, e , λ ) = 0 ⇒ w = N s ∑ i =1 λ i ϕ ( m i ) , (3.65)
$$

$$
∂ L ( w , b, e , λ ) ∂b = 0 ⇒ N s ∑ i =1 λ i = 0 , (3.66)
$$

$$
∂ L ( w , b, e , λ ) ∂e i = 0 ⇒ λ i = γe i , for i = 1 , . . . , N s , (3.67)
$$

$$
∂ L ( w , b, e , λ ) ∂λ i = 0 ⇒ w ⊤ ϕ ( m i ) + b + e i - y i = 0 , for i = 1 , . . . , N s . (3.68)
$$

Using (3.65) and (3.67) in (3.68) results in

$$
d i = N s ∑ j =1 λ j ϕ ( m j ) ⊤ ϕ ( m i ) + b + λ j γ , for i = 1 , . . . , N s , (3.69)
$$

which can be written in a matrix form as

$$
d = b 1 + ( Ψ + 1 γ I ) λ , (3.70)
$$

where 1 = [1 1 ··· 1]   and Ψ is the N s × N s matrix with ( i,j )th entry computed as ϕ ( m i )   ϕ ( m j ). Combining (3.70) and (3.66) into a single system of linear equations leads to

$$
[ 0 1 ⊤ 1 ( Ψ + 1 γ I ) ] [ b λ ] = [ 0 d ] , (3.71)
$$

whose solution is

and

$$
b = 1 ⊤ ( Ψ + 1 γ I ) - 1 d 1 ⊤ ( Ψ + 1 γ I ) - 1 1 , (3.72)
$$

$$
λ = ( Ψ + 1 γ I ) - 1 d - b ( Ψ + 1 γ I ) - 1 1 . (3.73)
$$

The quantity of interest evaluated at a new point m is estimated using

$$
F ( m ) ≈ N s ∑ i =1 λ i ϕ ( m i ) ⊤ ϕ ( m ) + b. (3.74)
$$

The resulting expressions only require inner products, ϕ ( m i )   ϕ ( m ), making it unnecessary to explicitly compute the mapping ϕ ( m ). This concept is known as the kernel trick [403]. In practice, ϕ ( m i )   ϕ ( m ) is computed using a kernel function. Various kernel options exist, but the Gaussian kernel, also known as the radial basis function, is commonly used in practical applications:

Hence,

$$
K ( m i , m ) = ϕ ( m i ) ⊤ ϕ ( m ) = exp ( - ‖ m i - m ‖ 2 2 σ 2 ) . (3.75)
$$

$$
F ( m ) ≈ N s ∑ i =1 λ i K ( m i , m ) + b. (3.76)
$$

LS-SVR has two free parameters, γ and σ , which have to be determined beforehand. Sousa and Reynolds [408] claim that for γ &gt; 200 the training procedure is nearly insensitive to this parameter. The value σ controls the smoothness of the SVR model. Sousa and Reynolds [408] propose to normalize the components of m and d in the range [0 , 1] and set

$$
σ = ϱ √ N m , (3.77)
$$

with   ∈ (0 , 1], say   = 0 . 2.

# 3.5.2.4 Example: Proxy of a Nonlinear Function

Fig. 3.3 presents plots of proxies derived from a quadratic function, a combination of quadratic and kriging models, and LS-SVR. These proxies are trained using only four sample points from the function:

$$
F ( m ) = m sin( m ) + 0 . 1 m 2 . (3.78)
$$

A quadratic model can effectively capture the general trend but falls short in representing the oscillatory behavior of F ( m ). Employing a quadratic model in combination with kriging and LS-SVR yields models that can partially capture the local variations of F ( m ). An additional benefit of kriging is the estimation of the standard deviation, which can be utilized to identify areas that may require more samples.







![](<ensemble_data_assimilation_e-book_version_images/imageFile33.png>)













 

 

 

























 

 

 

�







 



�







 



�







 



(a)

Quadratic

(b)

Quadratic + kriging

(c)

LS-SVR

Fig. 3.3: Proxies for the function defined in Eq. (3.78) . The red curve in each plot is the actual function, the solid black curve is the proxy, and the red circles are the four sample points. The dashed curves in (b) correspond to the quadratic + kriging ± one standard deviation. Example 3.5.2.4.

# 3.5.3 Other Frequently-Adopted Proxy Models

Numerous methods have been proposed as proxies in the context of reservoir data assimilation. Notable examples include variations of shallow neural networks [487, 391, 93, 48, 292] and deep neural networks [486, 427, 426, 385], physics-informed neural networks [190, 24, 95, 474], as well as polynomial chaos expansion [117, 54].

Another group of strategies for proxy modeling involves simplifying the forward model. This can be achieved through various techniques such as upscaling methods [462, 10], reduced-order modeling [227, 189, 468], streamline simulation [458, 231], multiscale methods [102, 103], among others.

# Remark 3.3: Challenges on Proxy Modeling

Despite the numerous applications reported in the literature, the use of proxies for reservoir data assimilation presents several challenges, particularly in balancing accuracy with computational efficiency.

Although proxies are designed to approximate the behavior of highfidelity models at reduced computational cost, their ability to capture the full complexity of reservoir dynamics can be limited. Proxies often struggle to represent nonlinear interactions between geological heterogeneities and flow processes, which can result in inaccuracies in model predictions. This problem is exacerbated by the “curse of dimensionality.” As the number of model parameters increases, constructing accurate proxies becomes exceedingly complex.

Additionally, the training process requires selecting appropriate datasets to represent the range of reservoir conditions, and this selection can introduce bias if not carefully managed. Moreover, as reservoir conditions evolve over time, proxies may require frequent updates or recalibration, further complicating their use in long-term forecasts or complex data assimilation problems.

# 3.6 Sensitivity Analysis

Practical reservoir data assimilation studies frequently incorporate a screening or sensitivity analysis (SA) step to identify the parameters that have the greatest influence on the predicted data. One fundamental reason for conducting SA is to reduce the number of parameters by eliminating those with low influence in predicting data. Additionally, SA is useful for enhancing the understanding of the reservoir’s behavior in relation to the main uncertainty parameters, offering deeper insights into the dynamics of the system.

The simplest SA method involves perturbing each model parameter individually while keeping the other parameters at a base value. Typically, two perturbations per parameter are considered—one at its lower value and another at its upper value. By comparing the variations in the predicted data with a base simulation case, we can rank the parameters according to their importance, typically presented in the form of a tornado plot (Fig. 3.4). The total number of simulations required in this approach is 2 N m + 1. Besides the obvious computational cost for problems with a large number of parameters, this method has the limitation of neglecting the combined effects of the model parameters.

There are more advanced SA methods beyond the standard approach of evaluating the forward model by varying each parameter between its lower

![](<ensemble_data_assimilation_e-book_version_images/imageFile34.png>)

-0.10

-0.06

-0.02

0.02

0.06

0.10

-0.6

-0.4

-0.2

0.0

0.2

0.4

0.6

PVT

EW

EO

KRWMAX

DELTA_DWOC

EXP_AQPERM

EXP_AQPERM

DELTA_DWOC

KRGMAX

EO

KRWMAX

EG

EW

PVT

Min

Min

DELTA_DGOC

KRGMAX

Max

Max

CPOR

CPOR

EG

DELTA_DGOC

AQPOR

AQPOR

(a)

Cumulative oil production

(b)

Cumulative water production

Fig. 3.4: Example of tornado plots from a one-at-a-time SA for a modified version of the PUNQ-S3 problem [150]. The vertical axis labels represent the selected model parameters. Each bar shows the relative change in the quantity of interest when the corresponding parameter is set to its minimum or maximum value, compared to the base case.

# 3.6.1 Sensitivity Analysis Based on Monte Carlo Simulations

In practice, SA is often performed using Monte Carlo simulations, where the goal is to estimate the sensitivity coefficients of a quantity of interest, F ( m ), with respect to m , based on an ensemble of N e random samples. This procedure is particularly convenient in the context of ensemble methods, where the sensitivity coefficients can be readily estimated from the prior ensemble simulations. Several approaches exist for this purpose, but a particularly useful method is to estimate the sensitivities using the correlation coefficients between m and F ( m ).

# 3.6.1.1 Pearson Correlation

Let m represent a model parameter and d the quantity of interest to be analyzed. One of the simplest methods for SA is to estimate the sensitivity values using the Pearson’s correlation coefficient:

$$
ρ md = ∑ N e j =1 ( m j - m ) ( d j - d ) √ ∑ N e j =1 ( m j - m ) 2 √ ∑ N e j =1 ( d j - d ) 2 , (3.79)
$$

where ρ md ∈ [ − 1;1] provides a measure of the strength of the linear relationship between m and d . ρ md &gt; 0 means that both m and d are increasing or decreasing together, while ρ md &lt; 0 means that m and d move in opposite directions. | ρ md | ≈ 1 corresponds to a linear relationship, while ρ md ≈ 0 indicates that there is no linear relationship between m and d .

# 3.6.1.2 Spearman Correlation

The Spearman correlation between two variables is equivalent to the Pearson correlation applied to the rank values of those variables. Instead of assessing only linear relationships like the Pearson correlation, the Spearman correlation evaluates monotonic relationships, whether linear or nonlinear. The Spearman correlation is less sensitive to outliers because it operates on the ranked values, meaning the actual differences between values do not influence the calculation.

# 3.6.1.3 Partial Correlation

Partial correlations aim to estimate the correlation between two random variables, removing the effect of other relevant variables. The partial correlation between m and d given a set of removed variables m 0 , denoted ρ md, m 0 , can be computed as the correlation between the residuals r m and r d resulting from a linear regression of m with m 0 and d with m 0 , respectively. The linear regression between and m can be written as

m 0

$$
m = w 0 + w 1 m 1 + w 2 m 2 + . . . + w N m - 1 m N m - 1 = x ⊤ w , (3.80)
$$

where x   = [1 m   0 ], i.e., x is the vector containing m 0 augmented with a 1 in the first entry to allow for a constant term in the regression. The coefficients of the linear regression can be computed by solving the leastsquares problem:

$$
w ⋆ m = arg min w N e ∑ j =1 ( m j - x ⊤ j w ) 2 = arg min w ‖ m - Xw ‖ 2 2 (3.81)
$$

where

$$
X = ⎡ ⎢ ⎣ 1 m 1 , 1 · · · m N m , 1 . . . . . . 1 m 1 ,N e · · · m N m ,N e ⎤ ⎥ ⎦ . (3.82)
$$

If N e ≥ N m and rank( X ) = N m , the solution of the LS problem is

$$
w ⋆ m = ( X ⊤ X ) - 1 Xm . (3.83)
$$

Similarly for d , we write

$$
w ⋆ d = ( X ⊤ X ) - 1 Xd . (3.84)
$$

The residuals for the j th samples of m , d and X are given by

$$
r m j = m j - x ⊤ j w ⋆ m (3.85)
$$

and

$$
r d j = d j - x ⊤ j w ⋆ d . (3.86)
$$

The partial correlation is computed with the standard formula

$$
ρ md, m 0 = ∑ N e j =1 r m j r d j √ ∑ N e j =1 r 2 m j √ ∑ N e j =1 r 2 d j . (3.87)
$$

# 3.6.1.4 Regression Coefficients

Another popular strategy is to use the regression coefficients of linear or quadratic polynomials as sensitivity coefficients. Note that because model parameters and data may present different magnitudes, it is important to normalize before regression. For example, we can write

$$
̂ m = m - m σ m (3.88)
$$

and

$$
̂ d = d - d σ d (3.89)
$$

and perform the regression with   m and   d .

# 3.6.1.5 Example: Sensitivity Analysis in the PUNQ-S3 Case

Fig. 3.5 presents tornado plots of cumulative oil production for a modified version of the PUNQ-S3 case [150]. These plots were generated using Monte Carlo sampling with an ensemble of 100 realizations. The four methods considered yielded similar rankings of model parameters, with the top three most influential parameters remaining consistent across all plots. These parameters also align with the results of the one-at-a-time SA shown in Fig. 3.4.

![](<ensemble_data_assimilation_e-book_version_images/imageFile35.png>)

-0.8

-0.6

-0.4

-0.2

0.0

0.2

0.4

-0.8

-0.6

-0.4

-0.2

0.0

0.2

0.4

PVT

PVT

EO

EO

DELTA_DWOC

DELTA_DWOC

EW

EW

DELTA_DGOC

DELTA_DGOC

EG

EG

KRGMAX

KRGMAX

AQPOR

AQPOR

EXP_AQPERM

EXP_AQPERM

CPOR

CPOR

KRWMAX

KRWMAX

(a)

Pearson

(b)

Spearman

-1.0

-0.6

-0.2

0.2

0.6

-0.8

-0.6

-0.4

-0.2

0.0

0.2

0.4

PVT

PVT

EO

EO

DELTA_DWOC

DELTA_DWOC

CPOR

EW

EW

CPOR

KRGMAX

KRGMAX

EXP_AQPERM

DELTA_DGOC

DELTA_DGOC

EXP_AQPERM

EG

EG

KRWMAX

KRWMAX

AQPOR

AQPOR

(c)

Partial correlation

(d)

Linear regression

Fig. 3.5: Tornado plots from a SA of cumulative oil production for a modified version of the PUNQ-S3 problem. The labels on the vertical axis represent the selected model parameters, while each bar represents the sensitivity coefficient estimated for each parameter. Example 3.6.1.5.

# 3.7 Parametrization

One of the primary challenges in applying optimization methods to reservoir data assimilation is dealing with a large number of model parameters. When every parameter in a reservoir model, such as the porosity and permeability of each gridblock, is allowed to vary independently, the resulting model space

(a) m ∼ N ( m pr , σ 2 I )

0.35

![](<ensemble_data_assimilation_e-book_version_images/imageFile14.png>)

0.30

0.25

0.20

0.15

0.10

0.05

0.00

(b) m ∼ N ( m pr , C m )

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

Fig. 3.6: Two random realizations of porosity distribution in a model. Panel (a) shows a realization generated by independently sampling each gridblock, resulting in a noisy realization. While there is a non-zero probability of obtaining a plausible model using this procedure, it never occurs in practice. Panel (b) show a realization generated with an underlying covariance structure, illustrating that the models of interest occupy only a fraction of the R N m space.

While the parameter space can be extremely large, the dynamic data often carries limited information. This limitation arises from the system’s diffusive nature, the fact that data are collected at limited numbers of wells sparsely distributed in the reservoir, the presence of measurement errors, and the inherently approximate nature of reservoir models. Consequently, the number of model parameters that can be reliably determined from the available data remains relatively small.

δ m = Pz .

(3.90)

Here, P is a matrix with dimensions N m × N z , and its columns constitute a basis for a vector space of dimension N z . Meanwhile, z is a vector containing coefficients corresponding to each basis vector. The primary objective is to choose P in such a way that N z   N m while ensuring it spans a subspace where m can be accurately represented.

# Remark 3.4: Reduced Parametrization and Uncertainty

The choice of a reduced parametrization involves a trade-off. On the one hand, representing the model with fewer basis vectors helps alleviate the problem’s ill-conditioning, thereby improving the performance of optimization algorithms. On the other hand, reducing the parametrization confines the solution search to a limited subspace, which can lead to an underestimation of uncertainty.

The preface of “Inverse Theory for Petroleum Characterization and History Matching,” [334] highlights this issue by stating: “ It is impossible to correctly estimate all the parameters of a model from inaccurate, insufficient, and inconsistent data, but reducing the number of parameters in order to get low levels of uncertainty is misleading. ”

# 3.7.1 Zonation

Zonation is one of the oldest and most straightforward parametrization methods, and it is still widely used in practice. In this approach, the basis vectors represent constant values within specific reservoir regionszones—and are zero elsewhere. These zones are usually predefined and selected based on geological interpretations and engineering judgment. While zonation typically results in an initial significant reduction in the objective function, the final mismatch tends to be larger than desired due to the limited number of parameters (degrees of freedom) and suboptimal zone selections.

Critiques of zonation primarily revolve around the potentially arbitrary nature of zone delineation, which may not accurately capture the geological characteristics of the reservoir. Additionally, zonation can introduce discontinuities in rock properties between zones, impacting the representation of subsurface features.

# 3.7.1.1 Example: Manual History Matching

Manual history matching is a widely practiced method in petroleum reservoir engineering for data assimilation involving direct manipulation of the reservoir model. In this approach, reservoir engineers typically apply modifications, such as zonal multiplication factors, to improve the model’s agreement with historical data. The process is often conducted in a trial-and-error manner, drawing on the engineer’s experience and close collaboration with geoscientists involved in the model’s construction. This method can be timeconsuming and subjective, as it heavily depends on the engineer’s judgment and expertise.

Fig. 3.7a shows an example of a permeability field obtained through a manual history matching approach for an oilfield in the Campos Basin. In this model, the field engineer modified the initial permeability by applying multiplication factors to specific areas to match water cut data at oil-producing wells. These areas can be easily identified by the rectangular shapes of the zones; for example, see the region around well P-209. For comparison, Fig. 3.7b shows the mean permeability obtained using an ensemblebased data assimilation method (ES-MDA, Chapter 5) for the same field, which exhibits a more natural permeability distribution, without the discontinuities observed in the manual history matched model.

One limitation of the zonation parametrization and manual approaches is the difficulty in generating multiple solutions. It is interesting to note that in the example shown in Fig. 3.7, the reservoir engineer achieved a data match by reducing the permeability around well P-209. For the same problem, the ensemble method found solutions that, on average, have high permeabilities around the same well. This result illustrates the multiplicity of solutions in a data assimilation problem.

# 3.7.2 Pilot Point

In the pilot-point method [101, 250], reservoir parameter values are determined at a small number of specific locations known as pilot points. The property values for the remaining gridblocks within the model are then computed using interpolation techniques, often employing kriging. Various strategies for selecting the locations of these pilot points have been discussed in the literature [357, 8].

I‐143

-

143

mD

10 4

10 3

P‐93

-

93

P‐111

-

111

P‐115

-

115

I‐123

-

123

I‐125

-

125

P‐113

-

113

P‐2

-

2

P‐95

-

95

I‐119

-

119

I‐121

-

121

P‐99

-

99

I‐145

-

145

P‐117

-

117

P‐209

-

209

I‐127

-

127

P‐97

-

97

I‐147

-

147

10 2

I‐143

-

143

mD

![](<ensemble_data_assimilation_e-book_version_images/imageFile15.png>)

10 4

10 3

10 2

P‐93

-

93

P‐111

-

111

P‐115

-

115

I‐123

-

123

I‐125

-

125

P‐113

-

113

P‐2

-

2

P‐95

-

95

I‐119

-

119

I‐121

-

121

P‐99

-

99

I‐145

-

145

P‐117

-

117

P‐209

-

209

I‐127

-

127

P‐97

-

97

I‐147

-

147

INTERNA

(a)

Manual HM with zonation

(b)

Ensemble mean

Fig. 3.7: Permeability for a model of an oilfield in the Campos Basin. Panel (a) shows the permeability after a manual history matching using a zonation parametrization. Panel (b) shows the ensemble mean permeability obtained with an ensemble-based data assimilation. Example 3.7.1.1.

Consequently, it may be necessary to introduce some form of regularization to control the property values at these pilot point locations.

# 3.7.3 Gradual Deformation

Gradual deformation is designed to gradually deform a geological model until it honors the measurements [368, 203]. It operates by expressing the model as a linear combination of independent Gaussian prior models, { m j } N s j =1 , where m j ∼ N ( m pr , C m ):

$$
̂ m = N s ∑ j =1 z j ( m j - m pr ) + m pr . (3.91)
$$

The coefficients must be selected such that

$$
N s ∑ j =1 z 2 j = 1 . (3.92)
$$

Note that for   N s j =1 z 2 j = 1 the expectation and covariance of   m become

$$
E [ ̂ m ] = E ⎡ ⎣ N s ∑ j =1 z j ( m j - m pr ) + m pr ⎤ ⎦ = m pr + N s ∑ j =1 z j E [ m j - m pr ] = m pr , (3.93)
$$

$$
C [ ̂ m ] = E ⎡ ⎢ ⎣ ( N s ∑ i =1 z i ( m i - m pr ) ) ⎛ ⎝ N s ∑ j =1 z j ( m j - m pr ) ⎞ ⎠ ⊤ ⎤ ⎥ ⎦ = N s ∑ i =1 N s ∑ j =1 z i z j E [ ( m i - m pr ) ( m j - m pr ) ⊤ ] = N s ∑ j =1 z 2 j C m = C m . (3.94)
$$

These results mean that selecting { z j } N s j =1 such that   N s j =1 z 2 j = 1 yields to   m to be a sample from the prior PDF. Imposing this condition, however, is somewhat contradictory if we want to generate conditional realizations, i.e., samples from the posterior. The most basic gradual deformation algorithm combines models in pairs and use

$$
̂ m ( ν ) = m 1 cos( πν ) + m 2 sin( πν ) , (3.95)
$$

  with ν ranging between 0 and 2. Note that in this case, we have z 1 = cos( πν ), z 2 = sin( πν ), and z 2 1 + z 2 2 = 1. We then minimize the objective function with respect to a single parameter, ν . If an acceptable data match is achieved, the process stops. Otherwise, m 1 is replaced with the best   m ( ν ), m 2 is sampled from the prior, and the optimization is repeated. Several refinements to this method exist; for instance, Hu et al. [204] developed a procedure for locally deforming the models.

# 3.7.4 Parametrizations Based on PCA

Principal component analysis (PCA) or Karhunen-Loève expansion is a technique used to decompose the spatial-covariance of an image into a series of

orthogonal basis. PCA of C m was one of the first parametrization methods used to describe permeability fields in reservoir data assimilation [164, 363].

For PCA, we need to solve the following eigenvalue problem

$$
C m x = λ x , (3.96)
$$

with λ denoting the eigenvalue of C m corresponding to the eigenvector x . The idea is to use a small set of eigenvectors corresponding to the largest

eigenvalues as a basis to parameterize the model. In this sense, PCA parametrization tends to be very effective. However, one problem is that if C m is large, the eigenvalue problem may not be computationally feasible to solve.

One alternative is to replace C m with a low-rank approximation computed from a set of N e prior realizations

$$
˜ C m = 1 N e - 1 N e ∑ j =1 ( m j - m ) ( m j - m ) ⊤ = ∆ M ∆ M ⊤ , (3.97)
$$

where

$$
∆ M = 1 √ N e - 1 [ m 1 - m , · · · , m N e - m ] . (3.98)
$$

Applying SVD (Appendix A, Section A.4) to ∆ M and keeping the N r ≤ min { N m ,N e − 1 } largest singular values and the corresponding singular vectors

$$
∆ M = U r Σ r V ⊤ r . (3.99)
$$

It is easy to show that we can write new realizations as

$$
̂ m = m + U r Σ r z , (3.100)
$$

  with z ∼ N ( 0 , I ). Note that because we select N e   N m , we have N r   N m .

# 3.7.4.1 Example: PCA with Low-Rank Prior Covariance

Consider the example from Section 2.4.1.3, which showed unconditional realizations of porosity on a 100 × 100 uniform grid generated using the Cholesky decomposition of the prior covariance C m . Using the same procedure, we generated an ensemble with N e = 1,000 realizations. Fig. 3.8 displays the first three realizations from this ensemble.

Here, we use this ensemble to construct a low-rank approximation of C m and employ Eq. (3.100) to sample a new realization of m by sampling z ∼ N ( 0 , I ). Since z ∈ R N r and N r ≤ N e − 1 &lt; N m , z serves as a reduced parametrization of m , which can be further refined by reducing the number of retained singular values. A common approach to determine N r is to calculate the number of singular values needed to retain a predefined fraction, ξ , of the

(a)

Realization 1

0.35

![](<ensemble_data_assimilation_e-book_version_images/imageFile16.png>)

0.30

0.25

0.20

0.15

0.10

0.05

0.00

(b)

Realization 2

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

(c)

Realization 3

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

Fig. 3.8: Three realizations of porosity generated with the Cholesky decomposition of C m . Example 3.7.4.1.

$$
∑ N r i =1 σ i ∑ N e i =1 σ i ≥ ξ, for ξ ∈ (0 , 1] . (3.101)
$$

Eq. (3.101) assumes that the singular values, σ i , are sorted in decreasing order. Fig. 3.9 presents a plot of the singular values of   C m . Given that we used 1,000 realizations and subtracted the average vector to form ∆ M , the total number of non-zero singular values is 999.

![](<ensemble_data_assimilation_e-book_version_images/imageFile39.png>)

(999,1)

100

1

(733,0.9)

0.8

Singular Value

10

(364,0.7)

0.6



(147,0.5)

0.4

1

(31,0.25)

0.2

(10,0.1)

0.1 0

0 1000

0

200

400

600

800

1000

N r

INTERNA Fig. 3.9: Singular values of   C m . The values besides each white circle indicate the number of singular values and corresponding energy, ξ . Example 3.7.4.1.

0.35

0.30

0.25

0.20

0.15

0.10

0.05

(a)

= 1 ( N

ξ

r

= 999)

r

0.00

(b)

= 0 . 9

( N

ξ

.

r

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

= 733)

r

(c)

= 0 . 7

( N

ξ

.

r

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

= 364)

r

(d)

= 0 . 5

( N

ξ

.

r

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

= 147)

r

![](<ensemble_data_assimilation_e-book_version_images/imageFile17.png>)

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

(e)

= 0 .

( N

ξ

25

r

= 31)

r

(f)

= 0 . 1

( N

ξ

.

r

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

= 10)

r

Fig. 3.10: PCA realization generated with different levels of truncation energy. Example 3.7.4.1.

# 3.7.5 Parametrizations Based on Data Sensitivity

PCA parametrization uses only prior information to define the basis vectors, which remain fixed throughout the data assimilation process. However, an “optimal parametrization” should ideally consider both the type and amount of data utilized. This can be achieved by incorporating data sensitivity (or a related measure) into the parametrization. An early example of such a parametrization is the gradzone method [40]. In this method, the primary eigenvectors of the matrix G   C − 1 e G are employed to identify regions (gradzones) that have the most significant impact on reducing the objective function. It is worth noting that instead of computing the entire sensitivity

Rodrigues [367] proposed a parametrization method based on the dominant right singular values of the dimensionless sensitivity matrix, G d = C − 1/2 e GC 1/2 m . Rodrigues also introduced a technique for computing the singular vectors associated with the largest singular values without explicitly constructing the matrix G d by employing the Lanczos algorithm [170]. Building on these ideas, Tavakoli and Reynolds [429] extended the methodology and provided a theoretical justification, arguing that parametrization using the leading right singular vectors of G d creates an optimal basis by discarding directions that contribute minimally to uncertainty reduction. Further developments and enhancements of this approach are discussed in subsequent works [430, 393, 395].

# 3.7.6 Parametrizations for Facies

The typical workflow for constructing reservoir models includes a facies modeling step, in which the reservoir is divided into regions with similar rock properties. Facies, in this context, are categorical variables representing distinct rock types. Incorporating facies into data assimilation tends to be challenging due to their categorical nature.

The literature presents a wide variety of methods for reparameterizing facies models in data assimilation. Among the earliest approaches is the use of level-set functions [64, 272, 305, 304, 347]. Another class of methods includes the dynamic updating of probability maps, which are incorporated as soft constraints in geostatistical simulations [212, 432, 65, 252, 388]. Additional techniques include the discrete cosine transform [213], kernel PCA [378], optimization-based PCA [453, 120], and PCA with truncation based on the cumulative density function of the prior [69, 70, 160].

To date, truncated Gaussian [296] and truncated plurigaussian (TPG) methods [157, 17, 35] are the most utilized and effective approaches for parameterizing facies models, especially in the context of ensemble-based data assimilation [267, 484, 387, 386]. These methods represent facies using one or more Gaussian latent vectors along with a rock-type rule. During the data assimilation process, these latent vectors are iteratively updated to generate new facies distributions.

INTERNA

(a)

z 1

1

![](<ensemble_data_assimilation_e-book_version_images/imageFile18.png>)

2.00

1.00

0.00

-1.00

-2.00

(b)

z 2

2

3.00

2.00

1.00

0.00

-1.00

-2.00

-3.00

(c)

Facies

4.00

3.50

3.00

2.50

2.00

1.50

1.00

0.16

0.14

0.12

0.10

0.08

0.06

0.04

0.02

0

0 -3.0

-2.0

-1.0

0

1.0

2.0

0.14

0.12

0.10

0.08

0.06

0.04

0.02

0

3.0

0 -3.0

-2.0

-1.0

0.3

0.2

0.1

0

1.0

2.0

3.0

0

(d)

z 1

INTERNA

INTERNA

(e) INTERNA

z 2

2

INTERNA

1

2

3

(f) INTERNA

Facies

INTERNA

4

4

1

2

3

2

1

(g)

Rock-type rule

rule

Fig. 3.11: Model with four facies generated by truncating two latent Gaussian vectors.

# 3.7.7 Parametrizations for Complex Geological Models

Parametrizations based on TPG are widely used in practical reservoir data assimilation applications [75, 123]. However, TPG may not adequately represent facies with complex geometries resulting from object-based modeling [107, 106], multiple-point statistics [179, 417, 290], or rule-based modeling [352]. Consequently, considerable research is underway to develop parametrization methods capable of representing complex facies distributions. Recent publications [308, 63, 57] suggest that deep learning methods show promise as alternative approaches for re-parameterizing facies models. Similar to TPG, some of these methods represent facies using Gaussian latent variables, allowing the prior PDF to be considered Gaussian. This approach aligns with the objective function formulation in Chapter 2, making these methods particularly suitable for use with ensemble smoothers.

# 3.7.8 Big-Loop Parametrization

In a conventional data assimilation problem, the goal is to sample the distribution p ( m | d obs ), where m contains, for example, values of porosity and permeability at the gridblocks of the model. This problem is represented by Bayes’ rule as:

$$
p ( m | d obs ) ︸ ︷︷ ︸ posterior ∝ p ( d obs | m ) ︸ ︷︷ ︸ likelihood × p ( m ) ︸ ︷︷ ︸ prior . (3.102)
$$

In a big-loop workflow, we may also want to estimate hyper-parameters, such as variogram ranges and azimuth, which are used to generate porosity and permeability realizations through geostatistical methods. This extended problem can be described using hierarchical priors in Bayes’ rule

$$
p ( m | d obs ) ︸ ︷︷ ︸ posterior ∝ p ( d obs | m ) ︸ ︷︷ ︸ likelihood × p ( m | z ) ︸ ︷︷ ︸ conditional prior × p ( z ) , ︸︷︷︸ hierarchical prior (3.103)
$$

where z contains the unknown hyper-parameters. This approach is more challenging due to the “double stochasticity”: m depends on both the random vector z and the random seed r used to initiate the geostatistical algorithm. Fig. 3.12 illustrates this issue. In a standard “small loop” problem, solving with a derivative-based method requires computing derivatives of the predictions with respect to m . However, in the big-loop case, we must employ the chain rule due to the dependency of m on z and account for the random seed r . This involves marginalizing the random seed by averaging the derivatives—repeating the derivative calculation for different random

seeds and computing the mean. This procedure, while necessary, significantly

increases the computational cost of the process.

![](<ensemble_data_assimilation_e-book_version_images/imageFile19.png>)

Small‐loop

-

loop

INTERNA

Big‐loop

-

loop

Fig. 3.12: Illustration of the smalland big-loop model updating schemes.

![](<ensemble_data_assimilation_e-book_version_images/imageFile43.png>)

4

# Ensemble Kalman Filter

Abstract: This chapter reviews the ensemble Kalman filter (EnKF), a widely used data assimilation method across various geophysical fields. It addresses key topics such as the Kalman filter, sequential data assimilation, ensemble covariances, parameter-state consistency, and square root formulations. This chapter also discuss how to integrate the EnKF with reservoir simulators.

# 4.1 Introduction

Reservoir data assimilation is typically framed as a parameter-estimation problem, aiming to estimate the vector of model parameters, m , given a set of observations, d obs . However, this chapter adopts a different approach by considering the sequential assimilation of data over time. In this context, it is convenient to formulate the problem in terms of a combined parameterstate vector. While parameters refer to the “static” uncertainty properties of the reservoir, states refer to the “dynamic” variables that evolve over time, such as pressure, temperature, phase saturation, and fluid composition.

The primary reason for expressing the problem in terms of both parameters and states is to enable the forward model to be initiated from any intermediate time step during the sequential data assimilation process. This approach assumes that the forward model is a first-order Markov process, meaning that the system’s state at time step t n , denoted as x n , depends solely on m and the state at the previous time step, t n − 1 , and not on any earlier instances, i.e.,

$$
x n = f ( m , x n - 1 ) , (4.1)
$$

where f ( · ) represents the nonlinear forward model.

Let y n ∈ R N y be the combined parameter-state vector at time t n defined as:

$$
y n = [ m x n ] = [ m f ( m , x n - 1 ) ] . (4.2)
$$

Also, let d n obs denote the set of observations available at time t n ( d n obs ∈ R N n ) 1 . Given d n obs , we can define three problems of interest:

• Filtering: find the distribution of the current parameter-state vector given the current observations, p ( y n | d n obs ). • Smoothing: find the distribution of a past parameter-state vector given

the current observations, p ( y k | d n obs ) for k &lt; n . • Forecasting: find the distribution of a future parameter-state vector

given the current observations, p ( y k | d n obs ) for k &gt; n .

Fig. 4.1 illustrates the evolution of the distribution of a state variable for three times steps before (prior) and after (posterior) the assimilation of a datum at time t n . The posterior distributions p ( y n − 1 | d n obs ), p ( y n | d n obs ), and p ( y n +1 | d n obs ) correspond to the smoothing, filtering, and forecasting solutions, respectively 2 .

# 4.2 Kalman Filter

Before delving into the EnKF, it is important to discuss its famous predecessor: the Kalman filter (KF), named after Rudolf E. Kálmán, one of its primary developers. The KF finds widespread applications in guidance, navigation, and vehicle control systems, as well as in time series analysis, signal processing, and econometrics.

1 Note that N n denotes the number of data points at time t n , which is different from our previous notation where N d denotes the total number of data points, including all time steps. 2

The distinction between filtering, smoothing, and forecasting is not very common in the reservoir data assimilation literature, but these terms are used frequently in other fields. Moreover, this terminology helps us to understand the names given to some of the methods discussed in this chapter. The attentive reader may have noticed that we used the term “forecasting” instead of “prediction.” It appears that these words are used interchangeably in the literature. In fact, the original Kalman filter paper by Kalman [228] uses the word “prediction.” However, we are going to make a distinction between the two words. We use “prediction” as a more general term; for example, we use “prediction” for a state generated from a model. In this sense, we can use a model to predict a past state, sometimes referred to as “hindcasting” [99]. We can also use the model to predict the present, which is referred to as “nowcasting” [338]. We reserve the word “forecasting” for the prediction of future states.

Ensemble Kalman Filter

-

-

-

--

-

(a)

Prior

![](<ensemble_data_assimilation_e-book_version_images/imageFile20.png>)

t n

n

(b)

Posterior

Fig. 4.1: Illustration of the distribution of a state variable before (prior) and after (posterior) the assimilation of a datum at t n . The posterior distributions indicated in (b), p ( y n − 1 | d n obs ) , p ( y n | d n obs ) , and p ( y n +1 | d n obs ) correspond to the solutions of the smoothing, filtering and forecasting problems, respectively.

From a theoretical standpoint, the main assumptions of the KF are that the underlying dynamical system is linear and that all error terms follow multivariate Gaussian distributions.

# 4.2.1 Kalman Filter as a Minimum Variance Estimator

In this section, the KF is derived as the best linear unbiased estimate for the combined parameter-state vector y . To reduce wording, we will simply refer to this vector as the state vector. First, we assume that the unknown true state at time t n , denoted by y n true , is given by:

$$
y n true = F n y n - 1 true + e n y . (4.3)
$$

Here, F n is an N y × N y matrix representing the linear forward model, and e n y is a Gaussian model error. In the following, we will either neglect the model error e n y or assume an error term e n that combines the effects of both model and measurement errors, as discussed in Chapter 2.

Similarly, let the vector of observations at t n be represented by

$$
d n obs = H n y n true + e n , (4.4)
$$

where H n is an N n × N y matrix and e n ∼ N ( 0 , C e n ) is the Gaussian dataerror vector. H n is often referred to as an observation matrix. The forecast state vector at is written as

t n

$$
y n,f = F n y n - 1 ,a , (4.5)
$$

where the superscripts f and a denote forecast and analysis, respectively. Note that Eq. (4.5) indicates that the forecast state at time t n depends on the analyzed (or updated) state at time t n − 1 only. We now define the innovation vector as

We now define the innovation vector as

$$
δ d n = d n obs - H n y n,f , (4.6)
$$

and the forecast error vector as

$$
δ y n,f = y n true - y n,f . (4.7)
$$

Before we continue, it is convenient to show that the forecast state is unbiased, i.e., the expectation of the forecast error is zero

$$
E [ δ y n,f ] = E [ y n true - y n,f ] = 0 . (4.8)
$$

To show (4.8), it is necessary to assume that at t 0 the true state is a sample from the prior, y 0 true ∼ N ( y 0 ,a , C a y 0 ). This is the same as assuming that we have an unbiased prior estimate of the truth. At time t 1 the true and forecast estimates are 1 0

$$
y 1 true = F 1 y 0 true , (4.9)
$$

and

$$
y 1 ,f = F 1 y 0 ,a . (4.10)
$$

Hence

$$
E [ δ y 1 ,f ] = E [ y 1 true - y 1 ,f ] = E [ F 1 ( y 0 true - y 0 ,a )] = F 1 ( E [ y 0 true ] - E [ y 0 ,a ]) = F 1 ( y 0 true - y 0 true ) = 0 . (4.11)
$$

Now by mathematical induction 3 , we assume that the same is valid for t n − 1 and conclude that

$$
E [ δ y n,f ] = E [ y n true - y n,f ] = E [ F n ( y n - 1 true - y n - 1 ,a )] = F n ( E [ y n - 1 true ] - E [ y n - 1 ,a ]) = F n ( y n - 1 true - y n - 1 true ) = 0 , (4.12)
$$

which completes the proof that the forecasts state is unbiased.

We can also show that the expectation of the innovation vector is zero

$$
E [ δ d n ] = E [ d n obs - H n y n,f ] = E [ H n y n true + e n - H n y n,f ] = H n E [ y n true - y n,f ] + E [ e n ] = 0 . (4.13)
$$

Now we define the analyzed state vector as

$$
y n,a = y n,f + K n δ d n , (4.14)
$$

where K n is the so-called Kalman gain. We define the analyzed error vector as

We define the analyzed error vector as

$$
δ y n,a = y n true - y n,a . (4.15)
$$

Note that the analysis (Eq. (4.14)) is unbiased because

$$
E [ δ y n,a ] = E [ y n true - y n,a ] = E [ y n true - y n,f - K n δ d n ] = E [ y n true - y n,f ] - K n E [ δ d n ] = 0 . (4.16)
$$

The forecast error-covariance is defined as

$$
C [ δ y n,f ] = E [ ( δ y n,f - E [ δ y n,f ]) ( δ y n,f - E [ δ y n,f ]) ⊤ ] = E [ δ y n,f ( δ y n,f ) ⊤ ] . (4.17)
$$

3 Mathematical induction is a technique used to prove statements about ordered sets. In mathematical induction, we first show that the statement holds for n = 1, then we assume it holds for n − 1 and show it holds for n .

Note that this error-covariance is the same as the covariance of the forecast state because

$$
C [ δ y n,f ] = C [ y n true - y n,f ] = E [( y n true - y n,f - E [ y n true - y n,f ]) × ( y n true - y n,f - E [ y n true - y n,f ]) ⊤ ] = E [( y n true - y n,f - y n true + E [ y n,f ]) × ( y n true - y n,f - y n true + E [ y n,f ]) ⊤ ] = E [ ( y n,f - E [ y n,f ]) ( y n,f - E [ y n,f ]) ⊤ ] = C [ y n,f ] = C f y n . (4.18)
$$

Similarly, the analyzed state/error-covariance is defined as

$$
C a y n = C [ δ y n,a ] = E [ δ y n,a ( δ y n,a ) ⊤ ] . (4.19)
$$

Finally, we can write the covariance of the innovation vector using

$$
C δ d n = C [ δ d n ] = E [ ( δ d n - E [ δ d n ]) ( δ d n - E [ δ d n ]) ⊤ ] = E [ δ d n ( δ d n ) ⊤ ] = E [ ( d n obs - H n y n,f ) ( d n obs - H n y n,f ) ⊤ ] = E [ ( H n y n true + e n - H n y n,f ) ( H n y n true + e n - H n y n,f ) ⊤ ] = E [ ( H n ( y n true - y n,f ) + e n ) ( H n ( y n true - y n,f ) + e n ) ⊤ ] = E [ ( H n ( y n true - y n,f ) + e n ) ( ( y n true - y n,f ) ⊤ H ⊤ n +( e n ) ⊤ )] = E [ H n ( y n true - y n,f ) ( y n true - y n,f ) ⊤ H ⊤ n ] + E [ H n ( y n true - y n,f ) ( e n ) ⊤ ] + E [ e n ( y n true - y n,f ) ⊤ ] + E [ e n ( e n ) ⊤ ] = H n E [ ( y n true - y n,f ) ( y n true - y n,f ) ⊤ ] H ⊤ n + E [ e n ( e n ) ⊤ ] = H n C f y n H ⊤ n + C e n . (4.20)
$$

We seek for a matrix K n that minimizes the expectation of the norm of the analyzed error vector,   δ y n,a   2 2 , which is given by

$$
E [ ‖ δ y n,a ‖ 2 2 ] = E [ ( y n true - y n,a ) ⊤ ( y n true - y n,a ) ] = E ⎡ ⎣ N y ∑ i =1 ( y n true ,i - y n,a i ) 2 ⎤ ⎦ = N y ∑ i =1 V [ y n true ,i - y n,a i ] = tr ( C a y n ) . (4.21)
$$

Therefore, we need to write an expression for the analyzed covariance matrix C a y n

$$
C a y n = C [ y n true - y n,a ] = C [ y n true - y n,f - K n ( H n y n true + e n - H n y n,f )] = C [ ( I - K n H n ) ( y n true - y n,f ) - K n e n ] . (4.22)
$$

Noting that the random vectors e n and ( y n true − y n,f ) are independent and that the expectations of both these terms are zero, we can demonstrate, using the usual technique of expanding expectations that

$$
C a y n = E [ ( I - K n H n ) ( y n true - y n,f ) ( y n true - y n,f ) ⊤ ( I - K n H n ) ⊤ ] + E [ K n e n ( e n ) ⊤ K ⊤ n ] = ( I - K n H n ) C [ y n true - y n,f ] ( I - K n H n ) ⊤ + K n C [ e n ] K ⊤ n = ( I - K n H n ) C f y n ( I - K n H n ) ⊤ + K n C e n K ⊤ n = ( I - K n H n ) ( C f y n - C f y n H ⊤ n K ⊤ n ) + K n C e n K ⊤ n = C f y n - C f y n H ⊤ n K ⊤ n - K n H n C f y n + K n H n C f y n H ⊤ n K ⊤ n + K n C e n K ⊤ n = C f y n - C f y n H ⊤ n K ⊤ n - K n H n C f y n + K n ( H n C f y n H ⊤ n + C e n ) K ⊤ n = C f y n - C f y n H ⊤ n K ⊤ n - K n H n C f y n + K n C δ d n K ⊤ n . (4.23)
$$

Taking the derivative 4 of tr   C a y n   with respect to K n gives

4 Appendix A (Section A.3) presents a basic review of matrix calculus.

$$
∂ tr ( C a y n ) ∂ K n = - C f y n H ⊤ n - ( H n C f y n ) ⊤ +2 K n C δ d n = - 2 C f y n H ⊤ n +2 K n C δ d n . (4.24)
$$

Setting this derivative equal to zero and solving for K n leads to

$$
K n = C f y n H ⊤ n C - 1 δ d n = C f y n H ⊤ n ( H n C f y n H ⊤ n + C e n ) - 1 . (4.25)
$$

Eq. (4.25) is the Kalman gain matrix originally derived by Kalman [228]. In statistics, this type of estimator is known as BLUE (best linear unbiased estimator), with “best” referring to the estimator that results in the lowest variance of the estimate. The literature on the KF is extensive, given its wide range of applications across various fields. The derivation and discussions presented here are confined to the key concepts necessary to introduce and motivate the development of ensemble-based variants.

# Remark 4.1: BLUE

BLUE (best linear unbiased estimator) is a statistical concept used to describe an estimator that satisfies the following three properties:

- 1. Linearity: The estimator is a linear function of the observed data.
- 2. Unbiasedness: The expected value of the estimator equals the true parameter being estimated. In other words, on average, the estimator is correct.
- 3. Best: Among all linear and unbiased estimators, the BLUE has the minimum variance.


# 4.2.1.1 Compact Notation

In the Kalman gain, the forecast state covariance matrix, C f y n , appears multiplied by the transpose of the observation matrix, H n . We can show that this product is equivalent to the cross-covariance between the state vector and predicted data, C f yd n ,

$$
C f yd n = E [ ( y n,f - E [ y n,f ]) ( d n,f - E [ d n,f ]) ⊤ ] = E [ ( y n,f - E [ y n,f ]) ( H n y n,f - E [ H n y n,f ]) ⊤ ] = E [ ( y n,f - E [ y n,f ]) ( y n,f - E [ y n,f ]) ⊤ H ⊤ n ] = C f y n H ⊤ n . (4.26)
$$

Similarly, the product H n C f y n H   n is equivalent to the auto-covariance of predicted data C f dd n because

$$
C f dd n = E [ ( d n,f - E [ d n,f ]) ( d n,f - E [ d n,f ]) ⊤ ] = H n E [ ( y n,f - E [ y n,f ]) ( y n,f - E [ y n,f ]) ⊤ ] H ⊤ n = H n C f y n H ⊤ n . (4.27)
$$

Therefore, we can write the KF analysis in a very compact and convenient form

$$
y n,a = y n,f + C f yd n ( C f dd n + C e n ) - 1 ( d n obs - H n y n,f ) . (4.28)
$$

The KF can be summarized as the recursive application of two steps: forecast and analysis , which is indicated in Pseudo-code 4.1. Fig. 4.2 illustrates the process.

# Pseudo-code 4.1: Kalman Filter

1. Forecast: given the best estimate of the true state at time t n − 1 , denoted by y n − 1 ,a , with uncertainty represented by the covariance C a y n − 1 , we advance the linear dynamical system to the next data assimilation time step based on the forward model using

$$
y n,f = F n y n - 1 ,a , (4.29)
$$

and

$$
C f y n = F n C a y n - 1 F ⊤ n . (4.30)
$$

2. Analysis: given the a set of observations at time t n , we update our estimates of the state and covariance using

and

where

$$
y n,a = y n,f + K n ( d n obs - H n y n,f ) , (4.31)
$$

$$
C a y n = ( I - K n H n ) C f y n , (4.32)
$$

$$
K n = C f y n H ⊤ n ( H n C f y n H ⊤ n + C e n ) - 1 . (4.33)
$$

![](<ensemble_data_assimilation_e-book_version_images/imageFile21.png>)

Fig. 4.2: Illustration of the data assimilation sequence of the Kalman filter. In the KF the PDF of the state vector at each time step is Gaussian. In this figure, the dashed PDFs correspond to the forecast and the solid PDF the analysis.

# 4.2.1.2 Example: Porosity of a Rock Sample

Consider the same problem discussed in Section 2.3.1.1, where the objective is to estimate the porosity of a rock sample by combining prior information, φ ∼ N ( φ pr ,σ 2 pr ), with a measurement, d obs ∼ N ( φ obs ,σ 2 e ). We can solve this problem by simply applying the KF equations. However,

for the sake of the exercise, let’s derive the KF equations directly for this problem. First, we express our best prior estimate of the porosity as

$$
φ f = φ pr = φ true + δφ f , (4.34)
$$

where δφ f represents the forecast error. We express the observed data as

$$
φ obs = φ true + e, (4.35)
$$

where e is the measurement error.

We do not know the values of δφ f and e , but we make the following assumptions about their statistics:

1. E [ δφ f ] = 0: unbiased prior estimate. 2. [ ] = 0: unbiased measurement errors.

E e

3. E [ δφ f e ] = 0: independent errors. 4. [ ] = 2 : we know the prior

V δφ f σ f variance. 5. [ ] = 2 : we know the variance of the

V e σ e measurement error.

We are looking for a linear estimator

which is unbiased

$$
φ a = k 1 φ f + k 2 φ obs , (4.36)
$$

$$
E [ φ a ] = E [ k 1 φ f + k 2 φ obs ] = φ true = E [ k 1 ( φ true + δφ f ) + k 2 ( φ true + e )] = φ true = E [ k 1 φ true + k 2 φ true ] = φ true . (4.37)
$$

Therefore

$$
k 1 + k 2 = 1 . (4.38)
$$

Our linear estimator becomes

$$
φ a = (1 - k 2 ) φ f + k 2 φ obs , (4.39)
$$

which is clearly a weighted average between φ f and φ obs . An expression for the error associated with the new estimate can be derived by noting that

$$
φ a = φ true + δφ a φ true + δφ a = (1 - k 2 ) ( φ true + δφ f ) + k 2 ( φ true + e ) δφ a = δφ f + k 2 ( e - δφ f ) . (4.40)
$$

This estimate is also unbiased

$$
E [ δφ a ] = E [ δφ f + k 2 ( e - δφ f )] = 0 . (4.41)
$$

The variance of the error in the estimate is

$$
V [ δφ a ] = E [ ( δφ a - E [ δφ a ]) 2 ] = E [ δφ 2 a ] = E [ ( δφ f + k 2 ( e - δφ f )) 2 ] = E [ δφ 2 f - 2 k 2 δφ 2 f + k 2 2 ( e 2 + δφ 2 f ) +2 k 2 δφ f e - 2 k 2 2 eδφ f ] = E [ δφ 2 f ] - 2 k 2 E [ δφ 2 f ] + k 2 2 E [( e 2 + δφ 2 f )] +2 k 2 E [ δφ f e ] - 2 k 2 2 E [ eδφ f ] = σ 2 f - 2 k 2 σ 2 f + k 2 2 ( σ 2 e + σ 2 f ) = σ 2 a . (4.42)
$$

To minimize the variance of the new estimate, we simply compute the derivative and set to zero

$$
dσ 2 a dk 2 = - 2 σ 2 f +2 k 2 ( σ 2 e + σ 2 f ) = 0 . (4.43)
$$

Now solving for k 2 , which corresponds to the Kalman gain, we obtain

$$
k 2 = σ 2 f σ 2 e + σ 2 f . (4.44)
$$

The porosity estimate becomes

$$
φ a = φ f + σ 2 f σ 2 e + σ 2 f ( φ obs - φ f ) , (4.45)
$$

with variance given by

$$
σ 2 a = σ 2 f - σ 4 f σ 2 e + σ 2 f . (4.46)
$$

# 4.2.2 Kalman Filter as a Bayesian Estimator

We presented the derivation of the KF as a minimum variance estimator. However, the KF equations can also be obtained from Bayes’ rule. In fact, when expressing the KF analysis equations in terms of the vector of model parameters, m , and utilizing the Kalman gain definition, we arrive at the following equations:

$$
m n,a = m n,f + C f m n G ⊤ n ( G n C f m n G ⊤ n + C e n ) - 1 ( d n obs - G n m n,f ) (4.47)
$$

and

$$
C a m n = C f m n - C f m n G ⊤ n ( G n C f m n G ⊤ n + C e n ) - 1 G n C f m n . (4.48)
$$

We replaced H n with G n to denote the sensitivity matrix of the predicted data with respect to the vector of model parameters, m , to be consistent with our previous notation. Noting that our best estimate of m at time zero is the prior mean, i.e., m 0 ,f = m pr , and the covariance is also the prior, C f m 0 = C m , we obtain:

and

$$
m 0 ,a = m map (4.49)
$$

$$
C a m 0 = C m c . (4.50)
$$

Assuming that measurement and model errors are uncorrelated in time and that the model’s evolution is a first-order Markov process, we can show that sequential and simultaneous data assimilation are equivalent, as discussed in Section 4.2.3. In this case, the result presented above holds for any time t n .

# 4.2.2.1 Example: Porosity of a Rock Sample

We can solve the same problem of Example 4.2.1.2 starting from the Bayes’ rule. In this case, we assume a Gaussian prior distribution for porosity

$$
p ( φ ) ∝ exp [ - 1 2 ( φ - φ pr ) 2 σ 2 pr ] (4.51)
$$

and a Gaussian Likelihood

$$
L ( φ ) ∝ exp [ - 1 2 ( φ obs - φ ) 2 σ 2 e ] . (4.52)
$$

Using Bayes’ rule, the posterior becomes

$$
p ( φ | φ obs ) ∝ L ( φ ) p ( φ ) ∝ exp [ - 1 2 ( φ obs - φ ) 2 σ 2 e ] exp [ - 1 2 ( φ - φ pr ) 2 σ 2 pr ] ∝ exp [ - 1 2 ( ( φ obs - φ ) 2 σ 2 e + ( φ - φ pr ) 2 σ 2 pr )] (4.53)
$$

We can expand the squared terms

$$
p ( φ | φ obs ) ∝ exp [ - 1 2 ( φ 2 obs - 2 φφ obs + φ 2 σ 2 e + φ 2 - 2 φφ pr + φ 2 pr σ 2 pr )] ∝ exp [ - 1 2 ( φ 2 obs σ 2 pr - 2 φφ obs σ 2 pr + φ 2 σ 2 pr + φ 2 σ 2 e - 2 φφ pr σ 2 e + φ 2 pr σ 2 e σ 2 e σ 2 pr )] ∝ exp [ - 1 2 ( φ 2 ( σ 2 pr + σ 2 e ) σ 2 e σ 2 pr - 2 φ ( φ obs σ 2 pr + φ pr σ 2 e ) σ 2 e σ 2 pr + φ 2 obs σ 2 pr + φ 2 pr σ 2 e σ 2 e σ 2 pr )] . (4.54)
$$

Because the prior Gaussian and the model is linear, the posterior is also Gaussian. Therefore

$$
p ( φ | φ obs ) ∝ exp [ - 1 2 ( φ - φ map ) 2 σ 2 φ c ] ∝ exp [ - 1 2 ( φ 2 - 2 φφ map + φ 2 map σ 2 φ c )] . (4.55)
$$

We have two expressions for p ( φ | φ obs ). In order for these expressions to be equivalent, the coefficients multiplying φ 2 must be the same. Hence

$$
1 σ 2 φ c = σ 2 pr + σ 2 e σ 2 e σ 2 pr , (4.56)
$$

which lead to

$$
σ 2 φ c = σ 2 e σ 2 pr σ 2 pr + σ 2 e . (4.57)
$$

Previously, we derived the following expression using the KF

$$
σ 2 a = σ 2 f - σ 4 f σ 2 e + σ 2 f = σ 2 f ( σ 2 e + σ 2 f ) - σ 4 f σ 2 e + σ 2 f = σ 2 f σ 2 e σ 2 f + σ 2 e . (4.58)
$$

Therefore, writing σ f = σ pr , we have σ φ c = σ a . Repeating the same procedure for the coefficients multiplying 2 φ gives

$$
φ map σ φ c = φ obs σ 2 pr + φ pr σ 2 e σ 2 e σ 2 pr . (4.59)
$$

Hence,

$$
φ map = φ obs σ 2 pr + φ pr σ 2 e σ 2 e + σ 2 pr = φ obs σ 2 pr + φ pr σ 2 e + φ pr σ 2 pr - φ pr σ 2 pr σ 2 e + σ 2 pr = φ pr + σ 2 pr σ 2 e + σ 2 pr ( φ obs - φ pr ) . (4.60)
$$

Again, writing φ pr = φ f and σ f = σ pr , we have φ map = φ a . We have arrived to at the same expressions starting from the assumption of BLUE and from Bayes’ rule with Gaussian prior and likelihood.

# 4.2.2.2 Example: Porosity Distribution in a Core Sample

Consider the same problem discussed in Section 2.3.1.4, where the objective is to estimate the porosity distribution in a rock core discretized in 50 gridblocks. Before, we obtained the MAP estimate and RML samples by assimilating 10 data points simultaneously. Now, we use the KF and assimilate data sequentially, mimicking “pseudo time steps.” Fig. 4.3 shows the evolution of the data assimilation process, indicating the best estimate after the assimilation of each datum and the corresponding uncertainty range. The estimated mean and standard deviation after the assimilation of the 10th data point are exactly the same as presented in Fig. 2.2b.

![](<ensemble_data_assimilation_e-book_version_images/imageFile46.png>)

















































 

  

  

�





��



��

�





��



��

�





��





  U GE RF 

  U GE RF 

  U GE RF 

(a)

Prior

(b)

1st datum

(c)

2nd datum

















































 

  

 

�





��



��

�





��





�





��





  U GE RF 

  U GE RF 

  U GE RF 

(d)

3rd datum

(e)

4th datum

(f)

5th datum

















































 

 

 

�





��





�





��





�





��





  U GE RF 

  U GE RF 

  U GE RF 

(g)

6th datum

(h)

7th datum

(i)

8th datum

































 

 

�





��





�





��





  U GE RF 

  U GE RF 

(j)

9th datum

(k)

10th datum

Fig. 4.3: KF applied to estimate the porosity in a core sample. The solid red line represents the ground truth. The red circles represent the observed data points. The dashed lines represent the best estimate, and the dotted lines represent the error bands corresponding to three standard deviations. Example 4.2.2.2.

# 4.2.3 Sequential Data Assimilation

Sequential data assimilation (SDA) refers to the process of integrating measured data into a dynamical system sequentially over a series of discrete time steps. The fundamental condition for SDA is that the system’s evolution can be modeled as a first-order Markov process, meaning that the state at time t n depends solely on the state at the previous time step, i.e.,

$$
y n = f ( y n - 1 , y n - 2 , . . . , y 0 ) = f ( y n - 1 ) . (4.61)
$$

In fact, when we derived the KF, we wrote the forecast state vector as

$$
y n,f = F n y n - 1 ,a . (4.62)
$$

Note that the first-order Markov condition can hold even for nonlinear prob5

.

lems

.

![](<ensemble_data_assimilation_e-book_version_images/imageFile22.png>)

Fig. 4.4: Sequential Bayesian data assimilation. The horizontal arrows indicate the evolution of the dynamical system, and the vertical arrows the data-conditioning steps.

SDA fits in the Bayesian framework as illustrated in Fig. 4.4, which depicts the main elements. In this process, sequential and simultaneous data assimilation are equivalent. In order to show this equivalence, first assume that at the time t n − 1 , we have updated the distribution of y n by incorporating all data available up to the time t n − 1 simultaneously. In this case, we write the posterior PDF as

$$
p ( y n | ̂ d n - 1 obs ) ∝ p ( y n ) p ( ̂ d n - 1 obs | y n ) , (4.63)
$$

    where p ( y n ) represents our prior knowledge about the distribution of y at time t n . In the above expression, we use a hat over the observed data vector

5 It is worth noting that the first-order Markov condition holds in reservoir simulations, where the state (say, pressure and saturation) at time t n is solely dependent on static parameters and the state at the preceding time step, t n − 1 . This property is precisely why we can employ restarts in reservoir simulators.

$$
̂ d n - 1 obs = ⎡ ⎢ ⎢ ⎢ ⎣ d n - 1 obs d n - 2 obs . . . d 0 obs ⎤ ⎥ ⎥ ⎥ ⎦ . (4.64)
$$

Now if we want to incorporate a new set of observations at time t n , we could start from scratch and write

$$
p ( y n | ̂ d n obs ) ︸ ︷︷ ︸ post ∝ p ( y n ) ︸ ︷︷ ︸ prior p ( ̂ d n obs | y n ) ︸ ︷︷ ︸ likelihood . (4.65)
$$

Eq. (4.65) is the standard Bayes’ rule for the PDF of state y at time t n conditioned to all observations from time zero until (and including) t n . In other words, this is the posterior PDF obtained by simultaneous data assimilation.

Alternatively, we could claim that just before time t n , the knowledge about y is summarized in the distribution p   y n |   d n − 1 obs   . Hence, we can just use p   y n |   d n − 1 obs   as the distribution prior to the assimilation of d n obs and update the PDF of y as

$$
p s ( y n | ̂ d n obs ) ︸ ︷︷ ︸ sequential post ∝ p ( y n | ̂ d n - 1 obs ) ︸ ︷︷ ︸ 'new' prior p ( d n obs | ̂ d n - 1 obs , y n ) ︸ ︷︷ ︸ 'new' likelihood . (4.66)
$$

We added a subscript “s” to denote that this is the posterior PDF obtained by assimilating data from t 0 to t n − 1 simultaneously, and assimilating the data at t n sequentially. We want to show that (4.65) and (4.66) are equivalent, which means

$$
p s ( y n | ̂ d n obs ) = p ( y n | ̂ d n obs ) . (4.67)
$$

First, we write

$$
p s ( y n | ̂ d n obs ) ∝ p ( y n | ̂ d n - 1 obs ) p ( d n obs | ̂ d n - 1 obs , y n ) ∝ p ( y n ) p ( ̂ d n - 1 obs | y n ) p ( d n obs | ̂ d n - 1 obs , y n ) . (4.68)
$$

Now, assuming that measurement and model errors are uncorrelated in time is equivalent to saying that

$$
p ( d n obs | ̂ d n - 1 obs , y n ) = p ( d n obs | y n ) (4.69)
$$

and

$$
p ( ̂ d n - 1 obs | y n ) p ( d n obs | y n ) = p ( ̂ d n obs | y n ) . (4.70)
$$

Using (4.70) in (4.68) results in

$$
p s ( y n | ̂ d n obs ) ∝ p ( y n | ̂ d n - 1 obs ) p ( d n obs | ̂ d n - 1 obs , y n ) ∝ p ( y n ) p ( ̂ d n obs | y n ) = p ( y n | ̂ d n obs ) . (4.71)
$$

This completes the derivation of the equivalence between sequential and simultaneous data assimilation. Note that the demonstration was limited to time t n , but it obviously holds for any time by mathematical induction. Returning to the KF, in which case we assume that all PDFs are Gaussian,

we can write that at time t n − 1 , our knowledge about the state vector is summarized by the PDF

$$
p ( y n - 1 ,a | ̂ d n - 1 obs ) = N ( y n - 1 ,a , C a y n - 1 ) . (4.72)
$$

Therefore, the two steps of the KF can be stated in the following Pseudocode 4.2.

# Pseudo-code 4.2: Kalman Filter (Bayesian Version)

- 1. Forecast: apply the forward model to obtain the PDF of the state at time t n given the observations up to time t n − 1 :

$$
p ( y n,f | ̂ d n - 1 obs ) = p ( F n y n - 1 ,a | ̂ d n - 1 obs ) . (4.73)
$$

- 2. Analysis: update the PDF using Bayes’ rule:


$$
p ( y n,a ) ≡ p ( y n,f | ̂ d n obs ) ︸ ︷︷ ︸ post ∝ p ( y n,f | ̂ d n - 1 obs ) ︸ ︷︷ ︸ prior p ( d n obs | y n,f ) ︸ ︷︷ ︸ likelihood . (4.74)
$$

# 4.3 Ensemble Kalman Filter

In the KF, the mean and covariance of the state vector are updated whenever new data become available. However, even for linear problems, updating the covariance matrix using the KF equations can become computationally unfeasible when dealing with high-dimensional state vectors. Additionally, if the problem is nonlinear, the KF cannot be applied directly, in which case the extended Kalman filter (EKF) serves as an alternative. The EKF uses

Evensen [136] introduced the ensemble Kalman filter (EnKF) as an alternative to address the issues encountered with the EKF in high-dimensional nonlinear dynamical systems. The EnKF is a Monte Carlo method in which an ensemble of states is updated over time and used to estimate the mean and covariance. While the EnKF was originally introduced in [136], the method was later refined in [51, 197], by introducing the concept of updating each state vector in the ensemble with independently perturbed observations, leading to the current implementation of the EnKF.

In the EnKF, uncertainty is represented and propagated using an ensemble of states. This contrasts with the KF and the EKF, where uncertainty is propagated through updates to the state covariance matrix. Furthermore, in practical applications of the EnKF, the number of state vectors in the ensemble is typically much smaller than the number of unknowns, making the ensemble update computationally more efficient than updating the state covariance matrix.

Since its introduction, the body of literature on EnKF has expanded significantly. The EnKF has found applications in several areas spanning disciplines such as oceanography [34, 236], atmospheric modeling [464, 200], numerical weather prediction [199, 425], hydrology [360, 82, 264, 418], and petroleum reservoir engineering [3, 331].

Reservoir data assimilation is typically defined as a parameter estimation problem. Therefore, in order to use EnKF in this context is convenient to write the equations in terms of the combined parameter-state vector y . As before, hereafter, we refer to y simply as the state vector.

Assuming that the prior PDF for the state vector at time t n is Gaussian and that the data errors also follow a Gaussian distribution, we can write

$$
p ( y n | ̂ d n - 1 obs ) ∝ exp { - 1 2 ( y n - y n,f ) ⊤ ( C f y n ) - 1 ( y n - y n,f ) } (4.75)
$$

and

$$
L ( y n | d n obs ) ∝ exp { - 1 2 ( d n obs - h ( y n )) ⊤ C - 1 e n ( d n obs - h ( y n )) } , (4.76)
$$

where h ( · ) denotes the nonlinear relationship between state and data, meaning that h ( y n ) is the predicted data vector at t n . Hence, the posterior PDF becomes

$$
p ( y n | ̂ d n obs ) ∝ exp {-O ( y n ) } , (4.77)
$$

$$
O ( y n ) = 1 2 ( y n - y n,f ) ⊤ ( C f y n ) - 1 ( y n - y n,f ) + 1 2 ( d n obs - h ( y n )) ⊤ C - 1 e n ( d n obs - h ( y n )) . (4.78)
$$

However, because the state-data relationship h ( y n ) is nonlinear, an analytical minimum of O ( y n ) cannot be computed.

One way to derive the EnKF analysis equation is by introducing a “trick” to deal with the nonlinearity in O ( y n ) 6 . The trick consists of augmenting the state vector by including the predicted data

$$
̂ y n = [ y n h ( y n ) ] = ⎡ ⎣ m x n h ( y n ) ⎤ ⎦ . (4.79)
$$

Then, we define the observation matrix, H n , as

$$
H n = [ O N m O N x I N n ] , (4.80)
$$

where O N m and O N x are null matrices with dimensions N n × N m and N n × N x , respectively, while I N n is the N n × N n identity matrix. Using the augmented state vector, the predicted data vector can be written as

$$
h ( y n ) = H n ̂ y n . (4.81)
$$

  Now, we assume that the prior PDF for the augmented state vector is Gaussian n n n

$$
p ( ̂ y n | d n obs ) ∝ exp {-O ( ̂ y n ) } , (4.82)
$$

where

$$
O ( ̂ y n ) = 1 2 ( ̂ y n - ̂ y n,f ) ⊤ ( C f ̂ y n ) - 1 ( ̂ y n - ̂ y n,f ) + 1 2 ( d n obs - H n ̂ y n ) ⊤ C - 1 e n ( d n obs - H n ̂ y n ) . (4.83)
$$

Because we wrote the predicted data vector as a linear function of   y n , we can find the posterior mean by setting ∇O (   y n ) = 0 and solving for   y n . This procedure leads to

6 This trick disguises the problem of nonlinearities, but it does not avoid it [256].

$$
̂ y n,a = ̂ y n,f + [ ( C f ̂ y n ) - 1 + H ⊤ n C - 1 e n H n ] - 1 H ⊤ n C - 1 e n ( d n obs - H n ̂ y n,f ) = ̂ y n,f + C f ̂ y n H ⊤ n ( H n C f ̂ y n H ⊤ n + C e n ) - 1 ( d n obs - H n ̂ y n,f ) = ̂ y n,f + K n ( d n obs - H n ̂ y n,f ) . (4.84)
$$

    Note that these expressions are equivalent to the expressions derived for the KF and the MAP estimate. However, here we are interested in sampling the posterior PDF. This can be accomplished using RML, in which case to obtain the j th sample of p (   y n | d n obs ), we replace   y n,f in the expression for O (   y n ) by   y n,f j ∼ N     y n,f , C f   y n   , and d n obs by d n obs ,j ∼ N ( d n obs , C e n ) and minimize the resulting objective function

$$
O r ( ̂ y n ) = 1 2 ( ̂ y n - ̂ y n,f j ) ⊤ ( C f ̂ y n ) - 1 ( ̂ y n - ̂ y n,f j ) + 1 2 ( d n obs ,j - H n ̂ y n ) ⊤ C - 1 e n ( d n obs ,j - H n ̂ y n ) . (4.85)
$$

Minimizing O r (   y n ) for   y n and calling the resulting state vector as   y n,a j leads to

$$
̂ y n,a j = ̂ y n,f j + [ ( C f ̂ y n ) - 1 + H ⊤ n C - 1 e n H n ] - 1 H ⊤ n C - 1 e n ( d n obs ,j - H n ̂ y n,f j ) = ̂ y n,f j + C f ̂ y n H ⊤ n ( H n C f ̂ y n H ⊤ n + C e n ) - 1 ( d n obs ,j - H n ̂ y n,f j ) = ̂ y n,f j + K n ( d n obs ,j - H n ̂ y n,f j ) . (4.86)
$$

Repeating this process for j = 1 , 2 ,...,N e gives an ensemble of N e conditional realizations. Eq. (4.86) forms the basis of the EnKF method.

To derive the final EnKF analysis equation, we need to develop expressions for the covariance matrix C f   y n . First, we note that C f   y n can be partitioned as C f C f C f

$$
C f ̂ y n = ⎡ ⎢ ⎣ C f mm n C f mx n C f md n C f xm n C f xx n C f xd n C f dm n C f dx n C f dd n ⎤ ⎥ ⎦ . (4.87)
$$

However, we only need the products

$$
C f ̂ y n H ⊤ n = ⎡ ⎢ ⎣ C f mm n C f mx n C f md n C f xm n C f xx n C f xd n C f dm n C f dx n C f dd n ⎤ ⎥ ⎦ ⎡ ⎣ O N m O N x I N n ⎤ ⎦ = ⎡ ⎢ ⎣ C f md n C f xd n C f dd n ⎤ ⎥ ⎦ = C f ̂ yd n (4.88)
$$

$$
H n C f ̂ y n H ⊤ n = C f dd n . (4.89)
$$

  Using these last two results in (4.86) gives

$$
̂ y n,a j = ̂ y n,f j + ⎡ ⎢ ⎣ C f md n C f xd n C f dd n ⎤ ⎥ ⎦ ( C f dd n + C e n ) - 1 ( d n obs ,j - H n ̂ y n,f j ) = ̂ y n,f j + C f ̂ yd n ( C f dd n + C e n ) - 1 ( d n obs ,j - H n ̂ y n,f j ) = ̂ y n,f j + K n ( d n obs ,j - h ( y n,f j )) . (4.90)
$$

Under the assumptions we have made, application of Eq. (4.90) for j = 1 , 2 ,...,N e provides a sampling for the posterior PDF p (   y n | d n obs ). Note that the trick of augmenting the state vector was done only to derive the EnKF equation with a form similar to the KF. In terms of computational implementation, however, we do not need to augment the state vector and Eq. (4.90) can be written directly in terms of y n .

# 4.3.1 Perturbed Observations

Eq. (4.90) was derived from RML replacing d n obs by a sample d n obs ,j ∼ N ( d n obs , C e n ), which is equivalent to adding a random vector e n j ∼ N ( 0 , C e n ) to the observations

$$
d n obs ,j = d n obs + e n j = d n obs + C 1/2 e n z n , (4.91)
$$

where z n ∼ N ( 0 , I ). This procedure is known as perturbed observation scheme in the ensemble data assimilation literature and it was independently introduced by Burgers et al. [51] and Houtekamer and Mitchell [197] in the EnKF formulation.

The perturbed observations are necessary to ensure that EnKF results in the correct posterior covariance in the linear case with infinite ensemble size. To show the role of e n j , consider the EnKF equation written as

$$
y n,a j = y n,f j + K n ( d n obs + e n j - H n y n,f j ) . (4.92)
$$

The corresponding equation for updating the ensemble mean is

$$
y n,a = y n,f + K n ( d n obs - H n y n,f ) , (4.93)
$$

where it has been used the fact that e n = 0 . Hence

$$
y n,a j - y n,a = y n,f j - y n,f + K n ( e n j - H n ( y n,f j - y n,f )) = δ y n,f j + K n ( e n j - H n δ y n,f j ) . (4.94)
$$

The expression for the posterior covariance of y n is

$$
C a y n = E [ ( y n,a j - y n,a ) ( y n,a j - y n,a ) ⊤ ] (4.95) = E [ ( δ y n,f j + K n ( e n j - H n δ y n,f j ))( δ y n,f j + K n ( e n j - H n δ y n,f j )) ⊤ ] = E [ δ y n,f j ( δ y n,f j ) ⊤ ] ︸ ︷︷ ︸ C f y n + E [ δ y n,f j ( K n e n j ) ⊤ ] ︸ ︷︷ ︸ = 0 - E [ δ y n,f j ( δ y n,f j ) ⊤ ] ︸ ︷︷ ︸ C f y n H ⊤ n K ⊤ n + E [ K n e n j ( δ y n,f j ) ⊤ ] ︸ ︷︷ ︸ = 0 - K n H n E [ δ y n,f j ( δ y n,f j ) ⊤ ] ︸ ︷︷ ︸ C f y n + K n E [ e n j ( e n j ) ⊤ ] ︸ ︷︷ ︸ C e n K ⊤ n - K n E [ e n j ( H n δ y n,f j ) ⊤ ] ︸ ︷︷ ︸ = 0 K ⊤ n - K n E [ H n δ y n,f j ( e n j ) ⊤ ] ︸ ︷︷ ︸ = 0 K ⊤ n + K n H n E [ δ y n,f j ( δ y n,f j ) ⊤ ] ︸ ︷︷ ︸ C f y n H ⊤ n K ⊤ n
$$

$$
= C f y n - C f y n H ⊤ n K ⊤ n - K n H n C f y n + K n C e n K ⊤ n + K n H n C f y n H ⊤ n K ⊤ n .
$$

Therefore, if we neglect the perturbation vector e n j in the EnKF analysis, the term n n  

$$
K n E [ e n j ( e n j ) ⊤ ] K ⊤ n = K n C e n K ⊤ n (4.96)
$$

present in the expression for C a y n disappears. Note that K n C e n K   n is at least positive semidefinite. Therefore, the resulting expression for C a y n has a positive semidefinite term missing. As a result, if we neglect e n j the entries in the matrix C a y n are underestimated. The traditional interpretation of perturbed observations treats the ob-

servations as random variables. The same concept is employed in RML. However, some authors argue that the correct interpretation involves perturbing the predicted data vector. The rationale behind this perspective is based on the assumption that the true system is a sample from the same distribution as the ensemble members. Since the measurements of the true system are already perturbed by observation errors, it follows that the predictions of each ensemble member should be perturbed in a similar manner [447]. Nevertheless, here, the equations are presented in terms of perturbed observations because this approach is more conventional in the data assimilation literature. It is worth noting that in practice, the actual calculations remain unchanged, whether one considers e n j as a perturbation added to the observations or to the predicted data. However, these two interpretations may yield different results when attempting to extend the methods to account for non-additive errors.

# 4.3.2 Ensemble-Based Covariance

The last step to obtain the final EnKF method is to introduce the ensemblebased approximations of the covariances C f md n , C f xd n and C f dd n as

$$
C f md n ≈ ˜ C f md n = 1 N e - 1 N e ∑ j =1 ( m n,f j - m n,f )( h ( y n,f j ) - h ( y n,f ) ) ⊤ = ∆ M n,f ( ∆ D n,f ) ⊤ , (4.97)
$$

and

$$
C f xd n ≈ ˜ C f xd n = 1 N e - 1 N e ∑ j =1 ( x n,f j - x n,f )( h ( y n,f j ) - h ( y n,f ) ) ⊤ = ∆ X n,f ( ∆ D n,f ) ⊤ , (4.98)
$$

$$
C f dd n ≈ ˜ C f dd n = 1 N e - 1 N e ∑ j =1 ( h ( y n,f j ) - h ( y n,f ) )( h ( y n,f j ) - h ( y n,f ) ) ⊤ = ∆ D n,f ( ∆ D n,f ) ⊤ . (4.99)
$$

The tildes over the covariance matrices were introduced to denote that these matrices are estimated from ensembles. ∆ M n,f , ∆ X n,f and ∆ D n,f in Eqs. 4.97, 4.98 and 4.99 are defined as

$$
∆ M n,f = 1 √ N e - 1 ( M n,f - M n,f ) = 1 √ N e - 1 [ m n,f 1 - m n,f , . . . , m n,f N e - m n,f ] , (4.100)
$$

$$
∆ X n,f = 1 √ N e - 1 ( X n,f - X n,f ) = 1 √ N e - 1 [ x n,f 1 - x n,f , . . . , x n,f N e - x n,f ] , (4.101)
$$

$$
∆ D n,f = 1 √ N e - 1 ( D n,f - D n,f ) (4.102) = 1 √ N e - 1 [ h ( y n,f 1 ) - h ( y n,f ) , . . . , h ( y n,f N e ) - h ( y n,f ) ] ,
$$

where

$$
m n,f = 1 N e N e ∑ j =1 m n,f j , (4.103)
$$

$$
x n,f = 1 N e N e ∑ j =1 x n,f j , (4.104)
$$

and

$$
h ( y n,f ) = 1 N e N e ∑ j =1 h ( y n,f j ) . (4.105)
$$

M n,f , X n,f , and D n,f are matrices with all columns equal to the corresponding ensemble means. A more compact notation can be written defining a centering matrix as

$$
A = 1 √ N e - 1 ( I - 1 N e 11 ⊤ ) , (4.106)
$$

where I is the N e × N e identity matrix and 1 = [1 1 ... 1]   is the N e dimensional vector with all entries equal to one. Using the centering matrix, we can write n,f n,f

$$
∆ M n,f = M n,f A , (4.107)
$$

$$
∆ X n,f = X n,f A , (4.108)
$$

and

$$
∆ D n,f = D n,f A . (4.109)
$$

The final EnKF analysis equation can be written as

$$
y n,a j = y n,f j + ˜ C f yd n ( ˜ C f dd n + C e n ) - 1 ( d n obs ,j - h ( y n,f j )) (4.110)
$$

for j = 1 , 2 ,...,N e , where

and

$$
˜ C f yd n = 1 N e - 1 N e ∑ j =1 ( y n,f j - y n,f ) ( h ( y n,f j ) - h ( y n,f ) ) ⊤ = ∆ Y n,f ( ∆ D n,f ) ⊤ (4.111)
$$

$$
∆ Y n,f = 1 √ N e - 1 ( Y n,f - Y n,f ) = 1 √ N e - 1 [ y n,f 1 - y n,f , . . . , y n,f N e - y n,f ] = Y n,f A . (4.112)
$$

Eq. (4.110) represents the final EnKF analysis equation. It shares a similar form with the original KF equation. However, unlike the KF, we do not directly update the covariance matrix of the state vector. Instead, we update the ensemble of state vectors, which serves as samples from the prior (forecast) distribution, to obtain samples of the posterior (analyzed) distribution.

# 4.3.2.1 Example: Porosity Distribution in a Core Sample

Consider the same problem introduced in Section 2.3.1.4. We have already computed the MAP estimate (Fig. 2.2), RML samples (Fig. 2.8) and the KF solution (Fig. 4.3) for this problem. Fig. 4.5 presents the results for this problem assimilating the 10 data points sequentially using EnKF with an ensemble of 100 members. The final ensemble from EnKF is very similar to the posterior samples obtained with RML. In fact, for linear-Gaussian

![](<ensemble_data_assimilation_e-book_version_images/imageFile48.png>)

















































 

  

  

�





��



��

�





��



��

�





��





  U GE RF 

  U GE RF 

  U GE RF 

(a)

Prior

(b)

1st datum

(c)

2nd datum

















































 

  

 

�





��



��

�





��





�





��





  U GE RF 

  U GE RF 

  U GE RF 

(d)

3rd datum

(e)

4th datum

(f)

5th datum

















































 

 

 

�





��





�





��





�





��





  U GE RF 

  U GE RF 

  U GE RF 

(g)

6th datum

(h)

7th datum

(i)

8th datum

































 

 

�





��





�





��





  U GE RF 

  U GE RF 

(j)

9th datum

(k)

10th datum

Fig. 4.5: EnKF results with N e = 100 for porosity in a core sample. The solid red line represents the ground truth. The red circles represent the observed data points. The gray lines represent samples obtained by EnKF for different numbers of observations. The dashed lines represent the ensemble mean. Example 4.3.2.1.

# 4.3.3 Parameters-State Consistency

In practice, the rationale for updating primary variables, which represent the state of the dynamical system, is to circumvent the need to initiate reservoir simulations from time zero (initial reservoir conditions) after each data assimilation time step. This approach operates under the assumption that the updated primary variables are statistically consistent with those that would be obtained by running the reservoir simulator using the updated set of model parameters from time zero. However, this consistency can only be rigorously established for linear-Gaussian problems [435].

However, the equations governing reservoir simulation are typically characterized by moderate to high nonlinearity. Consequently, the assumption of consistency may be significantly violated, potentially undermining the performance of data assimilation and giving rise to convergence challenges in the simulations. In practical terms, following data assimilation at time t n , reservoir simulations may be restarted with incorrect pressure and saturation values, thus compromising the historical material balance of the field. In extreme cases, the analysis step within the EnKF may yield non-physical values for these variables, such as negative pressures or saturations exceeding one.

Fig. 4.6 illustrates this problem by showing the water saturation profiles at 360 days for the linear two-phase flow discussed in Section 2.4.5.3. This figure includes the updated saturation profiles obtained after applying the EnKF analysis. Although the mean updated water saturation is very close to the true saturation, the updated individual realizations exhibit non-physical values.

![](<ensemble_data_assimilation_e-book_version_images/imageFile49.png>)

0.8

0.6

Water saturation

0.4

0.2

0

1

6

11

16

21

26

31

Gridblock

NTERNA Fig. 4.6: Water saturation profile at 360 days. The gray lines represent the ensemble of saturation profiles updated with EnKF analysis equation. The dashed line represents the ensemble mean and red line represents the ground truth. Reproduced from Emerick and Reynolds [131] with permission from Springer Nature.

To address the parameter-state consistency problem, one straightforward approach is to perform simulations from time zero at each data assimilation

# 4.3.4 Coupling EnKF with a Reservoir Simulator

Before we present the EnKF pseudo-code, it might be helpful to examine the components of the state vector from the perspective of reservoir simulation. Reservoir data assimilation is typically framed as a parameter-estimation problem, where the objective is to estimate model parameters based on a set of observations. The vector of model parameters generally comprises “static” rock properties, such as porosity, permeabilities, rock compressibility, and more. However, here the EnKF was introduced as a parameter-state estimation problem. In this scenario, the state encompasses dynamic variables like pressure and phase saturations. In a reservoir model, the state corresponds to the primary variables that are solved for in the fluid transport problem. Hence, the specific variables included in the state vector depend on the formulation of the particular problem at hand. For example, in a standard black-oil formulation for a petroleum reservoir, the state comprises pressure, water and gas saturations, and the gas-oil solubility ratio. In a compositional fluid model, the state may involve the molar fraction of each pseudo-component.

Recall that the parameter-state vector takes the following form:

$$
y n = [ m x n ] , (4.113)
$$

where m represents the vector of model parameters, and x n represents the vector of state variables at time t n . In the case of a standard black-oil simulator, the parameter-state vector is composed of

$$
y n = ⎡ ⎢ ⎣ model parameters ( m ) ︷ ︸︸ ︷ φ ⊤ , (ln κ ) ⊤ , . . . , ( p n r ) ⊤ , ( s n w ) ⊤ , ( s n g ) ⊤ , ( r n s ) ⊤ ︸ ︷︷ ︸ primary variables ( x n ) ⎤ ⎥ ⎦ ⊤ . (4.114)
$$

Here, φ and ln κ are vectors containing the porosity and log-permeability values for each gridblock in the model, while p n r , s n w , s n g , and r n s are vectors containing the pressure, water saturation, gas saturation, and gas-oil solubility ratio, respectively.

Pseudo-code 4.3 summarizes the EnKF process for reservoir data assimilation. Note that to apply the EnKF analysis at time step, t n , we need the

# Pseudo-code 4.3: Ensemble Kalman Filter

- 1. Initialization: generate the initial ensemble,   y 0 ,a j   N e j =1 , by sampling the prior distributions of parameters, m , and states, x .
- 2. For n = 1 to N t :


• Forecast step: generate N e unconditional (forecast) samples of y n and the corresponding predicted data, d n , by running the forward model from time t n − 1 to t n for j = 1 , 2 ,...,N e :

$$
y n,f j = [ m f j x n,f j ] = [ m f j f ( m f j , x n - 1 ,a j ) ] (4.115)
$$

and

$$
d n,f j = h ( m f j , x n - 1 ,a j ) , (4.116)
$$

where f ( · ) and h ( · ) denote the nonlinear forward and observation models, respectively.

• Perturb the vector of observations:

$$
d n obs ,j = d n obs + C 1/2 e n z n j , for j = 1 , 2 , . . . , N e , (4.117)
$$

where z n j ∼ N ( 0 , I ). Analysis step: update

• the combined parameter-state vector using the EnKF analysis equation:

$$
y n,a j = y n,f j + ˜ C f yd n ( ˜ C f dd n + C e n ) - 1 ( d n obs ,j - d n,f j ) , (4.118)
$$

for j = 1 , 2 ,...,N e .

# 4.3.4.1 Example: Two-Phase Flow in 2D Model

Consider the same synthetic data assimilation problem presented in Section 2.4.5.4. Previously, we presented the MAP estimate and posterior realizations obtained using an adjoint-based implementation of RML. Now, we present data assimilation results using the EnKF with an ensemble of 100 realizations. During data assimilation, we applied a distance-based localization scheme to regularize the EnKF [197] 7 .

Fig. 4.7 illustrates the gradual changes in the log-permeability for the first realization of the ensemble imposed by sequential data assimilation. Fig. 4.8 shows the first three prior and posterior realizations of the ensemble, along with the true log-permeability. The EnKF data assimilation recovered some of the main permeability features observed in the ground truth, such as the high-permeability corridor in the upper part of the model and the low-permeability region in the lower part. Fig. 4.9 presents the predicted water production rate for three wells in the model. The posterior predictions were obtained by running reservoir simulations from time zero with the final ensemble of log-permeability. The results in this figure demonstrate significant improvement in data matching, and the forecast encompasses the predicted data using the true log-permeability.

![](<ensemble_data_assimilation_e-book_version_images/imageFile50.png>)

7.00

7.00

7.00

7.00

7.00

6.56

6.56

6.56

6.56

6.56

6.11

6.11

6.11

6.11

6.11

5.67

5.67

5.67

5.67

5.67

5.22

5.22

5.22

5.22

5.22

4.78

4.78

4.78

4.78

4.78

4.33

4.33

4.33

4.33

4.33

3.89

3.89

3.89

3.89

3.89

3.44

3.44

3.44

3.44

3.44

3.00

3.00

3.00

3.00

3.00

(a) ( = 0

Prior days)

(b) = 600

Post days)

(c) = 1,350

Post

(d) = 2,850

Post

(e) = 3,900

Post

t

( t

600 days)

( t

days)

( t

days)

( t

days)

=

=

=

=

t

t

t

t

3.00

3.44

3.89

4.33

4.78

5.22

5.67

6.11

6.56

7.00

Fig. 4.7: Evolution of the first realization of log-permeability during the sequential data assimilation with EnKF for a 2D model under two-phase flow. Black circles represent the positions of producers, while black triangles denote the positions of water injection wells. Example 4.3.4.1.

7 Localization is a standard strategy to address issues arising from using a limited ensemble size to estimate covariances in the EnKF. This topic is discussed in detail in Chapter 7.

![](<ensemble_data_assimilation_e-book_version_images/imageFile51.png>)

7.00

7.00

7.00

7.00

6.56

6.56

6.56

6.56

6.11

6.11

6.11

6.11

5.67

5.67

5.67

5.67

5.22

5.22

5.22

5.22

4.78

4.78

4.78

4.78

4.33

4.33

4.33

4.33

3.89

3.89

3.89

3.89

3.44

3.44

3.44

3.44

3.00

3.00

3.00

3.00

(a)

True

(b)

Prior 1

(c)

Prior 2

(d)

Prior 3

7.00

7.00

7.00

6.56

6.56

6.56

6.11

6.11

6.11

5.67

5.67

5.67

5.22

5.22

5.22

4.78

4.78

4.78

4.33

4.33

4.33

3.89

3.89

3.89

3.44

3.44

3.44

3.00

3.00

3.00

(e)

EnKF 1

(f)

EnKF 2

(g)

EnKF 3

3.00

3.44

3.89

4.33

4.78

5.22

5.67

6.11

6.56

7.00

Fig. 4.8: True log-permeability, three prior realizations, and three posterior realizations obtained using EnKF for a 2D model under two-phase flow. Black circles indicate the positions of producers, and black triangles indicate the positions of water injection wells. Example 4.3.4.1.

# 4.3.5 Filter Divergence

Filter divergence occurs when the EnKF estimates deviate significantly from the true state, as illustrated in Fig. 4.10. Once filter divergence takes hold, it becomes an irreversible situation, and the EnKF is no longer capable of correcting the estimates to converge with the true state. This divergence phenomenon typically arises due to a gradual underestimation of the state covariance, leading to a scenario where     C f dd n       C e n   [60], causing the filter to begin missing observations. Several factors contribute to filter di-





![](<ensemble_data_assimilation_e-book_version_images/imageFile52.png>)



���

       DWHUUDWH EE GD  

      DWHUUDWH EE GD  

          DWHUUDWH EE GD  

���

���

���

���

���

��

���

���

��

��

���

��

��

���

��

��

 

 

 

�







����

����



 

 

�







����

����



 

 

�







����

����



 

 

  7 PH GD V 

  7 PH GD V 

  7 PH GD V 

(a)

Well 1

(b)

Well 2

(c)

Well 3

Fig. 4.9: Water production rate in bbl/day for three wells. Red circles are the observations, red line the prediction with the true log-permeability distribution. The gray and blue lines show the predictions from 100 prior and posterior realizations, respectively. The posterior predictions were obtained running the final EnKF realizations from time zero. Example 4.3.4.1.

![](<ensemble_data_assimilation_e-book_version_images/imageFile23.png>)

Fig. 4.10: Illustration of filter divergence.

# 4.3.6 Ensemble Square Root Filters

The KF update equation for the state covariance matrix can be written as

$$
C a y n = ( I - K n H n ) C f y n . (4.119)
$$

According to Whitaker and Hamill [463], because the EnKF employs an updating scheme based on perturbed observations, this equation is satisfied in a statistical sense only. In other words, EnKF satisfies Eq. (4.119) only in the limit of an infinite ensemble size. This limitation can lead to suboptimal filter performance when dealing with small ensembles. To address this issue, several implementations of the analysis equation have been developed, which are based on deterministic updates of the ensemble to ensure the exact satisfaction of Eq. (4.119). These implementations are commonly referred to as ensemble square root filters (EnSRF).

A typical EnSRF follows two main steps depicted in Pseudo-code 4.4.

# Pseudo-code 4.4: EnSRF

- 1. Update the mean:

$$
y n,a = y n,f + ˜ K n ( d n obs - h ( y n,f ) ) . (4.120)
$$

- 2. Update the ensemble deviations:


$$
∆ Y n,a = ∆ Y n,f T n R , (4.121)
$$

where T n R is called (right-)square root transform matrix.

The matrix T n R is selected such that

$$
˜ C a y n = ∆ Y n,a (∆ Y n,a ) ⊤ = ( ∆ Y n,f T n R ) ( ∆ Y n,f T n R ) ⊤ = ( I - ˜ K n H n ) ˜ C f y n . (4.122)
$$

Hence, square root filters are designed to ensure the exact satisfaction of the theoretical covariance update equation. However, this condition does not uniquely define T n R . Consequently, several different variants have been proposed in the literature. The procedure described in Pseudo-code 4.4 is often referred to as the right-multiplied EnSRF, as T n R multiplies ∆ Y n,f from the right. There are also a few left-multiplied schemes where the update equation takes the form

$$
∆ Y n,a = T n L ∆ Y n,f . (4.123)
$$

Since EnSRF are defined imposing the condition (4.119), they tend to reduce the underestimation of the ensemble variance typically observed in EnKF. There is a vast body of literature on square root ensemble filters in the fields of oceanography and numerical weather prediction; e.g., see [439,

373] and the references therein. Nevertheless, these methods have seldom been employed in the context of reservoir data assimilation applications. One issue with square root filters is that, while they ensure the correct covariance for linear problems, they can sometimes produce highly skewed ensembles in nonlinear cases. Lawson and Hansen [251] demonstrated with one-dimensional nonlinear problems that the EnSRF ensemble may collapse to a single state with a few distant outliers providing the expected variance.

![](<ensemble_data_assimilation_e-book_version_images/imageFile54.png>)

# Ensemble Smoother with Multiple Data Assimilation

Abstract: This chapter reviews the methods ensemble smoother (ES) and the ensemble smoother with multiple data assimilation (ES-MDA). Particular emphasis is placed on alternative derivations and implementations of ESMDA, with examples applied to reservoir problems.

# 5.1 Introduction

The sequential data assimilation scheme of the EnKF is highly appealing for atmospheric science; however, it presents certain challenges when applied to reservoir data assimilation. First, the frequent simulation restarts significantly increase the computational cost of the data assimilation and are particularly challenging when simulations are distributed across a cluster of computers. Additionally, there can be inconsistencies between updated model parameters and updated states, which can introduce convergence problems in the reservoir simulations. Finally, sequential data assimilation is impractical for integrated workflows involving updates in different components of a geomodeling process (e.g., seismic, structural, geological modeling, upscaling, and flow simulation).

One alternative to the EnKF is the ensemble smoother (ES) [448, 400]. In ES, all data are assimilated simultaneously in a single update, eliminating the need for simulation restarts. However, the single update scheme of ES has proven insufficient for properly conditioning reservoir models to dynamic data [78, 132, 133]. This limitation has driven the development of iterative forms of ES [78, 79, 132, 413, 279, 354].

This chapter presents the ensemble smoother with multiple data assimilation (ES-MDA), introduced by Emerick and Reynolds [132] as an iterative form of ES 1 . Other iterative ES methods are discussed in Chapter 6.

# 5.2 Ensemble Smoother

ES was introduced by van Leeuwen and Evensen [448], with its first application in reservoir models presented by Skjervheim et al. [400]. The primary difference between the EnKF and ES is that ES does not assimilate data sequentially over time. Instead, ES computes a global update using all available data simultaneously. This approach eliminates the need to restart reservoir simulations at each data assimilation time step. Additionally, ES addresses the parameter-state consistency problem discussed in Section 4.3.3, as it only requires the estimation of model parameters in reservoir applications.

The ES analysis equation to update a vector of model parameters, m , can be written as

$$
m c ,j = m j + ˜ C md ( ˜ C dd + C e ) - 1 ( d obs ,j - g ( m j )) , (5.1)
$$

for j = 1 , 2 ,...,N e . m c ,j is the j th posterior realization,   C md is the matrix containing the covariance values between model parameters and predicted data, while   C dd is the covariance matrix of predicted data. Both matrices are estimated based on the prior ensemble. d obs ,j is the j th realization of the perturbed data vector and g ( m j ) is the predicted data with the j th prior realization, m j . Eq. (5.1) is essentially the same analysis equation of EnKF. The primary

difference lies in the update scheme (Fig. 5.1). While ES performs a single linear update, EnKF executes a sequence of smaller updates, enabling it to handle nonlinear dynamics more effectively. As a result, ES typically produces significantly inferior data matches compared to those obtained with EnKF when applied to reservoir data assimilation problems [78, 132, 133].

The superior performance of EnKF compared to ES in terms of data match quality can be explained by interpreting EnKF from a Gauss-Newton (GN) perspective [364]. Recall that the RML objective function can be written as:

1 In a standard ES-MDA implementation, the update equation is applied a predefined number of times without convergence checking for termination. This has led some researchers to argue that ES-MDA should not be classified as an iterative method [288]. Nonetheless, we still refer to ES-MDA as an iterative form of ES for didactic purposes.

Ensemble Smoother with Multiple Data Assimilation

Updates

History

Forecast

Updates

History

Forecast

![](<ensemble_data_assimilation_e-book_version_images/imageFile24.png>)

(a)

EnKF

Time

(b)

ES

Fig. 5.1: Update schemes of EnKF and ES.

Time

$$
O r ( m ) = 1 2 ( m - m j ) ⊤ C - 1 m ( m - m j ) + 1 2 ( d obs ,j - g ( m )) ⊤ C - 1 e ( d obs ,j - g ( m )) . (5.2)
$$

In GN, we look for a minimizer of (5.2) with an iterative process where the vector of model parameters at   th iteration is updated using

$$
m ℓ +1 j = m ℓ j + β ℓ δ m ℓ +1 j , (5.3)
$$

where β   is a step size in the direction δ m   +1 j given by

$$
δ m ℓ +1 j = m j - m ℓ j + C m G ⊤ ℓ ( G ℓ C m G ⊤ ℓ + C e ) - 1 × ( d obs ,j - g ( m ℓ j ) + G ℓ ( m ℓ j - m j )) . (5.4)
$$

Consider the first iteration of GN with a full step, β 0 = 1, and an initial guess m 0 j = m j , where m j ∼ N ( m pr , C m ). Replacing the products C m G   0 and G 0 C m G   0 by the ensemble approximations

and

results in

$$
C m G ⊤ 0 ≈ ˜ C md (5.5)
$$

$$
G 0 C m G ⊤ 0 ≈ ˜ C dd (5.6)
$$

$$
m 1 j = m j + ˜ C md ( ˜ C dd + C e ) - 1 ( d obs ,j - g ( m j )) . (5.7)
$$

scenario, each data assimilation time step corresponds to one GN iteration. Still, due to consecutive production data, multiple GN updates occur. However, in the case of ES, all data points are assimilated in a single update, which may be insufficient to condition all realizations to the observations. Moreover, this process is prone to introduce overcorrection in the parameter values.

Pseudo-code 5.1 summarizes the ES method.

# Pseudo-code 5.1: Ensemble Smoother

- 1. Initialization: generate the initial ensemble, { m j } N e j =1 , by sampling the prior distribution of the model parameters.
- 2. Forecast step: run the forward model from time zero until the end of the historical period to compute the vector of predicted data

$$
d j = g ( m j ) , for j = 1 , 2 , . . . , N e . (5.8)
$$

- 3. Perturb the vector of observations:


$$
d obs ,j = d obs + C 1/2 e z j , for j = 1 , 2 , . . . N e , (5.9)
$$

where z j ∼ N ( 0 , I ). Analysis step: update

4. the vectors of model parameters using the ES analysis equation:

$$
m c ,j = m j + ˜ C md ( ˜ C dd + C e ) - 1 ( d obs ,j - d j ) (5.10)
$$

for j = 1 , 2 ,...,N e .

# 5.3 Ensemble Smoother with Multiple Data Assimilation

As mentioned in the introduction of this chapter, the global update scheme is an attractive feature of ES for reservoir data assimilation problems. Unfortunately, ES often fails to deliver acceptable data matches. This shortcoming has led to the proposal of various iterative forms of ES in the literature [78, 132, 79, 413, 279, 354, 140]. Among these methods, ES-MDA stands out due to the simplicity of its formulation and good performance.

$$
C m c = C m - C m G ⊤ ( GC m G ⊤ + C e ) - 1 GC m = C m - ∆ C m . (5.11)
$$

The matrix ∆ C m in Eq. (5.11) is at least positive semidefinite. Therefore, if we assimilate the same data multiple times without modifying C e , we subtract ∆ C m from C m multiple times. As a result, we obtain the wrong posterior covariance, and, more importantly, we underestimate the uncertainty in the model parameters.

In fact, MDA was initially introduced in the context of EnKF to assimilate infrequent data, such as production logging and 4D seismic, as outlined in [129]. The inspiration for this approach was drawn from the ideas presented by Rommelse [369]. The integration of MDA with ES was later proposed in [132], which also introduced the general condition for the equivalence of single and multiple data assimilation in the context of linear-Gaussian problems.

# 5.3.1 MDA for the Linear Case

Emerick and Reynolds [132] derived the general condition to make ES-MDA equivalent to ES for linear-Gaussian problems because ES provides a correct sampling in this case when N e → ∞ . This condition is described in Proposition 5.1.

# Proposition 5.1: MDA in the Linear Case

For the linear-Gaussian case, assimilating the same data multiple times with an inflated covariance matrix of the data errors is equivalent to assimilating data only once with the original data-error covariance matrix as long as the inflation factors satisfy the following condition:

$$
N a ∑ ℓ =1 1 α ℓ = 1 ( e.g., α ℓ = N a for ℓ = 1 , 2 , . . . , N a ) . (5.12)
$$

To demonstrate Proposition 5.1, we leverage the equivalence between simultaneous and sequential data assimilation. By replicating the entries of the vector d obs and matrices G and C e N a times, we form the following augmented versions

$$
̂ d obs ≡ ⎡ ⎢ ⎣ d obs . . . d obs ⎤ ⎥ ⎦ , (5.13)
$$

$$
̂ G ≡ ⎡ ⎢ ⎣ G . . . G ⎤ ⎥ ⎦ , (5.14)
$$

and

$$
̂ C e ≡ ⎡ ⎢ ⎢ ⎢ ⎣ α 1 C e O · · · O O α 2 C e · · · O . . . . . . . . . O · · · α N a C e ⎤ ⎥ ⎥ ⎥ ⎦ , (5.15)
$$

where O is the null matrix.

Using   G , we can write the augmented predicted data vector d as

$$
̂ d j = ̂ Gm j , (5.16)
$$

where m j ∼ N ( m pr , C m ), i.e., m j is a sample from the prior Gaussian PDF. Now, we formulate the RML objective function for the MDA case as

$$
̂ O r ( m ) = 1 2 ( m - m j ) ⊤ C - 1 m ( m - m j ) + 1 2 ( ̂ d obs ,j - ̂ Gm ) ⊤ ̂ C - 1 e ( ̂ d obs ,j - ̂ Gm ) . (5.17)
$$

Requiring the gradient of   O r ( m ) to vanish, solving for m , and denoting the result as m leads to

 

$$
̂ m = ̂ C m c [ C - 1 m ( m pr + C 1/2 m z m ) + ̂ G ⊤ ̂ C - 1 e ( ̂ d obs + ̂ C 1/2 e ̂ z d )] , (5.18)
$$

where z m ∼ N ( 0 , I ) and   z d ∼ N ( 0 , I ). To establish that m is a sample from

  the correct posterior PDF, i.e.,   m ∼ N ( m map , C m c ), it suffices to demonstrate the equivalence for the posterior mean and covariance, i.e., E [   m ] = m map and C [   m ] = C m c . The equivalence for the posterior covariance follows from

$$
C [ ̂ m ] = { C - 1 m + ̂ G ⊤ ̂ C - 1 e ̂ G } - 1 = ⎧ ⎪ ⎨ ⎪ ⎩ C - 1 m + [ G ⊤ · · · G ⊤ ] ⎡ ⎢ ⎣ 1 α 1 C - 1 e · · · O . . . . . . . . . O · · · 1 α Na C - 1 e ⎤ ⎥ ⎦ ⎡ ⎢ ⎣ G . . . G ⎤ ⎥ ⎦ ⎫ ⎪ ⎬ ⎪ ⎭ - 1 = { C - 1 m + ( N a ∑ ℓ =1 1 α ℓ ) G ⊤ C - 1 e G } - 1 , (5.19)
$$

which is equivalent to C m c if   N a   =1 α − 1   = 1. The equivalence for the posterior mean

follows:

$$
E [ ̂ m ] = C m c { C - 1 m ( m pr + C 1/2 m E [ z m ] ) + ̂ G ⊤ ̂ C - 1 e ( ̂ d obs + ̂ C 1/2 e E [ ̂ z d ] )} = C m c { C - 1 m m pr + ̂ G ⊤ ̂ C - 1 e ̂ d obs } = C m c ⎧ ⎪ ⎨ ⎪ ⎩ C - 1 m m pr + [ G ⊤ · · · G ⊤ ] ⎡ ⎢ ⎣ 1 α 1 C - 1 e · · · O . . . . . . . . . O · · · 1 α Na C - 1 e ⎤ ⎥ ⎦ ⎡ ⎢ ⎣ d obs . . . d obs ⎤ ⎥ ⎦ ⎫ ⎪ ⎬ ⎪ ⎭ = C m c ⎧ ⎪ ⎨ ⎪ ⎩ C - 1 m m pr + [ G ⊤ · · · G ⊤ ] ⎡ ⎢ ⎣ 1 α 1 C - 1 e d obs . . . 1 α Na C - 1 e d obs ⎤ ⎥ ⎦ ⎫ ⎪ ⎬ ⎪ ⎭ = C m c { C - 1 m m pr + ( N a ∑ ℓ =1 1 α ℓ ) G ⊤ C - 1 e d obs } = C m c { C - 1 m m pr + G ⊤ C - 1 e d obs } = m map . (5.20)
$$

The results (5.19) and (5.20) complete the proof of the equivalence for the linear case.

The condition expressed in Proposition 5.1 establishes the equivalence between ES and ES-MDA for linear-Gaussian problems. However, this equivalence does not extend to nonlinear problems. In the context of nonlinear problems, Emerick and Reynolds [132] utilized this condition to regulate the updates applied to the model. The concept involved replacing a single, potentially substantial correction to the model with N a smaller corrections, as illustrated in Fig. 5.2. In the intervals between these corrections, the forward model is evaluated for all ensemble members to update the covariance matrices,   C   md and   C   dd , used in the analysis. The ES-MDA implementation is quite simple requiring very little mod-

ification in an ES code. Pseudo-code 5.2 describes the main elements of a standard implementation of ES-MDA.

Ensemble Smoother with Multiple Data Assimilation

Updates

History

Forecast

![](<ensemble_data_assimilation_e-book_version_images/imageFile25.png>)

Time

Fig. 5.2: ES-MDA update scheme.

# Pseudo-code 5.2: ES-MDA

1. Initialization: generate the initial ensemble,   m 0 j   N e j =1 , by sampling the prior distribution of parameters. Choose the number of MDA iterations, N a , and the coefficients { α   } N a   =1 . Set   = 0. 2. Forecast step: run the forward model from time zero until the end

of the historical period to compute the vector of predicted data

$$
d ℓ j = g ( m ℓ j ) , for j = 1 , 2 , . . . , N e , (5.21)
$$

3. Perturb the vector of observations:

$$
d ℓ obs ,j = d obs + √ α ℓ +1 C 1/2 e z ℓ j , for j = 1 , 2 , . . . , N e (5.22)
$$

where z   j ∼ N ( 0 , I ). Analysis step: update

4. the vector of model parameters using

$$
m ℓ +1 j = m ℓ j + ˜ C ℓ md ( ˜ C ℓ dd + α ℓ +1 C e ) - 1 ( d ℓ obs ,j - d ℓ j ) , (5.23)
$$

for j = 1 , 2 ,...,N e . Set = + 1.

- 5.    
- 6. If   = N a then set m c ,j = m   j for j = 1 ,...,N e and stop, else return to step 2.


In ES-MDA, the observed data vector is perturbed using the inflated covariance, meaning that we sample d   obs ,j ∼ N ( d obs ,α   +1 C e ). This arises from the derivation, where we expressed   d   obs ,j =   d obs +   C 1/2 e   z d . This aspect distinguishes ES-MDA from other iterative forms of ES found in the literature. In Pseudo-code 5.2, we resample d   obs ,j at each data assimilation step. The rationale for resampling is rooted in our assumption that   z d is a random vector, which would be violated if we use the same perturbations for

# 5.3.2 MDA from Bayes' Rule

We derived the condition for the equivalence between single and multiple data assimilation for the linear-Gaussian case using linear algebra. Interestingly, this condition is more general and can also be directly obtained from Bayes’ rule. First, we write the posterior PDF as

$$
p ( m | d obs ) = ap ( d obs | m ) p ( m ) = a L ( m ) p ( m ) (5.24)
$$

where a is a normalizing constant and the likelihood is given by

$$
L ( m ) = c exp( -O d ( m )) (5.25)
$$

with c as a normalizing constant and

$$
O d ( m ) = 1 2 ( d obs - g ( m )) ⊤ C - 1 e ( d obs - g ( m )) . (5.26)
$$

Now, we can write a factorization of the likelihood as a product of N a terms as N a

$$
L ( m ) = N a ∏ ℓ =1 L ℓ ( m ) (5.27)
$$

where

$$
L ℓ ( m ) = c ℓ exp ( -O ℓ d ( m ) ) (5.28)
$$

with

$$
O ℓ d ( m ) = 1 2 ( d obs - g ( m )) ⊤ ( α ℓ C e ) - 1 ( d obs - g ( m )) . (5.29)
$$

It follows that

$$
L ( m ) = N a ∏ ℓ =1 c ℓ exp ( -O ℓ d ( m ) ) = N a ∏ ℓ =1 c ℓ exp ( - 1 α ℓ O d ( m ) ) = c exp [ - ( N a ∑ ℓ =1 1 α ℓ ) O d ( m ) ] . (5.30)
$$

The equality in Eq. (5.30) holds if

$$
N a ∑ ℓ =1 1 α ℓ = 1 , (5.31)
$$

which is the same condition presented in Proposition 5.1 for the linear case. However, no assumptions about the prior or the linearity of data are necessary in this case. This condition arises to ensure that Bayes’ rule holds after the factorization of the likelihood. It is important to note, however, that the resulting ES-MDA method still relies on the assumptions of gaussianity and linearity to derive the updating equation based on ES. This derivation also shows that ES-MDA is closely related to annealed importance sampling [315, 316, 414], where the objective is to move to a target distribution via a sequence of tempered transitions.

# Remark 5.1: Annealed Importance Sampling

Annealed importance sampling [316] is a Monte Carlo method designed to efficiently sample complex distributions by generating a sequence of intermediate distributions that transition gradually from an initial to the target distribution. The initial distribution, p 0 ( m ), is typically chosen to be easy to sample from, while the intermediate distributions, p   ( m ) = p 0 ( m ) β   , are defined by an annealing parameter β   ∈ [0 , 1], often interpreted as a temperature factor, drawing an analogy to thermodynamics. As the annealing process progresses, the intermediate distributions are adjusted using importance sampling and sampled through MCMC methods. The goal is to achieve faster convergence than standard MCMC, particularly when the target distribution has isolated modes, making it difficult to sample directly.

# 5.3.2.1 Example: Porosity of a Rock Sample

Consider the same example of estimating the porosity of a core sample from a sandstone reservoir described in Section 2.3.1.1. Here, the objective is to compute the posterior variance, σ 2 φ c , considering:

- (a) A single data assimilation.
- (b) Assimilating the same observation twice (without the MDA inflation).
- (c) Assimilating the same observation twice (with the MDA inflation).


(a) Single data assimilation: recall the expression derived in Section 2.3.1 for C m c (Eq. (2.46)):

Therefore

or

$$
C m c = ( G ⊤ C - 1 e G + C - 1 m ) - 1 .
$$

$$
1 σ 2 φ c = 1 σ 2 e + 1 σ 2 pr (5.32)
$$

$$
σ 2 φ c = σ 2 e σ 2 pr σ 2 e + σ 2 pr . (5.33)
$$

(b) Assimilation of data twice: after the first assimilation, we have

$$
1 σ 2 φ 1 = 1 σ 2 e + 1 σ 2 pr (5.34)
$$

or

$$
σ 2 φ 1 = σ 2 e σ 2 pr σ 2 e + σ 2 pr = σ 2 φ c . (5.35)
$$

After the second assimilation, we have

$$
1 σ 2 φ 2 = 1 σ 2 e + 1 σ 2 φ 1 = 1 σ 2 e + 1 σ 2 e + 1 σ 2 pr . (5.36)
$$

Hence

$$
σ 2 φ 2 = σ 2 e σ 2 pr 2 σ 2 e + σ 2 pr < σ 2 φ c , (5.37)
$$

which means that we underestimate the posterior variance.

(c) Assimilation of data twice with MDA inflation: after the first assimilation, we have 1 1 1

$$
1 σ 2 φ 1 = 1 α 1 σ 2 e + 1 σ 2 pr . (5.38)
$$

After the second assimilation, we have

$$
1 σ 2 φ 2 = 1 α 2 σ 2 e + 1 σ 2 φ 1 = 1 α 2 σ 2 e + 1 α 1 σ 2 e + 1 σ 2 pr = ( 1 α 2 + 1 α 1 ) ︸ ︷︷ ︸ =1 1 σ 2 e + 1 σ 2 pr = 1 σ 2 e + 1 σ 2 pr . (5.39)
$$

$$
σ 2 φ 2 = σ 2 e σ 2 pr σ 2 e + σ 2 pr = σ 2 φ c , (5.40)
$$

which means that we recovered the correct posterior variance.

# 5.3.3 MDA from Regularized Nonlinear Least-Squares

The ES-MDA analysis equation was derived to preserve the ability to correctly sample the multivariate Gaussian posterior that arises in linear settings. However, the same analysis equation can be obtained by approaching the inverse problem from a nonlinear least-squares perspective [209]. In this case, we seek for vector m that minimizes the following weighted leastsquares function 2

$$
O ( m ) = ‖ d obs - g ( m ) ‖ 2 C - 1 e . (5.41)
$$

We can derive an iterative procedure for minimizing O ( m ) using a first-order Taylor series around the current guess m   as

$$
g ( m ) ≈ g ( m ℓ ) + G ℓ ( m - m ℓ ) = g ( m ℓ ) + G ℓ δ m ℓ +1 . (5.42)
$$

Therefore, we can write a linearized version of O ( m ) as

$$
O ls ( δ m ℓ +1 ) = ‖ d obs - g ( m ℓ ) - G ℓ δ m ℓ +1 ‖ 2 C - 1 e . (5.43)
$$

Minimization of O ls ( δ m   +1 ) is generally ill-posed, so we seek for a regularized solution of the form

$$
O rls ( δ m ℓ +1 ) = ‖ d obs - g ( m ℓ ) - G ℓ δ m ℓ +1 ‖ 2 C - 1 e + α ‖ δ m ℓ +1 ‖ 2 C - 1 m , (5.44)
$$

where α &gt; 0.

As usual, we set ∇O rls ( δ m   +1 ) = 0 , which leads to

$$
0 = - G ⊤ ℓ C - 1 e ( d obs - g ( m ℓ ) - G ℓ δ m ℓ +1 ) + α C - 1 m δ m ℓ +1 (5.45) = - G ⊤ ℓ C - 1 e ( d obs - g ( m ℓ ) ) + ( G ⊤ ℓ C - 1 e G ℓ + α C - 1 m ) δ m ℓ +1 = - G ⊤ ℓ ( α C e ) - 1 ( d obs - g ( m ℓ ) ) ( G ⊤ ℓ ( α C e ) - 1 G ℓ + C - 1 m ) δ m ℓ +1 .
$$

Therefore, for C m and C e positive definite, we have

$$
δ m ℓ +1 = ( G ⊤ ℓ ( α C e ) - 1 G ℓ + C - 1 m ) - 1 G ⊤ ℓ ( α C e ) - 1 ( d obs - g ( m ℓ ) ) . (5.46)
$$

We can show that Eq. (5.46) is equivalent to

$$
δ m ℓ +1 = C m G ⊤ ℓ ( G ℓ C m G ⊤ ℓ + α C e ) - 1 ( d obs - g ( m ℓ ) ) . (5.47)
$$

To show this equivalence, it is necessary to show that

$$
( G ⊤ ℓ ( α C e ) - 1 G ℓ + C - 1 m ) - 1 G ⊤ ℓ ( α C e ) - 1 = C m G ⊤ ℓ ( GC m G ⊤ + α C e ) - 1 . (5.48)
$$

First note that

$$
G ⊤ ℓ + G ⊤ ℓ ( α C e ) - 1 G ℓ C m G ⊤ ℓ = G ⊤ ℓ ( α C e ) - 1 ( α C e ) + G ⊤ ℓ ( α C e ) - 1 G ℓ C m G ⊤ ℓ = G ⊤ ℓ ( α C e ) - 1 ( α C e + G ℓ C m G ⊤ ℓ ) . (5.49)
$$

Also

$$
G ⊤ ℓ + G ⊤ ℓ ( α C e ) - 1 G ℓ C m G ⊤ ℓ = C - 1 m C m G ⊤ ℓ + G ⊤ ℓ ( α C e ) - 1 G ℓ C m G ⊤ ℓ = ( C - 1 m + G ⊤ ℓ ( α C e ) - 1 G ℓ ) C m G ⊤ ℓ . (5.50)
$$

Since the left-hand side of (5.49) and (5.50) are the same, so are the right-hand side.

$$
G ⊤ ℓ ( α C e ) - 1 ( α C e + G ℓ C m G ⊤ ℓ ) = ( C - 1 m + G ⊤ ℓ ( α C e ) - 1 G ℓ ) C m G ⊤ ℓ . (5.51)
$$

Pre-multiplying both sides of (5.51) by   C − 1 m + G     ( α C e ) − 1 G     − 1 gives

$$
( C - 1 m + G ⊤ ℓ ( α C e ) - 1 G ℓ ) - 1 G ⊤ ℓ ( α C e ) - 1 ( α C e + G ℓ C m G ⊤ ℓ ) = C m G ⊤ ℓ . (5.52)
$$

Pos-multiplying both sides of (5.52) by   α C e + G   C m G       − 1 gives

$$
( C - 1 m + G ⊤ ℓ ( α C e ) - 1 G ℓ ) - 1 G ⊤ ℓ ( α C e ) - 1 = C m G ⊤ ℓ ( α C e + G ℓ C m G ⊤ ℓ ) - 1 , (5.53)
$$

which completes the proof of equivalence between (5.46) and (5.47).

The similarity between Eq. (5.47) and ES-MDA is evident. Using the ensemble approximations   C   md ≈ C m G     and   C   dd ≈ G   C m G     results in the same update equation of ES-MDA:

$$
m ℓ +1 = m ℓ + ˜ C ℓ md ( ˜ C ℓ dd + α C e ) - 1 ( d obs - g ( m ℓ ) ) . (5.54)
$$

This result reveals the similarity between MDA and regularization methods. This similarity has also practical interest. In fact, it has been used to derive schemes to select the number of data assimilations and the corresponding inflation coefficients [253, 356, 284, 122].

# 5.3.4 Examples

# 5.3.4.1 Example: Porosity Distribution in a Core Sample

Consider the same problem introduced in Section 2.3.1.4. Fig. 5.3 presents the results for this problem using ES and ES-MDA with an ensemble of 100 members. For ES-MDA, N a = 4 is used with constant inflation factors. Both methods yield very similar results, closely resembling those obtained with EnKF (Fig. 4.5) and RML (Fig. 2.8), as all these methods converge to the actual Gaussian posterior as the number of samples increases.





![](<ensemble_data_assimilation_e-book_version_images/imageFile57.png>)





























 

 

�











�











 U GE RF 

 U GE RF 

(a)

ES

(b)

ES-MDA

Fig. 5.3: ES and ES-MDA results with N e = 100 for porosity in a core sample. The solid red line is the ground truth. The red circles are the observations. The gray lines are samples from the ES (a) and ES-MDA (b). The dashed lines are the average computed over the 100 samples. Example 5.3.4.1.

# 5.3.4.2 Example: Nonlinear Univariate Problem

Unlike MCMC and RML, EnKF and ES-MDA are unable to capture the bimodal nature of the posterior distributions. After assimilating the first data point, both methods tend to cluster samples around the second mode, which is closer to the prior mean. As more data are assimilated, the prominence of the first mode increases. Notably, EnKF struggles to capture this mode, while ES-MDA, though not fully accurate in representing the posterior, achieves significantly better sampling than EnKF.

 

 

 

![](<ensemble_data_assimilation_e-book_version_images/imageFile58.png>)

 

 

 





































 





���







 

���

 







 

���

 









(a)

Prior 1st datum

(b)

EnKF 1st datum

(c)

ES-MDA 1st datum







 

 

 



















 





���







 

���

 







 

���

 









(d)

Prior 5th datum

(e)

EnKF 5th datum

(f)

ES-MDA 5th datum

Fig. 5.4: Prior, EnKF and ES-MDA sampling for a nonlinear univariate problem. The black curve in each plot corresponds to the correct posterior distribution. Example 5.3.4.2.

# 5.3.4.3 Example: Production Logging in a Single Phase Flow

Emerick and Reynolds [132] compared ES and ES-MDA in a single-phase problem involving a reservoir with a single well operating at a constant liquid production rate of 1,000 bbl/day. The objective was to estimate the logpermeability for each of the 40 layers of the model based on liquid rate measurements per layer at a single time step, simulating a production-logging dataset. Fig. 5.5 shows the predicted layer rates obtained with a prior ensemble of 100 realizations and after applying ES and ES-MDA with two and four data assimilations. The results indicate that while the single update from ES led to noticeable improvements in the predicted layer-rate data,

![](<ensemble_data_assimilation_e-book_version_images/imageFile59.png>)

Liquid rate

(

(bbl/day)

/day

)

Liquid rate

(

(   /day)

/day

)

1 0

100

250

1 0

100

250

50

50

200

00

200

00

150

150

1

1

6

6

11

11

Layer

Layer

16

16

21

21

26

26

31

31

36

36

(a)

Prior

(b)

ES

Liquid rate

(

(bbl/day)

/day

)

Liquid rate

(

(   /day)

/day

)

1 0

100

250

1 0

100

250

50

50

200

00

200

00

150

150

1

1

6

6

11

11

Layer

Layer

16

16

21

21

26

26

31

31

36

36

(c)

ES-MDA ( N

2)

(d)

ES-MDA ( N

4)

=

=

a

a

a

a

Fig. 5.5: Liquid rate for each reservoir layer. Red circles represent observed data, gray lines show the predicted data, and green lines represent the ensemble mean. Example 5.3.4.3. Reproduced from Emerick and Reynolds [132] with permission from Elsevier.

# 5.3.4.4 Example: Permeability in a Two-Phase Linear Flow

[131], where it is shown similar plots combining ten ensembles with N e = 100 each. The results in these figures show that ES-MDA resulted in reasonable estimates of the posterior marginal distributions of log-permeability and water production rate for this problem.

![](<ensemble_data_assimilation_e-book_version_images/imageFile60.png>)

8

8

7

7

3 4 5 6 Log-permeability

3 4 5 6 Log-permeability

6

6

5

5

4

4

3

3

2 1

2 1

1

6

11

16 Gridblock

21

26

31

1

6

11

16 Gridblock

21

26

31

Gridblock

Gridblock

(a)

MCMC

(b)

ES-MDA

NTERNA

NTERNA

Fig. 5.6: Marginal log-permeability distributions for a two-phase linear flow. The red line represents the ground truth, the dashed line denotes the median, and the solid black lines correspond to the 25th and 75th percentiles. The outer bounding lines encompass the 2nd and 98th percentiles. Example 5.3.4.4. Reproduced from Emerick and Reynolds [131] with permission from Springer Nature.

![](<ensemble_data_assimilation_e-book_version_images/imageFile61.png>)

70

70

Water Rate (bbl/day)

Water Rate (bbl/day)

60

60

50

50

40

40

30

30

20

20

10

10

0 0

0 0

0

200

400

600

800

0

200

400

600

800

Time (days)

Time (days)

(a)

MCMC

(b)

ES-MDA

NTERNA

NTERNA

Fig. 5.7: Predicted water production rate. The red line represents the ground truth, the dashed line denotes the median, and the solid black lines correspond to the 25th and 75th percentiles. The outer bounding lines encompass the 2nd and 98th percentiles. Example 5.3.4.4. Reproduced from Emerick and Reynolds [131] with permission from Springer Nature.

# 5.3.4.5 Example: Two-Phase Flow in 2D Model

Consider the same data assimilation problem of two-phase flow in a 2D model previously discussed in Chapters 2 and 4. Section 2.4.5.4 presented the MAP estimate and RML realizations, while Section 4.3.4.1 presented the EnKF results. Here, we consider the ES-MDA results. The data assimilation used N a = 4 with constant inflation factors to update an ensemble with N e = 100 realizations 2 .

Fig. 5.8 shows the first three prior and posterior realizations of the ensemble, along with the true log-permeability. Similarly to the EnKF, ES-MDA data assimilation recovered the main permeability features of the ground truth. Fig. 5.9 presents the predicted water production rate for three wells, demonstrating improvements in both data matching and production forecast.

# 5.3.4.6 Example: EnKF, ES and ES-MDA in the Brugge Case

Emerick and Reynolds [132] compared the performance of the EnKF, ES, and ES-MDA (with N a = 4) for assimilating production data in the Brugge case [346]. Fig. 5.10 illustrates a single realization of log-permeability both before and after data assimilation using these methods. All methods resulted in an increase in the permeability of the prior model. Fig. 5.11 presents the water rate data for well P5, highlighting that ES did not achieve a satisfactory improvement in the data matching. The EnKF results are closer to the observations but exhibit a slight bias, whereas ES-MDA provides a good match to the data.

# 5.3.5 How Many Data Assimilations?

In the original ES-MDA method, the value for N a must be specified in advance. If, for example, we select a value for N a and, after completing these N a iterations, we find that additional iterations are needed, we cannot simply add more iterations as it would violate the condition   N a   =1 α − 1   = 1. Instead, a new data assimilation process must be initiated, starting from the prior ensemble with a larger value for N a (and compatible values for α   ). Practical experience from synthetic and field cases suggests that setting

N a = 4 with α 1 = ...α 4 = 4 is a good initial guess. However, it is essential to note that there are instances where N a = 4 may not be sufficient. For example, the synthetic problem presented in [131] necessitated at least N a = 10 for reasonable results. Additionally, the resemblance between MDA

2 As with the EnKF case, the data assimilation with ES-MDA used distance-based localization to regularize the updates; see Chapter 7.

(a)

True

7.00

6.56

6.11

5.67

5.22

4.78

4.33

3.89

3.44

3.00

(b)

Prior 1

7.00

6.56

6.11

5.67

5.22

4.78

4.33

3.89

3.44

3.00

(c)

Prior 2

![](<ensemble_data_assimilation_e-book_version_images/imageFile62.png>)

7.00

7.00

6.56

6.56

6.11

6.11

5.67

5.67

5.22

5.22

4.78

4.78

4.33

4.33

3.89

3.89

3.44

3.44

3.00

3.00

(d)

Prior 3

![](<ensemble_data_assimilation_e-book_version_images/imageFile63.png>)

7.00

7.00

7.00

6.56

6.56

6.56

6.11

6.11

6.11

5.67

5.67

5.67

5.22

5.22

5.22

4.78

4.78

4.78

4.33

4.33

4.33

3.89

3.89

3.89

3.44

3.44

3.44

3.00

3.00

3.00

(e)

ES-MDA 1

(f)

ES-MDA 2

(g)

ES-MDA 3

3.00

3.44

3.89

4.33

4.78

5.22

5.67

6.11

6.56

7.00

Fig. 5.8: True log-permeability, three prior realizations, and three posterior realizations obtained using ES-MDA for a 2D model under two-phase flow. Black circles indicate the positions of producers, and black triangles indicate the positions of water injection wells. Example 5.3.4.5.

and regularization methods implies that initiating the data assimilation with large values for α   and gradually decreasing them during the process may enhance the quality of the final models. This approach is rooted in the observation that at the beginning of a data assimilation process, the predicted data are typically distant from the observations. This situation may lead to overcorrections in the values of the model parameters. In this scenario, large values of α   work as a regularization coefficient, damping the model corrections at early iterations.





![](<ensemble_data_assimilation_e-book_version_images/imageFile64.png>)



���

       DWHUUDWH EE GD  

      DWHUUDWH EE GD  

          DWHUUDWH EE GD  

���

���

���

���

���

��

���

���

��

��

���

��

��

���

��

��

 

 

 

�







����

����



 

 

�







����

����



 

 

�







����

����



 

 

  7 PH GD V 

  7 PH GD V 

  7 PH GD V 

(a)

Well 1

(b)

Well 2

(c)

Well 3

Fig. 5.9: Water production rate in bbl/day for three wells. Red circles are the observations, and the red line is the prediction with the true log-permeability distribution. The gray and blue lines show the predictions from 100 prior and posterior realizations, respectively. The posterior realizations were obtained with ES-MDA. Example 5.3.4.5.

0

1

2

![](<ensemble_data_assimilation_e-book_version_images/imageFile26.png>)

(a)

Prior

(b)

EnKF

3

4

5

6

7

8 0

0

1

2

3

4

5

6

7

8

(c)

ES

(d)

ES-MDA

0

1

2

3

4

5

6

7

8

0 Fig.

1 5.10:

2

3 Log-permeability

4

5 for

6 the

7

8 0 of

0

1 one

2

3

4 of

5

6

7 case.

8 Exam-

first layer realization the Brugge ple 5.3.4.6. Reproduced from Emerick and Reynolds [132] with permission from Elsevier.

# 5.3.5.1 Adaptive Selection of ES-MDA Inflation

Emerick [118] introduced a straightforward adaptive procedure for choosing N a and α   based on the evolution of the data-mismatch objective function. This method involves specifying the maximum number of data assimilations, denoted as N a, max , the maximum inflation factor α max , and a coefficient a 0 within the range (0 , 1], for example, a 0 = 0 . 25. The steps of this adaptive procedure are outlined in Pseudo-code 5.3.

The adaptive scheme outlined in Pseudo-code 5.3 was originally proposed based on practical observations without a formal mathematical justification. However, a more recent work by Iglesias and Yang [208] has provided a theoretical basis for a similar scheme. The interpretation involves considering

INTERNA P5

P5

INTERNA P5

250

Water rate (m 3 /day)

200

150

100

50

0 0

0

1000

2000

3000

2000 Time (days)

250

Water rate (m 3 /day)

200

150

100

50

0 0

4000

0

(a)

Prior

P5

PRIOR

INTERNA P5

![](<ensemble_data_assimilation_e-book_version_images/imageFile27.png>)

250

250

Water rate (m 3 /day)

Water rate (m 3 /day)

200

200

150

150

100

100

50

50

0 0

0 0

4000

0

1000

0

2000

3000

2000 Time (days)

(c)

ES

P5

INTERNA P5

ES

1000

2000

3000

2000 Time (days)

(b)

EnKF

1000

2000

3000

2000 Time (days)

(d)

ES-MDA

4000

4000

EnKF

ES-MDA

Fig. 5.11: Water production rate for well P5 of the Brugge case. Red circles are the observations, blue lines are the predicted data and the green line is the ensemble mean prediction. Example 5.3.4.6. Reproduced from Emerick and Reynolds [132] with permission from Elsevier.

the process as a Bayesian tempering process [315], where the updates are controlled by imposing a threshold on the Jeffreys’ divergence [214] between two consecutive updates. The threshold is determined using the discrepancy principle [306, 184]. The resulting expression for selection α   is given by

$$
α - 1 ℓ +1 = min { max { N d 2 O ℓ d , √ N d 2 V [ O ℓ d ] } , 1 - β ℓ } , (5.55)
$$

where O   d and V   O   d   are the mean and variance of the data mismatch objective function computed over the N e realizations of the ensemble, and β   =     i =1 α − 1 i . Two additional adaptive MDA schemes are presented in [253]. The first

one follows the procedure outlined in Pseudo-code 5.3, incorporating an additional check for the maximum allowed change in model parameters. If the change in any parameter for any ensemble member exceeds twice its prior standard deviation, the update is rejected. Subsequently, a new update is attempted with a doubled value of α   +1 . This process is iterated until no further violations occur. It’s important to note that this scheme does not require new reservoir simulations; rather, it involves repeated iterations of the analysis step.

# Pseudo-code 5.3: Adaptive ES-MDA

- 1. Initialization: generate the initial ensemble,   m 0 j   N e j =1 . Choose the values for α max , N a, max and a 0 . Set   = 0 and β 0 = 0 and

$$
a = min { α max O 0 N,d , a 0 } . (5.56)
$$

- 2. Forecast step: run the forward model from time zero until the end of the historical period to compute the vector of predicted data

$$
d ℓ j = g ( m ℓ j ) , for j = 1 , 2 , . . . , N e . (5.57)
$$

- 3. Compute the average normalized data-mismatch objective function

$$
O ℓ N,d = 1 N e N e ∑ j =1 O N,d ( m ℓ j ) , where (5.58)
$$

$$
O N,d ( m ℓ j ) = 1 2 N d ( d obs - d ℓ j ) ⊤ C - 1 e ( d obs - d ℓ j ) . (5.59)
$$

- 4. Compute:


$$
α ℓ +1 = min { aO ℓ N,d , α max } . (5.60)
$$

$$
β ℓ +1 = β ℓ + 1 α ℓ +1 . (5.61)
$$

$$
5. If ( β ℓ +1 > 1 - 1 α max ) or ( ℓ = N a, max - 1) then
$$

-  Recompute the inflation factor using

$$
α ℓ +1 = 1 1 - β ℓ . (5.62)
$$

-  Set β   +1 = 1.


6. Perturb the vector of observation:

$$
d ℓ obs ,j = d obs + √ α ℓ +1 C 1/2 e z ℓ j , (5.63)
$$

for j = 1 , 2 ,...,N e , where z   j ∼ N ( 0 , I ). Analysis step: update the vector of model

7. parameters using

$$
m ℓ +1 j = m ℓ j + ˜ C ℓ md ( ˜ C ℓ dd + α ℓ +1 C e ) - 1 ( d ℓ obs ,j - d ℓ j ) , (5.64)
$$

for j = 1 , 2 ,...,N e . If = 1 then stop,

8. β   +1 else set   =   + 1 and return to step 2.

The second adaptive scheme introduced in [253] draws inspiration from the earlier work by Iglesias and Dawson [209], which employed the regularized Levenberg-Marquardt scheme from [184]. In this scheme, the acceptance of an update is contingent on satisfying the following condition for all ensemble members:

$$
ρ 2 ∥ ∥ ∥ C - 1/2 e ( d obs ,j - d ℓ j ) ∥ ∥ ∥ 2 ≤ α 2 ℓ +1 ∥ ∥ ∥ ∥ C 1/2 e ( ˜ C ℓ dd + α ℓ +1 C e ) - 1 ( d ℓ obs ,j - d ℓ j ) ∥ ∥ ∥ ∥ 2 , (5.65)
$$

for ρ ∈ (0 , 1). Large values for ρ require larger α   +1 , and consequently, more MDA iterations are necessary. However, this also introduces more regularization into the process, which should reduce overcorrections in the models, resulting in smoother updates. The authors used ρ = 0 . 2 in their example. If the condition (5.65) is not satisfied, the update is repeated by doubling the value of α   +1 .

# 5.3.5.2 Geometric Selection of ES-MDA Inflation

Practical experience with the adaptive schemes proposed in [118, 253] has revealed that they frequently result in a sluggish data assimilation process, demanding a substantial number of iterations. Consequently, this makes the method less appealing for large-scale applications due to the associated high computational costs. Motivated by this issue, Rafiee and Reynolds [356] proposed selecting α   based on a geometrically decreasing sequence such that

$$
α ℓ +1 = γα ℓ = γ ℓ α 1 (5.66)
$$

for γ ∈ (0 , 1]. For a given value of α 1 and N a , we can compute γ by solving f ( γ ) = 0, where

$$
f ( γ ) = N a ∑ ℓ =1 1 γ ℓ - 1 α 1 - 1 . (5.67)
$$

This equation can be solved using, for example, the bisection method.

To motivate the selection of α 1 , it is convenient to express the first MDA iteration for updating the ensemble mean as follows:

$$
m 1 = m 0 +∆ M 0 ( ∆ D 0 ) ⊤ ( ∆ D 0 ( ∆ D 0 ) ⊤ + α 1 C e ) - 1 ( d obs - g ( m 0 ) ) = m 0 +∆ M 0 ( C - 1/2 e ∆ D 0 ) ⊤ [ ( C - 1/2 e ∆ D 0 )( C - 1/2 e ∆ D 0 ) ⊤ + α 1 I ] - 1 × C - 1/2 e ( d obs - g ( m 0 ) ) (5.68)
$$

or

$$
( ∆ M 0 ) + ( m 1 - m 0 ) = ( C - 1/2 e ∆ D 0 ) ⊤ × ( ( C - 1/2 e ∆ D 0 )( C - 1/2 e ∆ D 0 ) ⊤ + α 1 I ) - 1 × C - 1/2 e ( d obs - g ( m 0 ) ) , (5.69)
$$

where m 0 denotes a prior realization and   ∆ M 0   + is the pseudo-inverse of ∆ M 0 . Now call

$$
̂ m = ( ∆ M 0 ) + ( m 1 - m 0 ) , (5.70)
$$

$$
̂ d = C - 1/2 e ( d obs - g ( m 0 ) ) (5.71)
$$

and

$$
̂ ∆ D = C - 1/2 e ∆ D 0 . (5.72)
$$

  Hence, Eq. (5.69) can be written as

$$
̂ m = ̂ ∆ D ⊤ ( ̂ ∆ D ̂ ∆ D ⊤ + α 1 I ) - 1 ̂ d . (5.73)
$$

Eq. (5.73) represents the solution of a regularized linear least-squares problem (see Appendix B, Section B.4.4), where α 1 plays the role of the Tikhonov regularization parameter.

Rafiee and Reynolds [356] used the regularization condition of Eq. (5.65) as starting point to derive an expression for α 1 . We can write Eq. (5.65) as

$$
ρ 2 ≤ α 2 1 ∥ ∥ ∥ C - 1 ̂ d ∥ ∥ ∥ 2 ∥ ∥ ∥ ̂ d ∥ ∥ ∥ 2 (5.74)
$$

$$
( ̂ ) ρ 2 ≤ α 2 1 max i λ 2 i = α 2 1 max i 1 ( σ 2 i + α 1 ) 2 (5.75)
$$

    where C =     ∆ D   ∆ D   + α 1 I   . Then, note that

The equality occurs for

$$
ρ 2 ≤ α 2 1 1 ( σ 2 + α 1 ) 2 . (5.76)
$$

$$
α 1 = ρ 1 - ρ σ 2 , (5.77)
$$

where

$$
σ = 1 N r N r ∑ i =1 σ i , (5.78)
$$

with N r denoting the number of non-zero singular values of C . Rafiee and Reynolds [356] proposed to adopt ρ = 0 . 5, which leads to α 1 = σ 2 . The resulting procedure is summarized in Pseudo-code 5.4.

# Pseudo-code 5.4: Geometric MDA 1

1. Specify N a . 2. Compute

Compute

$$
α 1 = max { σ 2 , N a } , (5.79)
$$

where

$$
σ = 1 N r N r ∑ i =1 σ i . (5.80)
$$

3. Compute γ ∈ (0 , 1] by solving

$$
f 1 ( γ ) = N a ∑ k =1 1 γ k - 1 α 1 - 1 = 0 (5.81)
$$

using the bisection method.

4. Apply ES-MDA with α   +1 = γ   α 1 .

Emerick [122] proposed a similar procedure based on a geometric sequence of α   which requires the specification of the inflation factor at the last data assimilation, α N a = α min . The motivation for this procedure is to ensure that the geometric scheme α   +1 = γ   α 1 does not result in a sequence that decays too rapidly. The value of α 1 is computed using

3 See Appendix A for a brief review on linear algebra.

$$
α 1 = γ 1 - N a α N a , (5.82)
$$

where γ is obtained by solving

$$
f 2 ( γ ) = N a ∑ ℓ =1 1 γ ℓ - N a α N a - 1 , (5.83)
$$

using the bisection method. The value α 1 obtained with Eq. (5.82) is checked using the Morozov’s discrepancy principle (MDP) [306]. If the current value of α 1 is not sufficiently large to satisfy the MDP, N a is increased, and a new value for α 1 is computed. The MDP states that it is not reasonable to expect the solution to yield

an error smaller than the noise level in the data. Therefore, we can define a discrepancy function as

$$
h ( α ) = ∥ ∥ ∥ ̂ ∆ D ̂ m - ̂ d ∥ ∥ ∥ 2 - η 2 , (5.84)
$$

        where η is the noise level. Here, we assume that η 2 = E [     e   2 ] = N d , where e is the normalized data-error vector.    

  Using Eq. (5.84) we can compute α &gt; 0 such that h ( α ) = 0 by solving a root-finding problem. We start by writing the singular value decomposition of   ∆ D as

$$
̂ ∆ D = UΣV ⊤ , (5.85)
$$

  where U ∈ R N d × N d and V ∈ R N m × N m are orthogonal matrices and Σ ∈ R N d × N m is a matrix with diagonal element given by

$$
σ 1 ≥ σ 2 ≥ . . . ≥ σ N r > σ N r +1 = . . . = σ min { N d ,N m } = 0 . (5.86)
$$

Replacing Eq. (5.85) in (5.84) and using the properties UU   = I and VV   = I results in

$$
h ( α ) = ∥ ∥ ∥ ̂ ∆ D ̂ m - ̂ d ∥ ∥ ∥ 2 - η 2 = ∥ ∥ ∥ U ⊤ ( ̂ ∆ DVV ⊤ ̂ m - ̂ d )∥ ∥ ∥ 2 - η 2 = ∥ ∥ ∥ ΣV ⊤ ̂ m - U ⊤ ̂ d ∥ ∥ ∥ 2 - η 2 = N r ∑ i =1 ( σ i v ⊤ i ̂ m - u ⊤ i ̂ d ) 2 + N d ∑ i = N r +1 ( u ⊤ i ̂ d ) 2 - η 2 . (5.87)
$$

The vector m can be written as

 

$$
̂ m = ( ̂ ∆ D ⊤ ̂ ∆ D + α I ) - 1 ̂ ∆ D ⊤ ̂ d = ( VΣ ⊤ ΣV ⊤ + α I ) - 1 VΣ ⊤ U ⊤ ̂ d = V ( Σ ⊤ Σ + α I ) Σ ⊤ U ⊤ ̂ d = N r ∑ j =1 ( σ j σ 2 j + α u ⊤ j ̂ d ) v j . (5.88)
$$

Using Eq. (5.88) in (5.87) results in

$$
h ( α ) = N r ∑ i =1 ⎡ ⎣ σ i v ⊤ i ⎛ ⎝ N r ∑ j =1 ( σ j σ 2 j + α u ⊤ j ̂ d ) v j ⎞ ⎠ - u ⊤ i ̂ d ⎤ ⎦ 2 + N d ∑ i = N r +1 ( u ⊤ i ̂ d ) 2 - η 2 = N r ∑ i =1 [ σ 2 i σ 2 i + α u ⊤ i ̂ d - u ⊤ i ̂ d ] 2 + N d ∑ i = N r +1 ( u ⊤ i ̂ d ) 2 - η 2 = N r ∑ i =1 ( α σ 2 i + α u ⊤ i ̂ d ) 2 + N d ∑ i = N r +1 ( u ⊤ i ̂ d ) 2 - η 2 . (5.89)
$$

We can use the Newton-Raphson method [350] to compute α   such that h ( α   ) = 0, in which case it is necessary to compute the derivative

$$
d h ( α ) d α = N r ∑ i =1 2 ασ 2 i ( σ 2 i + α ) 3 ( u ⊤ i ̂ d ) 2 . (5.90)
$$

Note that d h ( α ) d α &gt; 0 for any α &gt; 0. Therefore, h ( α ) is a strictly increasing function of α . Moreover, note that

and

$$
lim α → 0 + h ( α ) = N d ∑ i = N r +1 ( u ⊤ i ̂ d ) 2 - η 2 = ∥ ∥ ∥ U ⊤ 0 ̂ d ∥ ∥ ∥ 2 - η 2 (5.91)
$$

$$
lim α →∞ h ( α ) = N d ∑ i =1 ( u ⊤ i ̂ d ) 2 - η 2 = ∥ ∥ ∥ ̂ d ∥ ∥ ∥ 2 - η 2 . (5.92)
$$

Therefore, h ( α ) = 0 has a unique solution as long as the noise level satisfies

$$
∥ ∥ ∥ U ⊤ 0 ̂ d ∥ ∥ ∥ 2 ≤ η 2 ≤ ∥ ∥ ∥ ̂ d ∥ ∥ ∥ 2 . (5.93)
$$

Pseudo-code 5.5 summarizes the geometric MDA process.

# Pseudo-code 5.5: Geometric MDA 2

1. Specify α N a , α max and N a . 2. Compute (0 1] by solving

γ ∈ ,

$$
f 2 ( γ ) = N a ∑ ℓ =1 1 γ ℓ - N a α N a - 1 = 0 (5.94)
$$

using the bisection method.

- 3. Compute

$$
α 1 = γ 1 - N a α N a . (5.95)
$$

- 4. Compute α   ∈ [ N a ,α max ] by solving h ( α ) = 0 using the NewtonRaphson method.  
- 5. If α 1 &lt; α set N a = N a + 1 and return to step Otherwise apply ES-MDA with α   +1 = γ   α 1 .


2.

Pseudo-code 5.6 presents the Newton-Rapshon to compute α   by solving h ( α   ) = 0.

4 R ( · ) and N ( · ) denote the range and null space. See Appendix A, Section A.2. 5

Localization is discussed in Chapter 7, Section 7.5.

# Pseudo-code 5.6: Newton-Rapshon to compute α  

1. Set α min = N a and specify α max and N max . 2. Compute

Compute

$$
h ( α min ) = N r ∑ i =1 ( α min σ 2 i + α min u ⊤ i ̂ d ) 2 - N d (5.96)
$$

- 3. If h ( α min ) ≥ 0 set α   = α

$$
min min and exit. α 1 = α min + α max 2 (5.97)
$$

- 4. Compute
- 5. For n = 1 to N max do


• Compute:

$$
h ( α n ) = N r ∑ i =1 ( α n σ 2 i + α n u ⊤ i ̂ d ) 2 - N d (5.98)
$$

$$
h ′ ( α n ) = N r ∑ i =1 2 α n σ 2 i ( σ 2 i + α n ) 3 ( u ⊤ i ̂ d ) 2 α n +1 = α n - h ( α n ) h ′ ( α n ) (5.99)
$$

$$
· If α n +1 ≥ α max set α ⋆ = α max and exit, else if ∣ ∣ α n +1 - α n ∣ ∣ < 10 - 3 set α ⋆ = α n +1 and exit.
$$

6. Set α   = α n .

# 5.3.5.3 Example: Geometric Selection of ES-MDA Inflation in the UNISIM-I-H Case

Emerick [122] tested the geometric selection of ES-MDA inflation on the UNISIM-I-H benchmark case [20], a synthetic reservoir based on actual data from the Namorado Field (Campos Basin). Fig. 5.12 presents a plot of the average data-mismatch norm versus the average model-change norm of logpermeability for data assimilations using N a = 4 and N a = 8 with both constant and geometric sequences of inflation factors. The dashed curve connects the “best” points, forming an analog to a Pareto front.

![](<ensemble_data_assimilation_e-book_version_images/imageFile67.png>)

0.75

4x-CONST

Average model-change norm

4x-GEO(1E2)

- 4x-GEO(1E3)
- 4x-GEO(1E4)
- 4x-GEO(1E5)


0.7

0.65

4x-GEO1

8x-CONST

- 8x-GEO(1E2)
- 8x-GEO(1E3)
- 8x-GEO(1E4)


0.6

0.55

8x-GEO(1E5)

8x-GEO1

8x-GEO2

0.5

0

2

4

6

8

Average data-mismatch norm

INTERNA Fig. 5.12: Average data-mismatch and model-change norms. Example 5.3.5.3. Reproduced from Emerick [122] with permission from Elsevier.

# 5.3.6 Deterministic ES-MDA

ES-MDA relies on the standard perturbed observation scheme, also known as the stochastic scheme. However, there exist deterministic schemes that eliminate the necessity of perturbed observations, such as square-root schemes. One such method is the deterministic ensemble Kalman filter (DEnKF), introduced by Sakov and Oke [374]. While DEnKF is not a square-root filter, it shares the same conceptual objective, aiming to avoid additional sampling errors introduced by perturbing observations. In terms of implementation, DEnKF closely resembles EnKF, involving the computation of the Kalman gain and allowing Schur product localization [197].

Emerick [121] combined ES-MDA with the deterministic scheme proposed by Sakov and Oke [374], giving rise to the deterministic ES-MDA (DESMDA) method. The motivation behind DES-MDA stems from two key as-

To introduce DES-MDA, it is beneficial to revisit the ES method for the linear case and express it as follows:

$$
m c ,j = m j + ˜ K ( d obs + e j - Gm j ) , for j = 1 , . . . , N e , (5.100)
$$

where

$$
˜ K = ˜ C m G ⊤ ( G ˜ C m G ⊤ + C e ) - 1 , (5.101)
$$

and

$$
e j = C 1/2 e z j (5.102)
$$

with z j ∼ N ( 0 , I ). The ES equation to update the mean is 7

Hence,

$$
m c = m + ˜ K ( d obs - Gm ) . (5.103)
$$

$$
m c ,j - m c = m j - m + ˜ K ( e j - G ( m j - m )) , for j = 1 , . . . , N e . (5.104)
$$

This can be written in a matrix form as

$$
∆ M c = ∆ M + ˜ K ( E - G ∆ M ) , (5.105)
$$

where

$$
E = [ e 1 · · · e N e ] , (5.106)
$$

and

$$
∆ M = 1 √ N e - 1 [ m 1 - m , · · · , m N e - m ] , (5.107)
$$

$$
∆ M c = 1 √ N e - 1 [ m c , 1 - m c , · · · , m c ,N e - m c ] . (5.108)
$$

Computing the covariance matrix of the posterior ensemble gives

6 One alternative to compute the data perturbations with non-diagonal C e is to use algorithms from geostatistics such as sequential Gaussian simulation. 7

Here, it is assumed that e = 0 . This is easily obtained in practice by correcting the entries of the vector z j to have exactly zero mean.

$$
˜ C m c = ∆ M c ∆ M ⊤ c = [ ∆ M + ˜ K ( E - G ∆ M ) ] [ ∆ M + ˜ K ( E - G ∆ M ) ] ⊤ = ˜ C m - ˜ C m G ⊤ ˜ K ⊤ - ˜ KG ˜ C m + ˜ KG ˜ C m G ⊤ ˜ K ⊤ + ˜ KEE ⊤ ˜ K ⊤ + ( I - ˜ KG ) ∆ ME ⊤ ˜ K ⊤ + ˜ KE ∆ M ⊤ ( I - G ⊤ ˜ K ⊤ ) . (5.109)
$$

This expression converges to the theoretical covariance update formula

$$
˜ C m c = ( I - ˜ KG ) ˜ C m (5.110)
$$

when N e → ∞ . The fact that the perturbed observation scheme only satisfies the update formula statistically has been regarded as a source of sampling errors 8 .

If we neglect the perturbed observations (setting E = 0 in the previous expression), we obtain

$$
˜ C m c = ˜ C m - 2 ˜ KG ˜ C m + ˜ KG ˜ C m G ⊤ ˜ K ⊤ . (5.111)
$$

Sakov and Oke [374] observed that by neglecting the quadratic term,   KG   C m G     K   , the theoretical covariance update could be obtained by multiplying the Kalman gain by half. This insight led to the development of DEnKF. In this scheme, the mean is updated using the standard formula, and deviations from the mean are updated using:

$$
∆ M c = ∆ M - 1 2 ˜ KG ∆ M . (5.112)
$$

This expression results in the following expression for the posterior covariance 1

$$
˜ C m c = ( I - ˜ KG ) ˜ C m + 1 4 ˜ KG ˜ C m G ⊤ ˜ K ⊤ . (5.113)
$$

Note that compared to the theoretical value,   C m c above has an extra positive semidefinite matrix 1 4   KG   C m G     K   . Therefore, this expression overestimates the theoretical covariance. Sakov and Oke [374] interpreted this fact as a built-in covariance inflation 9 .

The extension of the deterministic analysis with ES-MDA for nonlinear problems is direct. First, define the matrix with predicted data

$$
∆ D ℓ = 1 √ N e - 1 [ g ( m ℓ 1 ) - g ( m ℓ ) , · · · , g ( m ℓ N e ) - g ( m ℓ ) ] , (5.114)
$$

8 That is the motivation for deterministic or square-root schemes, which are designed to exactly satisfy the theoretical covariance update formula. 9

Covariance inflation [15] is a common ad hoc method used to compensate for excessive variance loss observed in ensemble methods (see Chapter 7, Section 7.4).

and write

$$
G ℓ ∆ M ℓ = ∆ D ℓ . (5.115)
$$

Then, the following products become

$$
˜ C ℓ m G ⊤ ℓ = ∆ M ℓ ∆ M ⊤ ℓ G ⊤ ℓ = ∆ M ℓ ∆ D ⊤ ℓ = ˜ C ℓ md (5.116)
$$

and

$$
G ℓ ˜ C ℓ m G ⊤ ℓ = G ℓ ∆ M ℓ ∆ M ⊤ ℓ G ⊤ ℓ = ∆ D ℓ ∆ D ⊤ ℓ = ˜ C ℓ dd . (5.117)
$$

Pseudo-code 5.7 summarizes the resulting DES-MDA method.

# Pseudo-code 5.7: DES-MDA

1. Initialization: generate the initial ensemble,   m 0 j   N e j =1 , choose N a and { α   } N a   =1 . Set   = 0. 2. Forecast step: compute the vector of predicted data

Forecast step: compute the vector of predicted data

$$
d ℓ j = g ( m ℓ j ) , for j = 1 , 2 , . . . , N e (5.118)
$$

3. Analysis step:

-  Compute the Kalman gain

$$
˜ K ℓ = ˜ C ℓ md ( ˜ C ℓ dd + α ℓ +1 C e ) - 1 (5.119)
$$

-  Update the ensemble mean

$$
m ℓ +1 = m ℓ + ˜ K ℓ ( d obs - d ℓ ) (5.120)
$$

-  Update the ensemble deviations

$$
∆ M ℓ +1 = ∆ M ℓ - 1 2 ˜ K ℓ ∆ D ℓ (5.121)
$$

-  Update the ensemble


$$
M ℓ +1 = m ℓ +1 1 ⊤ + √ N e - 1∆ M ℓ +1 (5.122)
$$

- 4. Set   =   + 1.
- 5. If   = N a then set m c ,j = m   j for j = 1 ,...,N e and stop, else return to step 2.


# 5.3.6.1 Example: DES-MDA in the UNISIM-I-H Case

Emerick [121] tested ES-MDA and DES-MDA on the UNISIM-I-H case using both production and 4D seismic data. Fig. 5.13 shows the normalized variance of log-permeability after data assimilation with ES-MDA and DESMDA for an ensemble of N e = 200 realizations. The results indicate that DES-MDA maintained a higher variability in the posterior ensemble without compromising the method’s overall ability to match the observed data, as illustrated in Figs. 5.14 and 5.15.

![](<ensemble_data_assimilation_e-book_version_images/imageFile28.png>)

(a)

ES-MDA

(b)

DES-MDA

0.0

0.2

0.0

0.4

0.2

0.6

0.8

0.0 0.4

0.8

1.0

0.2 0.6

1.0

0.8

0.4

0.6

1.0

0.8

1.0

Fig. 5.13: Normalized variance of log-permeability (layer 12) for the UNISIM-I-H case. Example 5.3.6.1. Reproduced from Emerick [121] with permission from Springer Nature.

![](<ensemble_data_assimilation_e-book_version_images/imageFile69.png>)





    DWHUFXW  

    DWHUFXW  

���

���

���

���

���

���













����

����















����

����







  7 PH GD V 

  7 PH GD V 

(a)

ES-MDA

(b)

DES-MDA

Fig. 5.14: Predicted water cut data for the well NA1A of the UNISIM-I-H case. Red dots are the observed data points, and gray and blue lines correspond to the predicted data from the prior and posterior ensemble, respectively, for the UNISIM-I-H case. Example 5.3.6.1. Reproduced from Emerick [121] with permission from Springer Nature.

Ensemble Smoother with Multiple Data Assimilation 300000

300000

240000

180000

120000

60000

0

60000

120000

180000 300000

300000

(a)

Observed

(b)

Prior

240000 (b) 240000

240000

![](<ensemble_data_assimilation_e-book_version_images/imageFile29.png>)

300000 180000

180000

120000

60000

0

60000

120000

180000

(c)

ES-MDA

(d)

DES-MDA

240000 (d)

300000

150000

0

300000 150000

150000

300000

Fig. 5.15: Observed and predicted 4D seismic data (P-impedance changes in kg/m 2 s) for the first realization for the UNISIM-I-H case (layer 12). Example 5.3.6.1. Reproduced from Emerick [121] with permission from Springer Nature.

300000

240000

180000

120000

60000

0

60000

120000

180000 300000

300000

240000 240000

240000

300000 180000

180000

120000

60000

0

60000

120000

180000

240000

300000

This page is reserved for your imagination.

![](<ensemble_data_assimilation_e-book_version_images/imageFile71.png>)

# Iterative Ensemble Smoothers

Abstract: This chapter reviews two widely used iterative versions of the ensemble smoother: the ensemble randomized maximum likelihood (EnRML) and the subspace iterative ensemble smoother (SIES).

# 6.1 Introduction

This chapter reviews two popular versions of iterative ES: the ensemble RML (EnRML) [78, 79] and the subspace iterative ES (SIES) [354, 142]. Other iterative forms of ES exist in the literature but are not discussed here. Notable examples include the iterative adaptive Gaussian mixture smoother (IAGS) [413], the regularized Levenberg-Marquardt for minimum-averagecost (RLM-MAC) [279], and the iterative local updating ensemble smoother (ILUES) [480].

# 6.2 Ensemble Randomized Maximum Likelihood

Chen and Oliver [78] introduced one of the earliest iterative forms of ES by adapting the scheme proposed by Gu and Oliver [178] in the context of sequential data assimilation. This method employs a Gauss-Newton (GN) update scheme to minimize the RML objective function:

$$
O r ( m ) = 1 2 ( d obs ,j - g ( m )) ⊤ C - 1 e ( d obs ,j - g ( m )) + 1 2 ( m - m j ) ⊤ C - 1 m ( m - m j ) . (6.1)
$$

In this method, the vector of model parameters is updated using

$$
m ℓ +1 j = m ℓ j + β ℓ δ m ℓ +1 j , (6.2)
$$

where β   ∈ [0 , 1] is the step size in the direction δ m   +1 j given by

$$
δ m ℓ +1 j = - ( ˜ C - 1 m + ˜ G ⊤ ℓ C - 1 e ˜ G ℓ ) - 1 × [ ˜ C - 1 m ( m ℓ j - m j ) + ˜ G ⊤ ℓ C - 1 e ( g ( m ℓ j ) - d obs ,j ) ] , (6.3)
$$

or equivalently

$$
δ m ℓ +1 j = m j - m ℓ j - ˜ C m ˜ G ⊤ ℓ ( ˜ G ℓ ˜ C m ˜ G ⊤ ℓ + C e ) - 1 × [ g ( m ℓ j ) - d obs ,j - ˜ G ℓ ( m ℓ j - m j ) ] . (6.4)
$$

As before, a tilde over a matrix indicates that this matrix is estimated based on the ensemble. Additionally, note that m j without the iteration index   refers to a prior realization.

Eq. (6.4) requires the sensitivity matrix at the   th iteration,   G   . Gu and Oliver [178] propose to write

and compute   G   as

$$
˜ G ℓ ∆ M ℓ = ∆ D ℓ , (6.5)
$$

$$
˜ G ℓ = ∆ D ℓ ∆ M + ℓ , (6.6)
$$

  where ∆ M +   is the pseudo-inverse of ∆ M   . As usual, the matrices ∆ D   and ∆ M   have the forms

and

$$
∆ D ℓ = 1 √ N e - 1 [ g ( m ℓ 1 ) - g ( m ℓ ) , · · · , g ( m ℓ N e ) - g ( m ℓ ) ] = D ℓ A (6.7)
$$

$$
∆ M ℓ = 1 √ N e - 1 [ m ℓ 1 - m ℓ , · · · , m ℓ N e - m ℓ ] = M ℓ A (6.8)
$$

where

$$
A = 1 √ N e - 1 ( I - 1 N e 11 ⊤ ) . (6.9)
$$

Chen and Oliver [78] demonstrated that this scheme achieved a significant reduction in data mismatch for the Brugge benchmark case [346]. However, this came at the cost of requiring several iterations due to the necessity of small step sizes to ensure acceptable convergence. This observation led Chen and Oliver [79] to replace the GN with a Levenberg-Marquardt (LM) update scheme. The LM scheme was introduced to regularize the search direction and better control the step length, improving the efficiency of the inversion process. The LM analogous of Eq. (6.3) is obtained by modifying the GN Hessian such that

$$
δ m ℓ +1 j = - ( (1 + λ ℓ ) ˜ C - 1 m + ˜ G ⊤ ℓ C - 1 e ˜ G ℓ ) - 1 × [ ˜ C - 1 m ( m ℓ j - m j ) + ˜ G ⊤ ℓ C - 1 e ( g ( m ℓ j ) - d obs ,j ) ] , (6.10)
$$

or equivalently

$$
δ m ℓ +1 j = m j - m ℓ j 1 + λ ℓ - ˜ C m ˜ G ⊤ ℓ ( ˜ G ℓ ˜ C m ˜ G ⊤ ℓ +(1 + λ ℓ ) C e ) - 1 × [ g ( m ℓ j ) - d obs ,j - ˜ G ℓ ( m ℓ j - m j ) 1 + λ ℓ ] . (6.11)
$$

One challenge with these schemes is that estimating   G   using the pseudoinverse of ∆ M   is noisy and unstable if N m   N e . Chen and Oliver [78] argue that this instability might not be critical because   G   is mostly premultiplied by   C m , which tends to smooth the estimates. This effect is illustrated in Fig. 6.1, which presents the values of the matrix G   (   = 0) and the product C m G     at two different times for the linear two-phase flow discussed in Section 2.4.5.3. Each panel shows the sensitivity estimated with the ensemble using Eq. (6.6) and calculated with the adjoint method. While the ensemble-based sensitivity values capture the overall structure of the adjoint, they are quite noisy. However, the product with the prior covariance tends to smooth out some of this noise. It is important to note that   C m corresponds to the prior covariance, which is not updated during the process. However,   G   still appears without the pre-multiplication in the GN and LM update equations, which could lead to instability issues.

50

30

10

-10

-30

-50 1

1

EnRML

Adjoint

6

11

16 Gridblock

Gridblock

(a)

30 days

21

26

31

50

30

10

-10

-30

-50 1

1

EnRML

Adjoint

6

11

16 Gridblock

21

Gridblock

(b)

360 days

26

31

150

100

50

0

-50

-100

-150 1

1

6

![](<ensemble_data_assimilation_e-book_version_images/imageFile30.png>)

EnRML

Adjoint

11

16 Gridblock

Gridblock

(c)

30 days

21

26

31

180

140

100

60

20

-20

-60

-100 1

1

EnRML

Adjoint

6

11

16 Gridblock

21

Gridblock

(d)

360 days

26

31

Fig. 6.1: Comparison between adjoint and ensemble-based sensitivity calculations. (a) and (b) display sensitivity values computed at 30 and 360 days, respectively. (c) and (d) show the corresponding products of the prior covariance with the transpose of the sensitivity matrix. Reproduced from Emerick and Reynolds [131] with permission from Springer Nature.

# 6.2.1 LM-EnRML

The challenges associated with the calculation of   G   led Chen and Oliver [79] to propose an implementation that avoids explicitly calculating   G   . To derive this implementation, they modified the Hessian in Eq. (6.10) by replacing   C m with   C   m , which means substituting the prior covariance estimate with the covariance estimate at the current iteration. With this modification, Eq. (6.10) becomes

$$
δ m ℓ +1 j = - [ (1 + λ ℓ ) ( ˜ C ℓ m ) - 1 + ˜ G ⊤ ℓ C - 1 e ˜ G ℓ ] - 1 × [ ˜ C - 1 m ( m ℓ j - m j ) + ˜ G ⊤ ℓ C - 1 e ( g ( m ℓ j ) - d obs ,j ) ] , (6.12)
$$

or equivalently

$$
δ m ℓ +1 j = - [ (1 + λ ℓ ) ( ˜ C ℓ m ) - 1 + ˜ G ⊤ ℓ C - 1 e ˜ G ℓ ] - 1 ˜ C - 1 m ( m ℓ j - m j ) - ˜ C ℓ m ˜ G ⊤ ℓ [ ˜ G ℓ ˜ C ℓ m ˜ G ⊤ ℓ +(1 + λ ℓ ) C e ] - 1 ( g ( m ℓ j ) - d obs ,j ) . (6.13)
$$

For the computational implementation of Eq. (6.13), Chen and Oliver [79] introduced the following scaled matrices:

$$
̂ ∆ M ℓ = C - 1/2 s ∆ M ℓ , (6.14)
$$

$$
̂ ∆ D ℓ = C - 1/2 e ∆ D ℓ , (6.15)
$$

  where C s is a scaling diagonal matrix containing the prior model variances, i.e., C s = diag ( C m ). Using (6.14)–(6.15) in (6.13) leads to

Using (6.14)-(6.15) in (6.13) leads to

$$
δ m ℓ +1 j = - C 1/2 s ̂ ∆ M ℓ [ (1 + λ ℓ ) I + ̂ ∆ D ⊤ ℓ ̂ ∆ D ℓ ] - 1 × ̂ ∆ M ⊤ ℓ ( ̂ ∆ M -⊤ ̂ ∆ M - 1 ) C - 1/2 s ( m ℓ j - m j ) - C 1/2 s ̂ ∆ M ℓ ̂ ∆ D ⊤ ℓ [ (1 + λ ℓ ) I + ̂ ∆ D ℓ ̂ ∆ D ⊤ ℓ ] - 1 × C - 1/2 e ( g ( m ℓ j ) - d obs ,j ) . (6.16)
$$

Note that   ∆ M without the iteration index   refers to the prior. Using truncated singular value decomposition

$$
̂ ∆ M = U m Σ m V ⊤ m (6.17)
$$

$$
̂ ∆ D ℓ = U d Σ d V ⊤ d , (6.18)
$$

  in (6.16) leads to the final LM-EnRML update direction:

$$
δ m ℓ +1 j = - C 1/2 s ̂ ∆ M ℓ V d [ (1 + λ ℓ ) I + Σ 2 d ] - 1 × V ⊤ d ̂ ∆ M ⊤ ℓ U m Σ - 2 m U ⊤ m C - 1/2 s ( m ℓ j - m j ) - C 1/2 s ̂ ∆ M ℓ V d Σ d [ (1 + λ ℓ ) I + Σ 2 d ] - 1 × U ⊤ d C - 1/2 e ( g ( m ℓ j ) - d obs ,j ) . (6.19)
$$

Chen and Oliver [79] also proposed an approximation to this expression by neglecting the term corresponding to the model mismatch in Eq. (6.16), leading to an update direction given by

$$
δ m ℓ +1 j = - C 1/2 s ̂ ∆ M ℓ V d Σ d [ (1 + λ ℓ ) I + Σ 2 d ] - 1 × U ⊤ d C - 1/2 e ( g ( m ℓ j ) - d obs ,j ) . (6.20)
$$

It is interesting to note that the update equation of the approximated version of LM-EnRML is very similar to the ES-MDA update equation, with (1 + λ   ) taking the role of the MDA data-error covariance inflation coefficient, α   . However, there are two noticeable differences: First, ES-MDA terminates based on the condition   N a   =1 α − 1   = 1, while LM-EnRML stops based on convergence criteria or the maximum number of iterations. Second, ES-MDA computes the data perturbations using the inflated data-error covariance, α   C e , and resamples each iteration, while LM-EnRML computes the perturbations based on C e and keeps the values constant throughout the entire iterative process.

Pseudo-code 6.1 summarizes the LM-EnRML method. This process requires the specification of the initial LM parameter, λ 0 &gt; 0, the maximum LM parameter, λ max &gt; 0, and the increase factor, γ &gt; 1. Chen and Oliver [79] suggest selecting λ 0 on the order of O 0 N,d and γ = 10. The maximum λ max is introduced in Pseudo-code 6.1 to halt the process when the data mismatch ceases to decrease. Additional termination criteria include the maximum number of iterations, a small reduction in the objective function, and minimal updates in the models over an iteration.

# Pseudo-code 6.1: LM-EnRML

- 1. Initialization: generate the initial ensemble,   m 0 j   N e j =1 , by sampling the prior distribution of parameters, select the values for λ 0 , λ max , and γ , set   = 0, and compute:

$$
̂ ∆ M = C - 1/2 s ∆ M = U m Σ m V ⊤ m (6.21)
$$

$$
d obs ,j = d obs + C 1/2 e z j , where z j ∼ N ( 0 , I ) (6.22)
$$

$$
d 0 j = g ( m 0 j ) , for j = 1 , 2 , . . . , N e (6.23)
$$

$$
O 0 N,d = 1 N e N e ∑ j =1 O N,d ( m 0 j ) (6.24)
$$

- 2. Model update:


$$
m ℓ +1 j = m ℓ j + δ m ℓ j , for j = 1 , 2 , . . . , N e , (6.25)
$$

where

$$
δ m ℓ +1 j = - C 1/2 s ̂ ∆ M ℓ V d [ (1 + λ ℓ ) I + Σ 2 d ] - 1 × V ⊤ d ̂ ∆ M ⊤ ℓ U m Σ - 2 m U ⊤ m C - 1/2 s ( m ℓ j - m j ) - C 1/2 s ̂ ∆ M ℓ V d Σ d [ (1 + λ ℓ ) I + Σ 2 d ] - 1 × U ⊤ d C - 1/2 e ( d ℓ j - d obs ,j ) , (6.26)
$$

$$
̂ ∆ M ℓ = C - 1/2 s ∆ M ℓ , (6.27)
$$

and

-   3. Model prediction:

$$
d ℓ +1 j = g ( m ℓ +1 j ) , for j = 1 , 2 , . . . , N e (6.29)
$$

$$
O ℓ +1 N,d = 1 N e N e ∑ j =1 O N,d ( m ℓ +1 j ) (6.30)
$$

- 4. If O   +1 N,d &gt; O   N,d then increase λ   = γλ   . If λ   &gt; λ max stop, else return to step 3.   +1  
- 5. If O N,d ≤ O N,d check the termination criteria. 6. If not terminated then reduce = , set


$$
̂ ∆ D ℓ = C - 1/2 e ∆ D ℓ = U d Σ d V ⊤ d . (6.28)
$$

λ   +1 λ   /γ   =   +1 and return to step 2.

# 6.3 Subspace Iterative Ensemble Smoother

Raanes et al. [354] revisited the EnRML method and proposed a new derivation based on the observation that the solution provided by EnRML can be written as a linear combination of the prior realizations. The resulting method, called the subspace iterative ensemble smoother (SIES), is argued to be simpler both in terms of derivation and implementation than EnRML. Since both methods start from the same premise, they converge to the same solution, except for roundoff errors and specific implementation details such as step size and singular value truncation. Evensen et al. [145] provided a detailed discussion on the implementation of SIES.

The starting point for SIES is to write the vector of model parameters at the   th iteration as a linear combination of the prior realizations as

$$
m ℓ j = m j +∆ Mw ℓ j , (6.31)
$$

where w   j ∈ R N e is the vector containing the coefficients of the linear combination. Note that m j is the j th prior realization and ∆ M contains the prior ensemble variations around the prior mean. The RML objective function can be written in terms of w as

$$
O r ( w ) = 1 2 ( d obs ,j - g ( m j +∆ Mw )) ⊤ C - 1 e ( d obs ,j - g ( m j +∆ Mw )) + 1 2 w ⊤ w , (6.32)
$$

with w ∼ N ( 0 , I ).

Raanes et al. [354] propose to minimize (6.32) using a GN scheme such that

where

$$
w ℓ +1 j = w ℓ j + β ℓ δ w ℓ +1 j (6.33)
$$

$$
w ℓ +1 j = - w ℓ j - ( ˜ G ℓ ∆ M ) ⊤ [ ( ˜ G ℓ ∆ M )( ˜ G ℓ ∆ M ) ⊤ + C e ] - 1 × ( g ( m j +∆ Mw ℓ j ) - d obs ,j - ˜ G ℓ ∆ Mw ℓ j ) . (6.34)
$$

Eq. (6.34) requires to compute the sensitivity matrix   G   , which can estimated using the pseudo-inverse of ∆ M   . Note that   G   always appear multiplied by ∆ M in Eq. (6.34), hence

$$
˜ G ℓ ∆ M = ∆ D ℓ ∆ M + ℓ ∆ M . (6.35)
$$

  Instead of computing ∆ M +   , Raanes et al. [354] noted that

$$
∆ M ℓ = M ℓ A = ( M +∆ MW ℓ ) A = ∆ M ( I + W ℓ A ) , (6.36)
$$

where M and W are the matrices containing the realizations of m and w in their columns. The matrix ( I + W   A ) is positive definite and we can write

$$
∆ M = ∆ M ℓ ( I + W ℓ A ) - 1 (6.37)
$$

$$
˜ G ℓ ∆ M = ∆ D ℓ ∆ M + ℓ ∆ M ℓ ( I + W ℓ A ) - 1 . (6.38)
$$

  Raanes et al. [354] noted that if the forward model is linear, d = Gm , Eq. (6.38) simplifies to

$$
˜ G ℓ ∆ M = ∆ D ℓ ∆ M + ℓ ∆ M ℓ ( I + W ℓ A ) - 1 = G ∆ M ℓ ∆ M + ℓ ∆ M ℓ ( I + W ℓ A ) - 1 = G ∆ M ℓ ( I + W ℓ A ) - 1 = ∆ D ℓ ( I + W ℓ A ) - 1 . (6.39)
$$

If the forward model in nonlinear, Raanes et al. [354] discuss two situations: First, if N m ≥ N e − 1, then rank(∆ M   ) = N e − 1 and

$$
∆ M + ℓ ∆ M ℓ = I - 1 N e 11 ⊤ . (6.40)
$$

In this case, Eq. (6.38) reduces to

$$
˜ G ℓ ∆ M = ∆ D ℓ ( I + W ℓ A ) - 1 , (6.41)
$$

  which is the same result for the linear case. However, if the forward model is nonlinear and N m &lt; N e − 1, we do not have the simplification obtained in Eq. (6.40). In this case, Raanes et al. [354] propose to use the SVD of ∆ M   and write

$$
∆ M + ℓ ∆ M ℓ = V m Σ + m U ⊤ m U m Σ m V ⊤ m = V m V ⊤ m . (6.42)
$$

Note that we only need the first N m right singular vectors of ∆ M   . In terms of computational implementation. Evensen et al. [145] note that instead of computing ( I + W   A ) − 1 , it is more efficient to solve the linear problem

$$
( I + W ℓ A ) ˜ G ℓ ∆ M = ∆ D ℓ , (6.43)
$$

Pseudo-code 6.2 summarizes the SIES method. This pseudo-code requires the specification of an initial step size, β 0 ≤ 1, a minimum step size β min &gt; 0, and a reduction factor γ &lt; 1. For linear problems, the method converges in one iteration with β 0 = 1. For nonlinear problems, however, it may be beneficial to use smaller step sizes. Evensen [142] suggest β 0 = 0 . 6, but this may vary depending on the problem. Pseudo-code 6.2 includes a heuristic to decrease the step size whenever an iteration fails to reduce the average datamismatch objective function. A reasonable choice for the reduction factor is γ = 0 . 5. A minimal value for the step size, such as β min = 0 . 01, is introduced to avoid unnecessary executions of the forward model in case of a nondecreasing search direction. The iterative process stops when β   &lt; β min , the maximum number of iterations is reached, or when a small reduction in the objective function or a small update in the models over an iteration is observed.

The SIES method operates in the ensemble subspace, meaning that the data assimilation parameters are the coefficients in the vectors w . This approach enables an efficient implementation that scales linearly with the number of data points, N d , and model parameters, N m . However, it complicates the application of standard Schur-product localization (see Chapter 7, Section 7.5). As a solution, a domain localization scheme can be employed (Chapter 7, Section 7.5.5).

- 1. Initialization: generate the initial ensemble,   m 0 j   N e j =1 , by sampling the prior distribution of parameters, select the values for β 0 , β min , and γ , set   = 0 and W 0 = O , and compute:

$$
d obs ,j = d obs + C 1/2 e z j , where z j ∼ N ( 0 , I ) (6.44)
$$

$$
d 0 j = g ( m j +∆ Mw 0 j ) , for j = 1 , 2 , . . . , N e (6.45)
$$

$$
O 0 N,d = 1 N e N e ∑ j =1 O N,d ( w 0 j ) (6.46)
$$

- 2. Compute   G   ∆ M by solving one of the following cases:


• If N m &lt; N e − 1:

$$
( I + W ℓ A ) ˜ G ℓ ∆ M = ∆ D ℓ V m V ⊤ m (6.47)
$$

where

• If N m ≥ N e − 1:

$$
∆ M ℓ = U m Σ m V ⊤ m (6.48)
$$

$$
( I + W ℓ A ) ˜ G ℓ ∆ M = ∆ D ℓ (6.49)
$$

3. Model update:

where

$$
w ℓ +1 j = w ℓ j + β ℓ δ w ℓ +1 j (6.50)
$$

$$
w ℓ +1 j = - w ℓ j - ( ˜ G ℓ ∆ M ) ⊤ [ ( ˜ G ℓ ∆ M )( ˜ G ℓ ∆ M ) ⊤ + C e ] - 1 × ( g ( m j +∆ Mw ℓ j ) - d obs ,j - ˜ G ℓ ∆ Mw ℓ j ) . (6.51)
$$

- 4. Model prediction:

$$
d ℓ +1 j = g ( m j +∆ Mw ℓ +1 j ) , for j = 1 , 2 , . . . , N e (6.52)
$$

$$
O ℓ +1 N,d = 1 N e N e ∑ j =1 O N,d ( w ℓ +1 j ) (6.53)
$$

- 5. If O   +1 N,d &gt; O   N,d then reduce β   = γβ   . If β   &lt; β min stop, else return to step 3.   +1  
- 6. If O N,d ≤ O N,d check the termination criteria. 7. If not terminated, increase = min 1


β   +1 { ,β   /γ } , set   =   + 1, and return to step 2.

This page is proof that less is more.

![](<ensemble_data_assimilation_e-book_version_images/imageFile73.png>)

7

# Sampling Errors and Rank Deficiency

Abstract: This chapter addresses the challenges posed by limited-sized ensembles, including sampling errors and restricted degrees of freedom. It also examines strategies to mitigate their adverse effects, with a particular emphasis on the method known as localization.

# 7.1 Introduction

The use of ensembles to estimate covariances is one of the primary reasons for the widespread adoption of ensemble methods across various fields. Ensembles allow handling nonlinear problems while avoiding complex derivative calculations, enabling seamless integration with sophisticated forward models at a reasonable computational cost. Furthermore, since these methods can be formulated within a Bayesian framework, posterior ensembles can be used to estimate the uncertainty in future performance predictions.

Unfortunately, the use of ensembles is also the “Achilles heel” of these methods. The computational demands of large-scale problems require limiting the ensemble size to a few hundred components, which degrades data assimilation performance, leading to two primary issues:

-  Rank deficiency: This limits the number of degrees of freedom available to assimilate data.
-  Spurious correlations: These lead to poor estimates of covariances, resulting in erroneous model updates.


The repercussions of these problems are often observed as incorrect updates in the models and excessive reduction in the ensemble variance [3]. In extreme cases, they can lead to the collapse of the ensemble, rendering the methods incapable of assimilating further data.

This chapter discusses the challenges posed by using limited-sized ensembles and explores strategies to mitigate their negative effects. In particular, it focuses on the method known as localization.

# Remark 7.1: Uncertainty Underestimation

Ensemble methods typically perform well in generating conditional realizations with satisfactory data matches. However, numerous studies have consistently reported excessive reductions in ensemble variability and overly narrow prediction ranges, limiting their effectiveness in uncertainty quantification [77, 130, 118, 119, 245, 277].

Uncertainty underestimation in ensemble methods is often attributed to sampling errors resulting from the limited ensemble size. However, other factors may contribute, including poorly characterized prior uncertainties, insufficient parametrization, underestimation of data uncertainties, and overconfidence in the model’s ability to accurately simulate the system behavior.

# 7.2 Rank Deficiency

One of the most severe consequences of the ensemble sizes used in practice is the limitation of degrees of freedom available for assimilating data. To understand this, it is convenient to review the ES analysis equation:

$$
m c ,j = m j + ˜ C md ( ˜ C dd + C e ) - 1 ( d obs ,j - d j ) , (7.1)
$$

for j = 1 , 2 ,...,N e , where d j = g ( m j ). Note that after computing the N d × N d matrix     C dd + C e   , we can solve the linear problem

$$
≡ ( ˜ C dd + C e ) x j = ( d obs ,j - d j ) (7.2)
$$

for the vector x j . Then, the analysis equation can be written as

$$
m c ,j = m j + ˜ C md x j = m j + 1 N e - 1 N e ∑ k =1 ( m k - m ) θ jk ︷ ︸︸ ︷ ( d k - d ) ⊤ x j = m j + 1 N e - 1 N e ∑ k =1 θ jk ( m k - m ) . (7.3)
$$

The vector m is itself represented by a linear combination of the set of prior state vectors, m j . Thus, it follows that we can write m c ,j as

$$
m c ,j = N e ∑ k =1 γ jk m k for j = 1 , 2 , . . . N e , (7.4)
$$

where the γ jk ’s are real numbers. This result shows that the j th analyzed state, m c ,j , in the ES is a linear combination of the set of N e prior vectors, m k . This means that we effectively have at most N e coefficients, { γ j } N e k =1 , that can be adjusted to match the observed data. In other words, { m k } N e k =1 defines a subspace of R N m , with dimension R N e , in which we can generate estimates. The same conclusion holds for EnKF, ES-MDA, and other ensemble methods.

Another way to look at this issue is to investigate the rank of the ensemble-based covariance matrix.

$$
C md ≈ ˜ C md = 1 N e - 1 N e ∑ j =1 ( m j - m )( d j - d ) ⊤ = ∆ M ∆ D ⊤ . (7.5)
$$

Note that ∆ M is a N m × N e matrix computed by subtracting the ensemble mean from each of its columns. Thus, rank(∆ M ) ≤ min { N m ,N e − 1 } . Typically, N e   N m , meaning that rank(∆ M ) ≤ N e − 1. A similar conclusion holds for ∆ D . Hence, rank(   C md ) ≤ N e − 1. Moreover, Lorenc [270] showed that the assimilation of a perfect datum

results in a loss of rank, effectively removing one degree of freedom. While we never assimilate perfect data, it is reasonable to expect that, after assimilating several data points, there will be a reduction in the available degrees of freedom.

# 7.2.1 Example: Porosity and Permeability of a Rock Sample

The loss of rank is straightforward to illustrate. For instance, consider the problem of estimating porosity and permeability in a core sample introduced in Section 2.3.1.3. We showed that the posterior covariance after assimilation of one observation of porosity is given by

$$
C m c = C m - C m G ⊤ ( C e + GC m G ⊤ ) - 1 GC m = ⎡ ⎢ ⎣ σ 2 φ ( 1 - σ 2 φ σ 2 e + σ 2 φ ) ρσ φ σ ln κ ( 1 - σ 2 φ σ 2 e + σ 2 φ ) ρσ φ σ ln κ ( 1 - σ 2 φ σ 2 e + σ 2 φ ) σ 2 ln κ ( 1 - ρ 2 σ 2 φ σ 2 e + σ 2 φ ) ⎤ ⎥ ⎦ . (7.6)
$$

Now, if we have a perfect measurement of porosity, i.e, σ e = 0, then C m c becomes 0 0

$$
C m c = [ 0 0 0 σ 2 ln κ ( 1 - ρ 2 ) ] , (7.7)
$$

which is singular. Therefore, assimilation of a perfect datum reduced the rank of the posterior covariance, now rank( C m c ) = 1.

# 7.3 Spurious Correlations

The second adverse effect of the limited ensemble size is its potential to yield inaccurate estimates of the covariances used in the computation of the Kalman gain. In this scenario, the estimated covariance matrices are prone to spurious correlations 1 , leading to erroneous updates in the ensemble members. Consequently, we observe changes in model parameters which have no influence on the assimilated data, exacerbating problems of excessive loss of ensemble variance 2 .

# 7.3.1 Example: Porosity and Permeability of a Rock Sample

To illustrate the impact of sampling errors, let’s revisit the problem of estimating porosity and permeability in a core sample. However, let’s assume that there are no prior correlations between porosity and permeability. In this case, the prior covariance takes the form:

1 There is well-known result in random matrix theory [25] that states if x j ’s are independent and identically distributed samples from N ( 0 , C x ), the error in covariance estimation with an ensemble of N e samples is

$$
‖ C x - ˜ C x ‖ = O (√ N x N e ) .
$$

This means that the estimated covariance   C x is very inaccurate in high dimensions for small ensembles, i.e., N e   N x . 2

Model nonlinearity also exacerbates the effect of sampling errors, as illustrated by Raanes et al. [353] in a compelling example involving a univariate problem with a Gaussian prior and two models—one linear and the other nonlinear. Despite the strong nonlinearity, the nonlinear model was designed to produce the exact same posterior Gaussian PDF as the linear case. Data were assimilated using a square root filter with an ensemble of 40 members. For the linear case, sampling errors were quickly attenuated, and the ensemble statistics converged to the exact values. However, in the nonlinear case, the sampling errors persisted, demonstrating a chronic issue.

$$
C m = [ σ 2 φ 0 0 σ 2 ln κ ] . (7.8)
$$

If we assimilate a single measurement of porosity, d obs = φ obs and C e = σ 2 e , it results in the following expression for the posterior covariance

$$
C m c = C m - C m G ⊤ ( C e + GC m G ⊤ ) - 1 GC m = [ σ 2 φ - σ 4 φ σ 2 e + σ 2 φ 0 0 σ 2 ln κ ] . (7.9)
$$

Because there is no prior correlation between φ and ln κ , one observation of φ does not reduce the variance of ln κ , which means no uncertainty reduction in our estimate of ln κ .

Now, let’s consider that the prior covariance is estimated by an ensemble. Due to sampling errors, a spurious correlation may be introduced between φ and ln κ . For instance, if we sample φ and ln κ independently and compute the correlation coefficient, it can result in spurious correlations, as illustrated in Fig. 7.1.

![](<ensemble_data_assimilation_e-book_version_images/imageFile74.png>)

10

10

10

8

8

8

Log-permeability

Log-permeability

Log-permeability

6

6

6

4

4

4

2

2

2

= 

10 0.286

N e =  =

100 0.088

N e =  =

1000 0.008

N e  =







=

0.286

= 0.088

= 0.008

0 0

0 0

0 0

0

0.1

0.2 Porosity

0.3

0.4

0

0.1

0.2 Porosity

0.3

0.4

0

0.1

0.2 Porosity

0.3

0.4

Porosity

Porosity

Porosity

INTERNA

INTERNA

INTERNA INTERNA Fig. 7.1: Example showing spurious correlations between φ and ln κ . Note that the correlation coefficient vanishes as we increase the size of the ensemble.

For concreteness, let us assume that the prior covariance estimated from the ensemble includes a small spurious cross-covariance c ε . Also, assume that | c ε | &lt; σ φ σ ln κ . 2

$$
˜ C m = [ σ 2 φ c ε c ε σ 2 ln κ ] . (7.10)
$$

The posterior covariance becomes

$$
˜ C m c = ⎡ ⎢ ⎣ σ 2 φ - σ 4 φ σ 2 e + σ 2 φ c ε - c ε σ 2 φ σ 2 e + σ 2 φ c ε - c ε σ 2 φ σ 2 e + σ 2 φ σ 2 ln κ - c 2 ε σ 2 e + σ 2 φ ⎤ ⎥ ⎦ . (7.11)
$$

Therefore, the variance of ln κ is reduced regardless of the sign of c ε , indicating that the uncertainty in ln κ is underestimated. Additionally, the mean is also altered. This effect diminishes as the ensemble size increases, since c ε → 0 as N e → ∞ . We can extend this example 3 and assume that there is an actual correla-

tion between φ and ln κ so that

$$
C m = [ σ 2 φ ρσ φ σ ln κ ρσ φ σ ln κ σ 2 ln κ ] . (7.12)
$$

But suppose, once again, that instead of C m , we have an inaccurate version,   C m , where the variances are correct but the cross-covariances are corrupted with additive sampling errors

$$
˜ C m = [ σ 2 φ ρσ φ σ ln κ + c ε ρσ φ σ ln κ + c ε σ 2 ln κ ] . (7.13)
$$

We already showed (Eq. (2.59)) that the posterior mean of ln κ for the case with correct C m is

$$
(ln κ ) map = (ln κ ) pr + ρσ φ σ ln κ σ 2 φ + σ 2 e ( φ obs - φ pr ) . (7.14)
$$

The corresponding value for the corrupted covariance is

$$
˜ (ln κ ) map = (ln κ ) pr + ( ρσ φ σ ln κ + c ε σ 2 φ + σ 2 e ) ( φ obs - φ pr ) . (7.15)
$$

We want to analyze the error in the estimate of ln κ .

$$
ln κ - ˜ (ln κ ) map = ln κ - (ln κ ) pr - ( ρσ φ σ ln κ + c ε σ 2 φ + σ 2 e ) ( φ + e φ - φ pr ) , (7.16)
$$

where we wrote φ obs = φ + e φ with e φ ∼ N (0 ,σ 2 e ). The error variance becomes

3 This extension is inspired in the discussion presented in [183] and [245].

$$
E [ ( ln κ - ˜ (ln κ ) map ) 2 ] = = E ⎡ ⎣ ( (ln κ - (ln κ ) pr ) - ( ρσ φ σ ln κ + c ε σ 2 φ + σ 2 e ) (( φ - φ pr ) + e φ ) ) 2 ⎤ ⎦ = E [ (ln κ - (ln κ ) pr ) 2 ] ︸ ︷︷ ︸ = σ 2 ln κ - 2 ( ρσ φ σ ln κ + c ε ) σ 2 φ + σ 2 e E [(ln κ - (ln κ ) pr ) ( φ - φ pr )] ︸ ︷︷ ︸ = c ln κ,φ = ρσ φ σ ln κ - 2 ( ρσ φ σ ln κ + c ε ) σ 2 φ + σ 2 e E [(ln κ - (ln κ ) pr ) e φ ] ︸ ︷︷ ︸ =0 + ( ρσ φ σ ln κ + c ε σ 2 φ + σ 2 e ) 2 E [ ( φ - φ pr ) 2 ] ︸ ︷︷ ︸ = σ 2 φ +2 ( ρσ φ σ ln κ + c ε σ 2 φ + σ 2 e ) 2 E [( φ - φ pr ) e φ ] ︸ ︷︷ ︸ =0 + ( ρσ φ σ ln κ + c ε σ 2 φ + σ 2 e ) 2 E [ e 2 φ ] ︸ ︷︷ ︸ = σ 2 e = σ 2 ln κ - 2 ( ρσ φ σ ln κ + c ε ) σ 2 φ + σ 2 e ρσ φ σ ln κ + ( ρσ φ σ ln κ + c ε σ 2 φ + σ 2 e ) 2 ( σ 2 φ + σ 2 e ) = σ 2 ln κ - ρ 2 σ 2 φ σ 2 ln κ σ 2 φ + σ 2 e + c 2 ε σ 2 φ + σ 2 e . (7.17)
$$

The last equality can be written as

$$
E [ ( ln κ - ˜ (ln κ ) map ) 2 ] = σ 2 ln κ - ρ 2 σ 2 φ σ 2 ln κ σ 2 φ + σ 2 e ( 1 - ( c ε ρσ φ σ ln κ ) 2 ) . (7.18)
$$

Hamill et al. [183] interpreted the term c ε ρσ φ σ ln κ as a “relative error” in the covariance. From Eq. (7.18), we can highlight two points: (i) if   c ε ρσ φ σ ln κ   &gt; 1, the variance of ln κ increases by assimilating data, which is clearly inconsistent. There is a degradation in the estimate of ln κ due to data assimilation. (ii) If the actual correlation coefficient between φ and ln κ is small, there is a higher likelihood of degradation in the estimates due to sampling error.

The second point is particularly significant because weak correlations are more challenging to estimate with limited samples. Lacerda et al. [245] illustrated this aspect by conducting a small numerical experiment to estimate the correlation coefficient between two parameters, φ and ln κ , based on an ensemble of N e = 50 members. They considered two cases where the true correlations are ρ = 0 and ρ = 0 . 8, and repeated the sampling 100 times. Fig. 7.2 shows the histograms of the estimates of ρ , indicating a large standard deviation for the case with ρ = 0.

![](<ensemble_data_assimilation_e-book_version_images/imageFile75.png>)

0.6

0.5

 =

0 (std. dev. = 0.157)

Relative Frequency

 =

0.8 (std. dev. = 0.040)

0.4

0.3

0.2

0.1

0

-0.5

-0.3

0.0

0.2

0.4

0.6

0.8

Correlation Coefficient

INTERNA Fig. 7.2: Histograms of the estimated correlation coefficient for two cases: uncorrelated variables ( ρ = 0 ) and strongly correlated variables ( ρ = 0 . 8 ). Reproduced from Lacerda et al. [245] with permission from Elsevier.

# 7.3.2 Example: Porosity Distribution in a Core Sample

Recall the problem introduced in Section 2.3.1.4. In Fig. 4.5, the EnKF results for 100 members were presented. Now, we investigate the same problem using EnKF with N e = 10. Fig. 7.3 shows the data assimilation results for each of the 10 data points. It can be observed that the ensemble was able to match most data points, albeit with a significant reduction in ensemble variability. However, at the last datum, it is possible to note an overcorrection in the values of porosity. This essentially happens because the ensemble variance becomes so small that the inversion becomes unstable.

# 7.4 Covariance Inflation

One ad hoc strategy to compensate for the excessive reduction in ensemble variance is known as covariance inflation [15]. In covariance inflation, we replace the forecast ensemble by

$$
y n,f inf ,j = γ ( y n,f j - y n,f ) + y n,f for j = 1 , 2 , · · · , N e , (7.19)
$$

where γ is the inflation factor, a number slightly greater than one, say γ = 1 . 05.

Note that Eq. (7.19) increases the variance but does not change the mean of y n,f . The optimal inflation factor is problem-dependent. There are several methods in the literature to compute the inflation coefficient; see, e.g., Raanes et al. [353] and references therein. Covariance inflation finds common use in oceanography and numerical weather prediction applications, particularly in the context of sequential data assimilation. However, it has







![](<ensemble_data_assimilation_e-book_version_images/imageFile76.png>)











































 

  

  

�





��



��

�





��



��

�





��





  U GE RF 

  U GE RF 

  U GE RF 

(a)

Prior

(b)

1st datum

(c)

2nd datum

















































 

  

 

�





��



��

�





��





�





��





  U GE RF 

  U GE RF 

  U GE RF 

(d)

3rd datum

(e)

4th datum

(f)

5th datum

















































 

 

 

�





��





�





��





�





��





  U GE RF 

  U GE RF 

  U GE RF 

(g)

6th datum

(h)

7th datum

(i)

8th datum

































 

 

�





��





�





��





  U GE RF 

  U GE RF 

(j)

9th datum

(k)

10th datum

Fig. 7.3: EnKF sampling with N e = 10 for porosity in a core sample. The solid red line represents the ground truth. The red circles represent the observed data points. The gray lines represent samples obtained by EnKF for different numbers of observations. The dashed lines represent the ensemble mean. Example 7.3.2.

# 7.5 Localization

Localization [197] is another ad hoc procedure employed to mitigate the negative effects of small ensembles. Typically, localization assumes that the covariances between model parameters and data are a function of distance. In its simplest form, localization aims to restrict the influence of a component of the innovation vector (data mismatch term) to a region around the data location. Localization is highly effective, simple to implement, and computationally inexpensive. However, determining the appropriate localization region depends on the specific problem.

The ES-MDA analysis with covariance localization can be expressed as:

$$
m ℓ +1 j = m ℓ j + ( R md ◦ ˜ C ℓ md )( R dd ◦ ˜ C ℓ dd + α ℓ +1 C e ) - 1 × ( d ℓ obs ,j - g ( m ℓ j )) . (7.20)
$$

Here, R md and R dd are the localization matrices with dimensions N m × N d and N d × N d , respectively. The symbol “ ◦ ” denotes the Schur or Hadamard product, which represents the element-wise product of the components of the matrices (see Remark 7.2).

Often, instead of “localizing” the matrices   C   md and   C   dd , we apply the Schur product directly to the Kalman gain, in which case the ES-MDA analysis can be expressed as:

$$
m ℓ +1 j = m ℓ j + ( R md ◦ ˜ K ℓ ) ( d ℓ obs ,j - g ( m ℓ j )) (7.21)
$$

where

$$
˜ K ℓ = ˜ C ℓ md ( ˜ C ℓ dd + α ℓ +1 C e ) - 1 . (7.22)
$$

Covariance and Kalman gain localization appear to yield similar results [126]. However, Kalman gain localization offers some advantages in terms of computational implementation; in particular, Kalman gain localization allows the use of subspace inversion, as discussed in Chapter 8.

# Remark 7.2: Schur (Hadamard) Product

Let A and B be N 1 × N 2 matrices. The Schur product of A and B , denoted by A ◦ B , is defined by the element-by-element product

$$
[ A ◦ B ] ij = A ij B ij (7.23)
$$

where A ij and B ij are the ( i,j ) entry of the matrices A and B , respectively. Note that A and B must be of same size but not necessarily square.

Schur Product Theorem: if the matrix A is positive definite and the matrix B is positive semidefinite with all of its main diagonal entries positive, then the product A ◦ B is positive definite [196].

# 7.5.1 Spurious Correlation

The original motivation behind localization is to eliminate or minimize the presence of spurious values resulting from sampling errors in the estimates of covariances and/or Kalman gain. Initially, localization was conceptualized as a cut-off radius, where only data within the radius were considered for computing the Kalman gain [197]. However, this method could lead to discontinuities in the estimates. To address this issue, Houtekamer and Mitchell [198] proposed using the Schur product with a localization matrix computed with a smooth correlation function. This alternative has proven to be more effective than a simple cut-off radius because it acts as a regularization strategy for the covariance/Kalman gain estimates.

Fig. 7.4 illustrates the effect of localization on covariance estimates. Panel (a) displays covariance values estimated with ensembles of 50, 100, and 1,000 samples. For comparison, the actual covariance computed with a spherical covariance function is included in each plot. Notice that while the covariance estimates tend to capture regions with higher covariance, they fail to vanish at positions with zero covariance. Increasing the size of the ensemble improves the estimates, but a considerable amount of spurious covariance values persists even for N e = 1,000. Panel (b) shows the correlation function used to taper (localize) the covariance estimates. Panel (c) displays the covariance estimates after applying the Schur product with the correlation function, demonstrating significant improvement in the estimated covariance values.

1

0.8

0.6

0.2 0.4 0.6 Covariance

0.4

0.2

0

-0.2

-0.4 0

0

25

50

50 Position

(a)

C m

m

 

75

1

0.8

0.6

0.2 0.4 0.6 Covariance

0.4

0.2

0

-0.2

100

-0.4 0

0

25

50

50 Position

(b)

R

75

100

1

0.8

0.6

0.2 0.4 0.6 Covariance

0.4

0.2

0

- 0.2
- 0.4 0


0

![](<ensemble_data_assimilation_e-book_version_images/imageFile31.png>)

25

50

50 Position

(c)

R ◦

C m

◦

m

 

75

100

Fig. 7.4: Illustration of the effect of localization in removing spurious correlations. (a) Covariance estimates with ensembles of 50, 100, and 1,000 samples. (b) Gaspari-Cohn correlation function used to taper the covariance estimates. (c) Covariance estimates after localization.

# 7.5.2 Degrees of Freedom

As discussed in Section 7.2, rank(   C m ) ≤ { N m ,N e − 1 } . However, this matrix is at least positive semidefinite 4 with positive values on the diagonal. Consequently, when we select a positive definite localization matrix R , the localized version, R ◦   C m , becomes full-rank (due to the Schur product theorem). This implies that localization enables the model update to be derived from a significantly larger space compared to the one spanned by the ensemble.

4 To show that   C m is at least positive semidefinite, suffices to show that x     C m x ≥ 0 for any vector x (see Appendix A, Section A.2). Note that   C m = ∆ M ∆ M   . Hence

$$
x ⊤ ˜ C m x = (∆ Mx ) ⊤ (∆ Mx ) = ‖ ∆ Mx ‖ 2 2 ≥ 0 . (7.24)
$$

Fig. 7.5 demonstrates the impact of the Schur product on increasing the rank of a 1,000 × 1,000 covariance matrix. In Fig. 7.5a, the number of non-zero singular values is constrained by the ensemble size. However, after applying the Schur product with a positive definite localization matrix, the number of non-zero singular values becomes 1,000, regardless of the ensemble size.

![](<ensemble_data_assimilation_e-book_version_images/imageFile78.png>)

100

100

100

100

50

50

10

10

25

25

Singular value

Singular value

10

10

1

1

100

0.1 100 Singular value

10

0.1

0.1

1

0.01

0.01

0

0

50

100

50 100 Number of singular values

0.001 0

0.001 0

0

200 Number

400

600

800

1000

0

200 Number

400

600

800

1000

of singular values

of singular values

(a)

(b)

C m

R ◦

C m

◦

m

m

 

 

INTERNA

INTERNA

#

#

Fig. 7.5: Singular values of a covariance matrix estimated by ensembles, shown before (a) and after (b) applying the Schur product with a positive definite localization matrix. The legend indicates the ensemble sizes.

Another perspective on the impact of localization is to examine the effect of the Schur product in updating each component of m . Previously, we demonstrated that m c ,j for ES without localization is a linear combination of the N e prior vectors, m j . Following the same procedure for the case with Kalman gain localization, we obtain:

$$
m c ,j = m j + ( R md ◦ ˜ K ) ( d obs ,j - g ( m j )) = m j + ( R md ◦ ˜ K ) δ d j = m j + N d ∑ k =1 ( R md k ◦ ˜ K k ) δd jk , (7.25)
$$

where R md k and   K k denote the k th columns of the localization matrix and Kalman gain, respectively. Now let’s examine the update equation for the i th entry of m j , denoted by m ij :

$$
m c ,ij = m ij + N d ∑ k =1 ˜ K ik θ ijk ︷ ︸︸ ︷ r ik δd jk = m ij + N d ∑ k =1 θ ijk ˜ K ik , (7.26)
$$

where i = 1 ,...,N m . r ik is the ( i,k ) entry of the localization matrix R md , corresponding to the localization coefficient between the i th model parameter and the k th observation. This result shows that for each i , we have a different set of coefficients θ ijk ’s. Therefore, each component of m j is updated with a different linear combination of the columns of   K . Thus, localization expands the degrees of freedom to assimilate data.

# 7.5.3 Distance-Based Localization

In distance-based localization, the localization matrix R md used in the Schur product is computed based on the distance between model parameters and observation locations. Essentially, the localization coefficients assign weights to covariance values based on their spatial separation: closer points receive higher weights, while distant points receive lower weights. A common choice is to use the fifth-order compact correlation function proposed by Gaspari and Cohn [162] (Fig. 7.6) to compute the entries of R md . The Gaspari-Cohn correlation function can be expressed as:

$$
r ( h ) = ⎧ ⎪ ⎪ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ - 1 4 ( h L ) 5 + 1 2 ( h L ) 4 + 5 8 ( h L ) 3 - 5 3 ( h L ) 2 +1 0 ≤ h ≤ L 1 12 ( h L ) 5 - 1 2 ( h L ) 4 + 5 8 ( h L ) 3 + 5 3 ( h L ) 2 - 5 ( h L ) +4 - 2 3 ( h L ) - 1 L ≤ h ≤ 2 L 0 h > 2 L, (7.27)
$$

where h is the spatial distance and L is known as the critical length.

Another function often adopted for computing localization coefficients is the Furrer-Bengtsson pseudo-optimal taper [156]:

$$
r ( h ) = 1 1 + (1 + C (0) 2 / C ( h ) 2 ) /N e , (7.28)
$$

where C ( h ) is a covariance function with compact support. Eq. (7.28) indicates that the strength of localization depends on the ensemble size, with the localization coefficients approaching one as the ensemble size tends to infinity.

In some situations, it may be desirable to use different critical lengths in different directions. This can be achieved by defining an ellipsoid with

1

0.8

0.6

0.4

0.2

Spherical

Exponential

Gaussian

Gaspari‐Cohn

-

Cohn

Exponential

Furrer‐Bengtsson

+ (Ne =

100)

Exponential

(Ne

=

100)

0

0

0.5

![](<ensemble_data_assimilation_e-book_version_images/imageFile32.png>)

1

1.5

2

INTERNA Fig. 7.6: Correlation functions frequently utilized in reservoir data assimilation. The dashed red curve represents the Furrer-Bengtsson taper with C ( h ) computed with an exponential correlation function and an ensemble with N e = 100.

$$
h L = √ ( ∆ x ′ L x ) 2 + ( ∆ y ′ L y ) 2 + ( ∆ z ′ L z ) 2 , (7.29)
$$

$$
⎡ ⎣ ∆ x ′ ∆ y ′ ∆ z ′ ⎤ ⎦ = ⎡ ⎣ cos θ - sin θ 0 sin θ cos θ 0 0 0 1 ⎤ ⎦ ⎡ ⎣ ∆ x ∆ y ∆ z ⎤ ⎦ . (7.30)
$$

![](<ensemble_data_assimilation_e-book_version_images/imageFile33.png>)

PÚBLICA Fig.

7.7: Localization ellipsoid in the x − y plane.

5 Appendix C, Section C.4.3 shows the equations for an ellipsoid rotated in the 3D space.

# 7.5.3.1 Example: Distance-Based Localization of the Kalman Gain

To illustrate the impact of distance-based localization on the Kalman gain, we examine a 2D reservoir model consisting of a grid of 60 × 60 blocks, operated with 16 oil-producing wells and nine water injection wells arranged in nine five-spot patterns. Figs. 7.8c and 7.8f show the Kalman gain values estimated from an ensemble of 100 permeability realizations for a datum of water cut and a datum of water injection rate for two wells, whose positions are highlighted in white. In both cases, large Kalman gain values are observed around the respective wells. However, especially in the water cut case, significant Kalman gain values are also observed in other regions of the model, far from the observation locations. For both cases, localization coefficients were computed using the Gaspari-Cohn function, with the main anisotropic direction aligned with the primary continuity direction in the permeability field (Figs. 7.8a and 7.8b). Figs. 7.8d and 7.8g show the corresponding Kalman gain estimates after applying localization. For comparison, we also computed the Kalman gain estimates with an ensemble of 5,000 realizations (Figs. 7.8e and 7.8h). Clearly, localization improved the Kalman gain estimates by removing spurious values away from the observation locations. However, comparing Fig. 7.8d with Fig. 7.8e, we observe that localization did not improve the Kalman gain estimate in the region connecting the injector and producer wells.

# 7.5.3.2 Example: Porosity Distribution in a Core Sample

Fig. 7.9 compares the data assimilation results for the example of porosity in a core sample (Example 7.3.2) with three different configurations: N e = 100, N e = 10, and N e = 10 with distance-based localization. Clearly, localization led to significant improvements in the final estimates. It is notable that the ensemble mean is reasonably close to the mean estimate with a larger ensemble. Moreover, we still observe relevant variability in the posterior realizations. Additionally, we no longer observe overcorrection in the porosity estimates.

# 7.5.3.3 Example: Field Data Assimilation without Localization

Fig. 7.10 shows the predicted data for two wells is an oilfield obtained by assimilating data with ES-MDA, with and without localization [118]. These results illustrate that ES-MDA without localization was still able to reasonably match the data, although it resulted in considerably lower variability in the predictions compared to the case using localization. Fig. 7.11 presents the final permeability fields. Here, it is evident that in the absence of localization, the values of permeability were driven to the minimum and maximum limits (truncated at 1 mD and 5,000 mD, respectively). Another interesting

1.0

0.8

0.6

0.4

0.2

1.0

1.0 1.0

0.8

0.8 0.8

0.6

0.6 0.6

0.4

0.4 0.4

0.2

0.2 0.2

(a)

Localization (water cut)

cut)

0.0

(b)

Localization (water injection)

injection)

0.0

0.0 0.0

(c) (

Kalman gain = 100)

N

100)

=

e

e

(f) (

Kalman gain = 100)

N

100)

=

e

e

0.08

![](<ensemble_data_assimilation_e-book_version_images/imageFile34.png>)

0.06

0.04

0.02

0.00

0.02

(d)

Kalman gain after localization ( = 100)

N

100)

=

e

e

1e 5

5

4.0

3.5

3.0

2.5

2.0

1.5

1.0

0.5

0.0

(g)

Kalman gain after localization ( = 100)

N

100)

=

e

e

0.08

0.06

0.04

0.02

0.00

0.02

(e) (

Kalman gain = 5,000)

N

5,000)

=

e

e

3.5

3.0

2.5

2.0

1.5

1.0

0.5

0.0

(h) (

Kalman gain = 5,000)

N

5,000)

=

e

e

0.08

0.08 0.08

0.06

0.06 0.06

0.04

0.04 0.04

0.02

0.02 0.02

0.00

0.00 0.00

0.02

0.02 0.02

1e 5  

5

-

3.5

3.5

3.5 3.5

3.0

3.0 3.0

2.5

2.5 2.5

2.0

2.0 2.0

1.5

1.5 1.5

1.0

1.0 1.0

0.5

0.5 0.5

0.0

0.0 0.0

Fig. 7.8: Example illustrating the impact of distance-based localization on the Kalman gain. Panels (a) and (b) display localization values computed with the Gaspari-Cohn correlation function. Panels (c)–(e) display the Kalman gain estimates for water-cut data, while panels (f)–(h) show the estimates for water injection rate. Black dots represent the locations of production wells, and triangles indicate the positions of water injectors. White wells correspond to those where the Kalman calculation is performed. Example 7.5.3.1. .

.





![](<ensemble_data_assimilation_e-book_version_images/imageFile82.png>)





























 

 

�











�











 U GE RF 

 U GE RF 

(a)

100

(b)

10

=

=

N e

N e

e

e

















 

�











 U GE RF 

(c)

10 with localization

=

N e

e

Fig. 7.9: Comparison of EnKF sampling with N e = 100, N e = 10 and N e = 10 with localization for porosity in a core sample. The solid red line represents the ground truth. The red circles represent the observed data points. The gray lines represent samples obtained by EnKF for different numbers of observations. The dashed lines represent the ensemble mean. Example 7.5.3.2

observation is that Figs. 7.11e and 7.11f are almost identical, indicating a collapse of the ensemble, while the corresponding results with localization exhibit significant variability.

# 7.5.3.4 Selection of the Critical Length

Currently, distance-based localization is the most effective method for mitigating the negative effects of small ensembles. The “optimal” localization function depends on the specific problem, varying with the type of data, parameter, and ensemble size. However, choosing reasonable localization regions is not overly challenging. The Gaspari-Cohn correlation function is widely used, but the critical aspect is selecting the appropriate critical

![](<ensemble_data_assimilation_e-book_version_images/imageFile83.png>)

2000

35000

Bottom-hole Pressure (kPa)

30000

Water Rate (m3/d)

1500

25000

20000

1000

15000

10000

500

5000

0 0

0 0

0

1000

2000

3000

4000

5000

6000

7000

0

1000

2000

3000

4000

5000

6000

7000

3000 4000 Time (days)

3000 4000 Time (days)

(a)

Water rate, localization

(b)

BHP, localization

2000

35000

Bottom-hole Pressure (kPa)

30000

Water Rate (m3/d)

1500

25000

20000

1000

15000

10000

500

5000

0 0

0 0

0

1000

2000

3000

4000

5000

6000

7000

0

1000

2000

3000

4000

5000

6000

7000

3000 4000 Time (days)

3000 4000 Time (days)

(c)

Water rate, no localization

(d)

BHP, no localization

Fig. 7.10: Predicted data for two wells obtained by assimilating data with ES-MDA, with and without localization. Red circles are the observed data, gray lines the prior and blue lines the posterior ensemble. Example 7.5.3.3. Reproduced from Emerick [118] with permission from Elsevier.

Emerick and Reynolds [128] argue that these critical lengths should be determined based on a combination of the data’s sensitive region and the underlying correlation lengths of the geological model. Sensitivity analyses using the adjoint method [467, 259] have shown that each type of data exhibits a unique region of influence. For instance, bottom-hole pressure data from a flowing well are highly sensitive to gridblock permeabilities and porosities near the well, while water-cut data from a producing well are sensitive to porosities and permeabilities along streamlines connecting the producing well to a water injection well. Therefore, it is logical to consider the region of influence of the data when determining the critical lengths for localization. Using a localization region significantly smaller than the actual influence region may lead to disproportionately large local adjustments in model parameters.

(a)

Prior 1

(c)

Post 1, localization

(b)

Prior 200

![](<ensemble_data_assimilation_e-book_version_images/imageFile35.png>)

(d)

Post 200, localization

(e)

Post 1, no localization

(f)

Post 200, no localization

Fig. 7.11: Permeability realizations before (prior) and after data assimilation with ESMDA, with and without localization. Example 7.5.3.3. Reproduced from Emerick [118] with permission from Elsevier.

Additionally, the localization region is influenced by geological structures, such as the covariance functions used in geostatistical modeling. Confining changes in model parameters to a region smaller than that dictated by the geological model’s correlation lengths may introduce alterations that compromise the geological realism of the final ensemble.

# 7.5.4 Non-Distance Dependent Localization

Crucial parameters used in reservoir data assimilation, such as rock property multipliers, relative permeability curves, analytical aquifer parameters, and rock and fluid compressibilities, may lack a direct spatial relationship with observations. Unlike typical reservoir rock properties, which are discretized on the grid, these parameters are usually represented by scalar values with regional or even global impacts on model behavior. We refer to these scalar parameters as “non-local” parameters.

Additionally, we may encounter non-local data. For instance, one might be interested in assimilating indirect measurements such as estimates of the global reservoir pressure or the results of some data reparametrization [280, 281]. In these cases, a non-distance-dependent localization scheme becomes essential 6 .

There are several methods proposed in the literature for constructing localization matrices without relying on the assumption that covariances (or the Kalman gain) are distance-dependent [156, 14, 38, 482, 280, 452]. Lacerda et al. [245] reviewed some of these methods and compared their performance in updating non-local parameters in a synthetic reservoir data assimilation problem. Here, we review two of these methods.

# 7.5.4.1 Furrer-Bengtsson Taper Function

Furrer and Bengtsson [156] derived a localization function for general covariance structures by minimizing the expectation of the Frobenius norm of the difference between a covariance matrix, C , and its localized estimate, R ◦   C :

$$
E [ ‖ C - R ◦ ˜ C ‖ 2 F ] = tr ( C 2 ) - 2 E [ tr ( C ( R ◦ ˜ C ))] + E [ ( R ◦ ˜ C ) 2 ] . (7.31)
$$

6 The term “localization” was introduced by Houtekamer and Mitchell [198] with the concept of restricting the spatial extent of updates to eliminate long-distance correlations. Consequently, for non-local model parameters or data points, the term localization may seem less fitting. Nevertheless, we continue to use the term localization for historical reasons and because it is widely accepted in the literature.

They minimized Eq. (7.31) term-by-term ignoring the positive-definiteness constraint. The resulting expression depends on the true covariance:

$$
r ik = c 2 ik c 2 ik + c 2 ik + c ii c kk N e . (7.32)
$$

Here, r ik denotes the ( i,k )th entry of the localization matrix R and c ik denotes the corresponding covariance value. Furrer and Bengtsson [156] proposed to replace c ik by the ensemble estimate,   c ik , forming a simple and computationally inexpensive non-distance-dependent localization procedure. The authors also suggested that sparseness can be introduced by zeroing small values of c ik , which can be done setting r ik = 0 if

$$
| c ik | √ c ii c kk = | ρ ik | < τ, (7.33)
$$

where τ ≥ 0 is a user-defined threshold. Instead of covariances, Eq. (7.32) can be rewritten in terms correlation coefficients as

$$
r ik = ˜ ρ 2 ik ˜ ρ 2 ik + 1+ ˜ ρ 2 ik N e , (7.34)
$$

  where   ρ ik is the correlation coefficient between the i th model parameter and the k th predicted data, which can be estimated from the current ensemble as

$$
˜ ρ ik = ∑ N e j =1 ( m ij - m i )( g k ( m j ) - g k ( m ) ) √ ∑ N e j =1 ( m ij - m i ) 2 √ ∑ N e j =1 ( g k ( m j ) - g k ( m ) ) 2 . (7.35)
$$

Regrettably, the application of ensemble estimates of covariances in Eq. (7.32) for the estimation of localization coefficients suffers from spurious correlations, leading to a decrease in method effectiveness. This issue is illustrated in Fig. 7.12, which revisits the example presented in Section 7.5.1. In Fig. 7.12a, we observe the localization values calculated with the FurrerBengtsson taper using both true covariances and the covariance values estimated from an ensemble of 50 members. While the method utilizing ensemble estimates manages to identify regions with large actual covariances, it, unfortunately, fails to diminish at distant locations. This failure is a direct consequence of the challenge in estimating small covariance values, as illustrated in the example of Fig. 7.2. Consequently, the estimated covariances after localization were not significantly improved, as indicated in Fig. 7.12b.

1

0.8

0.6

0.2 0.4 0.6 Covariance

0.4

0.2

0

1

0.8

0.6

0.2 0.4 0.6 Covariance

0.4

0.2

0

![](<ensemble_data_assimilation_e-book_version_images/imageFile36.png>)

-0.2

-0.2

-0.4 0

0

25

50

50 Position

(a)

R

75

100

-0.4 0

0

25

50

50 Position

(b)

R ◦

C m

◦

m

 

75

100

Fig. 7.12: Illustration of the Furrer-Bengtsson taper function. (a) Furrer-Bengtsson tapers estimated with the true covariance ( R 1 ) and covariance estimated with 50 ensemble members ( R 2 ). (b) Covariance estimates with N e = 50 after localization. A threshold of τ = 0 . 1 was adopted in the example. Note that the Schur product with R 1 results in a significant improvement of the covariance estimate. However, the true covariances are typically unknown. R 2 , on the other hand, fails to eliminate distant spurious correlations.

# 7.5.4.2 Correlation-Based Localization

Luo et al. [280] proposed a localization approach based on the correlation coefficients estimated from the ensemble. In its simplest form, this method assigns a localization coefficient of one if the absolute value of the corresponding correlation coefficient exceeds a user-defined threshold ( τ ):

$$
r ik = { 1 , if | ˜ ρ ik | > τ 0 , otherwise. (7.36)
$$

One alternative is to select τ proportional to the estimated error in the correlation coefficient, i.e.,

$$
τ = γσ ϵ , (7.37)
$$

where γ ∈ (0 , 3] is a scaling factor, and σ   represents the standard deviation of the error in the correlation coefficient, which can be estimated as [407]:

$$
σ ϵ = 1 - ˜ ρ 2 ik √ N e - 1 . (7.38)
$$

Fig. 7.13 illustrates the localization threshold resulting from Eqs. (7.37) and (7.38) as a function of the estimated correlation coefficient for different ensemble sizes. Smaller values of |   ρ ik | and N e require higher truncation values.

Luo et al. [280] proposed a method for selecting τ for grid-based model parameters. They suggested assuming that the sample correlation can be decomposed as

![](<ensemble_data_assimilation_e-book_version_images/imageFile86.png>)

0.14

50 Ensemble size

100

0.12

200

1000

0.1

1000

0.08



0.06

0.04

0.02

0 0

0

0.2

0.4

0.6

0.8

1



Fig. 7.13: Localization threshold as a function of the estimated correlation coefficient ( γ = 1 ).

$$
˜ ρ ik = ρ ik + ϵ ik , (7.39)
$$

  where ρ ik is the true correlation and   ik represents the noise due to sampling error, with   ik ∼ N (0 ,σ 2   ). The authors proposed dividing the grid parameters into groups. For example, one group assigned to each petrophysical property. For each group, they defined the random vector   of dimension N   containing the noise components of the estimated correlation coefficients. The parameter σ   is then computed using the median absolute deviation (MAD) estimator [113]

$$
σ ϵ = med ( abs ( ϵ )) 0 . 6745 , (7.40)
$$

where med(abs(   )) denotes the median of the absolute values of the components of the vector   . The threshold τ is computed using the universal rule [112]:

$$
τ = √ 2 ln ( N ϵ ) σ ϵ . (7.41)
$$

This procedure relies on a proper assessment of the noise level in the correlation estimates or, at least, a good estimate of its standard deviation σ   . Luo et al. [280] discuss two approaches to estimate   . The first approach, termed as “ideal,” proposes the use of a large ensemble, typically with a few thousand realizations, to estimate the true correlation values ρ ik in Eq. (7.39), and then, by difference, estimate the noise. Evidently, this approach has the drawback of requiring a large ensemble, which prevents the use of the method in practice. The second approach, termed as “practical,” suggests using techniques from image denoising to separate the noise from the sample correlation values. Later, Luo and Bhakta [278] proposed a simpler procedure to estimate the noise level in the correlation estimates. They suggested randomly shuffling the indices of the ensemble members to create a new ensemble statistically independent of the predicted data.

They assumed that any correlation coefficient between model parameters and data in the shuffled ensemble is due to sampling errors and use these values as a proxy for   . Luo and Bhakta [278] also proposed to replace the hard threshold scheme of Eq. (7.36) by a continuous tapering rule

$$
r ik = r ( 1 -| ˜ ρ ik | 1 - τ ) , (7.42)
$$

where r ( · ) is a correlation function. For example, the Gaspari-Cohn correlation function was adopted in [278].

Fig. 7.14 illustrates the effect of correlation-based localization on covariance estimates in the example presented in Section 7.5.1. The localization coefficients were computed using Eq. (7.42) with a threshold of τ = 0 . 1. The results in Fig. 7.14 show that correlation-based localization was efficient in removing long-distance spurious covariances; it also removed some actual covariances, especially for the case with N e = 1,000.

1

0.8

0.6

0.2 0.4 0.6 Covariance

0.4

0.2

0

![](<ensemble_data_assimilation_e-book_version_images/imageFile37.png>)

1

0.8

0.6

0.2 0.4 0.6 Covariance

0.4

0.2

0

-0.2

-0.2

-0.4 0

0

25

50

50 Position

(a)

C m

m

 

75

100

-0.4 0

0

25

50

50 Position

(b)

R ◦

C m

◦

m

 

75

100

Fig. 7.14: Illustration of the effect of localization in removing spurious correlations. (a) Covariance estimates with ensembles of 50, 100, and 1,000 samples. (b) Covariance estimates after correlation-based localization. A threshold of τ = 0 . 1 was adopted in the example.

Recently, Vishny et al. [452] introduced a method called noise-informed covariance estimation (NICE), which combines similar ideas used in correlation-based localization and the Furrer-Bengtsson taper.

# 7.5.4.3 Example: Correlation-Based Localization of the Kalman Gain

Fig. 7.15 demonstrates the impact of correlation-based localization on the Kalman gain for the same reservoir model of Example 7.5.3.1. Panels (a) and (d) show the correlation coefficient values estimated using Eq. (7.35), while panels (b) and (e) display the corresponding localization values calculated using Eq. (7.42) with the Gaspari-Cohn function for a threshold of

τ = 0 . 1. Panels (c) and (f) present the Kalman gain values after applying localization. These results highlight that correlation-based localization significantly reduced spurious Kalman gain values in regions distant from the well locations. However, it also removed actual Kalman gain values close to the well, underestimating the region under actual Kalman gain influence (compare Figs. 7.15c and 7.8e).

(a)

Correlation

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0.0

0.1

0.2

(b)

Localization

1.0

0.8

0.6

0.4

0.2

0.0

0.08

0.06

0.04

0.02

0.00

(c)

Kalman gain after localization

localization

0.02

(d)

Correlation

0.7

![](<ensemble_data_assimilation_e-book_version_images/imageFile38.png>)

0.6

0.5

0.4

0.3

0.2

0.1

0.0

0.1

0.2

(e)

Localization

1.0

0.8

0.6

0.4

0.2

0.0

1e 5

5

4.0

3.5

3.0

2.5

2.0

1.5

1.0

0.5

0.0

(f)

Kalman gain after localization

localization

Fig. 7.15: Example illustrating correlation-based localization of the Kalman gain. The first row shows results for water cut data, and the second row shows results for water injection rate. Panels (a) and (d) display correlation coefficients, while panels (b) and (e) show localization values computed using Eq. (7.42) for τ = 0 . 1 and the Gaspari-Cohn correlation function. Panels (c) and (f) show the Kalman gain values after localization. Black dots represent the locations of production wells, and triangles indicate the positions of water injectors. White wells correspond to those where the Kalman calculation is performed. Example 7.5.4.3.

# 7.5.4.4 Sensitivity Analysis to Define Localization Coefficients for Scalar Parameters

Experienced practitioners often select localization coefficients based on their knowledge of the field, for example, by assigning zero values to the co-

This procedure requires 2 N m,s reservoir simulations, where N m,s is the number of scalar parameters. However, two important considerations should be noted: firstly, if N m,s is large, this procedure can become computationally intensive; secondly, this method does not account for the interaction between parameters. During each simulation, only the value of the relevant parameter is changed, while the remaining parameters are kept at their base (mean) values.

# Pseudo-code 7.1: One-at-a-time sensitivity analysis for localization of scalar parameters

For each scalar parameter ( i = 1 ,...,N m,s ):

- 1. Run two reservoir simulations: one with the parameter at its minimum and another at its maximum, keeping all other parameters at their mean value:

$$
d min = g ( m i = m i, min ) (7.43)
$$

$$
d max = g ( m i = m i, max ) (7.44)
$$

- 2. Set k = 0
- 3. For each data source:


• For each time step ( n = 1 ,...,N t ): – = + 1

k k

– Set r ik = 0 – If the following

condition is true

$$
| d n max - d n min | σ e n > τ, (7.45)
$$

set r ik = 1 for the entire time series ( τ ≥ 0, say τ = 10 − 2 ).

# 7.5.4.5 Example: Localization of Scalar Parameters

Fig. 7.16 presents boxplots of scalar parameter values for a modified version of the PUNQ-S3 problem. This is the same problem considered in [245]. Each plot shows the actual parameter value (horizontal line in each plot), the prior distribution, and the posterior distributions obtained under different conditions: without localization (labeled as “No-local”), with localization coefficients computed using Eq. (7.34) (labeled as “FB”), and with a combination of Eq. (7.34) and the sensitivity analysis procedure described in Pseudo-code 7.1 (labeled as “FB+SA”). All data assimilation cases were based on ES-MDA with N e = 100 and N a = 4 with constant inflation factors. Each plot also includes results from a large ensemble, N e = 5,000, without localization as a reference.

The localization coefficients computed using Eq. (7.34) were determined solely from the prior ensemble and remained fixed throughout the iterations. The results presented in [245] indicate that this procedure led to slightly better results than updating the localization coefficients at every ES-MDA iteration.

Two parameters are presented in Fig. 7.16. The first parameter corresponds to a change in the original water-oil contact, which significantly impacts the model predictions, with the true value being 1 meter. The data assimilation with the large ensemble resulted in a narrow posterior distribution centered around the true value. However, data assimilation without localization led to biased estimates of the water-oil contact. Both FB and FB+SA corrected this bias, accurately recovering the actual parameter value.

The second parameter is a dummy variable with a prior distribution sampled from a standard Gaussian. Since this parameter does not affect the simulation model, no updates during data assimilation are expected. However, the results in Fig. 7.16b show that the case without localization significantly reduced the posterior distribution, indicating updates solely due to sampling errors. While the FB case increased the posterior variability, it could not maintain the correct level of variance and resulted in biased final estimates. This poor performance is partly due to weak correlations being more prone to sampling errors. The introduction of the sensitivity analysis resulted in a zero localization coefficient for the dummy parameter, preventing any unnecessary updates.

# 7.5.5 Domain Localization

Domain localization, also known as local analysis, involves dividing the analysis into a collection of independent local analyses, each assimilating a subset of the observations (Fig. 7.17). These local analyses are conducted by assimilating only the observations within the vicinity of the parameter location. It is expected that the number of observations in these local regions

![](<ensemble_data_assimilation_e-book_version_images/imageFile89.png>)



�

  (m)





�

  '( 7$B' 2&amp;

  '800 

�

�

�

�









3U RU 1R RFD 

)%

)% 6$

1H 

3U RU 1R RFD 

)%

)% 6$

1H 

(a)

Change in the water-oil contact

(b)

Dummy parameter

Fig. 7.16: Distribution of scalar parameter values for a modified version of the PUNQ-S3 problem with different localization setups. The horizontal line in each plot corresponds to the true parameter value. Example 7.5.4.5.

![](<ensemble_data_assimilation_e-book_version_images/imageFile90.png>)

INTERNA Fig. 7.17: Domain localization for updating the value of the parameter located at the highlighted gridblock. Only observations located within the localization region (depicted as the dashed circle) are used in the analysis.

Sakov and Bertino [372] showed that covariance localization and domain localization are not mathematically equivalent, but they tend to yield similar results when the analysis is primarily influenced by the prior. Chen and Oliver [81] concluded that LM-EnRML converges faster with domain localization compared to Kalman gain localization, particularly when the amount of data is large relative to the ensemble size. They also noted that

![](<ensemble_data_assimilation_e-book_version_images/imageFile91.png>)

# Computational Implementation of the Analysis

Abstract: This chapter examines the matrix operations essential for efficiently implementing the analysis step, with a focus on optimizing memory usage. Special attention is given to ES-MDA with Kalman gain localization .

# 8.1 Introduction

Ensemble-based methods are appreciated for their simplicity of implementation. However, naive approaches to implementing the analysis can quickly become computationally prohibitive. For example, consider a scenario with N m = 10 6 parameters and N d = 10 4 data points. In this case, the resulting Kalman gain matrix contains 10 10 entries. Assuming double precision numbers (8 bytes), storing the Kalman gain requires 80 GB of RAM. Moreover, proper implementation of the inversion step of the analysis is critical, both in terms of performance and the quality of results.

This chapter delves into the matrix operations essential for efficiently implementing the analysis step, with a specific focus on robust inversion schemes and minimizing memory usage. While the discussion primarily centers on ES-MDA with Kalman gain localization, many of the concepts discussed are transferable to other variants of ensemble methods.

The ES-MDA update equation can be written as

$$
m ℓ +1 j = m ℓ j + R md ◦ [ ˜ C ℓ md ( ˜ C ℓ dd + α ℓ +1 C e ) - 1 ] × ( d ℓ obs ,j + √ α ℓ +1 e ℓ j - g ( m ℓ j )) , (8.1)
$$

for j = 1 ,...,N e , where   is the data assimilation index. In the following, we write the analysis in matrix form and drop the superscript   , noting that all matrices are computed at the same data assimilation step.

# 8.2 Analysis in Matrix Form

We start defining the following matrices:

$$
M = [ m 1 , m 2 , · · · , m N e ] , (8.2)
$$

with the j th column corresponding to the j th model vector m j , and

$$
D = [ d 1 , d 2 , · · · , d N e ] , (8.3)
$$

where d j = g ( m j ), and

$$
E = [ e 1 , e 2 , · · · , e N e ] , (8.4)
$$

with e j ∼ N ( 0 , C e ). Then, we define

the matrices of ensemble anomalies ∆ M and ∆ D by subtracting the ensemble mean vector from each column of M and D , i.e.,

$$
∆ M = 1 √ N e - 1 ( M - M ) = 1 √ N e - 1 [ m 1 - m , · · · , m N e - m ] = MA (8.5)
$$

and

$$
∆ D = 1 √ N e - 1 ( D - D ) = 1 √ N e - 1 [ d 1 - d , · · · , d N e - d ] = DA , (8.6)
$$

where A is a centering matrix given by

$$
A = 1 √ N e - 1 ( I - 1 N e 11 ⊤ ) , (8.7)
$$

··· We also define an innovation matrix J as

$$
J = d obs 1 ⊤ + √ α E - D . (8.8)
$$

With these matrices, we can express the ES-MDA analysis equation in the following form:

$$
M updated = M + R md ◦ [ ∆ M ∆ D ⊤ ( ∆ D ∆ D ⊤ + α C e ) - 1 ] J . (8.9)
$$

Table 8.1 summarizes the dimension of the matrices included in Eq. (8.9).

Table 8.1: Summary of matrices dimensions in Eq. (8.9) .

<table>
  <tr>
    &lt;th&gt;Matrix M D R md C e</th>
    &lt;th&gt;Dimension N m × N e N d × N e N m × N d N d × N d</th>
  </tr>
  <tr>
    &lt;td&gt;E d obs ∆ M ∆ D J</td>
    &lt;td&gt;N d × N e N d × 1 N m × N e N d × N e N d × N e</td>
  </tr>
</table>


# 8.3 Inversion

Eq. (8.9) involves the inversion of a N d × N d matrix C given by

$$
C ≡ ∆ D ∆ D ⊤ + α C e . (8.10)
$$

Since the product ∆ D ∆ D   forms a real-symmetric positive semidefinite matrix, C is real-symmetric and positive definite, at least when C e is positive definite. Therefore, C has a real inverse. However, it may be poorly conditioned [139]. Hence, for implementation, we utilize a pseudoinverse of C computed through a truncated singular value decomposition (TSVD).

Even though C is typically positive definite, it may be poorly scaled, particularly if it is constructed based on data with varying magnitudes. In this case, computing the pseudoinverse of C using TSVD may result in the loss of information necessary for data matching during truncation of small singular values.

Therefore, it is crucial to rescale the components of the matrix C before applying the TSVD. One approach is to rescale C using the diagonal elements of C e :

$$
C e = S ̂ C e S , (8.11)
$$

  where S is the N d × N d diagonal matrix containing the square root of the diagonal components of C e , i.e., S = [diag ( C e )] 1/2 .   C e is the correlation matrix of the data errors.

Then,

$$
C = S ̂ CS = S [ S - 1 ∆ D ∆ D ⊤ S - 1 + α ̂ C e ] S . (8.12)
$$

Note that for the case with uncorrelated data-errors,   C e = I . Applying TSVD to C

 

$$
̂ C ≈ Φ r Λ r Φ ⊤ r , (8.13)
$$

  where Φ r is the N d × N r matrix with its j th column equal to the left singular vector of   C corresponding to the j th singular value. Λ r is a diagonal matrix containing the N r largest nonzero singular values of C . We introduced the approximation sign because we keep only the N r ≤ min { N d ,N e − 1 } largest singular values of   C . The pseudoinverse of C assumes the form

The pseudoinverse of C assumes the form

$$
C + = S - 1 ̂ C + S - 1 = S - 1 Φ r Λ - 1 r Φ ⊤ r S - 1 . (8.14)
$$

Pseudo-code 8.1 summarizes the pseudoinverse procedure for the case with uncorrelated data errors.

# Pseudo-code 8.1: Pseudoinverse with diagonal C e

- 1. S = [diag ( C e )] 1/2 { Data-error standard deviations } 1
- 2.   ∆ D = S − ∆ D  
- 3.   C =   ∆ D   ∆ D + α I 4. Φ Λ Φ = C { TSVD


r r   r   } 5. Ω = S 1 Φ

− r 6. Υ = Λ 1

− r 7. C + = ΩΥΩ

 

The computation cost of the TSVD procedure becomes impractical when the number of data points is large. Evensen [138] proposed a more computationally efficient approach known as subspace inversion. This method is particularly advantageous when the number of data points greatly exceeds the number of ensemble members, i.e., N d   N e . Instead of directly computing the pseudoinverse of C through TSVD,

subspace inversion involves performing SVD on   ∆ D = S − 1 ∆ D and truncate with the N r largest singular values. The computational gain comes from the fact that the number of columns of   ∆ D is N e . We start by writing the TSVD of ∆ D as

 

$$
̂ ∆ D = S - 1 ∆ D ≈ U r Σ r V ⊤ r . (8.15)
$$

Again, the approximation is because we truncate small singular values. We write C as

$$
C = S [ S - 1 ∆ D ∆ D ⊤ S - 1 + α ̂ C e ] S ≈ S [ U r Σ r V ⊤ r V r Σ r U ⊤ r + α ̂ C e ] S ≈ SU r Σ r [ I + α Σ - 1 r U ⊤ r ̂ C e U r Σ - 1 r ] Σ r U ⊤ r S = ( SU r Σ r ) [ I + Θ ] ( SU r Σ r ) ⊤ . (8.16)
$$

We introduced another approximation in the third line of the expression because U r U   r   = I . To justify this approximation, note first that U r U   r is an orthogonal matrix that projects vectors onto the space spanned by the columns of U r . Let x be two vector in R N d and   x = U r U   r x its corresponding projection. Then

̸

$$
˜ x ⊤ C ˜ x = ˜ x ⊤ S [ U r Σ r V ⊤ r V r Σ r U ⊤ r + α ̂ C e ] S ˜ x = x ⊤ SU r U ⊤ r [ U r Σ r V ⊤ r V r Σ r U ⊤ r + α ̂ C e ] U r U ⊤ r Sx = x ⊤ SU r Σ r [ I + α Σ - 1 r U ⊤ r ̂ C e U r Σ - 1 r ] Σ r U ⊤ r Sx = x ⊤ ˜ Cx . (8.17)
$$

This means that the quadratic form induced by   C corresponds to the quadratic form induced by C in the space spanned by the columns of U r . In Eq. (8.16), we introduced the matrix Θ defined as

N r × N r

$$
Θ ≡ α Σ - 1 r U ⊤ r ̂ C e U r Σ - 1 r . (8.18)
$$

The matrix Θ is real-symmetric positive definite (at least when we choose C e positive definite). Hence, we can use SVD to express the eigendecomposition of Θ as

$$
Θ = ΨΓΨ ⊤ . (8.19)
$$

Note that at this point, the rank of Θ is N r and there is no reason for another truncation of singular values. Therefore, we can write C as

$$
C ≈ ( SU r Σ r Ψ ) [ I + Γ ] ( SU r Σ r Ψ ) ⊤ . (8.20)
$$

Thus, the pseudoinverse of C becomes

$$
C + = ( S - 1 U r Σ - 1 r Ψ ) [ I + Γ ] - 1 ( S - 1 U r Σ - 1 r Ψ ) ⊤ . (8.21)
$$

Note that Σ r and I + Γ are diagonal matrices. Hence, the inverses are trivial to compute.

# 8.3.2.1 Case with Diagonal Data-Error Covariance

When we assume uncorrelated data errors, we have a diagonal matrix C e . In this situation, it suffices to use   C e = I and note that

$$
Θ ≡ α Σ - 1 r U ⊤ r ̂ C e U r Σ - 1 r = α Σ - 1 r U ⊤ r U r Σ - 1 r = α Σ - 2 r , (8.22)
$$

which is a diagonal matrix. Therefore, it is not necessary to do the SVD of Θ . Instead, write the pseudoinverse as

$$
C + = ( S - 1 U r Σ - 1 r ) [ I + Θ ] - 1 ( S - 1 U r Σ - 1 r ) ⊤ . (8.23)
$$

Pseudo-code 8.2 summarizes the subspace inversion procedure for the case with uncorrelated data errors.

# Pseudo-code 8.2: Subspace inversion with diagonal C e

$$
1. S = [ diag ( C e )] 1/2 { Data-error standard deviations } 2. ̂ ∆ D = S - 1 ∆ D 3. U r Σ r V ⊤ r = ̂ ∆ D { TSVD } 4. Θ = α Σ - 2 r 5. Ω = S - 1 U r Σ - 1 r 6. Υ = ( I + Θ ) - 1 7. C + = ΩΥΩ ⊤
$$

# 8.3.2.2 Case with Cholesky Factorization of the Data-Error Covariance

For the case with correlated data errors, the matrix C e is not diagonal. In this case, we typically use a square root of C e to compute the data perturbations, e j ’s. If the number of data points is not extremely large, the Cholesky decomposition can be used to compute the square root of C e . In this case, we write the Cholesky decomposition of the rescaled matrix C e as

$$
̂ C e = L e L ⊤ e , (8.24)
$$

where L e is a lower-diagonal matrix. Then, the matrix Θ becomes

$$
Θ ≡ α ( Σ - 1 r U ⊤ r L e ) ( Σ - 1 r U ⊤ r L e ) ⊤ . (8.25)
$$

The rest of the inversion remains unchanged. Pseudo-code 8.3 summarizes the subspace inversion procedure for the case with correlated data errors and Cholesky of C e .

# Pseudo-code 8.3: Subspace inversion with Cholesky of C e

- 1. S = [diag ( C e )] 1/2 { Data-error standard deviations } 1 1
- 2.   C e = S − C e S − { Correlation matrix }
- 3. L e L   e =   C e { Cholesky } 1
- 4.   ∆ D = S − ∆ D 5. U Σ V = ∆ D


r r   r   { TSVD } 1 1

$$
6. Θ = α ( Σ - 1 r U ⊤ r L e ) ( Σ - 1 r U ⊤ r L e ) ⊤
$$

 

= 1

ΨΓΨ  

Θ

7.

{ 1

   SVD }

}

Ψ

-

U

-

=

Ω

S −

r

Σ − r 1

Ψ

8.

r

r

9. Υ = ( I + Γ ) − +

+

⊤

=

C

ΩΥΩ  

10.

# 8.3.2.3 Case with Large Non-Diagonal Data-Error Covariance

For a case with a very large number of data points, it may not be feasible to store and factorize a large non-diagonal matrix C e . In these cases, one alternative is to construct a low-rank approximation of C e using an ensemble of perturbed observations, i.e.,

$$
˜ C e ≈ 1 N e - 1 EE ⊤ . (8.26)
$$

However, instead of computing   C e , we can apply the subspace inversion using E . Before, we need to rescale E as

$$
̂ E = 1 √ N e - 1 S - 1 E . (8.27)
$$

Then, the matrix Θ is redefined as

$$
Θ ≡ α ( Σ - 1 r U ⊤ r ̂ E )( Σ - 1 r U ⊤ r ̂ E ) ⊤ . (8.28)
$$

The rest of the inversion remains unchanged. Pseudo-code 8.4 summarizes this procedure.

# Pseudo-code 8.4: Subspace inversion with ensemble representation of C e

1. S = [diag ( C e )] 1/2 { Data-error standard deviations } 1 1

$$
2. ̂ E = 1 N e - 1 S - 1 E
$$

  e − 3.   ∆ D = S − 1 ∆ D 4. U Σ V = ∆ D

r r   r   { TSVD }

$$
5. Θ = α ( Σ - 1 r U ⊤ r ̂ E )( Σ - 1 r U ⊤ r ̂ E ) ⊤
$$

-   6. ΨΓΨ   = Θ { SVD } 1 1
- 7. Ω = S − U r Σ − r Ψ 8. Υ = ( I + Γ ) − 1


1

+

9. C = ΩΥΩ  

# 8.3.3 Sherman-Morrison-Woodbury Pseudoinverse

For a case with a diagonal matrix C e and N d   N e , we can use the ShermanMorrison-Woodbury formula (A.9) to derive an efficient inversion strategy. In this case, we write

$$
C = S ̂ CS = S [ ̂ ∆ D ̂ ∆ D ⊤ + α I ] S . (8.29)
$$

Using the Sherman-Morrison-Woodbury formula, we can write C − 1 as

$$
C - 1 = 1 α [ I - ̂ ∆ D ( ̂ ∆ D ⊤ ̂ ∆ D + α I ) - 1 ̂ ∆ D ⊤ ] S - 1 . (8.30)
$$

The matrix     ∆ D     ∆ D + α I   has dimension N e × N e . Therefore, if N e   N d this is a convenient form to compute the inverse. Using TSVD, we write

$$
̂ ∆ D ⊤ ̂ ∆ D + α I = Ξ r Λ r Ξ ⊤ r . (8.31)
$$

The pseudoinverse of C becomes

$$
C + = 1 α S - 1 [ I - ( ̂ ∆ DΞ r ) Λ - 1 r ( ̂ ∆ DΞ r ) ⊤ ] S - 1 . (8.32)
$$

Pseudo-code 8.5 summarizes this procedure.

# Pseudo-code 8.5: Sherman-Morrison-Woodbury pseudoinverse with diagonal C e

- 1. S = [diag ( C e )] 1/2 { Data-error standard deviations } 1
- 2.   ∆ D = S − ∆ D  
- 3. P =   ∆ D   ∆ D + α I 4. Ξ Λ Ξ = P { TSVD


r r   r }

$$
5. Υ = α - 1 [ I - ( ̂ ∆ DΞ r ) Λ - 1 r ( ̂ ∆ DΞ r ) ⊤ ]
$$

6. C + = S − 1 ΥS − 1

# 8.3.4 Truncation of Singular Values

The inversion methods described above involve truncating singular values. The most common approach for truncation is to determine the minimum number of singular values, N r , such that

$$
∑ N r i =1 σ i ∑ N R i =1 σ i ≥ ξ, (8.33)
$$

where ξ ∈ (0 , 1] is referred to as the truncation energy. In most applications, high values like ξ ≥ 0 . 99 are commonly used. However, in cases with a large number of redundant data points, using a lower value may be beneficial [78, 124].

Recently, Emerick and Neto [124] proposed using a method called “optimal hard thresholding” (OHT) [165] to determine the truncation level of   ∆ D in subspace inversion. According to this method, a truncation threshold, τ ∗ , is computed as

$$
τ ∗ = √ 2 . 858 σ med , (8.34)
$$

where σ med is the median singular value of   ∆ D .

# 8.3.4.1 Example: Truncation of Singular Values in the PUNQ-S3 Benchmark Problem

Table 8.2 presents the values of the data-mismatch objective function and normalized variance (NV) obtained by Emerick and Neto [124] for a modified version of the PUNQ-S3 benchmark problem [150]. The study utilized ES-MDA with subspace inversion and truncation based on the energy criterion ( ξ = 0 . 99) and the OHT method. Fig. 8.1 displays the singular value spectrum, highlighting the number of singular values retained for each case. Fig. 8.2 illustrates the predicted water cut data for one well in the model. These results demonstrate that the OHT method retained fewer singular values, leading to a smaller reduction in the posterior variance of the ensemble without compromising the quality of the data match.

Table 8.2: Data-mismatch objective function and normalized variance for a modified version of the PUNQ-S3 problem with truncation of singular values based on the energy criterion ξ = 0 . 99 and OHT. Example 8.3.4.1.

<table>
  <tr>
    &lt;th&gt;Case O d ( m ) (mean</th>
    &lt;th&gt;± std. dev.) NV</th>
  </tr>
  <tr>
    &lt;td&gt;ξ = 0 . 99 0.474 OHT 0.494</td>
    &lt;td&gt;± 0.015 0.230 0.027 0.303</td>
  </tr>
  <tr>
    &lt;td&gt;OHT</td>
    &lt;td&gt;±</td>
  </tr>
</table>


![](<ensemble_data_assimilation_e-book_version_images/imageFile92.png>)

1

1000

0.8

Cumulative energy

Singular value

100

0.6

0.4

10

0.2

N r =

= 35 0.893

N r =

= 84 0.99

Energy

= 0.893

Energy

= 0.99

1 0

0 100

4

0

0

0 2

80

100

60

80 Number of singular values 40 60

Fig. 8.1: Singular values of the matrix   ∆ D (prior ensemble) for a modified version of the PUNQ-S3 problem. The green line represents the truncation level determined by the optimal hard threshold method, while the dashed line indicates the truncation level based on the energy criterion. Example 8.3.4.1. Reproduced from Emerick and Neto [124] with permission from Elsevier.





![](<ensemble_data_assimilation_e-book_version_images/imageFile93.png>)





 DWHUFXW  

 DWHUFXW  

















 

 

�





 7 PH GD V 







�





 7 PH GD V 







�����������

�����������

(a)

(b)

OHT

= 0 .

99

ξ

99

Fig. 8.2: Water cut of a well for a modified version of the PUNQ-S3 problem. Red dots represent the observed data points, with error bars corresponding to one standard deviation of the data error. The gray lines show the predicted data from the prior ensemble, while the blue lines depict the predictions from the posterior ensemble. Example 8.3.4.1. Reproduced from Emerick and Neto [124] with permission from Elsevier.

# 8.4 Matrix Multiplications

Regardless if we use pseudoinverse, subspace inversion or Sherman-MorrisonWoodbury pseudoinverse, the inverse of the matrix C can be written as

$$
C - 1 ≈ C + = ΩΥΩ ⊤ , (8.35)
$$

where Ω is a N d × N r matrix and Υ is a N r × N r diagonal matrix. The definition of Ω and Υ depends on the inversion procedure

used:

• Pseudoinverse:

and

• Subspace inversion:

and

$$
Ω = S - 1 Φ r (8.36)
$$

$$
Υ = Λ - 1 r . (8.37)
$$

$$
Ω = S - 1 U r Σ - 1 r Ψ (8.38)
$$

$$
Υ = ( I + Γ ) - 1 . (8.39)
$$

• Sherman-Morrison-Woodbury Pseudoinverse :

$$
Ω = S - 1 (8.40)
$$

and

$$
Υ = α - 1 [ I - ( ̂ ∆ DΞ r ) Λ - 1 r ( ̂ ∆ DΞ r ) ⊤ ] . (8.41)
$$

For the case without localization, Evensen [137] presents the following order for performing the multiplications to update the ensemble of models in M :

$$
Ω 1 = ΥΩ ⊤ , ( N r × N d ) (8.42)
$$

$$
Ω 2 = Ω 1 J , ( N r × N e ) (8.43)
$$

$$
Ω 3 = ΩΩ 2 , ( N d × N e ) (8.44)
$$

$$
Ω 4 = ∆ D ⊤ Ω 3 , ( N e × N e ) (8.45)
$$

and finally

$$
M updated = M +∆ MΩ 4 . ( N m × N e ) (8.46)
$$

The resulting matrix dimensions are indicated alongside each multiplication to emphasize the sizes involved. This order of multiplication is particularly efficient because, typically, we have N m   N e . Moreover, these multiplications are optimized for the case where N d &gt; N e , which is the typical situation for smoothers.

If we have N d   N e , it is better to introduce a slight modification in the last two multiplications. Instead of computing Ω 4 , we compute

$$
Ω 5 = ∆ M ∆ D ⊤ . ( N m × N d ) (8.47)
$$

Then, we update the ensemble using

$$
M updated = M + Ω 5 Ω 3 . ( N m × N e ) (8.48)
$$

For the case with Kalman gain localization, the best multiplication order is

$$
Ω 1 = ΥΩ ⊤ , ( N r × N d ) (8.49)
$$

$$
Ω 6 = ∆ D ⊤ Ω , ( N e × N d ) (8.50)
$$

$$
Ω 7 = Ω 6 Ω 1 , ( N e × N d ) (8.51)
$$

$$
K = ∆ MΩ 7 , ( N m × N d ) (8.52)
$$

$$
K loc = R md ◦ K , ( N m × N d ) (8.53)
$$

$$
Ω 8 = K loc J , ( N m × N e ) (8.54)
$$

and finally

$$
M updated = M + Ω 8 . ( N m × N e ) (8.55)
$$

However, when N d is very large, the main challenge arises from the Kalman gain matrix, which has dimensions N m × N d . In such situations, an alternative approach is to update the matrix M in groups of rows. For each update, a smaller Kalman gain matrix is computed. In the limit, each row of M can be updated independently, significantly reducing the memory requirements of the analysis. Not only does this approach save memory by avoiding the allocation of the entire Kalman gain matrix, but it can also be

# 8.4.1 Example: Parallelization of the Analysis

Compared to the time required to execute the ensemble of reservoir simulations, the time required for the computation of analysis is relatively insignificant, especially if the number of model parameters and data points is not too large. Typical reservoir data assimilation problems involving production data have O (10 2 ) to O (10 7 ) model parameters and O (10 2 ) to O (10 3 ) data points. In these cases, a standard implementation of the analysis is sufficient, particularly if up-to-date linear algebra packages are used to perform matrix multiplications, taking advantage of the multiple CPUs available in modern workstations.

However, this scenario changes significantly when the number of data points increases, such as in cases involving 4D seismic data. Fortunately, the calculations required for the analysis are highly parallelizable. To illustrate that, consider the data assimilation exercise presented by Exterkoetter et al. [146], with a reservoir model discretized in 150 × 150 × 50 gridblocks operating with 36 production wells and 25 water injection placed in five-spot patterns as illustrated in Fig. 8.3a. The data assimilation parameters are the porosity and log-permeability of each gridblock, resulting in N m = 2,250,000. The observed data correspond to a 4D seismic dataset represented as the water saturation changes in every gridblock after 10 years of production, which corresponds to N d = 1,125,000 (Fig. 8.3b).

mD

10 2 10 3

1

10 0 10

-1

10

0.75

![](<ensemble_data_assimilation_e-book_version_images/imageFile39.png>)

0.45

0.15

A

A

(a)

Permeability INTERNA

INTERNA

Section A‐A

-

A

(b)

4D seismic

Fig. 8.3: Hypothetical data assimilation problem used to test the computational performance of the analysis in CPU and GPU implementations [146]. Example 8.4.1.

Exterkoetter et al. [146] compared the computational time required for the analysis step of the problem using CPU and GPU implementations. Both implementations utilized a distance-based Kalman gain localization with subspace inversion, as described in Section 8.3.2, and a diagonal C e . The ensemble size was 200. The CPU implementation was tested on an i7-9700K CPU with eight cores, while the GPU implementation used an NVIDIA RTX 3090 with 10,496 cores running CUDA 10.1. Table 8.3 shows the computational time required by both implementations. Notably, the standard CPU implementation took more than 2.3 days to complete the analysis calculation. This computational time was significantly reduced by leveraging the parallelism offered by GPUs. The time reduction is primarily due to the acceleration in matrix multiplications and the calculation of the localization coefficients. Kalman gain localization requires computing the distance between each data point and each model parameter, resulting in 1.125 million data points times 1.125 million gridblocks.

Table 8.3: Computational time of the analysis for a data assimilation problem with N m = 2,250,000, N d = 1,125,000 and N e = 200.

<table>
  <tr>
    &lt;th&gt;Case Time</th>
    &lt;th&gt;(hours)</th>
  </tr>
  <tr>
    &lt;td&gt;CPU GPU</td>
    &lt;td&gt;57.15 4.19</td>
  </tr>
  <tr>
    &lt;td&gt;GPU</td>
    &lt;td&gt;4.19</td>
  </tr>
</table>


![](<ensemble_data_assimilation_e-book_version_images/imageFile95.png>)

# 9

# Practical Aspects and Field Examples

Abstract: This chapter discusses key practical considerations for applying iterative ensemble smoothers in reservoir data assimilation, offering guidelines for researchers and practitioners. The content is organized into three main sections: parametrization, data handling, and result evaluation. The chapter concludes with three field examples that demonstrate data assimilation in petroleum reservoirs.

# 9.1 Introduction

Understanding the practical aspects of real-world data assimilation applications is essential for bridging the gap between theoretical models and their implementation in the field.

This chapter discusses key practical considerations in applying iterative ensemble smoothers for reservoir data assimilation and offers guidelines for researchers and practitioners. The discussion is organized into three main parts: parametrization, data handling, and evaluation of results. The chapter concludes with the presentation of three field examples that illustrate data assimilation in petroleum reservoirs.

# 9.2 Parametrization

One of the most notable differences between ensemble and optimizationbased methods for data assimilation is the number of parameters each method can handle. In ensemble-based methods, the computational cost

In contrast, ensemble methods are well-suited for handling problems with a vast number of model parameters. For example, these methods commonly allow reservoir rock properties to vary on a gridblock-by-gridblock basis, resulting in situations with easily O (10 7 ) uncertain variables. The key element of these methods lies in shifting the search for solutions from the “model space” to the “ensemble space.” In fact, the size of the ensemble can be interpreted as the number of “effective parameters.” Recall from Section 7.2 that in cases without localization, the posterior ensemble is a linear combination of the prior ensemble members, meaning that the data assimilation has N e effective parameters (coefficients of the linear combinations). Although localization increases the dimensionality of this space, the overall performance of data assimilation still heavily depends on the prior ensemble. While the size of the prior ensemble has an impact, practical applications typically limit the number of ensemble members to O (10 2 ). Therefore, more crucial than the ensemble size is the quality of the prior models in terms of accurately capturing the reservoir’s behavior and adequately spanning the prior uncertainty.

Section 3.7 introduced parametrization with an emphasis on finding a reduced representation of the parameter space to enable efficient solution finding. In this section, we shift focus and discuss parametrization from the perspective of selecting relevant reservoir uncertainty properties to ensure a robust prior ensemble. A key principle here is to avoid overconfidence in parameter selection. Neglecting a parameter implies assuming its value is known with certainty, which can lead to significant issues. Overlooking relevant parameters often forces other parameters to compensate, resulting in values that fall outside their expected ranges [330] and possibly introducing bias in the model forecasts.

Before delving into the main types of parameters used in reservoir data assimilation, we will briefly discuss two elements: the use of model realizations versus scenarios and the use of integrated workflows for creating and updating reservoir models.

# 9.2.1 Realizations versus Scenarios to Describe Uncertainty

The current practice in reservoir modeling involves combining scenarios and stochastic realizations to describe uncertainty. Scenarios are constructed to capture higher-level uncertainties, typically modeling only a few scenarios

(e.g., pessimistic, base, optimistic). Realizations, on the other hand, are generated using geostatistics to populate models with rock properties consistent with the data. Regarding these processes, Ringrose and Bentley [365] identifies three differing approaches to uncertainty handling in reservoir modeling:

- 1. Best guess approach: The preferred model is chosen as the best guess and uncertainty is represented by adding a range around the best guess.
- 2. Multiple stochastic approach: A large number of models are probabilistically generated by geostatistical simulation.
- 3. Multiple deterministic approach: A smaller number of models are built, each one reflecting a complete reservoir concept.


According to the authors, the “best-guess approach” puts faith in the ability of an individual or team to make a reasonably precise judgment. This process tends to generate the so-called anchoring effect 1 —“ once anchored, the adjustment away from the initial best guess is too limited as the outcome is overly influenced by the anchor point ” [445].

The “multiple stochastic approach” refers to the use of realizations, while the “multiple deterministic approach” refers to scenarios. Ringrose and Bentley [365] argue that the sole use of realizations to describe uncertainty may not be able to escape from anchoring around the “most likely” probabilistic outcome, highlighting the importance of scenarios in capturing higher-level uncertainties to represent plausible modeling hypotheses.

Since ensemble data assimilation methods rely on Gaussian assumptions for the prior, they are typically more effective at updating realizations. Mixing scenarios and realizations within a single ensemble may not yield optimal performance, particularly when the scenarios are highly distinct. In such cases, the formulation relying on the first two moments of the distribution (mean and covariance) becomes insufficient for updating the combined scenario-realization ensemble. This often results in the inability to generate plausible posterior models, with the components of the ensemble lacking the required geological realism or failing to match observations.

A more pragmatic approach involves generating an ensemble of realizations for each discrete scenario and performing separate data assimilation for each. During this process, certain scenarios may prove unfeasible and need to be discarded; a procedure sometimes referred to as prior model falsification [53].

However, this strategy is not without challenges. One significant issue is determining how to properly weigh the posterior scenarios and realizations for uncertainty evaluation in reservoir performance predictions. Methods for weighting posterior models, such as importance sampling [135], Bayesian model averaging [193], and Bayesian stacking [472], all suffer from the curse of dimensionality [4, 5].

# 9.2.2 Integrated Workflows

Integrated workflows for model updating have gained significant attention due to their automation of the reservoir model generation process. This integration combines geological modeling tools and reservoir simulators within workflows orchestrated by dedicated software that samples and updates parameters. Known as the “big-loop approach” [461], this process aims to make the model update process repeatable, thereby reducing time and inconsistencies. A notable example is Equinor’s Fast Model Update (FMU) [476, 401], which uses the open-source software ERT 2 .

Integrated workflows offer substantial benefits for reservoirs with sparse data and significant uncertainties. In such cases, these workflows enable the evaluation of diverse modeling scenarios by updating high-level uncertainty parameters that have a global impact on the models. However, reservoirs with numerous wells and extensive operational history often require local updates in the model realizations to achieve acceptable data matches. In these cases, the big-loop approach with global parameters can be used to discard unfeasible modeling scenarios and generate consistent ensembles for plausible ones. These ensembles can then serve as prior models for data assimilation, ensuring that data is honored on a well-by-well basis.

# 9.2.3 Main Types of Reservoir Parameters

Internally, ensemble methods do not distinguish between different types of reservoir properties used as model parameters. This flexibility is one of their key advantages, allowing them to be easily coupled with complex forward models and parametrizations without the need for specific implementations to calculate partial derivatives, unlike adjoint-based methods.

Nevertheless, it is useful to categorize reservoir parameters into three main types: grid parameters, scalar parameters, and structural parameters. This categorization facilitates discussion, as each type may require different strategies for prior ensemble generation and localization.

# 9.2.3.1 Grid Parameters

Grid parameters encompass rock properties such as porosity and permeability, including special parametrizations to represent facies. These parameters are characterized by the fact that they vary on a gridblock-by-gridblock basis. Therefore, the number of grid parameters is in the same order as the number of active gridblocks in the model.

The prior ensemble of grid parameters is almost invariably generated using geostatistics. During data assimilation, the lower and upper limits on the parameter values are typically enforced through truncation. These limits can be established either globally, regionally, or even on a gridblock-bygridblock basis. Setting limits on a gridblock-by-gridblock basis offers more detailed control over property values. Fig. 9.1 shows an example where using gridblock-by-gridblock limits resulted in a better estimation of the final porosity distribution in a model, preventing the occurrence of high-porosity values on the left side of the model. However, overly strict limits can constrain changes in the model. As a practical consequence, this may prevent the identification of areas with poor parametrization, limiting valuable feed-

back for improving the prior model [223].

(a)

Global limits

0.18 Porosity

![](<ensemble_data_assimilation_e-book_version_images/imageFile40.png>)

0.18

0

(b)

Gridblock-based limits

INTERNA Fig. 9.1: Example with two posterior realizations of porosity obtained with global and gridblock-based limits after data assimilation with ES-MDA for a field in the Santos Basin.

INTERNA

One interesting aspect of ensemble methods is the fact that they use the prior ensemble to construct the uncertainty space. This means that if a parameter value does not vary in the ensemble, it implies no associated uncertainty. A practical consequence is that “hard data” used in the prior geostatistical modeling are retained during data assimilation. Conversely, underestimating prior uncertainty will invariably lead to underestimation in the posterior.

Data assimilation with grid parameters invariably requires the use of a localization strategy. Currently, distance-based localization is the most effective approach. The choice of the “optimal” localization function depends on the specific problem, varying with the type of data, type of parameter, and ensemble size. Nonetheless, selecting reasonable localization regions is not overly challenging. The compact function of Gaspari and Cohn [162] is the most commonly used correlation function, and the selection of the localization radius (critical length) is the most relevant aspect.

In general, underestimating the size of the localization region is more detrimental than overestimating it. In reservoir applications, it is recommended to align the localization with the model’s anisotropic direction and

# Porosity

Porosity is a primary grid parameter used in reservoir data assimilation. It directly impacts reservoir volume and significantly influences overall reservoir pressure. Near wells, porosity is generally well-characterized due to the availability of well-logging data (hard data).

# Permeability

Permeability is the most crucial and widely used grid parameter in reservoir data assimilation, as it defines flow patterns within the reservoir and influences both pressure and saturation matching. However, permeability data are scarcer than porosity data, leading to greater uncertainties. Additionally, significant discrepancies often exist between permeability values measured in laboratory tests on rock cores and those estimated in the field through pressure transient analysis, sometimes differing by orders of magnitude. Typically, permeability is correlated with porosity, and these correlations are often used to construct well profiles that serve as conditioning data in geological models. Since permeability frequently exhibits a log-normal distribution, it is advisable to adjust the log-transformed values during data assimilation.

# Net-to-Gross Ratio

The net-to-gross ratio (NTG) is sometimes used as a grid parameter in data assimilation. NTG is a value between zero and one, indicating the fraction of reservoir rock in each gridblock of the model. NTG realizations are typically generated from the upscaling process because, in the fine-scale geological model, NTG is often modeled with binary values (reservoir/non-reservoir). In the coarse-scale flow simulation model, NTG serves as a simplified representation of facies. NTG impacts the porous volume and horizontal transmissibility in reservoir simulation, thereby redundantly affecting porosity and horizontal permeability during data assimilation.

# Vertical Transmissibility Multipliers

Vertical transmissibility multipliers are also very common to represent vertical barriers to flow, such as cementation or thin shale layers that have

# Facies

Facies are categorical variables that represent different rock types, posing a challenge for their update using ensemble methods. To address this complexity, facies realizations are typically re-parameterized into variables that assume continuous values, ideally following distributions close to Gaussian. Currently, one of the most widely adopted approaches for re-parameterizing facies in data assimilation with ensemble methods is the truncated plurigaussian (TPG) method [157, 17, 35].

In the TPG method, latent grid parameters used for generating facies realizations are updated simultaneously with other reservoir rock properties. During prior modeling, distinct geostatistical properties are assigned to each facies to characterize rock attributes such as porosity and permeability. Consequently, updating parameters associated with each facies type becomes necessary. The final realizations of the simulation are synthesized by combining the property values attributed to each facies, a technique often referred to as the “cookie-cutter approach” [104].

Fig. 9.2 shows an example of facies and permeability realization for an oilfield in the Campos Basin. The facies realization was generated using TPG by truncating two Gaussian random realizations, z 1 and z 2 . The final model contains four facies, with only two (R1 and R2) assumed to contribute to fluid flow. The permeability of these facies was modeled using SGS, and the final permeability model was constructed using the cookie-cutter approach. During data assimilation, the latent Gaussians, z 1 and z 2 , and the permeability of facies R1 and R2 are updated as reservoir parameters.

# 9.2.3.2 Scalar Parameters

Scalar parameters are single-value parameters that have a broad influence on the model, either globally or regionally. Examples encompass parameters defining relative permeability and capillary pressure tables, transmissibility multipliers, rock compressibility, parameters for aquifer influx modeling, and initial fluid contacts.

The prior ensemble of scalar parameters is typically constructed by independently sampling univariate distributions, assuming uncorrelated prior uncertainty. Commonly used distributions include normal and log-normal. However, practitioners often favor distributions with compact support, such

z 1

1

3

z 2

2

0

-3

0

-3

3 -3

(a)

Truncation rule

rule

3

0

-3

(b)

z 1

1

3

0

-3

(c)

z 2

2

R1

R2

CEMENTED

NON-RES

(d)

Facies

![](<ensemble_data_assimilation_e-book_version_images/imageFile41.png>)

INTERNA

INTERNA

INTERNA

10 mD

3

10 2

10 1

10 0

10 mD

3

10 2

10 1

10 0

10 mD

3

10 2

10 1

10 0

(e)

Permeability facies R1

(f)

Permeability facies R2

(g)

Permeability

R1

R2

PERM_1

INTERNA INTERNA INTERNA Fig. 9.2: Facies realization generated using TPG for an oilfield in the Campos Basin. Panel (a) shows the truncation rule. Panels (b) and (c) display the Gaussian random fields, while panel (d) presents the resulting facies realization. Panels (e) and (f) depict the permeability realizations for facies R1 and R2, respectively, and panel (g) shows the final permeability realization.

as uniform, triangular, and PERT distributions (see Appendix C, Section C.1.18).

When dealing with correlated prior uncertainty, sampling can be achieved using the Cholesky decomposition of the prior covariance matrix, assuming all scalar parameters follow normal distributions. However, if parameters have different distributions, more advanced sampling strategies are needed, such as employing copulas [318].

Selecting coefficients for the localization matrix for scalar parameters poses a greater challenge because these parameters lack an associated spa-

tial location, making it impossible to calculate spatial distances between parameters and data points. Despite this limitation, it is still feasible to introduce a degree of “localization” based on field knowledge. For instance, one approach involves setting the coefficients of the localization matrix to zero for parameters identified as insensitive to the data. Alternatively, the non-distance-dependent localization schemes discussed in Section 7.5.4 can be employed.

# Relative Permeability

Relative permeability curves govern the displacement speed of different phases within the reservoir, making the associated parameters highly utilized in reservoir data assimilation problems with multiphase flow. These curves are initially derived from laboratory displacement tests on core samples. In these tests, determining the endpoints is generally more reliable than defining the curve shapes. A key consideration for using relative permeability curves in simulations is their dependence on the model scale; identical curves can lead to different water and gas breakthrough times based on the dimensions of the model gridblocks. To address this, the curves are often adjusted during upscaling to account for the absence of heterogeneities in coarse simulation grids and to compensate for numerical dispersion effects in multiphase fluid flow. These adjusted curves are sometimes called pseudocurves [29, 116]. Consequently, uncertainty in relative permeability curves is typically much larger than the variability observed in laboratory measurements, especially in fields with limited production history where fluid breakthroughs have not been fully observed.

Relative permeability curves are provided as tables in most reservoir simulators. For more effective data assimilation, these curves are re-parameterized using power-law models (Fig. 9.3). The most common model used is the Brooks-Corey model, which can be expressed as

$$
κ r i = κ r i, max s e i n i (9.1)
$$

with

$$
s n i = s i - s i, min s i, max - s i, min , (9.2)
$$

where κ r i is the relative permeability of the phase i at saturation s i . The exponent e i determines the shape of the curve. s n i in the normalized saturation with s i, min and s i, max denoting the minimum and maximum phase saturation, respectively. For example, the relative permeability for the water phase in an oil-water table we have s i, min = s w,cr and s i, max = 1 − s o,rw , where s w,cr is the critical water saturation and s o,rw is the residual oil saturation.

Another frequently used model to parametrize relative permeabilities is the LET model [269]. Unlike the Corey, the LET model provides more de-

$$
κ r i = κ r i, max s L i n i s L i n i + E i (1 - s n i ) T i . (9.3)
$$

The parameters L i , E i , and T i do not have direct physical interpretations. Parameter L i governs the lower segment of the curve, akin to the Corey exponent, while T i influences the upper segment. Parameter E i determines the position of the curvature transition. A value of E i = 1 signifies a neutral point, where the curve is influenced by L i and T i . Increasing E i shifts the transition point towards the upper curve segment. According to Lomeland et al. [269], the conditions are L i ≥ 1, E i &gt; 0, and T i ≥ 0 . 5.

![](<ensemble_data_assimilation_e-book_version_images/imageFile98.png>)

1

1





0.8

0.8

ro,max =

ro,max =

0.8

0.8





0.5

0.5

rw,max =

rw,max =

0.6

0.6

L o

4

4

e o

= E =

=

r

r

o

1

 r

 r

T =

0.4

0.4

L w

2

o

1

= E =

o

w

1

e w

2

T =

=

0.2

0.2

2

w

w

s o,rw

s o,rw

0.20

0.20

0.15

s w,cr

0.15

s w,cr

=

=

=

=

0

0

0

0.25

0.5

0.75

1

0

0.25

0.5

0.75

1

s w

s w

w

w

(a)

Corey

(b)

LET

1.2

Drainage

s

0.15

w,con = s =

o,rw

0.20

Imbibition

c =

0.8

0.1 bar

w

c =

0.01 bar

o

e

0.5

pw

= e =

c (bar)

0.4

0.5

po

po

c

p

0

0

0.25

0.5

0.75

1

c w

0.05 bar

= c =

-0.4

0.1 bar

o

e

0.5

pw

= e =

po

0.5

po

-0.8

s w

w

(c)

Capillary pressure

Fig. 9.3: Typical power-law models used to re-parametrize relative permeability and capillary pressure curves in reservoir models.

# Capillary Pressure

Like relative permeability, capillary pressure in reservoir simulation models is typically represented in tabular form, requiring re-parametrization. One alternative, in this case, is to use the expressions proposed by Skjaeveland et al. [398]:

$$
p c = c 1 ( s 1 - s 1 , min 1 - s 1 , min ) e p 1 - c 2 ( s 2 - s 2 , min 1 - s 2 , min ) e p2 , (9.4)
$$

where p c is the capillary pressure defined as the difference between the pressure in the non-wetting phase, p 2 , and the pressure in the wetting phase, p 1 . For example, for a oil-water system with water as preferential wetting phase, we write s 1 = s w (water saturation), s 2 = s o (oil saturation), s 1 , min = s w,con (connate water saturation), and s 2 , min = s o,rw (residual oil saturation). The parameters c 1 , c 2 , e p1 , and e p2 control the shape of the curves. Fig. 9.3c shows an example of drainage and imbibition curves generated with Eq. (9.4).

One important aspect of the parametrization is the spatial distribution of relative permeability and capillary pressure properties in the model. There are several alternatives, but in practice, the most common approaches include dividing the model into fixed regions, such as partitioning the reservoir according to geological formations. For each region, a different parametrization of relative permeability and capillary pressure is adopted. Alternatively, relative permeability and capillary pressure can be assigned to each reservoir facies. A third option, often used in practical applications, is to divide the reservoir into “flow units,” where the goal is to group rock types with similar flow behavior. This is typically done based on porosity and permeability values, using methods like the flow zone indicator (FZI) [12]. One advantage of using facies or flow units is the ability to update these regions during data assimilation.

# Faults

Scalar transmissibility multipliers across faults and between blocks play a crucial role in pressure and saturation matching in reservoir modeling. Fault positions are usually identified via seismic interpretation and remain static during data assimilation. These parameters consist of a single multiplier per fault between zero and one. Initializing these values with a log-normal distribution is often preferred, with adjustments made to the logarithm of the multiplier during data assimilation.

Although fault transmissibility multipliers are commonly treated as scalar parameters, they can alternatively be represented as grid parameters. For example, Emerick [123] presented a data assimilation example in which fault transmissibility multipliers were handled as grid parameters. This approach

improves flexibility by allowing multipliers to vary along faults and simplifying the implementation of distance-based localization.

# Discrete Parameters

Ensemble methods are designed for real-valued parameters, and using parameters with discrete distributions is generally not recommended. However, practitioners sometimes employ them. In such cases, an alternative approach involves applying a normal scores transformation (see Fig. 9.4) to the discrete distribution. The transformed parameters are then updated during data assimilation. It is essential to ensure that the discrete parameter values

are ordered to maintain a monotonic effect on the model predictions.

![](<ensemble_data_assimilation_e-book_version_images/imageFile99.png>)

Discrete

Standard

normal

0.5

0.6

0.5

0.5

0.4

Probability

0.4

0.3

( z )

0.3

z

0.3

(

f

0.2

0.2

0.2

0.1

0.1

0

0 -4

1

2

3 value

-4

-2

0

2

4

Parameter

z

(a)

Distributions

1

1

0.8

0.8

0.6

0.6

)

CDF

F ( z )

(

F

0.4

0.4

u =

0.3

0.2

0.2

0 0

0 -4

0

1

2

3

-4

-2

0

2

4

Parameter value

z



z 

-0.5

(b) Cumulative distributions

INTERNA Fig. 9.4: Illustration of normal transformation and sampling of discrete parameters. During data assimilation, the normal-transformed values, z , are updated and the corresponding discrete values are obtained using the CDF.

# 9.2.4 Structural Parameters

Structural parameters determine the reservoir’s geometry, thereby shaping the simulation model grid. Often, these parameters are relevant in new fields with limited wells and production history. The external and internal geometry of the reservoir can greatly influence flow behavior and the initial fluid volume.

One of the earliest studies to incorporate structural parameters into ensemble data assimilation was conducted by Seiler et al. [389], where they updated the top and bottom reservoir surfaces and deformed a corner-point grid to align with the updated surfaces. Today, commercial geomodeling software enables the specification of uncertainty in the input parameters of the structural model and the automatic reconstruction of the reservoir grid. These tools make it feasible to account for structural uncertainty in practical applications.

# 9.2.4.1 Example: Uncertainty in the Fault Position

Fig. 9.5 shows reservoir grids generated in a synthetic data assimilation exercise, where fault positions are estimated using data from a producer-injector well pair. The integration of geological modeling software with an ES-MDAbased data assimilation tool allows for grid updates during the process, leading to a significant improvement in the data match, as demonstrated in Fig. 9.6.

# 9.3 Observed Data

# 9.3.1 Production Data

Production data correspond to dynamic measurements gathered from production and injection wells during field operations, typically including fluid flow rates and pressure readings. These datasets are characterized by long time series. The use of production data in assimilation processes requires proper consideration of three interdependent aspects: data selection, frequency, and error covariance.

Data selection depends on the specific problem and should be guided by factors such as data acquisition methods and model limitations. A clear recommendation is to avoid unreliable data points (outliers). One straightforward method to identify outliers is to compare the mean innovation (the difference between the observed value and the ensemble mean prediction) to the combined standard deviations of predicted data, σ d , and data-error, σ e .

INTERNA

INTERNA

(a)

Reference

true: + 200

200

INTERNA

(b)

Prior 1

prior 42: + 980

980

(c)

Prior 2

INTERNA

INTERNA

(d)

Posterior 1

![](<ensemble_data_assimilation_e-book_version_images/imageFile42.png>)

post 42: +393

(e)

Posterior 2

post 51: ‐30

-

30

prior 51: ‐

970

970

Fig. 9.5: Reservoir grids generated with varying fault positions. The red circle marks the location of the oil-producing well, while the blue circle marks the location of the gas injection well. Example 9.2.4.1.

![](<ensemble_data_assimilation_e-book_version_images/imageFile101.png>)

 



 DVR  UDW R PP 

 

���





M



3UHVVXUH M3D 

























 7 PH GD V 















 7 PH GD V 







�����������

�����������

(a)

Gas-oil ratio (producer)

(b)

Pressure (gas injector)

Fig. 9.6: Gas-oil ratio and bottom-hole pressure for a synthetic reservoir problem with uncertainty in the fault position. Red circles represent observed data, while gray and blue lines show predicted data from the prior and posterior ensembles, respectively. The error bars in the observed data points correspond to one standard deviation of the data error. Example 9.2.4.1.

If the innovation is significantly large compared to the sum of these standard deviations, the data point can be considered an outlier:

$$
if ∣ ∣ ∣ d obs ,i - g i ( m ) ∣ ∣ ∣ > 3 ( σ d,i + σ e,i ) , then d obs ,i is labeled as 'outlier. ' (9.5)
$$

Note that data points meeting the previous condition are not necessarily outliers (in the sense of being biased or severely corrupted by noise). They may also fall under this condition because the ensemble of models fails to capture the system’s physical behavior, indicating model deficiency (model error). In both cases, removing these data points from the study may be beneficial. Alternatively, instead of removing the data point, its weight can be reduced by inflating the corresponding error standard deviation. One option is to set:

$$
σ e,i = 1 γ ∣ ∣ ∣ d obs ,i - g i ( m ) ∣ ∣ ∣ - σ d,i , γ ∈ [1 , 3] . (9.6)
$$

    In petroleum reservoirs, production data are typically reported at high frequencies, often on a daily basis. However, much of this data is derived by distributing the total production among wells using allocation tables, which are updated less frequently during periodic separation tests. As a result, the high frequency of production data may not provide significant additional information.

Another aspect is the presence of redundant information in long time series. Consecutive data points are expected to provide similar information content because they are correlated due to the system’s dynamic behavior. It is important to note, however, that this type of correlation differs from data-error correlation, which is handled by the matrix C e . Redundant information in the data is managed by the matrix   C dd in the ensemble smoother formulation. Unlike C e , which is predefined,   C dd is calculated based on ensemble predictions and, therefore, may be affected by sampling errors. Emerick and Neto [124] demonstrated through a series of test problems that reducing the frequency of production data can help mitigate variance loss in this case without compromising data-match quality.

The selection of the data-error covariance, C e , greatly influences the performance of data assimilation, as it determines the weight of each observation and the balance between the prior model and the data. Underestimating C e leads to excessively strong updates in model parameters, while overestimating it prevents effective use of all available information. Unfortunately, choosing an appropriate C e is challenging. Data often contain more than just random noise, and systematic errors in data acquisition are hard to characterize and may be unknown to users. Moreover, C e is frequently used to address forward modeling deficiencies [124].

Usually, we assume independence in production data errors, resulting in a diagonal C e . However, this assumption is often incorrect. Production data is usually derived from rate allocation based on infrequent separator

Table 9.1: Typical values for data-error standard deviation of production data

<table>
  <tr>
    &lt;th&gt;Data Oil rate 5–10% of the Water rate 10–15% of the Water cut 10–15% of</th>
    &lt;th&gt;Standard deviation data value (min. 10 m 3 /day) data value (min. 10 m 3 /day) the data value (min. 0.01)</th>
  </tr>
  <tr>
    &lt;td&gt;GOR 15–20% Pressure (flowing) Pressure (static)</td>
    &lt;td&gt;of the data value 5–10 bars 1–5 bars</td>
  </tr>
</table>


# 9.3.1.1 Example: Water Production Data

In petroleum reservoirs, especially in fields with water injection or strong aquifer influence, the volume of produced water is one of the most commonly used data for assimilation. Reservoir engineers often utilize the water cut as observed data, representing the ratio between water production and total liquid production rates. Other options include using the water production rate or cumulative water production. Fig. 9.7 shows an example of water production for a well in an onshore oilfield, presented in terms of water cut (Fig. 9.7a), water rate (Fig. 9.7b), and cumulative water production (Fig. 9.7c). This figure also shows the predicted data from a model operated at a specified oil rate. From the viewpoint of information content, all three representations of water production data contain the same information. However, a visual inspection of the plots may lead to different conclusions regarding the quality of the data match, even though the predictions are from the same model. The water production plot gives the impression of a better data match compared to the water cut and cumulative production plots. The water cut data exhibit a more “erratic” behavior, with significant short-term variations highlighting mismatches with the predicted water cut. The cumulative water data, on the other hand, follow a monotonically increasing curve that smooths out these oscillations. Nonetheless, the initial

mismatch observed in water production propagates through the cumulative data.

Although using cumulative production data may seem attractive for data assimilation due to the continuous nature of the curves, in practice, it requires accounting for correlated errors when defining the matrix C e .

1.0

0.8

)

-

(

0.6 cut (‐)

0.6

0.4 Water

0.4

0.2

0

Observed Predicted

Predicted

120

100

100 (m 3 /d)

80

Water rate

60

40

20

1990

1992

1996 Year

1998

1994

Year

(a)

Water cut

2000

INTERNA

2002

0

Observed Predicted

Predicted

1990

1992

1996 Year

1998

1994

Year

(b)

Water rate

2000

2002

INTERNA

14

4 m 3 )

12

(10

10

water

8

Cumulative

6

4

2

0

Observed Predicted

![](<ensemble_data_assimilation_e-book_version_images/imageFile43.png>)

Predicted

1990

1992

1996 Year

1998

1994

Year

(c)

Cumulative water

2000

2002

Fig. 9.7: Example of water production data for a well in an onshore oilfield. All panels show the same data but with different formats and the prediction from a model. Example 9.3.1.1.

# 9.3.1.2 Example: Well Pressure Data Sensitivity

Well-pressure measurements acquired with permanent downhole gauges (PDGs) are important sources of information for reservoir data assimilation. These data are typically divided into flowing and static pressures. Flowing pressure refers to the pressure measured while a well is producing or injecting fluids, whereas static pressure is measured when the well is shut in, allowing pressures to stabilize and reflect the reservoir’s equilibrium state. Flowing and static pressures typically contain different information content. Flowing pressure is highly sensitive to the near-wellbore region and is affected by short-term fluctuations in flow rates, while static pressure data capture the

Due to the high sensitivity of flowing pressure data to the well productivity/injectivity index, practitioners often prefer the assimilation of static pressure measurements. After conditioning the models to static pressure, the match for flowing pressure is achieved by adjusting well productivity/injectivity index multipliers.

# 9.3.1.3 Example: Rate versus Ratio Data

Identifying problematic data points is often easier when analyzing ratio data, such as water cut and gas-oil ratio (GOR), compared to flow rate data. Fig. 9.9 shows this with actual data from two wells in an oilfield. For the first well, we observe periods with perfectly constant water cut (Fig. 9.9b), which is highly unlikely to reflect actual measurements. However, these constant water cut values are somewhat obscured when analyzing only the flow rate data (Fig. 9.9a). A similar issue arises with gas rate data; the gas rate plot (Fig. 9.9c) does not clearly indicate suspicious data points. In the GOR plot, however, it is easy to spot data points that deviate from the general trend. For example, Fig. 9.9d highlights two suspicious data points: the first with a large GOR value and another with GOR values below the initial value of the gas-oil solubility ratio.

# 9.3.1.4 Example: Use of Rate Allocation Tables

![](<ensemble_data_assimilation_e-book_version_images/imageFile103.png>)

3480

16

10

days

3470

14

20

days

3460

12

29

days

(psi)

31

days

10 Sensitivity

10

3450

40

days

Pressure

8

3440

50

days

6

3430

4

3420

2

3410

0 0

3400 0

0

20

40

60

80

100

0

10

20

30

40

50

60

Time

(days)

Gridblock

(a)

BHP

(b)

Sensitivity

10

days

1.6

20

days

29

days

1.2

31

days

Sensitivity

40

days

50

days

0.8

0.4

0 0

0

20

40

60

80

100

Gridblock

(c)

Sensitivity

Fig. 9.8: Sensitivity values of bottom-hole pressure (BHP) with respect to permeability for a single-phase problem. Panel (a) shows the BHP prediction, indicating a drawdown period of 30 days followed by a 30-day build-up. Panel (b) displays the sensitivity values of BHP with respect to the permeability of each gridblock at different times. Panel (c) presents the same sensitivity values with an adjusted vertical scale. Example 9.3.1.2.

# 9.3.1.5 Example: Errors in Injection Rates

120

100

Water rate (m 3 /d)

80

60

40

20

0 1987

1987

1990

1993 Year

Year

1995

(a)

Well 1 (water rate)

1

0.8

Water cut

0.6

0.4

0.2

1998

0 1987

1987

Periods with constant water cut

constant

water

cut

1990

1993 Year

Year

1995

(b)

Well 1 (water cut)

1998

60000

50000

Gas rate (m 3 /d)

40000

30000

20000

10000

0 1987

1987

1993

1998

2004 Year

Year

GOR &lt; Solubitiy ratio

Gas-oil ratio (m 3 /m 3

2009

2014

2020

600 )

500

400

300

200

100

0 1987

1987

(c)

Well 2 (gas rate)

Outilier?

GOR &lt;

&lt;

Solubility

ratio

1993

1998

2004 Year

Year

2009

2014

(d)

Well 2 (gas-oil ratio)

2020

Fig. 9.9: ments can

Examples of data from an actual oilfield, illustrating how problematic measurebe more easily identified in ratio data. Example 9.3.1.3.

ments can be more easily identified in ratio data. Example 9.3.1.3.

600

![](<ensemble_data_assimilation_e-book_version_images/imageFile44.png>)

Gas-oil ratio (m 3 /m 3 )

450

300

150

0

2015

2017

2016

2018 Year

2019

2020

2021

Year

INTERNA Fig. 9.10: Example of GOR data for a well in the Santos Basin. The red circles represent GOR measurements obtained from separation tests, while the green circles indicate GOR data calculated based on allocation tables. Example 9.3.1.4. Adapted from Emerick [123].

INTERNA

Practical Aspects and Field Examples

Average pressure (bars)

290

![](<ensemble_data_assimilation_e-book_version_images/imageFile45.png>)

285

280

275

270

265

260

255

250 1990

1990

1992

1994

1996

1998

2000

2002

Year

Fig. 9.11: Example of the effect of a 2% systematic error in the specified water injection rate on the reservoir pressure for a model of a field in the Campos Basin. The black dots correspond to the base prediction of the reservoir pressure. The red dots represent the predictions with a ± 2% variation in the water injection rate, and the blue dots represent the predictions with a ± 7.5% variation in the original volume of oil in place. Example 9.3.1.5.

# 9.3.1.6 Simulation Controls

During data assimilation, well controls in the models are set to honor the historical flow rates observed in the field. For oil-producing wells, there are three common control options: (1) impose the oil rate, (2) impose the liquid rate (oil plus water), and (3) compute the total fluid rate at reservoir condition and use this as the well-control. All three approaches are used in practice. The first approach is sometimes preferred because the simulator prioritizes the primary fluid of interest (oil). However, the second and third approaches have the advantage of honoring the historical fluid balance, often making it easier to match the average field pressure. For injection wells, the typical approach involves controlling the wells based on the observed injection rates.

The data used as well-controls are typically not included as observations in data assimilation. Ideally, we expect all models to honor the imposed control data. However, sometimes the models are unable to meet the specified constraints. Fig. 9.12 shows an example where prior models from an oilfield could not honor the specified liquid production rate, causing the bottom-hole pressure to reach a lower limit. This situation is undesirable and can negatively affect data assimilation performance. When the wellcontrols switch from a liquid rate to a pressure constraint, the ensemble loses the ability to estimate covariances between pressure data and model parameters, preventing the assimilation of these data. This situation commonly occurs in injection data when the simulation reaches the maximum allowable well pressure. In such cases, a possible approach is to use the injection rates as observed data for assimilation, even though they are also prescribed as control variables.

INTERNA

Observed Data

![](<ensemble_data_assimilation_e-book_version_images/imageFile46.png>)

2000

300

Liquid rate (m 3 /day)

Pressure (bar)

1000

150

0 0

0 0

6000

0

2000

4000

0

Time (days)

(a)

Liquid production

2000

4000

Time (days)

(b)

Pressure

6000

INTERNA Fig. 9.12: Example of a well where the prior models were not able to honor the specified historical liquid production rate. The simulator switched the controls to minimum bottomhole pressure.

# 9.3.2 4D Seismic Data

4D seismic, involving repeated seismic surveys over time, provides detailed insights into fluid movements and pressure changes within reservoirs. However, integrating 4D seismic data into reservoir models is more complex than incorporating production data. This complexity is due to several factors. The large volume of data points significantly increases computational demands, necessitating more degrees of freedom to accurately capture changes in rock properties while maintaining geological plausibility. Additionally, errors, biases, and inaccuracies in the forward model tend to be more pronounced in 4D seismic datasets, presenting substantial challenges that are difficult to identify and correct during the assimilation process.

4D seismic data assimilation is generally performed in one of three domains: the seismic domain, which includes attributes like amplitudes and time shifts; the elastic domain, which involves pressure and shear-wave velocity or impedance data; and the simulation domain, which deals with pressure and phase saturation. The elastic domain is often favored because it offers a good balance between data preparation and forward modeling [336]. Alternative representations of 4D data in the literature include discrete images [438, 327], fluid fronts [443, 254], and coefficients related to data compression methods [280, 146].

In 4D seismic assimilation, observed and simulated seismic data must be compared on a consistent scale. This entails converting observed seismic data from time to depth and adjusting it to a grid that aligns with the simulator’s response. However, because seismic data typically have lower vertical resolution compared to the simulation’s vertical discretization, 4D seismic data are often interpreted as “maps” corresponding to multiple layers of the simulation model.

# 9.3.2.1 Petroelastic Modeling

A petroelastic model (PEM) is used to convert reservoir simulation results, such as pressure and fluid saturation, into elastic properties. This model is crucial for 4D seismic data assimilation, and extensive literature on PEMs can be found in works by Mavko et al. [298] and Grana et al. [175]. Most PEMs are based on the Gassmann fluid substitution model [163], often supplemented with (semi-)empirical correlations to estimate the elastic properties of rock and fluid.

Characterizing the elastic properties of the dry-rock frame of the reservoir is typically the most influential and uncertain aspect of PEM. This characterization involves developing correlations for porosity, lithology, and effective pressure effects derived from well-logging data and laboratory experiments with rock core samples. Among these factors, the pressure-dependent behavior of elastic properties is generally the most uncertain.

Fluid density and bulk modulus are also critical components in PEMs. Many applications use the correlations presented in Batzle and Wang [31] for these parameters. For more complex fluid descriptions, such as compositional modeling of volatile oils, miscible gas injection, and high CO 2 content, Neto et al. [319] provide a recent and detailed discussion advocating the use of equations of state calibrated with laboratory measurements.

# 9.3.2.2 Example: 4D Seismic Data

Fig. 9.13 shows an example of 4D seismic data used for data assimilation in an oilfield in the Campos Basin. The 4D data correspond to the difference in inverted P-impedance between two streamer surveys acquired 14 years apart, normalized by the impedance of the base survey. Fig. 9.13a shows the seismic data in a cross-section in the original seismic scale after the timeto-depth conversion. In this figure, the positive seismic anomalies (depicted in blue) correspond to an increase in P-impedance, primarily reflecting the effect of water replacing oil in the reservoir. The original position of the oilwater contact is indicated. In this field, multiple wells inject water below the original contact. Negative anomalies (depicted in tones from red to yellow) are also visible and are interpreted as artifacts (side lobes) 3 . Due to these artifacts and the limited vertical resolution of streamer surveys, the 4D seismic data were represented as maps computed over the positive seismic anomalies for two main geological formations in this reservoir. These maps were then upscaled to match the horizontal discretization of the simulation grid, resulting in the image presented in Fig. 9.13b, which was used for

3 Side lobes are unwanted artifacts that appear in seismic data images [233]. These artifacts are typically generated by the secondary lobes of the wavelet. Ideally, seismic inversion from amplitude to impedance should remove these artifacts by eliminating the wavelet’s effect. However, in practice, side lobes are frequently observed in 4D impedance datasets.

data assimilation. Figs. 9.13c and 9.13d show the predicted 4D seismic data before and after data assimilation, where improvements in the predicted seismic data are notable.

PROD

PROD

INJ

PROD

0.05

0

-0.05

O/W

Side‐lobe

-

lobe

0.05

0

-0.05

(a)

Observed (section)

(b)

Observed

OBS

![](<ensemble_data_assimilation_e-book_version_images/imageFile47.png>)

INTERNA

0.05

0.05

0

0

-0.05

-0.05

(c)

Predicted (prior) POST 5

(d)

Predicted (post)

PRIOR 5

5

POST

5

INTERNA

INTERNA

Fig. 9.13: 4D seismic data (normalized P-impedance changes) for oilfield in the Campos Basin. Panel (a) shows a cross-section of the observed 4D data in the seismic scale, indicating the original position of the oil-water contact (dashed horizontal blue line). Panel (b) shows the observed 4D data transferred to the reservoir simulation grid. Panel (c) shows the predicted 4D data with a prior model realization while Panel (d) shows the corresponding prediction after data assimilation. The horizontal yellow line in (b)–(d) indicates the position of the cross-section shown in Panel (a). Example 9.3.2.2.

# 9.3.2.3 4D Seismic Data-Error Covariance

Choosing the data-error covariance matrix, C e , for 4D seismic data presents a significantly greater challenge than production data. Firstly, 4D seismic datasets are prone to systematic errors due to inconsistent data acquisition conditions, extensive data processing, and uncertainties in time-to-depth conversion and amplitude-to-impedance inversion. Moreover, modeling errors in 4D seismic data, particularly issues related to scale transference and limitations of petroelastic models, are prevalent. Unlike production data, assuming uncorrelated data errors is often less realistic for seismic datasets [329]. However, using a non-diagonal C e can be problematic for large datasets where memory storage of C e may be impractical. In such

As with other data types, removing or downweighting unreliable 4D seismic data points is crucial during assimilation. In this context, the normalized root-mean-squared error (NRMS) [241] is widely used to identify problematic data arising from survey repeatability issues. Several works propose strategies to estimate C e in the context of 4D seismic data assimilation; see, e.g., Oliver [329] and references therein. One important aspect is to consider both data and model errors in this process. Alfonzo and Oliver [9] proposed estimating C e based on the residuals of the data assimilation (the difference between observed and predicted 4D data from posterior realizations). This procedure is relatively general, simple to implement, and allows estimation of the combined effect of data and model errors. One drawback is that it requires repeating the data assimilation, increasing computational costs. Emerick and Neto [125] proposed estimating C e based on the residuals between the observed seismic data and its projection onto the subspace defined by predicted data from the prior ensemble, eliminating the need for repetitions of the data assimilation. They used this procedure to identify and eliminate data points with significant discrepancies, compute error variance, and estimate error correlations across long distances.

# 9.3.3 Other Data

# 9.3.3.1 Tracer Data

Tracers are substances used to track fluid movement in applications involving multiphase flow. They are widely used for monitoring operations and reservoir characterization in applications including the injection and storage of waste fluids [87, 312], groundwater flow and contaminant transport in aquifers [351], and production in oil and gas fields [342, 477].

In practice, a tracer is injected into one well and monitored as it is recovered from one or more production wells. Data on tracer breakthrough time recovered mass and concentration over time provide information about inter-well pore volume and connectivity. There are also single-well tracer tests, which are used to estimate residual oil saturation [477].

There are two main types of tracers: radioactive and chemical. Radioactive tracers emit detectable radiation, offering high sensitivity and precision, while chemical tracers are versatile and can be tailored to specific reservoir conditions. Tracers can be further classified based on their behavior in the reservoir. Conservative tracers remain in the same phase throughout their movement, providing direct information about fluid flow paths and velocities. Partitioning tracers, on the other hand, shift between phases, revealing

Tracer modeling encompasses several physical and chemical effects, such as diffusion and dispersion, partitioning between fluid phases, adsorption onto reservoir rock, and radioactive decay. This modeling can be particularly sensitive to numerical dispersion, especially in large-scale 3D models where the volume of tracer pulse injections is negligible compared to the volumes of injected and produced fluids. Consequently, it is crucial to account for the model’s limitations when incorporating tracers into the data assimilation process. For example, depending on the formulation, numerical scheme, and spatial and temporal discretizations, it may not be realistic to assimilate a full-time series of tracer concentration data. Instead, we might consider using only the tracer breakthrough time as the observed data and assume a relatively large data-error variance.

# 9.3.3.2 Example: Tracer and 4D Seismic Data

Fig. 9.14 shows a 4D seismic image and the interpreted pathways of chemical tracers with observed breakthroughs for the central area of a carbonate oilfield in the Santos Basin. The figure includes six oil-producing wells (labeled P1 to P6), two water injection wells (IW1 and IW2), four gas injection wells (IG1 to IG4), and two wells with water-alternating-gas injection (WAG1 and WAG2). The 4D image is a normalized map displaying hardening (blue) and softening (red) anomalies derived from time-lapse amplitude data. Hardening anomalies are interpreted as increases in reservoir impedance due to water injection, while softening anomalies are associated with gas injection. Notably, the 4D data is consistent with the tracer breakthrough information (indicated by blue and red arrows in Fig. 9.14b). This information helps geoscientists understand fluid distributions within the reservoir. For example, it is possible to identify preferential fluid paths for injected water aligned with geological faults in the field. Further details on this field can be found in [97] (see also Field 2 in Section 9.5.2).

# 9.3.3.3 Pressure Transient Data

Pressure transient analysis involves monitoring pressure changes in a well over a controlled period of operation. By analyzing the pressure response, engineers can interpret reservoir behavior using analytical models, such as the radial flow model, to estimate key reservoir parameters, including permeability, skin effects, reservoir boundaries, and fluid properties. Pressure transient data are also assimilated into numerical reservoir models, particularly in newer fields with limited well coverage or a brief production history. In such cases, special attention must be given to reducing time step sizes

0.01 0.02

0

- 0.01
- 0.02
- 0.02


IG3

IG3

P2

P3

IG4

P2

IW1

P3

IG4

![](<ensemble_data_assimilation_e-book_version_images/imageFile48.png>)

IW1

IG1

WAG2

IG1

P4

WAG2

P4

P1

IW2

P1

IW2

WAG1

P5

WAG1

IG2

P5

P6

IG2

P6

(a)

4D Seismic

(b)

Tracer

INTERNA INTERNA Fig. 9.14: Comparison between 4D seismic and tracer data for an oilfield in the Santos Basin. Panel (a) shows the 4D seismic data, while panel (b) indicates the interpreted pathways of chemical tracers with observed breakthroughs, injected in the water phase (blue arrows) and gas phase (red arrows). Example 9.3.3.2.

# 9.3.3.4 Well Profile Data

Well profile data comprise measurements of pressure and flow rate taken along the well trajectory. Among these, pressure profiles obtained using repeat formation testers (RFTs) [404] are invaluable for detecting reservoir compartmentalization and indicating fluid contact positions. Flow rate profiles acquired through production-logging tools (PLTs) [192] are frequently employed in data assimilation, especially for wells that have recently been drilled in the field. These profiles are instrumental in evaluating the relative contributions of various reservoir formations to the total flow rate of the well.

# 9.3.3.5 Example: Pressure Transient and PLT Data

Coutinho et al. [94] presents an example of PLT and pressure transient data assimilation using the standard EnKF for a vertical well in an oilfield in the Santos Basin. The model parameters correspond to permeability multipliers, one for each reservoir layer. Fig. 9.15a shows the pressure data and the corresponding predictions obtained from the prior and posterior ensembles, indicating a visible improvement in the data matches. Fig. 9.15b

presents a log-log diagnostic plot of the first build-up period, displaying pressure changes and pressure derivatives. These results indicate that, despite improvements in the predicted pressure data, the posterior ensemble was unable to capture the correct level of the pressure derivative. Note that pressure changes and pressure derivatives are derived from pressure measurements and are not used as data during assimilation; rather, they are presented in Fig. 9.15b for analysis of the results. Fig. 9.15c shows the PLT data, which corresponds to the cumulative contribution of each reservoir layer to total liquid production. Fig. 9.16 shows the prior and posterior distributions of permeability multipliers, indicating that only a few reservoir layers are effectively contributing to total well production.

 

![](<ensemble_data_assimilation_e-book_version_images/imageFile109.png>)

 

���

 3  EDUV 



      3UHVVXUH EDUV 

���

��



   D HU

���

��

 3DQG

���



���



 

 

 

 

�

���

���

���

���

����

��



��

 



      &amp;XPX DW YH D HUUDWH EE GD  

WH  GD  

 7 PH GD  

(a)

Pressure

(b)

Build-up log-log plot

(c)

PLT

Fig. 9.15: Pressure and PLT for a well in an oilfield in the Santos Basin. Red circles represent observed data, while gray and blue lines show predicted data from the prior and posterior ensembles after data assimilation with EnKF, respectively. Panel (a) shows the pressure data. Panel (b) shows a log-log diagnostic plot of the first build-up period, where the white circles and squares represent the pressure changes and pressure derivatives, respectively. Panel (c) shows the PLT data in terms of the cumulative contribution of each reservoir layer to the total liquid production. Example 9.3.3.5. Adapted from Coutinho et al. [94] with permission from the authors.

# 9.3.3.6 Well Log Data

Similar to well profile data, well logging involves measurements taken along the well trajectory. Various methods and tools are used for well logging, including electric, acoustic, and radioactive logs. These logs provide indirect measurements of reservoir rock and fluid properties. Despite being susceptible to noise and interpretation errors, log data are generally considered very accurate. They represent a primary source of information for reservoir characterization and are used as conditioning data in geostatistics to generate prior realizations. Because these data are precisely honored in geostatistics, they are often referred to as “hard data.”

It is worth noting that ensemble methods use the prior ensemble to construct the uncertainty space for data assimilation. This means that if a

![](<ensemble_data_assimilation_e-book_version_images/imageFile110.png>)

 

 

















 

 

 

 

 

 













��

��

    D HU

    D HU

��

��

��

��





 

 

 

 

 

 

























��

��







 0X W S  HU













 0X W S  HU







����������

����������

(a)

Prior

(b)

Posterior

Fig. 9.16: Distribution of layer permeability multipliers. Example 9.3.3.5. Adapted from Coutinho et al. [94] with permission from the authors.

# 9.4 Results Evaluation

The quality and adequacy of the initial ensemble are critical for successful data assimilation. The ensemble must accurately reflect uncertainties, ensuring it samples the prior uncertainty space adequately. Beginning data assimilation with an inadequate ensemble leads to well-known consequences: failure to match observed data, geological models lacking plausibility, and inaccurate uncertainty estimates in reservoir performance forecasts.

However, achieving this adequacy is often challenging in practical applications, as important uncertainty parameters are frequently overlooked during the problem setup. This oversight arises from inherent limitations in recognizing all relevant aspects of the problem, including biases from modeling assumptions and constraints in time and resources. To address this, it is crucial to thoroughly analyze processes and results, revisiting assump-

- 1. Model creation: Select the main modeling hypotheses, including parametrization, observations, and error tolerances.
- 2. Model criticism ( a priori perspective): Analyze the consistency of the prior models compared to observations.
- 3. Model calibration: Perform data assimilation to update the model parameters based on the observations.
- 4. Model criticism ( a posteriori perspective): Analyze the consistency of the posterior models.
- 5. Model improvements: Revisit the model creation step if necessary.


These steps may require iteration. Both preand post-calibration model criticism should focus on three main aspects:

-  Geological plausibility.
-  Ability to reproduce the observed behavior of dynamic data.
-  Ability of the ensemble to adequately estimate the range of uncertainties in predictions.


In Chapter 4, we derived the EnKF starting from the RML objective function. In Chapter 5, we similarly used RML to introduce ES-MDA. Although this is not the only way to present these methods, it highlights a key similarity between them: both aim to minimize an objective function consisting of two components—the prior and the likelihood. The likelihood term increases when predicted data diverge from observations, while the prior term increases as models deviate from the initial ones. Thus, the goal is to find the minimal adjustments to the prior models necessary to match the observations [328]. However, when initial model predictions differ significantly from the data, substantial changes to the models are required to minimize the likelihood term, often compromising geological plausibility.

For example, if none of the initial model realizations can replicate the production behavior of one or more wells, it indicates flaws in the prior modeling. In these cases, it is generally more beneficial and efficient to invest time in refining the initial modeling rather than attempting to correct it later during the calibration phase.

# 9.4.1 Example: Non-Representative Priors

Fig. 9.17 demonstrates an ES-MDA application where the initial modeling did not adequately represent key uncertainties. This is evident from the initial water production curves, which show minimal variation across the 100 prior realizations and a significant mismatch with the observations. Although ES-MDA managed to produce an ensemble that matched the water

Fig. 9.19 presents another field example highlighting discrepancies between observed data and prior modeling. Here, the observed pressure data for a particular well showed a significant deviation from the predicted range of the prior ensemble. As a result, ES-MDA led to an unrealistic reduction in permeability around the well location. Subsequent investigations identified inconsistencies in the specified water injection for a nearby well within the model.

# 9.4.2 Prior Observation Coverage and Mean Squared Error

The previous examples show that when simulated production profiles diverge significantly from observed production history, the initial models are not suitable for the calibration step. However, identifying this issue is not always straightforward through visual inspection alone, particularly in fields with many wells. In this section, we discuss metrics designed to evaluate the quality of the prior ensemble based on predicted production data. These metrics act as qualitative indicators, and failure to meet them indicates a need to revisit the prior model.

# 9.4.2.1 Observation Coverage (OC)

This metric assesses whether the range of predicted data is sufficiently broad to encompass the observations. We count the number of data points ( ± σ e ) that fall within the minimum and maximum predictions. Based on the value of OC, we classify the ensemble as follows:

-  Excellent: OC &gt; 0 . 95.
-  Good: 0 . 8 &lt; OC ≤ 0 . 95.
-  Fair: 0 . 7 &lt; OC ≤ 0 . 8.
-  Poor: OC ≤ 0 . 7.


(a)

Permeability (prior)

![](<ensemble_data_assimilation_e-book_version_images/imageFile49.png>)

mD

mD

10 3

10 3

10 2

10 2

10 1

10 1

10 0

10 0

(b)

Permeability (posterior)

1

rate (norm)

INTERNA

Water

0

2000

4000 (days)

Time

(c)

Water production (prior)

1

rate (norm)

Water

6000

0

![](<ensemble_data_assimilation_e-book_version_images/imageFile50.png>)

2000

4000 (days)

6000

Time

(d)

Water production (posterior)

Fig. 9.17: Example of data assimilation using ES-MDA, where the prior model predictions have been improved by introducing transmissibility multipliers across several faults mapped from seismic data. This figure represents a later data assimilation study of the same field presented in Fig. 9.17. Well 1 is the same well shown in Fig. 9.17, but with a longer production history. Example 9.4.1. Adapted from Emerick [123].

INTERNA

# 9.4.2.2 Mean Squared Error (MSE)

This metric evaluates whether the predicted data from the prior ensemble are biased compared to the observations. The MSE is calculated using the square of the Mahalanobis distance relative to the covariance C = ∆ D ∆ D   + C e :

$$
D ( m ) = ( d obs - g ( m ) ) ⊤ C - 1 ( d obs - g ( m ) ) . (9.7)
$$

The inverse of C can be computed using the procedures discussed in Chapter 8, Section 8.3. Alternatively, for the sole purpose of computing the MSE,

mD

mD

10 3

10 3

10 2

10 2

10 1

10 1

permi_001_prior

10 0

10 0

INTERNA

INTERNA

(a)

Permeability (prior)

(b)

Permeability (posterior)

![](<ensemble_data_assimilation_e-book_version_images/imageFile51.png>)

10 0

10 0

10 -1

10 -1

10 -2

10 -2

10 -3

10 -3

transi_001_prior

10 -4

10 -4

INTERNA

INTERNA

(c)

Transmissibility multiplier (prior)

(d)

Transmissibility multiplier (posterior)

(prior)

(posterior)



 

 DWHUFXW  







 

 DWHUFXW  













 7 PH GD V 



�����������

 

(e)

Water cut (Well 1)







 7 PH GD V 



�����������

(f)

Water cut (Well 2)

 

Fig. 9.18: Example of data assimilation with ES-MDA where the prior model predictions have been improved with the introduction of transmissibility multipliers across several faults mapped from seismic data. This is a later data assimilation study of the same field presented in Fig. 9.17. In this figure, Well 1 is the same well with data presented in Fig. 9.17, but with a longer production history. Red circles in (e) and (f) represent observed data, while gray and blue lines show predicted data from the prior and posterior ensembles, respectively. Example 9.4.1.

permi_001_post

transi_001_post

![](<ensemble_data_assimilation_e-book_version_images/imageFile114.png>)

![](<ensemble_data_assimilation_e-book_version_images/imageFile116.png>)

Well

mD

10 3

10 2

10 1

(a)

Permeability (prior)

mD

10 3

10 2

10 1

(b)

Permeability (posterior)

40000

(kPa)

30000

Pressure

20000

10000

INTERNA

0

1995

2003

Year

2011

(c)

Pressure (prior)

40000

(kPa)

30000

Pressure

20000

10000

2019

0

![](<ensemble_data_assimilation_e-book_version_images/imageFile52.png>)

1995

2003

Year

2011

2019

(d)

Pressure (posterior)

Fig. 9.19: Example of data assimilation with ES-MDA where the data are inconsistent with the prior ensemble. The observed bottom-hole pressure in a particular well fell completely outside the predicted range of the prior ensemble. Consequently, data assimilation led to an unrealistic reduction in permeability around the well location. Subsequent investigation revealed inconsistencies in the water injection specified for a nearby well in the model. Example 9.4.1.

INTERNA

it is sufficient to use only the diagonal terms

$$
C = ⎡ ⎢ ⎣ V [ g 1 ( m )] + σ 2 e, 1 0 . . . 0 V [ g N d ( m )] + σ 2 e,N d ⎤ ⎥ ⎦ (9.8)
$$

and compute the MSE as

$$
MSE = D ( m ) N d . (9.9)
$$

Based on the value of MSE, we classify the ensemble as follows:

≤ 1.

• OK: MSE

1 &lt; MSE ≤ 2.

• Fair:

&gt; 2.

• Biased: MSE

Instead of using MSE, we can apply the chi-square hypothesis test. In this approach, we define the null hypothesis as “ d obs is a sample from N ( g ( m ) , C ).” The metric D ( m ) follows a chi-square distribution with N d degrees of freedom, χ 2 N d . The CDF of χ 2 N d is given by

$$
P χ ( D ( m )) = 1 Γ ( N d / 2) γ ( N d 2 , D ( m ) 2 ) , (9.10)
$$

where Γ ( · ) is the Gamma function and γ ( · , · ) is the lower incomplete Gamma function. The p -value of the null hypothesis is

$$
p = 1 - P χ ( D ( m )) . (9.11)
$$

If p &gt; p 0 (say p 0 = 0 . 05), the null hypothesis is true.

# 9.4.2.3 Example: OC and MSE

Fig. 9.20 displays the predicted water cut for three wells in an oilfield in the Campos Basin, along with their corresponding OC and MSE values. Strictly speaking, the prior ensemble only passes the quality test for the first well. However, in practice, it can be challenging and time-consuming to create a prior ensemble that meets the quality criteria for all wells. These metrics are not strict thresholds but rather indicators of ensemble quality. They can be computed on a well-by-well basis, as shown in Fig. 9.20, for a group of wells or even for the entire field, providing a global assessment. Using these metrics also helps to track improvements in prior modeling.

# 9.4.3 Plausibility of the Posterior Realizations

Validating the results can pose challenges, especially concerning the plausibility of the posterior models due to the numerous realizations involved. It is essential to evaluate the statistical properties of all data assimilation parameters by comparing them before and after assimilation. Calculating metrics that assess the overall changes in the models can be helpful in this regard. However, a comprehensive and thoughtful evaluation of the posterior models necessitates the collaboration of a multidisciplinary team.







![](<ensemble_data_assimilation_e-book_version_images/imageFile117.png>)

 

 

 

    DWHUFXW  

    DWHUFXW  

    DWHUFXW  

���

���

���

���

���

���

���

���

���

 

   



����





����

����



 

����

����







����

����

 



 

����







����

����

 





  7 PH GD V 

    7 PH GD V 

    7 PH GD V 

(a)

Well 1

(b)

Well 2

(c)

Well 3

= 1 . = 0

28

= 1 . = 3

02

= 0 . =

61

OC MSE

00

(Excellent) (OK)

OC MSE

00

(Excellent) (Biased)

OC MSE

61 10

(Poor) 45 (Biased)

.

28

.

02

.

45

MSE

.

(OK)

MSE

.

(Biased)

MSE

.

(Biased)

Fig. 9.20: Examples of predicted water cut for wells from a field in the Campos Basin with varying levels of OC and MSE . Red dots are the observed data points. The error bars in the observations correspond to one standard deviation of the data error. Light blue lines are the predicted data from the prior ensemble. The green line is the average prediction. Example 9.4.2.3.

# 9.4.3.1 Normalized Model Change (NMC)

We can calculate the differences between the posterior and prior realizations to identify areas where the model has undergone significant modifications. Standardizing these changes by dividing them by the prior standard deviation is recommended in this context. The NMC metric summarizes these model changes:

$$
NMC = 1 N m N m ∑ i =1 ∣ ∣ ∣ ∣ m c ,i - m i σ m,i ∣ ∣ ∣ ∣ , (9.12)
$$

where m i and m c ,i represent the i th values of the model parameter before and after data assimilation, respectively. σ m,i denotes the corresponding prior standard deviation. A NMC value of 1 indicates an average change approximately equal to one standard deviation of the prior uncertainty.

# 9.4.3.2 Cosine Similarity (CS)

Another valuable measure for assessing the similarity between two models is the cosine similarity (CS). It calculates the cosine of the angle between two vectors, indicating whether these vectors are aligned in a similar direction, i.e.

$$
CS = m ⊤ m c ‖ m ‖‖ m c ‖ ∈ [ - 1 , 1] , (9.13)
$$

where m and m c are the prior and posterior realizations, respectively. In this context, CS = 1 indicates that the two models are identical.

# 9.4.3.3 Facies Overlap Coefficient (FOC)

For categorical or discrete properties such as facies, a useful metric for evaluating the similarity between two models is the overlap coefficient:

$$
FOC ( m i , m j ) = { 1 if m i = m j 0 otherwise. (9.14)
$$

We can use the average FOC for the model as a measure of similarity between prior and posterior realizations.

# 9.4.3.4 Normalized Variance (NV)

For linear-Gaussian problems, it can be shown that the posterior covariance, C m c , has the form [334]:

$$
C m c = C m - C m G ⊤ ( C e + GC m G ⊤ ) - 1 GC m = C m - ∆ C m . (9.15)
$$

The matrix ∆ C m is real symmetric positive semidefinite, ensuring all diagonal entries are nonnegative. Let c i , c   i , and δc i denote the i th diagonal entry of C m , C m c , and ∆ C m , respectively. The normalized variance, NV i , of the i th model parameter m i is defined as:

$$
NV i = c ′ i c i = 1 - δc i c i . (9.16)
$$

NV i ranges between 0 and 1, providing a measure of the reduction in variance of m i due to data assimilation [334]. A NV i value of 1 indicates no reduction in uncertainty, while NV i = 0 signifies a complete collapse in the uncertainty estimate.

# 9.4.3.5 Example: Model Changes

Results Evaluation

0.00

0.05

0.35

0.30

0.35

0.30

3

2

1.00

0.90

0.25

0.20

0.15

0.10

0.05

0.25

0.20

0.15

0.10

0.05

1

0

1

2

0.80

0.70

0.60

0.50

0.40

0.00

0.00

3

0.30

0.10

1.0

(a)

Porosity (Prior)

(Prior)

0.15

0.00

0.20

0.05

0.25

0.10

1.2

(e)

Facies (Prior)

(Prior)

1.4

1.0

(b)

Porosity (Posterior)

(c)

Normalized changes

(Posterior)

changes

0.30

0.15

0.35 3

0.20

0.25

0.30

0.35 0 0.30

0

0.30

1 0.40

1

![](<ensemble_data_assimilation_e-book_version_images/imageFile53.png>)

3

0.25 2

0.30 1

2

2

1

1

(f)

Facies (Posterior)

(g)

(Posterior)

overlap

1.6

1.2

1.8

1.4

2.0 0.0

0.0

1.6

0.2

1.8

0.4

2.0

(d)

Normalized variance

variance

2 0.50

2

0.60

3

0.70

0.80

1

Facies overlap

0.6

0

0.8

1.0

0.90

Metric

Normalized model change Cosine similarity

Facies overlap

coefficient Average normalized variance

Average normalized variance

Value

0.739 0.968

0.868

0.849

0.849

Fig. 9.21: Example of model changes after data assimilation with ES-MDA in a turbidite reservoir in the Campos Basin. Example 9.4.3.5.

1.00

# 9.4.4 Data-Mismatch Objective Function

The data-mismatch objective function divided by the number of data points serves as a useful metric to quantify the quality of data matching:

$$
O N,d ( m ) = 1 2 N d ( d obs - g ( m )) ⊤ C - 1 e ( d obs - g ( m )) . (9.17)
$$

For diagonal C e , O N,d reduces to

$$
O N,d ( m ) = 1 2 N d N d ∑ i =1 ( d obs ,i - g i ( m ) σ e,i ) 2 . (9.18)
$$

The average objective function for posterior samples in linear-Gaussian problems is expected to be around 1/2 [330]. However, achieving this level of objective function is typically observed only in controlled synthetic problems where model and data uncertainties are well characterized and significant model errors are absent. Establishing stringent criteria for data matching quality in real-world field applications can be challenging and subjective, as terms like “good” or “acceptable” data matches vary depending on context. Experienced practitioners emphasize the importance of aligning evaluation criteria with the study’s objectives when assessing model adequacy.

Nevertheless, the objective function defined in Eq. (9.18) provides a valuable reference point. One useful interpretation of O N,d ( m ) values is how they compare to the standard deviation of the observation error. For instance, if the absolute difference | d obs ,i − g i ( m ) | in (9.18) equals σ e,i for all data points, then O N,d ( m ) = 0 . 5. Similarly, mismatches of 2 σ e,i or 3 σ e,i correspond to O N,d ( m ) = 2 and O N,d ( m ) = 4 . 5, respectively (see Fig. 2.17, Chapter 2). Higher values of O N,d ( m ) may indicate the need to re-evaluate the validity of the data assimilation process, including prior modeling or the possibility that data-error covariances have been underestimated.

# 9.4.4.1 Example: Data Mismatch Objective Function

INTERNA

0.8

cut

0.6

Water

0.4

0.2

0 0

0

0.8

cut

0.6

Water

0.4

0.2

1000

(a)

O

3000

2000

Time (days)

m

= 0 .

INTERNA

)

48

N,d (

INTERNA

4000

0 0

0

1000

(b)

O

3000

2000

Time (days)

m

= 4 .

40

)

40

N,d (

4000

INTERNA

![](<ensemble_data_assimilation_e-book_version_images/imageFile54.png>)

0.8

cut

0.6

Water

0.4

0.2

0 0

0

3000

4000

1000

2000

Time (days)

(c)

m

O

N,d (

= 12 .

INTERNA

)

80

INTERNA

0.8

cut

0.6

Water

0.4

0.2

0 0

0

1000

3000

2000

Time (days)

(d)

m

= 60 .

40

)

O

40

N,d (

4000

Fig. 9.22: Example of predicted water cut data for well in the Campos Basin with corresponding values of data mismatch objective function. The error bars correspond to ± σ e,i , which were defined as 10% of the data values (with a minimum of 0.01). Example 9.4.4.1. Adapted from Emerick [123].

# 9.5 Field Examples

This section presents three data assimilation case studies from real petroleum reservoirs. The first case involves a field with a long production history, demonstrating the effectiveness of data assimilation in problems with a large number of production data points. The second case focuses on a carbonate reservoir, highlighting the assimilation of 4D seismic data. The third case illustrates the data assimilation involving facies updates. It is important to note that these cases were not designed specifically as examples for this book. They represent actual applications conducted by teams of engineers and geoscientists. Therefore, these examples should not be viewed as ideal applications or for drawing generalized conclusions about performance. Instead, they should be considered in the context of real-world applications, which are often constrained by practical factors such as strict deadlines and specific study objectives.

# 9.5.1 Field 1

The first example pertains to a mature oilfield in the Campos Basin operating with water injection for more than 32 years. This field is characterized by a turbidite reservoir with poorly consolidated sandstones, low clay content, and high permeability [47, 221]. The simulation model consists of 332 × 376 × 18 gridblocks (502,389 active). The reservoir fluid is modeled using a black-oil formulation. Production data includes quarterly measurements of water cut and gas-oil ratio from 121 wells, as well as pressure data collected during well shutdown periods. The data-error covariance matrix was assumed diagonal with standard deviations computed as 10% of the corresponding water cut values, with a minimum limit of 0.01. For gas-oil ratio data, an error standard deviation of 20% was assumed. Additionally, a constant value of 1,000 kPa was used for the pressure data. These data were assimilated using 10 ES-MDA iterations with constant inflation factors and Kalman gain localization to update 100 realizations.

The data assimilation parameters include porosity, horizontal, and vertical permeability for each gridblock of the model. Additionally, vertical transmissibility multipliers between the main geological formations were used to account for the presence of thin shale barriers. During data assimilation, the logarithm of permeabilities and transmissibility multipliers were adjusted. Other data assimilation parameters include rock compressibility, transmissibility multipliers across 50 faults, and Corey exponents of oil-water relative permeability curves.

Fig. 9.23 shows the evolution of the data-mismatch objective function throughout the ES-MDA iterations. The average objective function decreased significantly from an initial value of 47.18 to a final value of 5.14, indicating a substantial improvement in the data-match quality of the models. This improvement is further illustrated in Fig. 9.24, which presents the production data from four wells in the field. Each plot includes the observed data along with the predicted data from both the prior and posterior models.

Analyzing the metrics for the prior ensemble reveals that the observation coverage for the entire field is 0.84, indicating that 84% of the observed data points fall within the range of predicted data with the prior ensemble. A well-by-well analysis shows that 21% of the wells have poor observation coverage (OC &lt; 0 . 7), while 56% exhibit excellent coverage (OC &gt; 0 . 95). The overall mean squared error is 3.0, classifying the prior ensemble as biased, as discussed in Section 9.4.2.2.

Fig. 9.25 depicts the posterior mean values of the transmissibility multipliers across the 50 faults mapped in this field. The faults are ranked based on their multiplier values and categorized as closed, partially sealed, or open to flow.

Fig. 9.26 shows the first two realizations of porosity, horizontal permeability, and vertical transmissibility multipliers before and after data assimilation. Local changes in rock properties, particularly permeability and

 

![](<ensemble_data_assimilation_e-book_version_images/imageFile120.png>)

 2E HFW YHIXQFW RQ



3U RU









  WHUDW RQ



 

 

 

3RVW

���������

Fig. 9.23: Evolution of the data-mismatch objective function for Field 1.

![](<ensemble_data_assimilation_e-book_version_images/imageFile121.png>)

 

 

 

 DWHUFXW  

 DWHUFXW  





























 7 PH GD V 

 









 7 PH GD V 

 



�����������

�����������

(a)

Well 1 (Water cut)

(b)

Well 2 (Water cut)





 

 DVR  UDW R PP 





3UHVVXUH 03D 









 









 

 

�





 7 PH GD V 

 





�





 7 PH GD V 

 





�����������

�����������

(c)

Well 3 (Gas-oil ratio)

(d)

Well 4 (Pressure)

![](<ensemble_data_assimilation_e-book_version_images/imageFile122.png>)

Closed

Open

Partially sealing faults

faults

faults

1

Transmissibility multiplier

0.1

0.01

0.001

0.0001

1

5

10

15

20

25

30 number

35

40

45

50

Fault

INTERNA Fig. 9.25: Posterior mean transmissibility multipliers across faults for Field 1.

transmissibility multipliers, are evident. Despite these updates, the posterior realizations preserve the main characteristics of the corresponding prior models, which is often considered empirical evidence of successful data assimilation. Just for reference, the average values of normalized model change and cosine similarity for this case are 0.540 and 0.997, respectively. The average normalized variance for the grid parameters is 0.8, indicating that significant variability was still present in the posterior ensemble.

There are numerous other results and aspects of this case that could be explored further. The results presented in Figs. 9.23 through 9.26 were selected solely to illustrate the overall application.

0.2 0.3

0.1

0

0

(a)

Porosity (prior 1)

INTERNA

INTERNA

0.2 0.3

0.1

0

0

(b)

Porosity (post 1)

INTERNA

0.2 0.3

0.1

0

0

(c)

Porosity (prior 2)

INTERNA

0.2 0.3

0.1

0

0

(d)

POR 001 prior Porosity (post 2)

POR 001 prior

POR 001 post

![](<ensemble_data_assimilation_e-book_version_images/imageFile55.png>)

10 mD

4

10 3

10 2

10 1

10 mD

4

10 3

10 2

10 1

10 mD

4

10 3

10 2

10 1

10 mD

4

10 3

10 2

10 1

(e)

Permeability (prior 1)

(prior 1)

INTERNA

(f)

Permeability (post 1)

(post 1)

INTERNA

(g)

Permeability (prior 2)

(prior 2)

INTERNA

PERMI (h)

001 prior Permeability (post 2)

PERMI 001 prior

(post 2)

INTERNA

PERMI 001 post

10 0

10 -1

10 -2

10 -3

10 0

10 -1

10 -2

10 -3

10 0

10 -1

10 -2

10 -3

10 0

10 -1

10 -2

10 -3

(i)

Transmissibility multiplier (prior 1)

INTERNA

INTERNA

(j)

Transmissibility multiplier (post 1)

INTERNA

INTERNA

(k)

Transmissibility multiplier (prior 2)

INTERNA

INTERNA

(l)

TRANSK 001 prior Transmissibility multiplier (post 2)

TRANSK 001 prior

INTERNA

INTERNA

TRANSK 001 post

# 9.5.2 Field 2

The second field example involves a giant carbonate reservoir in Brazil’s presalt region. The reservoir model for this field is discretized into 217 × 362 × 71 gridblocks, incorporating dual porosity and dual permeability to simulate flow in the fracture system. Including both matrix and fractures, the total number of active gridblocks is 2,150,510. The fluid model is compositional with nine pseudo-components. Data assimilation involved using 200 realizations of the geological model to calibrate the porosity of the rock matrix, as well as the horizontal and vertical permeability of both the matrix and fractures. Additionally, the parameters for the oil-water and gas-liquid relative permeability curves were adjusted during data assimilation. Production in this field commenced in 2009 through an extended well test, and currently, over 100 wells operate in this field. The production data used in the data assimilation consists of monthly measurements of water cut, gas-oil ratio, and pressure data during well shutdown periods. The data-error covariance matrix for production data was assumed to be diagonal, with a standard deviation of 10% for water cut and gas-oil ratio data values. For pressure measurements, a constant value of 200 kPa was assumed.

In 2015, this field became the focus of a pioneering pilot project to assess the feasibility of 4D seismic technology for monitoring water-alternating-gas (WAG) injection in ultradeep offshore reservoirs with complex overburden and low-compressibility rocks. Data collection for the project included base and monitor surveys acquired two years apart using ocean bottom nodes (OBN) technology. The results from this pilot project demonstrated the effectiveness of OBN surveys for production monitoring in pre-salt reservoirs [97].

Although the 4D data is limited to the central part of the field, the model of the entire field was updated by assimilating production data from all wells. However, here, the focus is on the results within the pilot area, which includes six oil-producing wells, two water injection wells, four gas injection wells, and two WAG wells, as illustrated in Fig. 9.27.

The 4D seismic data consist of a normalized map depicting hardening and softening anomalies. These data were compared to simulated maps of P-impedance differences between the monitor and base dates, normalized by the base survey. To achieve this, the simulation models were integrated with a PEM based on the Gassmann equation to compute the predicted impedance response. An upscaling process using weighted averaging across the reservoir thickness was employed to compute predicted seismic maps. The PEM utilizes empirical correlations derived from experimental data to estimate the elastic properties of the dry-rock frame (Fig. 9.28), and a cubic equation of state, calibrated with experimental data, to estimate the fluid properties.

Fig. 9.34a illustrates the observed seismic data, highlighting primary time-lapse anomalies. The majority of these anomalies fall within the range

0.01 0.02

0

- 0.01
- 0.02
- 0.02


IG3

P2

P3

IG4

IW1

![](<ensemble_data_assimilation_e-book_version_images/imageFile56.png>)

WAG2

IG1

P4

IW2

P1

WAG1

P5

IG2

P6

Fig. 9.27: Observed 4D seismic data showing normalized P-impedance changes for Field 2. Wells P1–P6 are producers, IW1 and IW2 are water injectors, IG1–IG4 are gas injectors, WAG1 and WAG2 are water-alternating-gas injectors.

![](<ensemble_data_assimilation_e-book_version_images/imageFile125.png>)

1.1

70

Bulk (model)

60

1.05

Bulk (lab)

Dry Rock Moduli (GPa)

Dry Muduli Correction

50

Shear (model)

1

Shear (lab)

40

0.95

Bulk (model)

30

Bulk (lab)

0.9

20

Shear (model)

Shear (lab)

0.85

10

0 0

0.8 0

0

0.05

0.1

0.15

0.2

0.25

0

10

20

30

40

50

Porosity

Effective Pressure (MPa)

(a)

(b)

INTERNA \ Força Porosity

INTERNA \ Força de Trabalho Effective pressure

de Trabalho

INTERNA \ Força de Trabalho

#

#

Fig. 9.28: Empirical correlations used in the PEM to estimate elastic properties of the dry rock frame for Field 2.

of [ − 0 . 02 , 0 . 02], which may appear small given the stiffness of carbonate rocks. However, the high-quality OBN acquisitions ensured well-defined time-lapse anomaly images. In the figure, hardening anomalies (blue scale) are primarily associated with water injection from wells IW1, IW2, and WAG1, while softening anomalies (red scale) relate to gas injection. Hardening around gas injector IG1 results from injected CO 2 , denser than reservoir fluid at current pressure. During data assimilation, seismic data-error covariance assumed a diagonal matrix with a constant standard deviation of 0.004. Emerick and Neto [125] considered the same field problem using the data projection method mentioned in Section 9.3.2 to estimate the data-

Fig. 9.29 shows the evolution of the data-mismatch objective functions for production and 4D seismic data. The average objective function for production data decreased from 120.0 to 13.0, while the objective function for 4D seismic data reduced from 6.5 to 2.0. It is noteworthy that the final production data objective function exceeds the 4.5 limit, corresponding to a three standard deviation, as discussed in Section 9.4.4. Additionally, tests with further ES-MDA iterations showed only marginal reductions. These results suggest that there is still room for improvement in the model by revisiting the initial steps of the process.

![](<ensemble_data_assimilation_e-book_version_images/imageFile126.png>)

 2E HFW YHIXQFW RQ

 2E HFW YHIXQFW RQ





 

 

3U RU





  WHUDW RQ





3RVW

3U RU





  WHUDW RQ





3RVW

���������

���������

(a)

(b)

Production

4D seismic

Fig. 9.29: Evolution of the data-mismatch objective function for Field 2.

Fig. 9.30 shows the porosity and horizontal permeability of the first layer in the first two realizations of the prior and posterior ensembles. Evident changes in the petrophysical properties are observed as a result of data assimilation, although the main characteristics of the prior realizations are preserved in the posterior ones. It is noteworthy that the two posterior models presented in this figure look remarkably similar to each other, indicating that a significant portion of the ensemble variability was lost in the process. Fig. 9.31 shows images of normalized variance, which corroborates this indication.

0.16

0.16

0.0 0.04 0.08 0.12

0.04

0.0

0.08 0.12 0.16

0.12

0.0 0.04

0.04

0.0

INTERNA

0.16

0.16

0.0 0.04 0.08 0.12

0.04

0.0

(a)

Porosity (Prior 1)

INTERNA

0.16

0.16

0.0 0.04 0.08 0.12

0.04

0.0

(b)

POR 001 PRIOR Porosity (Prior 2)

POR 001 PRIOR

(c)

Porosity (Posterior 1)

(d)

POR 001 POST Porosity (Posterior 2)

POR 001 POST

INTERNA

INTERNA

![](<ensemble_data_assimilation_e-book_version_images/imageFile57.png>)

10 10 mD

10 10 mD

10 2 3 4

10 2 3 4

10 3

10 3

10 0 10 1

10 0 10 1

10 1

10 1

10 0

10 0

INTERNA

10 10 mD

10 4

4

10 0 10 1 10 2 3

10 1

10 0

(e)

Permeability (Prior 1)

INTERNA

10 10 mD

10 4

4

10 0 10 1 10 2 3

10 1

10 0

(f)

PERMI 001 PRIOR Permeability (Prior 2)

PERMI 001 PRIOR

POR

POR

PERMI

(g)

Permeability (Posterior 1)

(h)

PERMI 001 POST Permeability (Posterior 2)

PERMI 001 POST

INTERNA

INTERNA

INTERNA INTERNA Fig. 9.30: First two realizations of porosity and horizontal permeability for Field 2.

PERMI

1

1

0 0.25 0.5 0.75

0.25

0

1

1

0 0.25 0.5 0.75

0.25

0

![](<ensemble_data_assimilation_e-book_version_images/imageFile58.png>)

(a)

Porosity

(b)

POR NV Permeability

POR NV

INTERNA

INTERNA

INTERNA INTERNA Fig. 9.31: Normalized variance of porosity and horizontal permeability for Field 2.

Fig. 9.32 illustrates two sets of oil-water relative permeability curves for this field. The final curves still show considerable variability compared to the prior ones. This result was achieved by applying an ad hoc localization coefficient of 0.1 for these parameters during data assimilation [123].

![](<ensemble_data_assimilation_e-book_version_images/imageFile129.png>)





     5H DW YHSHUPHDE   W 

     5H DW YHSHUPHDE   W 

���

���

���

���

���

���

���

���









���

���

 





���

���



   6DWXUDW RQ

  6DWXUDW RQ

(a)

Region 1

(b)

Region 2

Fig. 9.32: Two oil-water relative permeability curves for Field 2. The blue and green lines represent the posterior water and oil relative permeability curves, respectively, while the grey lines indicate the prior estimates.

good illustration of this achievement. Nevertheless, this does not imply that the entire data assimilation process is complete. In reality, reservoir modeling should be seen as a continuous process, with each cycle of assimilation revealing more about the field and generating feedback for the next round of models.

 



![](<ensemble_data_assimilation_e-book_version_images/imageFile130.png>)

 



 DVR  UDW R PP 





3UHVVXUH 03D 





















 

 

�







 7 PH GD V 









�







 7 PH GD V 









�����������

�����������

(a)

P1 (Gas-oil ratio)

(b)

P2 (Pressure)

 

 

 

 





 DWHUFXW  

 DWHUFXW  





















 

 

�







 7 PH GD V 









�







 7 PH GD V 









�����������

�����������

(c)

P3 (Water cut)

(d)

P4 (Water cut)

Fig. 9.33: Production data for four wells of Field 2. Red circles represent observed data, while gray and blue lines show predicted data from the prior and posterior ensembles, respectively. The error bars in the observed data points correspond to one standard deviation of the data error. Vertical dashed lines indicate the times of the base and monitor surveys.

Figs. 9.34b and 9.34c show the predicted 4D seismic data from the first two realizations of the ensemble before data assimilation, whereas Figs. 9.34d and 9.34e display the corresponding results after data assimilation. The posterior models exhibit significant improvements in the predicted 4D data, achieved through a better representation of overall pore pressure, a more accurate distribution of water-flooded areas, particularly near P4 and P5, and a better depiction of the region with increased gas saturation around well WAG2.

0.01 0.02

0.01

-0.01 0

-0.01

-0.02

0.01 0.02

0.01

0

0

-0.02 -0.01

IW1

P4

IW2

P5

Practical Aspects and Field Examples

IG3

P3

P2

WAG2

IG4

IG1

P6

P1

WAG1

IG2

INTERNA

(a)

Observed

0.02

0 0.01 0.02

0

-0.01

-0.02 -0.01

![](<ensemble_data_assimilation_e-book_version_images/imageFile59.png>)

0.02

0.02

INTERNA -0.01 0 0.01

-0.01

- 0.02
- 0.02


(b)

Prior 1

0.02

0.02

INTERNA -0.01 0 0.01

-0.01

- 0.02
- 0.02


(c)

Prior 2

DIMPP 001 PRIOR

(d)

Posterior 1

(e)

Posterior 2

INTERNA INTERNA Fig. 9.34: Predicted P-impedance changes for the first two realizations before and after data assimilation in Field 2.

INTERNA

INTERNA

DIMPP 001 POST

# 9.5.3 Field 3

The third field example is also an offshore oilfield located in the Campos Basin. In this field, the reservoir consists of a sequence of amalgamated channels deposited in a turbidite system, characterized by numerous faults and structural discontinuities. This field was selected as an example due to the inclusion of facies updates during data assimilation. The simulation model is composed of 147 × 153 × 47 gridblocks, totaling 380,749 active gridblocks. The reservoir fluid is modeled using a black-oil formulation. Observed production data includes quarterly water cut measurements over a 38-year production period, along with a few isolated static pressure measurements.

The initial ensemble of facies was constructed by the field geologist using sequential indicator simulation (SIS) [7, 104] with locally varying azimuths [43]. These facies realizations were converted into a TPG parametrization following the procedure outlined in [123]. Fig. 9.35 illustrates the rock-type rule and the latent variables, z 1 and z 2 , used to generate the facies realization. The truncation thresholds in the rock-type rule were determined by solving optimization problems to match the facies proportions of the original SIS realizations.

The data assimilation parameters include the latent variables z 1 and z 2 , as well as the porosity, horizontal, and vertical permeability for the facies “coarse sand” and “sand.” The porosity and permeability for the facies “cemented” and “non-reservoir” are assumed to be zero. Other data assimilation parameters include scalar variables defining rock compressibility, the oilwater relative permeability curve, and the transmissibility multiplier across 126 faults.

The data assimilation used 16 ES-MDA iterations with constant inflation factors and Kalman gain localization to update an ensemble with 200 realizations. Fig. 9.36 shows the evolution of the data mismatch objective function. The average objective function reduced from an initial value of 18.4 to 3.1. Fig. 9.37 illustrates the improvements in the predicted water cut data for four wells in this field. For this field case, the overall observation coverage is 0.91, which is classified as “good” according to the criteria presented in Section 9.4.2. The mean squared error is 2.11, which is slightly above the threshold to be classified as “biased.” It is interesting to note that none of the three field examples presented in this chapter started the data assimilation with prior ensembles having observation coverage classified as “excellent” and mean squared error classified as “OK.” This underscores the challenges involved in modeling reservoirs in operational settings. In this third field example, the ad hoc procedure described in Section 9.3.1 was used to increase the data-error standard deviation. This effect is noticeable for Well 2 (Fig. 9.37b) in the period between 10,000 and 12,000 days, where larger error bars are shown.

Z1 001 prior

3

3

0

0

-3

-3

[ht!]

[ht!] INTERNA

INTERNA

(a)

z 1

1

![](<ensemble_data_assimilation_e-book_version_images/imageFile60.png>)

Facies 001 prior

Non-res

Coarse sand Sand

Cemented

Non-res

Non-res

INTERNA

(b)

z 2

2

Coarse sand

Sand

Cemented

(c)

Facies INTERNA

INTERNA

(d)

Rock-type rule

Fig. 9.35: Illustration of the TPG scheme used to parameterize the facies realizations with two latent variables, z 1 and z 2 . The rock-type rule in (d) is applied to truncate z 1 and z 2 , defining four facies types. The specific values of the truncation thresholds vary across the reservoir to reproduce a non-stationary distribution of facies proportions. Field 3.

![](<ensemble_data_assimilation_e-book_version_images/imageFile133.png>)

 2E HFW YHIXQFW RQ



 

3U RU 











 

   WHUDW RQ

 











 3RVW

���������

Fig. 9.36: Evolution of the data-mismatch objective function for Field 3.





![](<ensemble_data_assimilation_e-book_version_images/imageFile134.png>)

 

 

 DWHUFXW  

 DWHUFXW  













 

 

����





  7 PH GD V 







����





  7 PH GD V 







�����������

�����������

(a)

Well 1

(b)

Well 2





 

 

 DWHUFXW  

 DWHUFXW  













 

 

����





  7 PH GD V 







����





  7 PH GD V 







�����������

�����������

(c)

Well 3

(d)

Well 4

Fig. 9.37: Water cut data for four wells of Field 3. Red circles represent observed data, while gray and blue lines show predicted data from the prior and posterior ensembles, respectively. The error bars in the observed data points correspond to one standard deviation of the data error.

Facies 001 prior

Facies 002 prior

INTERNA

INTERNA

Coarse sand

Sand Cemented

Cemented

Non-res

INTERNA

Coarse sand

Sand Cemented

Cemented

Non-res

(a)

Facies (Prior 1)

(b)

Facies (Prior 2)

![](<ensemble_data_assimilation_e-book_version_images/imageFile61.png>)

Facies 001 post

Coarse sand

Coarse sand

Sand Cemented

Sand Cemented

Cemented

Cemented

Non-res

Non-res

INTERNA

(c)

Facies (Posterior 1)

(d)

Facies (Posterior 2)

Facies 002 post

Fig. 9.38: First two facies realizations before and after data assimilation for Field 3.

Fig. 9.40 illustrates the relative permeability curves before and after data assimilation. The final ensemble essentially converged to nearly identical curves. This situation is common in reservoir data assimilation cases, as these parameters strongly impact scenarios involving breakthrough of injected fluids. In this particular field, this result does not seem surprising, given the 38-year production history with water breakthroughs in all oilproducing wells.

PROB FACIES 1 PRIOR

PROB FACIES 2 PRIOR

INTERNA

INTERNA

1

0.8

0.6

0.4

0.2

0

INTERNA

1

0.8

0.6

0.4

0.2

0

(a)

Coarse sand (Prior)

(b)

Sand (Prior)

![](<ensemble_data_assimilation_e-book_version_images/imageFile62.png>)

PROB FACIES 1 POST

1

1

0.8

0.8

0.6

0.6

0.4

0.4

0.2

0.2

0

0

INTERNA

(c)

Coarse sand (Posterior)

(d)

Sand (Posterior)

PROB FACIES 2 POST

Fig. 9.39: Probability of occurrence for facies “coarse sand” and “sand” before and after data assimilation for Field 3.

![](<ensemble_data_assimilation_e-book_version_images/imageFile137.png>)

 

5H DW YHSHUPHDE   W 





















 6DWXUDW RQ



 

 

����������

Fig. 9.40: Oil-water relative permeability curves for Field 3. The blue and green lines represent the posterior water and oil relative permeability curves, respectively, while the grey lines indicate the prior estimates.

# 9.6 Representative Models

As a final discussion in this chapter, it is important to address the use of representative models. A common practice in the industry involves selecting certain model realizations as “representative” of percentiles such as p10, p50, and p90 for decision-making.

While discussing results at the p10, p50, and p90 estimates is logical, the selection of representative models is highly questionable. The core issue with this approach is that different models can produce similar forecasts for one quantity while showing vastly different forecasts for other quantities of interest.

For example, Fig. 9.41a shows a plot of predicted cumulative oil production generated with an ensemble of model realizations for the PUNQ-S3 benchmark problem [150]. From this plot, three realizations were selected to represent the p10, p50, and p90 percentiles of cumulative production. The predicted cumulative productions of these models are highlighted in red, blue, and green in this plot. However, these realizations are no longer representative when analyzing another quantity of interest. For example, Fig. 9.41b shows a histogram of the original volume of oil in place (OIP) for the same ensemble. In this figure, the OIP values of the realizations representing cumulative production percentiles are indicated with colored vertical lines. Clearly, these realizations are not representative of the p10, p50, and p90 percentiles of OIP.

  

![](<ensemble_data_assimilation_e-book_version_images/imageFile138.png>)

�

P 3

6

10



&amp;XPX DW YHSURGXFW RQ 







 

�





����

����





  7 PH GD V 

(a)

Cumulative production



![](<ensemble_data_assimilation_e-book_version_images/imageFile139.png>)



 

   &amp;XPX DW YHIUHTXHQF 

5H DW YHIUHTXHQF 



���



���



���



 

���

��



 9R XPH

 6 P 3

 

 

10 6

3

  10

 

�

(b)

OIP

Fig. 9.41: Cumulative oil production and OIP for the PUNQ-S3 model. The red, blue and green lines in Panel (a) represents the predicted cumulative oil production from representative models of the percentiles p10, p50 and p90, respectively. The OIP of these models are indicated in the histogram in Panel (b) with the vertical lines. The red, blue and green circles indicate the p10, p50, and p90 values of OIP.

There are several publications in the literature proposing more robust strategies for selecting representative models from ensembles; see, e.g., [18,

394, 286] and references therein. The basic idea behind these methods is to select realizations considering multiple quantities of interest simultaneously.

However, the natural procedure in ensemble-based data assimilation is to utilize the entire ensemble of models to evaluate the uncertainty range for any quantity of interest. Nevertheless, fully adopting this ensemble-based approach can be more challenging than it appears. One major hurdle is the lack of methods and tools for analyzing and validating ensembles of models. Another challenge is the additional computational complexity involved in evaluating different operational conditions with ensembles. For example, optimization processes involving ensembles of models are exceptionally demanding in terms of computational resources [152, 397].

![](<ensemble_data_assimilation_e-book_version_images/imageFile140.png>)

A

# Elements of Linear Algebra

Abstract: This appendix summarizes key linear algebra concepts relevant to reservoir data assimilation.

# A.1 Preliminaries

This book adopts a standard notation where lowercase x represents a scalar, lowercase bold x represents a vector, and uppercase bold X represents a matrix. The vectors are always column vectors:

$$
x = ⎡ ⎢ ⎣ x 1 . . . x N ⎤ ⎥ ⎦ . (A.1)
$$

Often, matrices are written in terms of their columns as

$$
X = [ x 1 · · · x N ] , (A.2)
$$

where the j th column is the vector x j and the entry ( i,j ) is the scalar x ij . The product between two matrices C = AB is computed as

$$
c ij = ∑ k a ik b k,j . (A.3)
$$

If A is N 1 × N 2 and B is N 2 × N 3 , then C is N 1 × N 3 . Note that AB   = BA , i.e., matrix multiplication is, in general, not commutative. Matrix multiplication is distributive, A ( B + C ) = AB + AC , and associative, A ( BC ) = ( AB ) C .

̸

A   denotes the transpose of the matrix A . If A = A   we say that A is symmetric. The transpose of a product is

$$
( AB ) ⊤ = B ⊤ A ⊤ , (A.4)
$$

and the same is valid for vectors:

$$
( x ⊤ y ) ⊤ = y ⊤ x . (A.5)
$$

The inner (dot) product between two vectors is

$$
x ⊤ y = [ x 1 · · · x N ] ⎡ ⎢ ⎣ y 1 . . . y N ⎤ ⎥ ⎦ = N ∑ i =1 x i y i . (A.6)
$$

We prefer to use x   y to denote the inner product instead of notations such as x · y and   x , y   .

The matrix-vector product appears several times in this book

$$
Cx = y . (A.7)
$$

If the size of x is N x and the size of y is N y , then C is a N y × N x matrix. This product can be used to represent a system with N y linear equations and N x unknowns. The inverse of a square matrix C is denoted by C 1 and it is defined as

− the matrix such that 1 1

$$
C - 1 C = CC - 1 = I . (A.8)
$$

I is the identity matrix and has the same dimension of C and C − 1 .

Morrison-Woodbury formula: Let C be a N x × N x matrix, U and V be N x × N y matrices. Then, the following identity is true

$$
( C + UV ⊤ ) - 1 = C - 1 - C - 1 U ( I + V ⊤ C - 1 U ) - 1 V ⊤ C - 1 . (A.9)
$$

# A.2 Vector Spaces

Definition 1: A set V over a field F is said to be a vector or a linear space if

- 1. For x and y in V , x + y is an element of V and x + y = y + x .
- 2. For any x , y and z in V , ( x + y ) + z = x + ( y + z ).
- 3. There exists a unique vector 0 in V such that x + 0 = x for all x in V .


- 4. For each x in V , there exists a unique element − x in V such that x + ( − x ) = 0 .
- 5. For every pair of scalars α and β , ( αβ ) x = α ( β x ) and ( α + β ) x = α x + β x for every x in V .
- 6. For every scalar α and pair of elements x and y in V , α ( x + y ) = α x + α y .


Elements of V are referred to as vectors. If F is the set of real numbers, V is said to be real vector space. The vector space we are interested in here is the set of all N x -dimensional columns vectors in R N x , i.e., x ∈ R N x .

Definition 2: A real valued function   ·   defined on a vector space V is said to be a norm on V if

- 1.   x   ≥ 0 for every x in V and   x   = 0 if and only if x = 0 .
- 2. For every x in V and every scalar α ,   α x   = | α |  x   .
- 3. For every x and y in V ,   x + y   ≤   x   +   y   .


Some useful norms on R N x :

-  Euclidian norm (   2 ):

$$
‖ x ‖ 2 = ( N x ∑ i =1 x 2 i ) 1/2 = √ x ⊤ x . (A.10)
$$

-  Maximum norm (   ∞ ):

$$
‖ x ‖ ∞ = max 1 ≤ i ≤ N x | x i | . (A.11)
$$

-  p -norm (   p ):

$$
‖ x ‖ p = ( N x ∑ i =1 | x i | p ) 1 /p . (A.12)
$$

-  Mahalanobis distance [285]:


$$
‖ x ‖ C = √ x ⊤ Cx . (A.13)
$$

with C ∈ R N x × N x .

Definition 3: The determinant of a square matrix C , denoted det( C ), is a function that maps R N x × N x → R . The absolute value of det( C ) quantifies the extent to which the matrix C scales the volume of space. A det( C ) = 0 indicates that the matrix C collapses the space along at least one dimension, resulting in a loss of volume. Consequently, if det( C ) = 0, the matrix C is singular. Conversely, if det( C ) = 1, the matrix preserves the volume during transformation.

Definition 4: An eigenvalue and eigenvector of a square matrix C ∈

R N x × N x are a scalar λ and a non-zero vector x ∈ R N x such that

$$
Cx = λ x . (A.14)
$$

This equation can be written as

$$
( C - λ I ) x = 0 , x = 0 . (A.15)
$$

  =

This means that the matrix ( C − λ I ) is singular, hence

$$
det ( C - λ I ) = 0 . (A.16)
$$

The last equation forms a polynomial equation with degree N x . This means that C has N x eigenvalues (roots of the polynomial), counting multiplicities. Let Λ be the diagonal matrix containing the eigenvalues of C

N x × N x and X be the N x × N x matrix with the corresponding eigenvectors in its columns. We can write

$$
CX = XΛ . (A.17)
$$

If all the eigenvectors are linearly independent, then X − 1 exists and

$$
C = XΛX - 1 , (A.18)
$$

which is called eigenvalue decomposition of C , also known as spectral decomposition.

In this book, we are particularly interested in covariance matrices. These matrices are:

-  Real: C ∈ R N x × N x .
-  Symmetric: C = C   .
-  Non-singular: λ j &gt; 0, for j = 1 ,...,N x .


The eigenvalue decomposition of a non-singular covariance matrices have a nice property: the eigenvectors are orthogonal, which mean that

$$
C = XΛX ⊤ , (A.19)
$$

i.e., X   = X − 1 . Note that orthogonality is equivalent to write

$$
x ⊤ i x j = { 1 if i = j 0 if i = j. (A.20)
$$

i   =

Definition 5: A real symmetric matrix C is said to be positive definite if for every x ∈ R N x , x   Cx ≥ 0 and x   Cx = 0 if and only if x = 0 . We use the notation

$$
C ≻ O , (A.21)
$$

where O is the null matrix. C is said positive semidefinite if x   Cx ≥ 0 with x   Cx = 0 for some x   = 0 . We write

̸

$$
C ⪰ O .
$$

(A.22)

Lemma 1: Let C ∈ R N x × N x :

• If C is real symmetric, then the eigenvalues { λ j } N x j =1 of C are all real and C has a set of orthonormal eigenvectors, { x j } N x j =1 . • If C is positive definite, then all eigenvalues of C are positive and hence

C in nonsingular.

-  If C is real symmetric, then C is positive definite if and only if all eigenvalues of C are positive.
-  det( C ) is equal to the products of the eigenvalues of C .


Definition 6: The null (or kernel) space of C ∈ R N x × N x is the set of all vectors x ∈ R N x that satisfy Cx = 0 . The null space of C is denoted by N ( C ). The dimension of the null space is denoted by dim N ( C ) and it is referred to as the nullity of C .

Definition 7: The range (or column space) of C ∈ R N x × N x is the set of all vector y ∈ R N y that there exists at least one x ∈ R N x which satisfies Cx = y . The range is denoted by R ( C ). The dimension of the range is denoted by dim R ( C ) and it is called the rank of C . Two important results:

$$
dim R ( C ) = dim R ( C ⊤ ) (A.23)
$$

and

$$
dim R ( C ) + dim N ( C ) = N x . (A.24)
$$

Note that N x is the number of columns of C . For = 1 , let c denote the th

j ,...,N x j j column of the N y × N x matrix C , i.e.,

$$
C = [ c 1 c 2 · · · c N x ] . (A.25)
$$

For x ∈ R N x

$$
Cx = [ c 1 c 2 · · · c N x ] ⎡ ⎢ ⎢ ⎢ ⎣ x 1 x 2 . . . x N x ⎤ ⎥ ⎥ ⎥ ⎦ = N x ∑ j =1 x j c j . (A.26)
$$

Therefore y = Cx means that y is a linear combination of the columns of C .

Lemma 2: Let C ∈ R N y × N x and X ⊆ R N x be the vector space spanned by the columns of C . Then,

• Every vector in R ( C ) is a linear combination of the columns of C (vectors c j ’s). In other words, the range of C is identical to the span of { c j } N x j =1 .

• If n denotes the number of linearly independent columns of C , then dim R ( C ) = dim X = n and n ≤ N x . • In all cases, dim ( C ) min .

R ≤ { N y ,N x } • The following three statements are

equivalent:

(a) The set { c j } N x j =1 is linearly independent. (b) dim ( C ) = 0.

N

(c) dim R ( C ) = N x .

Lemma 3: Let C ∈ R N y × N x be the matrix mapping R N x → R N y :

-  The number of linearly independent columns of C is equal to N y , if and only if for every y ∈ R N y , there exists at least one x ∈ R N x which satisfy Cx = y . N
-  If N x &lt; N y , then there exists vectors y ∈ R y such that Cx = y has no solution.


Lemma 4: The following statements are equivalent:

-  Cx = y has a unique solution for every y ∈ R N y .
-  dim R ( C ) = N y and dim N ( C ) = 0. • dim ( C ) = and = ( C is


R N y N y N x square).

Lemma 5: Cx = y has more than one solution for every y ∈ R N y if and only if dim R ( C ) = N y and dim N ( C ) &gt; 0.

# A.3 Vector and Matrix Calculus

Let x ∈ R N x be a column vector

$$
x = ⎡ ⎢ ⎢ ⎢ ⎣ x 1 x 2 . . . x N x ⎤ ⎥ ⎥ ⎥ ⎦ = [ x 1 x 2 · · · x N x ] ⊤ (A.27)
$$

The gradient operator is also a column vector

$$
∇ = ⎡ ⎢ ⎢ ⎢ ⎢ ⎣ ∂ ∂x 1 ∂ ∂x 2 . . . ∂ ∂x Nx ⎤ ⎥ ⎥ ⎥ ⎥ ⎦ . (A.28)
$$

The gradient ∇ acts as N x -dimensional vector operator that can be applied to any 1 × N x matrices. Therefore, it does not make sense to write ∇ x , but we can write

$$
∇ x ⊤ = ⎡ ⎢ ⎢ ⎢ ⎢ ⎣ ∂ ∂x 1 ∂ ∂x 2 . . . ∂ ∂x Nx ⎤ ⎥ ⎥ ⎥ ⎥ ⎦ [ x 1 x 2 · · · x N x ] = ⎡ ⎢ ⎢ ⎢ ⎢ ⎣ ∂x 1 ∂x 1 ∂x 2 ∂x 1 · · · ∂x Nx ∂x 1 ∂x 1 ∂x 2 ∂x 2 ∂x 2 · · · ∂x Nx ∂x 2 . . . . . . . . . . . . ∂x 1 ∂x Nx ∂x 2 ∂x Nx · · · ∂x Nx ∂x Nx ⎤ ⎥ ⎥ ⎥ ⎥ ⎦ = ⎡ ⎢ ⎢ ⎢ ⎣ 1 0 · · · 0 0 1 · · · 0 . . . . . . . . . . . . 0 0 · · · 1 ⎤ ⎥ ⎥ ⎥ ⎦ = I . (A.29)
$$

The gradient of a real-valued function g ( x ) is a vector

$$
∇ g ( x ) = ⎡ ⎢ ⎢ ⎢ ⎢ ⎣ ∂g ( x ) ∂x 1 ∂g ( x ) ∂x 2 . . . ∂g ( x ) ∂x Nx ⎤ ⎥ ⎥ ⎥ ⎥ ⎦ , (A.30)
$$

and the Hessian matrix has the form

$$
B = ∇ [ ( ∇ g ( x )) ⊤ ] . (A.31)
$$

Let y = g ( x ) be a real-valued vector function. Then

$$
∇ g ( x ) ⊤ = ⎡ ⎢ ⎢ ⎢ ⎢ ⎣ ∂ ∂x 1 ∂ ∂x 2 . . . ∂ ∂x Nx ⎤ ⎥ ⎥ ⎥ ⎥ ⎦ [ g 1 ( x ) g 2 ( x ) · · · g N y ( x ) ] = ⎡ ⎢ ⎢ ⎣ ∂g 1 ( x ) ∂x 1 ∂g 2 ( x ) ∂x 1 · · · ∂g Ny ( x ) ∂x 1 . . . . . . . . . . . . ∂g 1 ( x ) ∂x Nx ∂g 2 ( x ) ∂x Nx · · · ∂g Ny ( x ) ∂x Nx ⎤ ⎥ ⎥ ⎦ = [ ∇ g 1 ( x ) ∇ g 2 ( x ) · · · ∇ g N y ( x ) ] ≡ G ⊤ . (A.32)
$$

Recall that it does not make sense to compute ∇ g ( x ).

We call the transpose of G   as the Jacobian or sensitivity matrix:

$$
G = ⎡ ⎢ ⎢ ⎣ ∂g 1 ( x ) ∂x 1 ∂g 1 ( x ) ∂x 2 · · · ∂g 1 ( x ) ∂x Nx . . . . . . . . . . . . ∂g Ny ( x ) ∂x 1 ∂g Ny ( x ) ∂x 2 · · · ∂g Ny ( x ) ∂x Nx ⎤ ⎥ ⎥ ⎦ . (A.33)
$$

Let f = f ( x ) and g = g ( x ) be N x -dimensional vectors, both vectors are function of x . Then

$$
∇ ( f ⊤ g ) = ∇ ( f ⊤ ) g + ∇ ( g ⊤ ) f . (A.34)
$$

For example, if b is a constant vector, then

$$
∇ ( b ⊤ x ) = ( ∇ b ⊤ ) x + ( ∇ x ⊤ ) b = b (A.35)
$$

and

$$
∇ ( x ⊤ b ) = ( ∇ x ⊤ ) b + ( ∇ b ⊤ ) x = b . (A.36)
$$

Let C be a N x × N x constant matrix. Then

$$
∇ ( x ⊤ Cx ) = ( ∇ x ⊤ ) Cx + [ ∇ ( Cx ) ⊤ ] x = Cx + [ ∇ ( x ⊤ C ⊤ )] x = Cx + [ ∇ ( x ⊤ ) C ⊤ + ∇ ( C ) x ] x = Cx + C ⊤ x . (A.37)
$$

If C is symmetric, i.e. C = C   , then ∇   x   Cx   = 2 Cx .

Derivative with Respect to a Matrix: Let X be a N 1 × N 2 matrix and f = f ( X ) be a real-valued function of X . Then, we define

$$
∂f ∂ X = [ ∂f ∂x ij ] , (A.38)
$$

which is a N 1 × N 2 matrix. For example, let X be a

N x × N x (square) and define

$$
f = tr ( X ) = N x ∑ i =1 x ii . (A.39)
$$

Then,

$$
∂f ∂ X = ∂ tr ( X ) ∂ X = [ ∂ ∑ N x i =1 x ii ∂x ij ] = I . (A.40)
$$

Let X be a N 1 × N 2 matrix and, C be a N 2 × N 1 constant matrix. Then

$$
∂ tr ( XC ) ∂ X = ∂ tr ( C ⊤ X ⊤ ) ∂ X = C ⊤ . (A.41)
$$

Also, if C is N 2 × N 2 real-symmetric constant matrix. Then and tr XCX  

$$
∂ tr ( XCX ⊤ ) ∂ X = 2 XC . (A.42)
$$

# A.4 Singular Value Decomposition

Let C ∈ R N y × N x . The singular value decomposition (SVD) of C is a decomposition as product of three matrices:

$$
C = UΣV ⊤ , (A.43)
$$

where U ∈ R N y × N y is the matrix with left singular vectors of C , V ∈ R N x × N x is the matrix with right singular vectors of C , and Σ ∈ R N y × N x is the matrix containing the singular values of C in its main diagonal. All singular values of C are non-negative.

-  If N y &lt; N x :

$$
Σ = ⎡ ⎢ ⎢ ⎢ ⎣ σ 1 0 · · · 0 0 · · · 0 0 σ 2 0 0 · · · 0 . . . . . . . . . . . . . . . 0 0 · · · σ N y 0 · · · 0 ⎤ ⎥ ⎥ ⎥ ⎦ (A.44)
$$

-  If N y = N x :

$$
Σ = ⎡ ⎢ ⎢ ⎢ ⎣ σ 1 0 · · · 0 0 σ 2 · · · 0 . . . . . . . . . 0 0 · · · σ N y ⎤ ⎥ ⎥ ⎥ ⎦ (A.45)
$$

-  If N y &gt; N x :


$$
Σ = ⎡ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎣ σ 1 0 · · · 0 0 σ 2 · · · 0 . . . . . . . . . 0 0 · · · σ N x 0 0 · · · 0 . . . . . . . . . 0 0 · · · 0 ⎤ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎦ (A.46)
$$

The matrices U and V are orthogonal, i.e.,

$$
UU ⊤ = U ⊤ U = I (A.47)
$$

and

$$
VV ⊤ = V ⊤ V = I . (A.48)
$$

Therefore,

$$
U ⊤ = U - 1 (A.49)
$$

and

$$
V ⊤ = V - 1 . (A.50)
$$

The product CC   is a N y × N y symmetric matrix and

$$
CC ⊤ = ( UΣV ⊤ ) ( UΣV ⊤ ) ⊤ = UΣV ⊤ VΣ ⊤ U ⊤ = UΣΣ ⊤ U ⊤ . (A.51)
$$

Note that ΣΣ   is a N y × N y diagonal matrix. Hence, U are eigenvectors of CC   and λ i = σ 2 i is an eigenvalue of CC   . The product C C is a symmetric matrix and

  N x × N x

$$
C ⊤ C = ( UΣV ⊤ ) ⊤ ( UΣV ⊤ ) = VΣU ⊤ UΣ ⊤ V ⊤ = VΣ ⊤ ΣV ⊤ . (A.52)
$$

Note that Σ   Σ is a N x × N x diagonal matrix. Hence, V are eigenvectors of C   C and λ i = σ 2 i is an eigenvalue of C   C . As opposed to the eigenvalue decomposition, the SVD exists for rectan-

gular and/or rank-deficient matrices. However, SVD and eigenvalue decomposition coincide for real symmetric positive-definite matrices. Let C be a real symmetric positive definite, then

$$
C = XΛX ⊤ (eigen-decomposition) (A.53)
$$

$$
C = UΣV ⊤ (SVD) (A.54)
$$

and U = V = X and Σ = Λ .

# A.5 Pseudoinverse

Let C ∈ R N y × N x . The Moore-Penrose pseudoinverse of a matrix C is defined as + − 1

$$
C + = lim α → 0 ( C ⊤ C + α I ) - 1 C ⊤ . (A.55)
$$

Practical algorithms to compute C + are based on SVD, in which case the pseudoinverse of C is + +

$$
C + = VΣ + U ⊤ , (A.56)
$$

where Σ + is the pseudoinverse of Σ , which is formed by replacing every nonzero diagonal entry by its reciprocal and transposing the resulting matrix.

Note that because of the orthogonality properties of U and V   , we have

$$
CC + = ( UΣV ⊤ ) ( VΣ + U ⊤ ) = UΣΣ + U ⊤ = UU ⊤ = I (A.57)
$$

and

$$
C + C = I . (A.58)
$$

Let C be a N x × N x positive-definite matrix, then the inverse C − 1 exists. Also 1 1

$$
CC - 1 = C - 1 C = I . (A.59)
$$

In this particular case, C − 1 = C + (the inverse and pseudoinverse of C coincide).

In many cases of practical interest, we want to keep only the N r nonzero singular values (and the corresponding singular vectors). Note that if C is N y × N x , then N r ≤ min { N y ,N x } . For the case with N y &lt; N x , C can be decomposed as

$$
C = UΣV ⊤ = [ U r . . . U 0 ] ⎡ ⎢ ⎢ ⎣ Σ r . . . 0 · · · · · · · · · 0 . . . 0 ⎤ ⎥ ⎥ ⎦ ⎡ ⎣ V ⊤ r · · · V ⊤ 0 ⎤ ⎦ C = U r Σ r V ⊤ r . (A.60)
$$

U r is N y × N r and U   r U r = I , but U r U   r   = I . V r is N x × N r and V   r V r = I , but V r V   r   = I . Σ r is a N r × N r matrix.

̸

̸

# A.5.1 Range, Null Space and Rank

Another application of the SVD is that it provides an explicit representation of the range and null space of a matrix C :

• U r forms a basis for R ( C ). • V forms a basis for ( C ).

0 N

As a consequence, the rank of C is equal to the number of nonzero singular values of C .

# A.5.2 Poor Conditioning

The conditioning indicates how rapidly a function value changes with respect to small changes in its arguments. Consider the function

$$
f ( x ) = C - 1 x . (A.61)
$$

We define the condition number of the matrix C , denoted as κ ( C ), as the ratio of the magnitude of the largest and the smallest eigenvalues

$$
κ ( C ) = | λ max | | λ min | . (A.62)
$$

When κ ( C ) is large, the function f ( x ) becomes particularly sensitive to errors in the argument.

# A.6 Square Root of a Matrix

Let C be a real N x × N x real symmetric positive definite matrix. C has only positive eigenvalues { λ j } N x j =1 with eigenvectors { x j } N x j =1 . Hence, we can write

$$
CX = XΛ , (A.63)
$$

where X is the N x × N x matrix with eigenvectors of C and Λ is the N x × N x diagonal matrix with eigenvalues of C . Recall that X is an orthogonal matrix, i.e., XX   = X   X = I . Therefore, we can write C as

$$
C = XΛX ⊤ . (A.64)
$$

Λ is a diagonal matrix, with elements greater than zero. Hence, we can define the square root of Λ , denoted by Λ 1/2 , as

$$
Λ 1/2 = ⎡ ⎢ ⎣ √ λ 1 . . . √ λ N x ⎤ ⎥ ⎦ (A.65)
$$

So we can write C as

$$
C = XΛ 1/2 Λ 1/2 X ⊤ = XΛ 1/2 ( X ⊤ X ) Λ 1/2 X ⊤ = ( XΛ 1/2 X ⊤ )( XΛ 1/2 X ⊤ ) = ( XΛ 1/2 X ⊤ ) 2 . (A.66)
$$

and its inverse as

$$
C 1/2 = XΛ 1/2 X ⊤ (A.67)
$$

$$
C - 1/2 = ( C 1/2 ) - 1 = XΛ - 1/2 X ⊤ . (A.68)
$$

Note that C 1/2 and C − 1/2 are real symmetric and positive definite matrices. More generally, we can define the square root of C a matrix L such that

$$
C = LL ⊤ . (A.69)
$$

In particular, very often, we choose L to be the lower triangular matrix obtained from the Cholesky decomposition of C .

![](<ensemble_data_assimilation_e-book_version_images/imageFile141.png>)

# Elements of Linear Inverse Problems

Abstract: This appendix reviews fundamental concepts of linear inverse problem theory. While data assimilation is inherently nonlinear, many methods are based on principles from linear problems. In particular, this appendix revisits key topics such as least squares and regularization.

# B.1 Discrete Linear Problems

Although physical problems are typically continuous, we focus our attention on discrete inverse problems, where we aim to estimate a finite set of model parameters. These parameters are described by an N m -dimensional vector

$$
m = [ m 1 m 2 · · · m N m ] ⊤ , (B.1)
$$

given a N d -dimensional vector of observations

$$
d obs = [ d obs , 1 d obs , 2 · · · d obs ,N d ] ⊤ . (B.2)
$$

We refer to linear problems as those in which the theoretical relationship between data and model parameters takes the form

$$
d = g ( m ) = Gm , (B.3)
$$

where G is the N d × N m sensitivity matrix. For convenience, we define the vector of

model parameters as an element of the linear vector space R N m , referred to as the model space. Similarly, the set of all possible vectors of observed data belongs to a data space, which is assumed to be R N d .

The sensitivity matrix G maps the model space into the data space, i.e., G : R N m → R N d . Recall that the null space of G , N ( G ), is the set of all vectors in the model space such that Gm = 0 . In contrast, the range of G , R ( G ), is the set of all vectors d in the data space such that there is at least one m satisfying Gm = d .

Let g i denote the i th column of the N d × N m sensitivity matrix G

$$
G = [ g 1 g 2 · · · g N m ] . (B.4)
$$

Then, for a given N m -dimensional vector m , we have

$$
d = Gm = [ g 1 g 2 · · · g N m ] ⎡ ⎢ ⎢ ⎢ ⎣ m 1 m 2 . . . m N m ⎤ ⎥ ⎥ ⎥ ⎦ = N m ∑ i =1 m i g i . (B.5)
$$

This result shows that every vector d in the range of G is a linear combination of the columns of G .

Recall that if the columns of G are linearly independent, then there are no nontrivial solutions to Gm = 0 and vice versa. (This also means that N m ≤ N d ). If the number of linearly independent columns of G is equal to N d , then there is at least one vector m which satisfies Gm = d obs . If N m &lt; N d , then there exist data vectors d obs such that the equation Gm = d obs has no solution. Gm = d obs has a unique solution for every d obs in the data space if all of the rows of G are independent and N m = N d (i.e., G is a nonsingular square matrix). In this case, m = G − 1 d obs .

# B.2 Ill-Posed Problems

Practical inverse problems are typically ill-posed. To define an ill-posed problem, it is convenient to first define a well-posed problem [182]. A problem is considered well-posed if it satisfies the following conditions:

- 1. There exists a solution to the problem (existence).
- 2. There is at most one solution to the problem (uniqueness).
- 3. The solution depends continuously on the data (stability).


- A problem that does not satisfy these criteria is termed ill-posed.
- B.3 Classification of Linear Inverse Problems


1. Purely underdetermined problems: The inverse problem Gm = d obs is considered purely underdetermined if, for every d obs in the data space,

there exists more than one vector m in the model space that satisfies the equation. This condition holds true if and only if the following two conditions are satisfied:

- (i) There are more model variables than data ( N m &gt; N d , i.e., dim N ( G ) &gt; 0).
- (ii) All of the rows of G are linearly independent (the data are independent, i.e., dim R ( G ) = N d ).


2. Purely overdetermined problems: The inverse problem Gm = d obs is considered purely overdetermined if the dimension of the null space of G is 0 and there exist d obs for which the equation has no solution. In simpler terms, there is no vector m that satisfies Gm = d obs . However, it is still desirable to find ”solutions” m to the inverse problem, meaning vectors m that approximately satisfy Gm = d obs in some sense. If the dimension of the range of G is less than N d , then there exists at least one d obs for which Gm = d obs has no solution. It can be demonstrated that the following three conditions are equivalent:

- (i) The N m × N m real-symmetric matrix G   G is a nonsingular positivedefinite matrix.
- (ii) dim R ( G ) = N m . (iii) dim ( G ) = 0.


N

3. Mixed determined problems: The inverse problem of Gm = d obs is termed mixed-determined if it exhibits characteristics of both underdetermined and overdetermined problems. This implies that some parameters are overdetermined while others are underdetermined. Establishing a mixed-determined problem involves demonstrating that it does not fall strictly into the category of either purely underdetermined or purely overdetermined problems. It is noteworthy that the majority of practical inverse problems encountered in various fields are mixed determined.

# B.4 Solutions for Discrete Linear Inverse Problems

# B.4.1 Least Squares

Consider the inverse linear problem Gm = d obs , where N d &gt; N m , indicating more data points than unknown parameters. In such cases, exact solutions are typically non-existent. One approach is to seek the least-squares solution ( m ls ):

$$
m ls = arg min m ‖ d obs - Gm ‖ 2 2 = arg min m [ ( d obs - Gm ) ⊤ ( d obs - Gm ) ] = arg min m O ( m ) . (B.6)
$$

We refer to O ( m ) as the objective function. To find m ls we need to find the minimum of O ( m ). First, we compute the gradient of O ( m )

$$
∇O ( m ) = ∇ [ ( d obs - Gm ) ⊤ ( d obs - Gm ) ] = - 2 G ⊤ ( d obs - Gm ) . (B.7)
$$

Then, to compute m ls , we set ∇O ( m ) = 0 and solve for m

$$
- 2 G ⊤ ( d obs - Gm ) = 0 , (B.8)
$$

or

$$
G ⊤ Gm = G ⊤ d obs . (B.9)
$$

If the N m × N m matrix G   G is nonsingular, implying dim R ( G ) = N m , then we encounter an overdetermined problem, and the least-squares solution becomes:

$$
m ls = ( G ⊤ G ) - 1 G ⊤ d obs . (B.10)
$$

# B.4.2 Weighted Least Squares

Consider the same inverse linear problem Gm = d obs and assume that N d &gt; N m , which typically has no exact solution. We may give a different weight for each data point when computing the least-squares estimate. For example, we may want to give higher weight to more reliable data points. In this case, we define the weighted least-squares solution:

$$
m wls = arg min m ‖ d obs - Gm ‖ 2 W = arg min m [ ( d obs - Gm ) ⊤ W ( d obs - Gm ) ] = arg min m O ( m ) , (B.11)
$$

where W is a diagonal matrix containing the data weights.

To find m wls we use the same procedure:

Hence,

$$
∇O ( m ) = ∇ [ ( d obs - Gm ) ⊤ W ( d obs - Gm ) ] = - 2 G ⊤ W ( d obs - Gm ) = 0 . (B.12)
$$

$$
G ⊤ WGm = G ⊤ Wd obs . (B.13)
$$

If the N m × N m matrix G   WG is nonsingular, i.e., dim R ( G ) = N m , then we have an overdetermined problem and

$$
m wls = ( G ⊤ WG ) - 1 G ⊤ Wd obs . (B.14)
$$

# B.4.3 Constrained Least Squares

Now, let’s consider the scenario where N d &lt; N m , i.e., more parameters than data, a common situation in reservoir data assimilation. Suppose dim R ( G ) = N d . This implies that Gm = d obs has a solution for all d obs , actually presenting an infinite number of solutions (an underdetermined problem). Suppose that we have a prior estimate of m , denoted as m pr . For instance, m pr could represent the best guess provided by a geologist regarding our model. In this case, we might be interested in finding m that satisfies the problem Gm = d obs while staying close to the prior estimate, m pr . This problem can be formulated as the following constrained least-squares problem:

$$
min ‖ m - m pr ‖ 2 2 (B.15) s.t. Gm = d obs .
$$

Constrained optimization problems can be solved using the method of Lagrange multipliers 1 , in which case we define the Lagrangian function

1 The method of Lagrange multipliers is designed to solve constrained optimization problems of the form

$$
min O ( x ) s.t. f ( x ) = 0 .
$$

To solve this problem, first we define the Lagrangian function

$$
L ( x , λ ) = O ( x ) - λ ⊤ f ( x ) ,
$$

$$
set ∇ x L ( x , λ ) = 0 , ∇ λ L ( x , λ ) = 0 , and solve for x and λ .
$$

$$
L ( m , λ ) = ( m - m pr ) ⊤ ( m - m pr ) - λ ⊤ ( Gm - d obs ) , (B.16)
$$

and solve

$$
∇ m L ( m , λ ) = 2 ( m - m pr ) - G ⊤ λ = 0 , (B.17)
$$

for m , which leads to

$$
m = m pr + 1 2 G ⊤ λ . (B.18)
$$

Repeating the process for the gradient with respect to λ results in

$$
∇ λ L ( m , λ ) = Gm - d obs = 0 , (B.19)
$$

or Gm − d obs = 0 . Using (B.17) results in

$$
G ( m pr + 1 2 G ⊤ λ ) - d obs = 0 , (B.20)
$$

which leads to

$$
GG ⊤ λ = 2( d obs - Gm pr ) . (B.21)
$$

If the rank of the N d × N d matrix GG   is N d (underdetermined problem), then   GG     − 1 exists and

$$
λ = 2 ( GG ⊤ ) - 1 ( d obs - Gm pr ) . (B.22)
$$

Using this result in (B.17) leads to the final estimate

$$
m cls = m pr + G ⊤ ( GG ⊤ ) - 1 ( d obs - Gm pr ) . (B.23)
$$

# B.4.4 Regularized Least Squares

In real-world scenarios, d obs is always corrupted with noise stemming from measurement errors. Consequently, there is no need to enforce an estimate m that precisely satisfies Gm = d obs . Additionally, we may have some prior knowledge about the solution, aiding in the regularization of the inverse problem. The most straightforward approach to integrate these two aspects is by defining the following objective function:

$$
O ( m ) = α ‖ m - m pr ‖ 2 2 + ‖ d obs - Gm ‖ 2 2 (B.24) = α ( m - m pr ) ⊤ ( m - m pr ) + ( d obs - Gm ) ⊤ ( d obs - Gm ) ,
$$

where α &gt; 0 is a scalar.

To minimize O ( m ), we set ∇O ( m ) = 0 and solve for m .

$$
∇O ( m ) = α ( m - m pr ) - G ⊤ ( d obs - Gm ) = 0 (B.25) = α I ( m - m pr ) - G ⊤ ( d obs - Gm - Gm pr + Gm pr ) = 0 ,
$$

or

$$
( α I + G ⊤ G ) ( m - m pr ) = G ⊤ ( d obs - Gm pr ) . (B.26)
$$

Note that α I + G   G =   α I + G   G     . Hence, α I + G   G is real symmetric. Moreover, this is also positive definite because

$$
x ⊤ ( α I + G ⊤ G ) x = α x ⊤ x + xG ⊤ Gx (B.27) = α ‖ x ‖ 2 2 + ‖ Gx ‖ 2 2 ≥ α ‖ x ‖ 2 2 > 0 , for x = 0 ,
$$

  =

which means that x     α I + G   G   x &gt; 0 for x   = 0 . Therefore, this matrix has a real inverse and the regularized least-squares estimate becomes

̸

$$
m rls = m pr + ( α I + G ⊤ G ) - 1 G ⊤ ( d obs - Gm pr ) . (B.28)
$$

By selecting α &gt; 0, we can compute the regularized least-squares solution. As α approaches 0, m rls converges to m ls , the classical least-squares solution. The magnitude of α dictates the relative importance of   d obs − Gm   2 2 and   m − m pr   2 2 in the objective function. With increasing α , the weight of   m − m pr   2 2 amplifies, while   d obs − Gm   2 2 tends to rise, leading to a decrease in the fidelity of the data match.

# B.4.5 Tikhonov Regularization

Named after the Russian mathematician Andrey Tikhonov, the Tikhonov regularization method combines the least-squares solution with a regularization term of the form

$$
m tk = arg min m { ‖ d obs - Gm ‖ 2 2 + ‖ L ( m - m pr ) ‖ 2 2 } = arg min m [ ( d obs - Gm ) ⊤ ( d obs - Gm ) + ( m - m pr ) ⊤ L ⊤ L ( m - m pr ) ] = arg min m O ( m ) , (B.29)
$$

where L is called the Tikhonov matrix. If we set L = √ α I , for α &gt; 0, we return to the standard regularized least squares. This procedure is closely related to the Levenberg-Marquardt optimization algorithm. To find m tk , we use the same procedure. We set ∇O ( m ) = 0 and solve for m .

$$
m tk = m pr + ( L ⊤ L + G ⊤ G ) - 1 G ⊤ ( d obs - Gm pr ) . (B.30)
$$

If we choose L such that L   L is positive definite, than   L   L + G   G   − 1 exists.

# B.4.6 SVD Solution

SVD can be useful to construct approximate solutions of linear inverse problems. Recall that the N d × N m matrix G can decomposed as the product of three matrices

$$
G = UΣV ⊤ ,
$$

where U is a N d × N d matrix with left singular vectors of G , V is a N m × N m matrix with right singular vectors of G , Σ is a N d × N m matrix with nonzero elements only in the diagonal.

If G is square and nonsingular, the solution of the inverse problem Gm = d obs can be obtained using

$$
Gm = d obs ( UΣV ⊤ ) m = d obs U ⊤ UΣV ⊤ m = U ⊤ d obs Σ - 1 ΣV ⊤ m = Σ - 1 U ⊤ d obs VV ⊤ m = VΣ - 1 U ⊤ d obs m = VΣ - 1 U ⊤ d obs , (B.31)
$$

where we use the fact that U   U = I , VV   = I and Σ − 1 Σ = I . In this case, it is trivial to compute Σ − 1 because this is a diagonal matrix. Actually, if G is square and nonsingular, G − 1 exists and G − 1 = VΣ − 1 U   . (SVD gives the true inverse of G ).

In general, however, G is not square and some singular values are zero (or others may be close to zero). In this case, we consider the solution

$$
m svd = V r Σ - 1 r U ⊤ r d obs , (B.32)
$$

where N r ≤ min { N d ,N m } is the number of nonzero singular values. U r is N d × N r and U   r U r = I , but U r U   r   = I . V r is N m × N r and V   r V r = I , but V r V   r   = I . Σ r is a N r × N r matrix 2 . Note that (B.32) has the form

̸

̸

Note that (B.32) has the form

2 The SVD solution has interesting properties. For example, if Gm = d obs has more than one solution, the SVD solution is the one with minimum length. In contrast, if Gm = d obs has no solution, the SVD solution is the least-squares solution.

$$
m svd = V r b , (B.33)
$$

where b = Σ − 1 r U   r d obs is a N r -dimensional vector. This implies that m svd is a linear combination of the first N r right-singular vectors of G , i.e.,

$$
m svd = V r b = [ v 1 v 2 · · · v N r ] ⎡ ⎢ ⎢ ⎢ ⎣ b 1 b 2 . . . b N r ⎤ ⎥ ⎥ ⎥ ⎦ = N r ∑ j =1 v j b j = N r ∑ j =1 v j ( u ⊤ j d obs σ i ) . (B.34)
$$

# B.4.6.1 Removing Small Singular Values

In practical applications, we often remove the small singular values even if they are nonzero. The typical criterion is to keep only the N r ≤ N R = { N d ,N m } largest singular values such that

$$
∑ N r j =1 σ j ∑ N R j =1 σ j ≥ ξ, (B.35)
$$

where ξ ≤ 1. Note that the condition (B.35) assumes that the singular values are sorted in a decreasing order.

To comprehend the rationale behind truncating the singular values, let’s consider the SVD solution of the problem Gm = d obs :

$$
m svd = V r Σ - 1 r U ⊤ r d obs . (B.36)
$$

Observed data always contain noise. So, even if we knew the ground truth values for m , denoted as m true , Gm true would not return d obs . Instead, we could express it as:

$$
d obs = Gm true + e . (B.37)
$$

where e is the noise. Therefore,

$$
m svd = V r Σ - 1 r U ⊤ r [ Gm true + e ] = V r Σ - 1 r U ⊤ r [ U r Σ r V ⊤ r m true + e ] = V r V ⊤ r m true + V r ⎡ ⎢ ⎣ 1 σ 1 u ⊤ 1 e . . . 1 σ r u ⊤ r e ⎤ ⎥ ⎦ . (B.38)
$$

Suppose that m true lies in the span of V r , i.e., we can write m true = V r b . Hence

$$
m svd = V r V ⊤ r V r b + V r ⎡ ⎢ ⎣ 1 σ 1 u ⊤ 1 e . . . 1 σ r u ⊤ r e ⎤ ⎥ ⎦ = V r ⎡ ⎢ ⎣ b 1 + 1 σ 1 u ⊤ 1 e . . . b r + 1 σ r u ⊤ r e ⎤ ⎥ ⎦ . (B.39)
$$

This outcome suggests that the noise vector is scaled by the singular values. Consequently, small singular values may amplify errors in estimating m . Conversely, decreasing the number of singular values, along with their corresponding singular vectors, diminishes the capability to replicate the true model, as the columns of V r will no longer fully span the model space.

# B.4.6.2 Optimal Hard Threshold of Singular Values

Gavish and Donoho [165] derived the optimal threshold to truncate singular values, τ ∗ , in the case of estimating a low-rank matrix, G , from an observed matrix,   G , corrupted with white noise of level γ &gt; 0, i.e.,

$$
˜ G = G + γ Z , (B.40)
$$

  where the noise matrix Z has normality distributed zero-mean and unityvariance entries. They found that for a square N × N matrix G , the optimal threshold is

$$
τ ∗ = 4 √ 3 √ Nγ. (B.41)
$$

If the noise level γ is unknown, they proposed approximations for τ ∗ in the form

$$
τ ∗ ≈ ωσ med , (B.42)
$$

where σ med is the median singular value of   G and ω = 2 . 858 if G is square. They also derived a procedure to compute ω for rectangular matrices.

# B.4.6.3 Relation Between Regularization and SVD

Consider we are looking for the following regularized least-squares estimate

$$
m rls = arg min m { ‖ d obs - Gm ‖ 2 2 + α ‖ m ‖ 2 2 } = arg min m O ( m ) . (B.43)
$$

with α &gt; 0. Setting ∇O ( m ) = 0 , we obtain

$$
( α I + G ⊤ G ) m = G ⊤ d obs . (B.44)
$$

Now the SVD of G and write

$$
G = UΣV ⊤ . (B.45)
$$

Using this result

Therefore,

$$
( α I + G ⊤ G ) m = G ⊤ d obs ( α VV ⊤ + VΣ ⊤ ΣV ⊤ ) m = VΣ ⊤ U ⊤ d obs V ( α I + Σ ⊤ Σ ) V ⊤ m = VΣ ⊤ U ⊤ d obs V ⊤ V ( α I + Σ ⊤ Σ ) V ⊤ m = V ⊤ VΣ ⊤ U ⊤ d obs ( α I + Σ ⊤ Σ ) ︸ ︷︷ ︸ diagonal matrix V ⊤ m = Σ ⊤ U ⊤ d obs . (B.46)
$$

Note that

$$
m rls = V ( α I + Σ ⊤ Σ ) - 1 Σ ⊤ U ⊤ d obs = N r ∑ j =1 V j ( σ j u ⊤ j d obs σ 2 j + α ) . (B.47)
$$

$$
lim α → 0 N r ∑ j =1 v j ( σ j u ⊤ j d obs σ 2 j + α ) = N r ∑ j =1 v j ( u ⊤ j d obs σ j ) = m ls , (B.48)
$$

which is the standard least-squares estimate.

We also can interpret the regularization effect by noting that

$$
v j ( σ j u ⊤ j d obs σ 2 j + α ) ≈ ⎧ ⎨ ⎩ 0 , if 0 ≈ σ j ≪ α v j ( u ⊤ j d obs σ j ) , if σ j ≫ α (B.49)
$$

Therefore, the regularization term α   m   2 2 functions similarly to the elimination of small singular values. Contributions from large singular values ( σ j   α ) remain (almost) unaffected, while contributions from small singular values ( σ j   α ) are (almost) nullified.

![](<ensemble_data_assimilation_e-book_version_images/imageFile142.png>)

C

# Elements of Probability and Geostatistics

Abstract: This appendix summarizes essential concepts of probability and geostatistics pertinent to reservoir data assimilation.

# C.1 Basic Concepts

# C.1.1 Random Variables

A random variable 1 x is a quantity that takes on varying random values. Random variables can be either discrete, assuming a finite (countable) set of values, or continuous, associated with real numbers.

# C.1.2 Probability Mass Function

The probability of a discrete random variable is characterized by a probability mass function (PMF), denoted as P ( x ), which must satisfy the following conditions:

- 1. The domain of P ( x ) is the set of all possible values of x .
- 2. 0 ≤ P ( x ) ≤ 1. An impossible event has P ( x ) = 0 and a certain event has P ( x ) = 1.
- 3.   x P ( x ) = 1.


1 This book departs from the conventional notation in the probability literature, where capital letters represent random variables.

# C.1.3 Probability Density Function

For continuous random variables, the probability density function (PDF), denoted by p ( x ), is used and must satisfy the following conditions:

- 1. The domain of p ( x ) is the set of all possible values of x .
- 2. p ( x ) ≥ 0. (Note that we do not require p ( x ) ≤ 1.)
- 3.   ∞ −∞ p ( x ) dx = 1.


The PDF does not directly provide the probability of a specific event. In fact, for a continuous random variable x , the probability of x taking any exact value a is zero, i.e., P ( x = a ) = 0. Instead, we compute the probability of x falling within the interval between a and b as:

$$
P ( a ≤ x < b ) = ∫ b a p ( x ) dx. (C.1)
$$

# C.1.4 Cumulative Density Function

The cumulative density function (CDF) for a random variable x with PDF p ( x ) is defined as a

$$
P ( x ≤ a ) = ∫ a -∞ p ( x ) dx. (C.2)
$$

# C.1.5 Joint Probability

Let x 1 ,...,x N be a set of random variables with density p ( · ) such that the joint probability that a realization of the set lies within the region a 1 ≤ x 1 &lt; b 1 ,...,a N ≤ x N &lt; b N is

$$
P ( a 1 ≤ x < b 1 , . . . , a N ≤ x N < b N ) = ∫ b 1 a 1 · · · ∫ b N a N p ( x 1 , . . . , x N ) dx 1 . . . dx N . (C.3)
$$

We represent this set of random variables as a random vector, x = [ x 1 ··· x N ]   . The joint probability of x be within the region Ω is

$$
P ( x ∈ Ω) = ∫ Ω p ( x ) d x . (C.4)
$$

# C.1.6 Marginal PDF

The marginal PDF for a random variable x i is found by integrating the joint PDF over the remaining N − 1 variables. For example, the marginal density for x 1 is

$$
p ( x 1 ) = ∫ ∞ -∞ · · · ∫ ∞ -∞ p ( x 1 , x 2 , . . . , x N ) dx 2 . . . dx N . (C.5)
$$

# C.1.7 Conditional PDF

The conditional PDF of x given y is defined by

$$
p ( x | y ) = p ( x, y ) p ( y ) . (C.6)
$$

The same is valid for random vectors, i.e.,

$$
p ( x | y ) = p ( x , y ) p ( y ) . (C.7)
$$

# C.1.8 The Chain Rule of Conditional Probabilities

The joint PDF can be decomposed as a product of conditionals:

$$
p ( x 1 , x 2 , . . . , x N ) = p ( x 1 ) p ( x 2 | x 1 ) p ( x 3 | x 1 , x 2 ) · · · p ( x N | x 1 , . . . , x N - 1 ) = p ( x 1 ) N ∏ i =2 p ( x i | x 1 , . . . , x i - 1 ) . (C.8)
$$

This result follows from the definition of conditional probabilities and the proof uses mathematical induction. First, we note that the chain rule holds for N = 2:

$$
p ( x 1 , x 2 ) = p ( x 1 ) p ( x 2 | x 1 ) . (C.9)
$$

Then, we assume it holds for N − 1. For convenience, call   x = [ x 1 ··· x N − 1 ]  

$$
p ( x 1 , . . . , x N - 1 ) = p ( ̂ x ) = p ( x 1 ) N - 1 ∏ i =2 p ( x i | x 1 , . . . , x i - 1 ) . (C.10)
$$

Finally, we show it holds for N

$$
p ( x 1 , . . . , x N ) = p ( ̂ x , x N ) = p ( x N | ̂ x ) p ( ̂ x ) = p ( x N | x 1 , . . . , x N - 1 ) p ( x 1 ) N - 1 ∏ i =2 p ( x i | x 1 , . . . , x i - 1 ) = p ( x 1 ) N ∏ i =2 p ( x i | x 1 , . . . , x i - 1 ) . (C.11)
$$

Hence, by mathematical induction the chain rule of conditional probabilities holds. The chain rule is a basic component to justify the sequential data assimilation used in the Kalman filter.

# C.1.9 Expected Value

The expected value of a function g ( · ) of a random variable x whose PDF is p ( x ) is given by

$$
E [ g ( x )] = ∫ ∞ -∞ g ( x ) p ( x ) dx. (C.12)
$$

The expected value of a random variable x is also called the mean value and is given by

$$
E [ x ] = µ x = ∫ ∞ -∞ xp ( x ) dx. (C.13)
$$

The expected value of the product of two random variables x is

$$
E [ xy ] = ∫ ∞ -∞ ∫ ∞ -∞ xyp ( x, y ) dxdy. (C.14)
$$

# C.1.10 Independent Random Variables

Two random variables x and y are said to be independent if

$$
p ( x, y ) = p ( x ) p ( y ) . (C.15)
$$

If x and y are independent than

$$
E [ xy ] = ∫ ∞ -∞ ∫ ∞ -∞ xyp ( x, y ) dxdy = ∫ ∞ -∞ ∫ ∞ -∞ xyp ( x ) p ( y ) dxdy = (∫ ∞ -∞ xp ( x ) dx )(∫ ∞ -∞ yp ( y ) dy ) = E [ x ] E [ y ] .
$$

$$
(C.16)
$$

# C.1.11 Variance

The variance of a random variable x is

$$
V [ x ] = E [ ( x - E [ x ]) 2 ] = E [ ( x - µ x ) 2 ] = E [ x 2 ] - 2 E [ xµ x ] + E [ µ 2 x ] = E [ x 2 ] - 2 µ x E [ x ] + µ 2 x = E [ x 2 ] - µ 2 x = σ 2 x , (C.17)
$$

where σ x is the standard deviation of x . The variance of the sum of two random

variables, x and y , can be calculated using the following formula:

$$
V [ x + y ] = E [ (( x + y ) - E [( x + y )]) 2 ] = E [ (( x + y ) - ( µ x + µ y )) 2 ] = E [ (( x - µ x ) + ( y - µ y )) 2 ] = E [ ( x - µ x ) 2 +( y - µ y ) 2 +2( x - µ x ) ( y - µ y ) ] = V [ x ] + V [ y ] + 2 E [( x - µ x ) ( y - µ y )] = V [ x ] + V [ y ] + 2 C [ x, y ] , (C.18)
$$

where C [ x,y ] is the covariance of x and y defined as

$$
C [ x, y ] = E [( x - µ x ) ( y - µ y )] . (C.19)
$$

# C.1.12 Covariance

The covariance of x and y can be written as

$$
C [ x, y ] = E [( x - E [ x ]) ( y - E [ y ])] = E [( x - µ x ) ( y - µ y )] = E [ xy - xµ y - yµ x + µ x µ y ] = E [ xy ] - µ x µ y - µ y µ x + µ x µ y = E [ xy ] - µ x µ y . (C.20)
$$

If x and y are independent, meaning E [ xy ] = E [ x ] E [ y ], then C [ x,y ] = 0. It is important to note that while C [ x,y ] = 0 indicates that x and y are uncorrelated, this does not imply that they are independent. However, for multivariate Gaussian distributions, uncorrelated random variables are indeed independent.

# C.1.13 Correlation Coefficient

We define the Pearson correlation coefficient ρ xy ∈ [ − 1 , 1] as

$$
ρ xy = C [ x, y ] σ x σ y . (C.21)
$$

The correlation coefficient measures a linear correlation between two quantities.

# C.1.14 Covariance Matrix

Let x be a random vector. The covariance of x , denoted as C x , is defined as

$$
C x = E [ ( x - E [ x ]) ( x - E [ x ]) ⊤ ] = E [ ( x - µ x ) ( x - µ x ) ⊤ ] = E [ xx ⊤ - µ x x ⊤ - x µ ⊤ x + µ x µ ⊤ x ] = E [ xx ⊤ ] - E [ µ x x ⊤ ] - E [ x µ ⊤ x ] + E [ µ x µ ⊤ x ] = E [ xx ⊤ ] - µ x µ ⊤ x - µ x µ ⊤ x + µ x µ ⊤ x = E [ xx ⊤ ] - µ x µ ⊤ x . (C.22)
$$

Therefore, the covariance of x is a matrix (covariance matrix) with the form

$$
C x = ⎡ ⎢ ⎢ ⎢ ⎣ E [ x 1 x 1 ] - µ 1 µ 1 · · · E [ x 1 x N ] - µ 1 µ N E [ x 2 x 1 ] - µ 2 µ 1 · · · E [ x 2 x N ] - µ 2 µ N . . . . . . . . . E [ x N x 1 ] - µ N µ 1 · · · E [ x N x N ] - µ N µ N ⎤ ⎥ ⎥ ⎥ ⎦ . (C.23)
$$

If the components x i and x j are uncorrelated, i.e., E [ x i x j ] = µ i µ j , C x is a diagonal matrix. The diagonal elements of C x are V [ x i ] = σ 2 x i . Similarly, the (cross-)covariance of two random vectors, x and y , as

Similarly, the (cross-)covariance of two random vectors, x and y , as

$$
C xy = E [ ( x - E [ x ]) ( y - E [ y ]) ⊤ ] . (C.24)
$$

# C.1.15 Ensemble Estimators

Let x 1 ,...,x N e be N e independent and identically distributed samples from a distribution with mean µ x and finite variance σ 2 x . We can then use the following ensemble estimates:

-  Mean:

$$
E [ x ] = µ x ≈ x = 1 N e N e ∑ j =1 x j . (C.25)
$$

-  Variance:

$$
V [ x ] = σ 2 x ≈ 1 N e - 1 N e ∑ j =1 ( x j - x ) 2 . (C.26)
$$

-  Pearson correlation coefficient:


$$
ρ xy ≈ ∑ N e j =1 ( x j - x ) ( y j - y ) √ ∑ N e j =1 ( x j - x ) √ ∑ N e j =1 ( y j - y ) . (C.27)
$$

Similar expressions can be written for random vectors:

-  Mean:

$$
E [ x ] ≈ x = 1 N e N e ∑ j =1 x j . (C.28)
$$

-  Covariance:


$$
C xy = E [ ( x - E [ x ]) ( y - E [ y ]) ⊤ ] ≈ 1 N e - 1 N e ∑ j =1 ( x j - x ) ( y j - y ) ⊤ = ˜ C xy . (C.29)
$$

# C.1.16 Bias

Suppose we are estimating the true value x of our model using an estimator   x . The bias of the estimator is defined as

$$
B [ ̂ x ] = E [ ̂ x - x ] = E [ ̂ x ] - x. (C.30)
$$

  An estimator   x is considered unbiased if B [   x ] = 0.

# C.1.17 Mean Square Error

The MSE of an estimator x is defined as

 

$$
MSE [ ̂ x ] = E [ ( ̂ x - x ) 2 ] = E [( ( ̂ x - E [ ̂ x ]) + ( E [ ̂ x ] - x ) 2 )] = E [ ( ̂ x - E [ ̂ x ]) 2 +2( ̂ x - E [ ̂ x ]) ( E [ ̂ x ] - x ) + ( E [ ̂ x ] - x ) 2 ] = E [ ( ̂ x - E [ ̂ x ]) 2 ] ︸ ︷︷ ︸ = V [ ̂ x ] +2( E [ ̂ x ] - x ) E [( ̂ x - E [ ̂ x ])] ︸ ︷︷ ︸ = E [ ̂ x ] - E [ ̂ x ] =0 + ( E [ ̂ x ] - x ︸ ︷︷ ︸ = B [ ̂ x ] ) 2 = V [ ̂ x ] + B [ ̂ x ] 2 . (C.31)
$$

    This result indicates that an estimator   x with small MSE represent a compromise between bias and variance.

# C.1.18 Typical Distributions

# C.1.18.1 Normal (Gaussian)

We denote that x is sampled from a normal (Gaussian) distribution with mean µ x and variance σ 2 x using x ∼ N ( µ x ,σ 2 x ) (Fig. C.1). The PDF and CDF of a univariate Gaussian distribution are given by:

and

$$
PDF: p ( x ) = 1 σ x √ 2 π exp ( - ( x - µ x ) 2 2 σ 2 x ) (C.32)
$$

$$
CDF: P ( x ) = 1 2 [ 1 + erf ( x - µ x σ x √ 2 )] . (C.33)
$$

![](<ensemble_data_assimilation_e-book_version_images/imageFile143.png>)

1

 = 

=

 = 

=

0,  

1

0,  

1

0.8

=

=

=

=

0,

2

0,

2

0.8

 =

=

 =

=

2, 

0.5

2, 

0.5

0.6

0.6

x )

)

P (

)

(

(

0.4

P

p ( x

0.4

0.2

0.2

0

0

-6

-4

-2

0

2

4

6

-6

-4

-2

0

2

4

6

x

x

(a)

PDF

(b)

CDF

Fig. C.1: Normal (Gaussian) distribution.

Gaussian distributions are widely used and often considered a default choice for two key reasons:

1. Many real-world phenomena approximate a Gaussian distribution due to the Central Limit Theorem, which states that the average of independent, identically distributed random variables converges in distribution to a Gaussian.

2. Among all distributions with the same variance, the Gaussian has the highest level of uncertainty 2 . In practice, choosing a Gaussian corresponds to adopting the least informative prior.

This book frequently assumes Gaussian distributions. A third reason for this assumption is that the theory for linear-Gaussian problems is wellestablished and forms the foundation for many of the methods discussed throughout the book.

# C.1.18.2 Multivariate Gaussian

We use x ∼ N ( µ x , C x ) to denote that the random vector x is a sample from a multivariate Gaussian distribution with mean µ x and covariance C x . The PDF of x has the form:

$$
p ( x ) = 1 [ (2 π ) N x det ( C x ) ] 1/2 exp { - 1 2 ( x - µ x ) ⊤ C - 1 x ( x - µ x ) } . (C.34)
$$

Fig. C.2 displays the contour plot of a bivariate Gaussian distribution with a mean vector µ x = 0 and covariance matrix

$$
C x = [ 1 ρ ρ 1 ] . (C.35)
$$

When ρ = 0, x 1 and x 2 are uncorrelated, which, for Gaussian distributions, also implies that they are independent.

# C.1.18.3 Log-Normal

A random variable x is log-normally distributed if its logarithm, z = ln x , is normally distributed, i.e., ln x ∼ N ( µ x ,σ 2 x ) (Fig. C.3). The PDF and CDF of x have the forms:

and

$$
PDF: p ( x ) = 1 xσ x √ 2 π exp ( - (ln x - µ x ) 2 2 σ 2 x ) (C.36)
$$

$$
CDF: P ( x ) = 1 2 [ 1 + erf ( ln x - µ x σ x √ 2 )] . (C.37)
$$

2 Specifically, the Gaussian distribution has the maximum entropy among distributions with the same variance and support on ( −∞ , ∞ ). In Information Theory, entropy is a common measure of uncertainty. The Maximum Entropy Principle suggests that, given the available information, the probability distribution with the highest entropy should be selected.

![](<ensemble_data_assimilation_e-book_version_images/imageFile144.png>)

  

�

�

  

�

�

  

�

�

  

�

�

  

�

�

  

�

�

  

�

�

  

�

�

  

�

�

�

�

�

�

�

�

�

�

�

2

2



2

2



2

2



x 2 x 2 x 2





x 2 x 2 x 2





x 2 x 2 x 2





  

�

�

  

�

�

  

�

�

  

�

�

  

�

�

  

�

�

     

�

�

�

�

     

�

�

     

�

�

�

  

�

�

  

�

�

�

�

�

  

�

�

  

�

�

  

�

�

�

�

�

  

�

�

  

�

�

�

�

�

  

�

�

  

�

�

  

�

�

�

�

�

  

�

�

  

�

�

�

�

�

  

�

�

  

�

�

  

�

�

 x 1  x 1  x 1

x

x

 x 1  x 1  x 1

x

x

 x 1  x 1  x 1

x

x

1

1

1

1

1

1

1

1

1

(a)

(b)

(c)

=

. 8

8

= 0

= 0 . 8

8

ρ

− 0

.

ρ

ρ

.

Fig. C.2: Bivariate Gaussian distributions.

1

![](<ensemble_data_assimilation_e-book_version_images/imageFile145.png>)

1

 = 

=

0,  

1

=

=

0,

0.5

0.8

0.8

 =

=

1, 

0.25

0.6

0.6

)

)

P ( x )

)

(

(

P

p ( x

0.4

0.4

 = 

=

0,  

1

=

=

0,

0.5

0.2

0.2

 =

=

1, 

0.25

0

0

0

2

4

6

0

2

4

6

x

x

(a)

PDF

(b)

CDF

Fig. C.3: Log-normal distribution.

# C.1.18.4 Chi-squared

A chi-squared distribution with k degrees of freedom is the distribution of a sum of the squares of k independent normally distributed random variables (Fig. C.4). This means that if x =   k i =1 z 2 i with z j ∼ N (0 , 1), then x ∼ χ 2 ( k ). The PDF and CDF of x have the forms:

and

$$
PDF: p ( x ) = 1 2 k/ 2 Γ ( k/ 2) x k/ 2 - 1 e - x/ 2 (C.38)
$$

$$
CDF: P ( x ) = 1 Γ ( k/ 2) γ ( k 2 , x 2 ) , (C.39)
$$

![](<ensemble_data_assimilation_e-book_version_images/imageFile146.png>)

1

k =

1

0.6

k =

3

0.8

k =

6

0.4

0.6

)

)

P ( x )

p ( x )

(

(

P

p

0.4

0.2

k =

1

0.2

k =

3

k =

6

0

0

0

2

4

6

0

2

4

6

x

x

(a)

PDF

(b)

CDF

Fig. C.4: Chi-squared distribution.

# C.1.18.5 Uniform

We use x ∼ U ( a,b ) to denote that the x is a sample from a uniform distribution with boundary parameters a and b (Fig. C.5). The PDF and CDF of x have the forms:

and

$$
PDF: p ( x ) = { 1 b - a , for a ≤ x ≤ b 0 for x < a or x > b (C.40)
$$

$$
CDF: P ( x ) = ⎧ ⎪ ⎨ ⎪ ⎩ 0 , for x < a x - a b - a , for a ≤ x ≤ b 1 for x > b (C.41)
$$

# C.1.18.6 Triangular

The triangular distribution has three parameters: lower limit a , upper limit b , and mode c , where a ≤ c ≤ b (Fig. C.6). The PDF and CDF of a triangular distribution have the forms:

![](<ensemble_data_assimilation_e-book_version_images/imageFile147.png>)

1

a =

1, b

=

3

a =

1, b

=

3

0.6

0.8

0.4

0.6

)

x )

P ( x )

x

(

(

P

p (

0.4

0.2

0.2

0 0

0 0

0

1

2

3

4

0

1

2

3

4

x

x

(a)

PDF

(b)

CDF

Fig. C.5: Uniform distribution.

and

$$
PDF: p ( x ) = ⎧ ⎪ ⎪ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ 0 , for x < a 2( x - a ) ( b - a )( c - a ) , for a ≤ x < c 2( b - x ) ( b - a )( b - c ) , for c < x ≤ b 0 for x > b (C.42)
$$

$$
CDF: P ( x ) = ⎧ ⎪ ⎪ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ 0 , for x ≤ a ( x - a ) 2 ( b - a )( c - a ) , for a < x ≤ c 1 - ( b - x ) 2 ( b - a )( b - a ) , for a < x ≤ c 1 for x > b (C.43)
$$

![](<ensemble_data_assimilation_e-book_version_images/imageFile148.png>)

a =

4,

-

b

=

4, c

=

0

1

a =

4,

-

b

=

4, c

=

0

0.3

a =

4,

-

b

=

6, c

=

-3

a =

4,

-

b

=

6, c

=

-3

a =

2,

-

b

=

6, c

=

4

0.8

a =

2,

-

b

=

6, c

=

4

0.2

0.6

)

x )

)

P (

(

(

p ( x

P

0.4

0.1

0.2

0 -6

0 -6

-6

-4

-2

0

2

4

6

-6

-4

-2

0

2

4

6

x

x

(a)

PDF

(b)

CDF

Fig. C.6: Triangular distribution.

# C.1.18.7 PERT

The PERT distribution is similar to the triangular distribution but with a smoother shape. The distribution has three parameters: lower limit a , upper limit b , and mode c , where a ≤ c ≤ b (Fig. C.7). The PDF and CDF of a PERT distribution have the forms:

and

$$
PDF: p ( x ) = ( x - a ) α 1 - 1 ( b - x ) α 2 - 1 B ( α 1 , α 2 ) ( b - a ) α 1 + α 2 - 1 (C.44)
$$

$$
CDF: P ( x ) = I z ( α 1 , α 2 ) , (C.45)
$$

where B ( · , · ) is the beta function and I z ( · , · ) is the incomplete beta function with 4 c + b 5 a

$$
α 1 = 4 c + b - 5 a b - a , (C.46)
$$

$$
α 2 = 5 b - a - 4 c b - a , (C.47)
$$

and

$$
z = x - a b - a . (C.48)
$$

![](<ensemble_data_assimilation_e-book_version_images/imageFile149.png>)

a =

4,

-

b

=

4, c

=

0

a =

4,

-

b

=

4, c

=

0

1

a =

4,

-

b

=

6, c

=

-3

a =

4,

-

b

=

6, c

=

-3

0.3

a =

2,

-

b

=

6, c

=

4

a =

2,

-

b

=

6, c

=

4

0.8

0.6

)

0.2

x )

p ( x )

x

(

(

p

P (

0.4

0.1

0.2

0 -6

0 -6

-6

-4

-2

0

2

4

6

-6

-4

-2

0

2

4

6

x

x

(a)

PDF

(b)

CDF

Fig. C.7: PERT distribution.

In statistics, likelihood is a concept used to evaluate how well a statistical model explains data. While probability asks about the chance of observing specific data given a particular model, likelihood reverses this perspective: it assesses the probability of different models given the observed data. Formally, the likelihood of a set of parameter values given some observed outcomes is defined as the probability of those outcomes occurring given the parameter values. This can be expressed as:

$$
L ( m | d ) = L ( m ) ≡ p ( d | m ) . (C.49)
$$

Here, L ( m ) represents the likelihood function, which measures how well the model m fits the data d . Essentially, the likelihood function provides a quantitative measure of how plausible a particular model is in explaining the observed data [428].

# C.2.1 Maximum Likelihood Estimation

Maximum likelihood estimation (MLE) is a method used to identify the best parameters for a statistical model based on given data. The goal of MLE is to find the parameter values that maximize the likelihood function, which measures how well the model explains the observed data. In practice, this is often achieved by maximizing the log-likelihood function. The maximum likelihood estimate is obtained by solving the following optimization problem:

$$
m ml = arg max m [ln L ( m )] . (C.50)
$$

# C.3 Bayes' Rule

Perhaps the simplest way to introduce the Bayes’ rule is using Venn diagrams. Fig. C.8 shows a Venn diagram with to possible events, A and B that can occur in a sample space Ω.

From the definitions of conditional probabilities

and

$$
P ( A | B ) = P ( A ∩ B ) P ( B ) (C.51)
$$

$$
P ( B | A ) = P ( B ∩ A ) P ( A ) , (C.52)
$$

![](<ensemble_data_assimilation_e-book_version_images/imageFile150.png>)

A∩B

∩

B

B

A



Fig. C.8: Venn diagram indicating the probability of occurrence of two events, A and B in sample space Ω .

$$
P ( A | B ) P ( B ) = P ( B | A ) P ( A ) . (C.53)
$$

$$
P ( A | B ) = P ( B | A ) P ( A ) P ( B ) = P ( B | A ) P ( A ) P ( B | A ) P ( A ) + P ( B | ˜ A ) P ( ˜ A ) , (C.54)
$$

where P ( A ) + P (   A ) = P (Ω) = 1 and   A means “not A .” This last expression is Bayes’ rule, which allows us to evaluate, for example, the probability of event A given the occurrence of event B .

In this book, we use Bayes’ rule to obtain the conditional (posterior) distribution of a random vector of model parameters m , given a set of observations d obs , expressed as

$$
p ( m | d obs ) = p ( d obs | m ) p ( m ) p ( d obs ) . (C.55)
$$

Since p ( d obs ) is independent of m , it acts as a constant term. This constant can be determined from the expression for the marginal distribution, leading to

$$
p ( m | d obs ) = p ( d obs | m ) p ( m ) ∫ m p ( d obs | m ) p ( m ) d m . (C.56)
$$

Bayes’ rule is a direct application of the definitions of joint and conditional probabilities. However, the interpretation given to the resulting equation forms the foundation of Bayesian statistics. Specifically, we write

$$
p ( m | d obs ) ︸ ︷︷ ︸ posterior = const ×L ( m | d obs ) ︸ ︷︷ ︸ likelihood × p ( m ) ︸ ︷︷ ︸ prior , (C.57)
$$

which means that the posterior distribution is proportional to the product of the likelihood and the prior.

Geostatistics is a specialized branch of statistics that focuses on analyzing and interpreting spatial or spatiotemporal datasets. Early geostatistical methods were closely linked to interpolation techniques, particularly with the development of kriging. However, contemporary geostatistics extends beyond mere interpolation, incorporating a range of sophisticated techniques for spatial analysis and modeling.

This section provides a brief review of fundamental geostatistical concepts that are essential for understanding the topics discussed in this book. For a more comprehensive exploration of geostatistics, several excellent resources are available, including Deutsch [104], Wackernagel [456], and Mariethoz and Caers [290]. Numerous commercial and open-source geostatistical software options are also available. Notable open-source examples include GSLIB [105], gstat [343], SGeMS [362], and GeoStats.jl [194].

# C.4.1 Stationarity

Consider a random variable z . We want to model z as a function of its spatial position, i.e., z ( u ). The covariance of z at two locations, u and u + h is given by

$$
C [ z ( u ) , z ( u + h )] = E [( z ( u ) - E [ z ( u )]) ( z ( u + h ) - E [ z ( u + h )])] . (C.58)
$$

-  First-order stationarity: the expected value at any location in the specified region is constant.

$$
E [ z ( u )] = E [ z ( u + h )] . (C.59)
$$

-  Second-order stationarity: the covariance between the value of the random function at two points is only a function of the distance between the two points.


$$
C [ z ( u ) , z ( u + h )] = C ( h ) . (C.60)
$$

# C.4.2 Transformation of Variables

Many estimation and simulation methods in geostatistics rely on the assumption that the PDF is Gaussian. Therefore, we often transform variables to approximately univariate Gaussian.

The Box-Cox transform is often used

$$
z = x λ - 1 λ , with λ = 0 . (C.61)
$$

  =

For λ → 0, we have the log-transform

$$
z = ln( x ) . (C.62)
$$

The log-transform is very useful for permeability and transmissibility values. The normal score transform (Fig. C.9) is a nonparametric method that converts a given frequency distribution into a univariate Gaussian distribution. Also known as Gaussian anamorphosis, this transformation applies to each parameter’s marginal distribution independently, meaning it does not account for the multivariate Gaussian distribution. Consequently, there is no guarantee that the joint distribution of all variables will be Gaussian. However, in practice, this method often improves the Gaussian properties of the joint PDF [456].

![](<ensemble_data_assimilation_e-book_version_images/imageFile151.png>)

1

1

0.8

0.8

0.6

0.6

)

( z )

x

z

P

)

P

P ( x

0.4

0.4

0.2

0.2

0 0

0 -4

0

2

4

6

8

10

12

14

16

-4

-2

0

2

4

x

z

0.5

0.5

0.4

0.4

0.3

0.3

)

)

x

z

)

)

p ( z

p ( x

0.2

0.2

0.1

0.1

0 0

0 -4

0

2

4

6

8

10

12

14

16

-4

-2

0

2

4

x

z

≈

z   ≈

1.8

x =

4

Fig. C.9: Normal score transform.

In geostatistics, the concept of variogram is often preferred over the covariance, even though both contain equivalent information. Mathematically, the variogram is defined as half the variance of the difference between values at two locations separated by a distance h ; this is also referred to as the semivariogram. For stationary models, the variogram depends only on the distance h between locations, not their absolute positions. The variogram γ ( h ) of a random variable z has the form

$$
γ ( h ) = 1 2 V [ z ( u ) - z ( u + h )] = C (0) -C ( h ) = C (0) [ 1 - C ( h ) C (0) ] = C (0) [1 - ρ ( h )] , (C.63)
$$

where γ ( h ), C ( h ), and ρ ( h ) represent the variogram, covariance, and correlation functions, respectively. Typical covariance functions include:

$$
Spherical: C ( h ) = σ 2 { 1 - 3 h 2 L + h 3 2 L 3 , 0 ≤ h ≤ L 0 , h > L, (C.64)
$$

and

$$
Exponential: C ( h ) = σ 2 exp ( - 3 h L ) , (C.65)
$$

$$
Gaussian: C ( h ) = σ 2 exp ( - 3 h 2 L 2 ) , (C.66)
$$

where L is the correlation length.

![](<ensemble_data_assimilation_e-book_version_images/imageFile152.png>)

1

1

0.8

0.8

1 1

1 1

L =  2 =

L =  2 =





2

2

= 1

= 1

0.6

0.6

0.6 h )

)

h

)

Spherical

Spherical

(

C ( h

C

0.4  (

0.4

0.4

Exponential

Exponential

Gaussian

Gaussian

0.2

0.2

0 0

0 0

0

0.5

1

1.5

2

0

0.5

1

1.5

2

h

h

(a)

Variogram

(b)

Covariance

INTERNA

INTERNA

#

#

Fig. C.10: Variogram and covariance functions.

For stationary models, the covariance depends solely on the separation distance h between locations rather than their absolute positions. However, in practice, the covariance between two locations can also be a function of direction, reflecting anisotropy in the spatial relationships. For example, in channel deposits, we often observe longer correlations along the direction of the channel. In the 3D space, this anisotropy results in correlation lengths that form a 3D ellipsoid, capturing the directional variability in spatial continuity.

For the 3D case, we can transform an anisotropic covariance into isotropic by stretching and rotating.

• Rotation: the 3D ellipsoid is rotated from the x y z coordinate system to the x   y   z   using

$$
⎡ ⎣ x ′ y ′ z ′ ⎤ ⎦ = ⎡ ⎣ cos α 0 - sin α 0 1 0 sin α 0 cos α ⎤ ⎦ ⎡ ⎣ 1 0 0 0 cos β sin β 0 - sin β cos β ⎤ ⎦ ⎡ ⎣ cos θ - sin θ 0 sin θ cos θ 0 0 0 1 ⎤ ⎦ ⎡ ⎣ x y z ⎤ ⎦ (C.67)
$$

The rotation angles are usually called θ = azimuth, β = dip and α = rake.

• Stretching: we compute the ratio h/L in the covariance function as

$$
h L = √ ( ∆ x ′ L 1 ) 2 + ( ∆ y ′ L 2 ) 2 + ( ∆ z ′ L 3 ) 2 , (C.68)
$$

where ∆ x   , ∆ y   and ∆ z   are the distances in the x   , y   , and z   directions, respectively. L 1 , L 2 and L 3 are the corresponding correlation lengths.

# C.4.4 Kriging

Kriging is one of the most fundamental methods in geostatistics, with its theoretical foundation developed by Matheron [295], building on the earlier work of Krige [242]. Initially conceived as an interpolation technique, kriging is mathematically related to regression analysis and can be derived as a best linear unbiased estimator (BLUE). It also has a Bayesian interpretation, where, under the assumption of a linear-Gaussian process, the kriging model corresponds to the posterior mean.

Several variants of kriging exist, including simple kriging, ordinary kriging (where the mean is locally estimated), kriging with trend (where the mean is modeled as a function of spatial position), cokriging (which incorporates correlations with secondary variables), among others.

Kriging provides a smooth solution based on a local average of the available data. While this smoothing effect offers a reliable average value, it removes fine-scale details of reservoir heterogeneity that are critical for certain applications. Additionally, kriging is a deterministic method, providing a unique estimate of the property of interest. To address these limitations, geostatistical methods that generate multiple model realizations are often preferred, as they allow for a more detailed representation of heterogeneity and provide a means to assess uncertainty in model predictions.

Like kriging, geostatistical simulation can also be interpreted within a Bayesian framework. Under the assumption of a linear-Gaussian process, the simulated realizations represent samples from a multivariate Gaussian distribution. When averaged, multiple realizations converge to the kriging estimate, which corresponds to the posterior mean. In geostatistics, methods that rely on covariance functions or variograms are commonly referred to as “two-point geostatistics,” as they focus on spatial relationships between pairs of points.

There are various geostatistical (stochastic) simulation methods, with sequential Gaussian simulation (SGS) [171] being one of the most widely used [104]. The core concept of SGS is to simulate each gridblock sequentially along a random path. A sample from p ( m ) is obtained using the chain rule of conditional probabilities:

1. Start at the first gridblock and sample m 1 ∼ p ( m 1 ). 2. Proceed to the second gridblock and sample (

m 2 ∼ p m 2 | m 1 ). 3. Continue to the third gridblock and sample (

m 3 ∼ p m 3 | m 1 ,m 2 ). ...

...

4. Visit the last gridblock and sample m N m ∼ p ( m N m | m 1 ,...,m N m − 1 ).

A model m = [ m 1 ,...,m N m ]   generated using this process represents a sample of the distribution p ( m ). The model parameters can be visited in any sequence, as long as all parameters are eventually accounted for [171]. Each conditional distribution p ( m i | m 1 ,...,m i − 1 ) follows a one-dimensional Gaussian distribution. In SGS, the mean and variance of this Gaussian distribution are estimated using simple kriging. To maintain computational efficiency, SGS typically considers only a limited number of nearby parameters in the neighborhood when estimating each conditional distribution.

# C.4.6 Geostatistical Simulation of Facies

The parameters of geostatistical models are derived from available sample data, such as well logs and seismic measurements. For a geostatistical model

One of the most widely used geostatistical methods for simulating facies is sequential indicator simulation (SIS) [7]. Similar to SGS, SIS visits each gridblock in a random order. At each step of the process, the following occurs:

- 1. Identify nearby data and previously simulated gridblocks.
- 2. Construct the conditional distribution by kriging, calculating the probability of each facies type occurring at the current location.
- 3. Draw a simulated facies type based on the computed probabilities.


Another commonly used method is truncated Gaussian simulation (TGS) [296]. The core concept behind TGS is to generate a realization from a continuous Gaussian field and then apply a series of thresholds to transform the continuous values into categorical facies. Since the facies are derived from an underlying continuous variable, the resulting facies tend to exhibit a natural order, meaning it is unlikely to observe non-adjacent facies (e.g., facies 1 and facies 3) in direct contact with each other. This method is particularly useful for modeling facies with a stratified or gradational structure.

# C.4.7 Beyond Covariance-Based Models

Covariance is effective at capturing the similarity (correlation) between two spatial locations, providing insights into two-point correlations. However, this approach falls short when modeling more complex geological features, such as sinuous 3D channels. For these intricate patterns, methods that account for multiple-point correlations are required 3 .

There are geostatistical algorithms designed to reproduce complex facies distributions that cannot be accurately described with single covariance functions. Among these, the use of locally varying anisotropy (LVA) [43] is quite common. LVA applies standard two-point algorithms but calculates distances while considering changing anisotropy within the model, allowing

3 A more technical explanation for this limitation is that Gaussian models are constrained by the fact that the Gaussian distribution represents the probability distribution with maximum entropy for a given mean and covariance. Essentially, the multivariate Gaussian distribution maximizes spatial disorder and is thus unable to effectively represent structured features like channel systems [224]. This inherent property limits its ability to capture more complex geological patterns that extend beyond simple correlations.

Boolean or object-based simulation [107, 106] involves the random placement of geological structures (objects) within the model. The shapes and characteristics of these objects (e.g., length, width, and sinuosity) are also selected randomly. In this approach, data conditioning requires solving an inverse problem, where objects are adjusted and transformed until the data matches. Although object-based algorithms are capable of producing realistic geological structures, they are challenging to condition when dealing with large amounts of local data.

Another class of algorithms includes multiple-point statistics (MPS) [179, 417, 290], which use training images as a database of geological patterns. Originally, MPS was viewed as an alternative to object-based modeling, designed to generate complex geological structures while being easier to condition on large amounts of data [412]. Today, there are many algorithms in this category, employing techniques similar to the ones used in machine learning and computer graphics [289].

The previous methods are often called classical geostatistical methods, as they rely on probabilistic models to generate the distribution of geological structures. In contrast, there are methods specifically designed to describe the depositional processes that formed the reservoir. These approaches are generally classified as rule-based modeling and process-based modeling [352]. Rule-based methods [202, 424] use predefined geological rules, heuristics, and geometric constraints to construct models. While they can produce more realistic geological structures compared to classical geostatistical methods, they are less effective at conditioning to well and seismic data.

Process-based modeling [341, 89, 52] simulates the physical processes that govern geological formations, such as sediment transport, erosion, and deposition. These models use numerical solutions of physical laws to generate highly realistic geological structures. The main challenges of process-based modeling include poorly known initial and boundary conditions needed to constrain the numerical model, severe limitations in conditioning models to observations, and high computational costs, which hinder the generation of multiple realizations and reduce the ability to represent uncertainty. As a result, process-based approaches are not commonly used for full-field model generation. Instead, they are typically utilized to gain insights into the expected reservoir geometry and heterogeneity.

Nothing to see here. Move along.

![](<ensemble_data_assimilation_e-book_version_images/imageFile153.png>)

D

# Brief Literature Review

Abstract: This appendix offers a brief literature review, highlighting influential papers and current applications of ensemble methods in reservoir modeling.

# D.1 Introduction

Ensemble-based data assimilation methods have gained widespread attention for their ability to manage high-dimensional problems and quantify uncertainty, making them particularly well-suited for complex geophysical systems. The literature on this topic is extensive and continues to grow. This section presents a concise review of ensemble-based data assimilation methods, focusing on their application to subsurface characterization and monitoring.

# D.2 EnKF and Its Variants

Evensen [136] introduced the EnKF to overcome the limitations of the extended Kalman filter (EKF) in managing high-dimensional, nonlinear dynamical systems. The EKF relies on linearizing the model and observation equations around the estimated state mean, which requires derivative calculations. As noted by Evensen [139], these linearizations can result in unstable propagation of the state covariance. Additionally, updating covariance matrices in the EKF becomes impractical for large-scale problems. In contrast, the EnKF is a Monte Carlo-based method that uses an ensemble of state vectors to approximate the mean and covariance, updating them sequentially over time. Typically, the number of state vectors in the EnKF ensemble is much smaller than the number of unknowns, allowing the method to efficiently

Although the EnKF was initially introduced by Evensen [136], its formulation was later clarified by Burgers et al. [51] and Houtekamer and Mitchell [197], who introduced the concept of updating each ensemble member with independently perturbed observations, which led to the modern implementation of the EnKF.

The initial development of the EnKF occurred primarily in the fields of numerical weather prediction (NWP) and oceanography. Recent review papers by Houtekamer and Zhang [200] and Carrassi et al. [60] summarize key developments and ongoing challenges in these areas. EnKF-like methods are currently operational at the TOPAZ Ocean System, developed by the Nansen Environmental and Remote Sensing Centre (NERSC) [375], and in the atmospheric model at the Canadian Meteorological Centre (CMC) [201].

Variants of the EnKF fall into two main categories: “stochastic” and “deterministic (or square root)” schemes. Stochastic versions of the EnKF use a perturbed-observation 1 scheme to derive the analysis equation. Advocates of square-root schemes argue that data perturbation introduces additional sampling errors into the process [60], which can be avoided with the squareroot variants. Notable examples of deterministic schemes include the ensemble transform Kalman filter (ETKF) [39], the ensemble adjustment Kalman filter (EAKF) [13], the ensemble square root filter (EnSRF) [463], the local ensemble transform Kalman filter (LETKF) [207], and the deterministic ensemble Kalman filter (DEnKF) [374].

The adoption of the EnKF for reservoir data assimilation by Nævdal et al. [313] initiated a series of research efforts, particularly in petroleum engineering, leading to numerous subsequent studies. Comprehensive reviews of the main developments, challenges, and early applications of the EnKF in reservoir data assimilation from 2002 to early 2011 are provided by Aanonsen et al. [3] and Oliver and Chen [331]. The first reported field application of the EnKF for reservoir data assimilation was presented by Skjervheim et al. [399]. Subsequent field examples include studies by Bianco et al. [36], Evensen et al. [144], Haugen et al. [188], and Emerick and Reynolds [127].

1 van Leeuwen [447] noted that while traditional interpretations of stochastic EnKF schemes focus on perturbing observations, it is more appropriate to perturb the predictions. This approach assumes that the true system is a realization from the same distribution as the ensemble members. Since the true system’s measurements are already affected by observation errors, the predictions of each ensemble member should be perturbed in a similar manner. In practice, the calculations are the same whether perturbations are applied to the observations or the predicted data. However, these interpretations may yield different results when extending the methods to address nonadditive errors.

# D.3 From EnKF to Iterative ES

Sequential data assimilation is a key factor in the success of the EnKF and its variants in NWP. The recursive updates in time help to maintain the model states close to the observations. However, data assimilation in NWP differs significantly from that in reservoir applications. In NWP, forecasts are made on a scale of hours to a few days, whereas in reservoir modeling, predictions are made over years. Additionally, NWP typically assimilates a much larger volume of observations. The short-term nature and the large number of data points in NWP tend to reduce the violation of the linearity during the update step.

In contrast, reservoir data assimilation traditionally focuses on parameter estimation, aimed at determining “static” model parameters, while NWP deals with state estimation, focusing on dynamic variables like pressure and temperature distributions. The main uncertainty in NWP lies in the initial condition, whereas in reservoir applications, it is the spatial distribution of rock properties. In addition, NWP involves unstable dynamics, where small changes in initial conditions can lead to divergent solutions, while reservoir models exhibit stable dynamics. Due to these differences, the sequential data assimilation approach of the EnKF is well-suited for NWP but less effective for reservoir modeling.

To make sequential data assimilation work for reservoirs, the process must be framed as a combined parameter-state estimation problem. This approach prevents the need to rerun reservoir simulations from the initial condition at each assimilation time step. This approach assumes that the updated reservoir states (i.e., the simulator’s primary variables) remain statistically consistent with those obtained from forward simulations initialized at time zero using the updated model parameters. However, this consistency is guaranteed only in the linear-Gaussian case [435]. In practice, consistency violation tends to degrade the data assimilation results [435, 459].

One way to ensure consistency between updated parameters and primary variables is to rerun the reservoir simulator from time zero using the latest model parameters after each assimilation step. While this ensures consistency, it significantly increases computational cost. Wang et al. [459] referred to this method as the half-iteration EnKF (HI-EnKF). To improve efficiency, Wang et al. [459] proposed rerunning the ensemble from time zero only if the average relative change in the ensemble mean exceeds a specified threshold.

Although sequential updates help to manage nonlinearity, applications with strong nonlinearities may require iterative methods to constrain ensemble members effectively, especially when high-quality observations are available [376, 42].

One of the first iterative EnKF methods was introduced by Gu and Oliver [178], who combined an ensemble-based sequential scheme with a GaussNewton (GN) RML formulation, calling it ensemble randomized maximum likelihood (EnRML). This method involves rerunning simulations from time

Skjervheim et al. [400] proposed using the ES for reservoir applications, arguing that the batch update approach of ES might suffice given the diffusive and stable nature of reservoir models. ES offers significant computational advantages by eliminating the need for frequent simulation restarts and providing flexibility in integrating complex parametrizations, including structural parameters and facies. It also interfaces more easily with commercial simulators, facilitating its adoption in operational workflows.

However, subsequent studies revealed that a single ES update is insufficient for constraining reservoir models to multiple observations [78, 132], leading to the proposal of iterative versions of ES. Chen and Oliver [78] introduced batch-EnRML, which incorporated the EnRML scheme of Gu and Oliver [178] into the smoother framework, showing good results in the Brugge case, though it required several iterations to converge. Around the same time, Emerick and Reynolds [132] introduced the ES-MDA method, which exhibited good data assimilation results with a significantly lower computational cost compared to batch-EnRML. The same authors proposed in [131] a comparative study of ensemble methods in a simple but highly nonlinear reservoir problem. Among the methods investigated, ESMDA showed remarkable performance, achieving good approximations of the posterior marginal distribution of log-permeability and water production, comparable to those obtained through rigorous MCMC sampling. In the same year, Chen and Oliver [79] presented an improved implementation of EnRML by replacing the GN update with an LM update formula and introducing a more stable Hessian approximation. The resulting LMEnRML method demonstrated computational performance comparable to ES-MDA in both the two-phase flow case proposed in [131] and the Brugge case, with the added potential advantage of not requiring the pre-selection of the number of iterations.

Stordal [413] introduced the iterative adaptive Gaussian mixture smoother (IAGS), an extension of the adaptive Gaussian mixture filter proposed in Stordal et al. [416] and Stordal and Lorentzen [415]. This method integrates an EnKF-like update equation with weighting and resampling steps akin to those used in particle filters [114]. The authors draw parallels between IAGS, EnRML, and ES-MDA, particularly noting that the IAGS’s bandwidth parameter corresponds to the LM parameter in EnRML or the inflation coefficient in ES-MDA. The key distinction lies in the inclusion of the

Luo et al. [279] introduced a variation of the EnRML within the framework of iterative ensemble smoothing, utilizing the regularized LevenbergMarquardt (RLM) algorithm from Jin [220] to solve a minimum-average-cost (MAC) problem. This method, referred to as RLM-MAC, was compared with a version of LM-EnRML discussed in Chen and Oliver [79]. The results showed that RLM-MAC outperformed LM-EnRML in the Lorenz 96 model [276], while their performance was comparable in reservoir data assimilation scenarios.

The standard ES-MDA method requires specifying the number of assimilations and the sequence of inflation coefficients in advance. This requirement spurred research into adaptive ES-MDA schemes. Emerick [118] introduced an ad hoc adaptive scheme based on the evolution of the data-mismatch objective function. Building on this, Le et al. [253] incorporated an additional check to limit the maximum allowable change in model parameters. The same authors also introduced a scheme that employed the regularized LM approach from Hanke [184]. However, these early adaptive schemes were found to require an excessive number of iterations for operational use. To address this issue, Rafiee and Reynolds [356] proposed selecting the MDA inflation coefficients based on a geometrically decreasing sequence, an idea that was further explored in subsequent studies [122, 284, 396].

More recently, Raanes et al. [354] revisited the EnRML method and introduced a new derivation based on the fact that estimates from ensemble methods are confined to the subspace defined by the prior ensemble. The resulting method, the subspace iterative ensemble smoother (SIES), is simpler in both derivation and implementation compared to EnRML.

Currently, iterative forms of ES rank among the most effective and widely adopted methods for reservoir data assimilation. Their application in realworld field cases has expanded significantly, and these methods have become standard tools in applications for petroleum reservoirs.

# D.4 Localization

Localization is a standard technique used to address the limitations imposed by small ensemble sizes. Houtekamer and Mitchell [197] first introduced localization by applying a distance cutoff to the Kalman gain, ensuring that only parameters and states within a specified distance from the observation were updated. Later, Houtekamer and Mitchell [198] improved this approach by incorporating the Schur product for localization. The authors observed that using the Schur product resulted in relatively smoother mod-

An alternative implementation of localization is known as local analysis or domain localization. This method involves performing multiple localized updates, using only observations near each parameter location. Compared to standard Schur-product localization, domain localization does not require the explicit formation of covariance or Kalman gain matrices, making it applicable to square root schemes. Sakov and Bertino [372] compared both methods and concluded that they produce similar results. Chen and Oliver [81] also compared domain localization with Schur-product localization of the Kalman gain and found that LM-EnRML converges faster with domain localization.

Arroyo-Negrete et al. [19] and Devegowda et al. [108] proposed using streamlines to identify model gridblocks that are sensitive to data, which are then used to define the corresponding localization values. Chen and Oliver [77] and Emerick and Reynolds [128] noted that, while streamlinebased localization is intuitive and appealing because it incorporates some of the fluid transport physics into the localization process, relying solely on these regions of influence risks confining model updates too narrowly around wells, particularly when the prior model covariance exhibits long correlation ranges.

Localization schemes typically assume that the Kalman gain or the covariances between parameters and data depend on distance. However, some localization schemes are designed for more general covariance structures. One of the earliest non-distance-based localization methods is the hierarchical filter proposed by Anderson [14]. In this approach, an ensemble is divided into sub-ensembles, which are then used to compute correction coefficients for the Kalman gain. Instead of dividing the ensembles, Zhang and Oliver [482] suggested using bootstrap resampling to generate new ensembles. Furrer and Bengtsson [156] derived a localization function for general covariance structures by minimizing the norm of the difference between the true covariance and the localized estimate on a term-by-term basis without enforcing positive definiteness. The final expression depends on the true covariance, but the authors suggest replacing the true covariance with the ensemble estimate to construct a non-distance-based localization function. Bishop and Hodyss [37] proposed generating the localization matrix by raising each element of a sample correlation matrix of model variables to a specified power. Luo et al. [280] suggested calculating localization values by using correlation coefficients estimated from the ensemble and applying a threshold to determine the final values. Lacerda et al. [245] reviewed several of these methods and compared their effectiveness in updating non-local parameters in a synthetic reservoir data assimilation problem. They concluded that most of these methods require careful tuning of internal parameters, which significantly affects their performance.

Luo and Bhakta [278] extended their correlation-based method by introducing a procedure to estimate the noise level in the correlation esti-

The premature loss of ensemble variance remains a significant challenge in ensemble methods. Localization is currently the most effective approach to mitigate this issue, but it requires careful tuning to achieve optimal results. Developing robust strategies to address sampling errors, including adaptive localization schemes, is an active area of research.

# D.5 Model Errors

The “perfect model assumption” is prevalent in many reservoir data assimilation applications. This assumption unrealistically posits that the model would accurately represent the true behavior of the reservoir if the correct values of uncertain parameters were known. In reality, however, models inevitably simplify the actual system, leading to errors from these inherent approximations. Such errors are commonly referred to as model errors, but other terms appear in the literature, including model inadequacy, model discrepancy, model bias, and structural uncertainty [235, 49].

The formal incorporation of model errors into reservoir data assimilation has been a relatively recent development in the literature. Studies such as [450, 330, 141, 9] have shown that neglecting model errors can lead to overconfidence in the data and underestimation of uncertainty in model forecasts.

Model errors in data assimilation are commonly addressed by assuming that they are additive and Gaussian or by reducing the weight of observations, which is achieved by increasing the data-error variance [80, 124]. This approach is discussed in Sun et al. [422], where the authors introduce an ad hoc procedure to mitigate the excessive reduction in uncertainty that occurs when model errors are present.

Oliver and Alfonzo [330] introduce a method for incorporating model errors by adjusting the data-error covariance, C e , based on the residuals (i.e., the difference between observed and simulated data) after data assimilation. The approach updates C e and then repeats the assimilation process, starting from the prior ensemble. This method has been further explored in the context of production data assimilation [277] and 4D seismic data assimilation [9]. Emerick and Neto [125] introduced an efficient variation of

Evensen [141] expanded upon the traditional approach of assuming additive model errors by introducing a method to estimate the model error term concurrently with the model parameters during data assimilation. While this approach broadens the treatment of model errors, it still relies on the assumption of Gaussian error distributions. Overall, the development of robust methods for handling non-Gaussian model errors in data assimilation remains an open problem.

# D.6 Facies

Due to the inherent Gaussianity assumptions in the formulation of ensemble methods, they are better suited for covariance (variogram) based reservoir models. Consequently, these methods may face difficulties in preserving complex geological features, with categorical facies being a particularly challenging example. As a result, the development of robust parametrizations strategies for facies has become a highly active area of research, leading to a substantial number of publications in recent years.

One of the earliest works on facies updating using ensemble methods was presented by Liu and Oliver [267], which employed the truncated plurigaussian (TPG) method [157, 17, 35]. The TPG parametrization has since been explored and further refined in subsequent studies [267, 484, 387, 386]. Today, TPG remains one of the most widely used and effective approaches for parameterizing facies models within ensemble-based methods.

Another approach to updating facies models with ensemble methods involves the use of level-set functions [64, 272, 305, 304, 347]. As noted by Mannseth [287], there is a relationship between level-set and TPG methods, as any plurigaussian field can be represented by a corresponding level-set function.

However, TPG and level-set functions present significant challenges when representing facies with complex geometries, such as channels, particularly those produced by object-based modeling [107, 106], multiple-point statistics techniques [179, 417, 290], or rule-based modeling [352]. Consequently, numerous studies have proposed alternative strategies for models with channelized facies distributions. Notable examples include discrete cosine transform [213], kernel principal component analysis [378, 377], sparse dictionary learning with K-SVD [237], and methods based on thresholded principal component analysis [453, 71, 120].

Another class of methods involves updating “probability maps,” which are then used to recompute the facies distribution using geostatistical algorithms. Variations of this approach exist; for example, some studies employ “pseudo-wells” in areas with high facies probability as conditioning data

Recently, deep learning networks, particularly deep generative models, have emerged as a promising research direction for developing facies parametrizations. Various approaches have been explored in the literature, including deep belief networks [55], variational autoencoders [246, 56], generative adversarial networks [62, 247, 115, 63, 308], style transfer networks [268], and latent diffusion models [148]. Some of these deep learning strategies are compared in [57]. One attractive feature of these methods is that they allow us to represent facies in terms of latent Gaussian random fields, which is particularly appealing in the context of ensemble methods. The primary challenge of using these models lies in the substantial computational cost required to train deep learning networks, particularly when applied to multi-million-cell 3D reservoir models.

# D.7 4D Seismic Data Assimilation

4D (time-lapse) seismic imaging involves conducting repeated seismic surveys over time to monitor fluid movements and pressure variations within reservoirs. The literature on 4D seismic data assimilation is quite extensive. Oliver et al. [336] provides a comprehensive review of this topic, detailing key methods, challenges, and recent applications.

The assimilation of 4D seismic data presents several challenges, particularly due to the presence of significant errors and biases in the seismic datasets, as well as limitations in the forward modeling process. Moreover, 4D seismic typically involves a large number of data points, which can exacerbate issues with variance underestimation in ensemble methods. There are also scale issues, as seismic datasets have lower vertical resolution than current reservoir simulation models. These aspects have been the subject of several investigations. For example, Oliver [329] analyzed the impact of spatially correlated errors in 4D seismic data and found that ignoring these correlations led to biased parameter estimates and inadequate uncertainty quantification. The effect of model errors on the assimilation of 4D seismic data has also been investigated in [9, 320, 282, 125].

4D seismic assimilation is commonly performed in one of three main domains: the seismic domain, which involves seismic attributes such as amplitudes and time shifts; the elastic domain, which includes pressure and shear-wave velocity or impedance data; and the simulation domain, which focuses on pressure and phase saturation. Among these, the elastic domain is often preferred because it provides a balanced approach to both data preparation and forward modeling [336]. Additionally, several publications have proposed alternative representations of 4D datasets to address the challenges posed by the large volume of data points and data errors. These include dis-

The first application of ensemble methods for assimilating 4D seismic data was introduced by Skjervheim et al. [399], who applied EnKF to integrate production and 4D data in an oilfield. Iterative forms of ES have also been tested in several publications, including ES-MDA [133, 118, 323, 475, 320, 321, 370, 125], RLM-MAC [274, 282, 275], and SIES [321, 294].

# D.8 Data-Space Inversion

Data-space inversion (DSI) offers an alternative to the traditional modelspace inversion commonly used in reservoir data assimilation. The core concept of DSI involves directly updating the predictions derived from a prior ensemble of models to reflect observed production history without modifying the underlying models themselves. This approach enables the generation of an ensemble of forecasts without the need for the time-consuming model updating process. One limitation of DSI is that it only provides forecast estimates, not the corresponding models. In practice, however, reservoir models are useful for evaluating various operational scenarios. Thus, DSI and modelspace inversion should be viewed as complementary approaches rather than competing methods.

The DSI method introduced by Sun and Durlofsky [419] employs PCA to reparameterize the predicted data from the prior ensemble into a lowerdimensional space and uses RML to sample from the posterior distribution of predicted data. The authors applied a data transformation prior to PCA to enhance linearity. Sun et al. [421] further extended the DSI method by introducing a more generalized data transformation procedure, and Sun and Durlofsky [420] applied the method to a geological carbon storage problem.

Earlier, Scheidt et al. [381] proposed a similar concept in a method called prediction-focused analysis (PFA), which involves projecting prior predictions into a low-dimensional space and using kernel smoothing to estimate the joint distribution of historical and forecasted data. However, PFA seems to be limited to problems with a small number of data points, as it requires projection into very few dimensions (two or three in the examples presented). Satija and Caers [379] improved the PFA method by incorporating canonical functional component analysis to enhance linearity in the

Lima et al. [263] combined ES-MDA and DSI, resulting in a more robust and efficient DSI implementation. This method has been further enhanced through the use of various deep learning techniques, leading to successful applications in naturally fractured reservoirs [218] and geological carbon storage [469, 217].

# D.9 Ensemble Kalman Inversion

Ensemble methods have also been applied to general inverse problems. Iglesias et al. [210] introduced the term ensemble Kalman inversion (EKI), which has since gained significant attention in the inverse problem literature [240, 481, 208, 382, 109]. In practice, the EKI process closely resembles iterative ES. Notably, the regularization scheme used in EKI is essentially the same as that adopted in ES-MDA, with the primary difference being the termination criteria. EKI implementations typically use a regularization criterion based on the discrepancy principle [184], while ES-MDA terminates the data assimilation based on the sum of the reciprocals of the data-error inflation coefficients. Moreover, EKI appears to focus on generating the “best” model rather than quantifying uncertainty in the posterior, which might be one reason for the difference in stopping criteria.

# D.10 Ensemble-Based Optimization

Ensemble methods have also been utilized as control optimization techniques, particularly in the petroleum literature. The first publication proposing the use of the EnKF equation for control optimization was presented by Lorentzen et al. [271]. However, the method was later refined by Chen et al. [83], who introduced regularization to the ensemble-gradient estimate and coined the term ensemble-based optimization (EnOpt). Another distinction between EnOpt and the earlier work by Lorentzen et al. [271] is that Chen et al. [83] designed EnOpt to optimize the expected value of an objective function calculated across the ensemble of model realizations.

Using EnOpt, Chen and Oliver [76] achieved the highest net present value in the Brugge benchmark problem [346], drawing significant attention to the method. The idea behind EnOpt is to sample an ensemble of controls around the current solution, use the ensemble to compute the covariance between controls and the optimization objective function, and use this covariance to define the search direction in the steepest ascent method.

# D.11 Ensemble-Based Methods in Multimodal Distributions

Even for Gaussian priors with Gaussian data errors, the objective function discussed in Chapter 2 (Eq. (2.28)) is strictly quadratic only when the forward model is linear. In the nonlinear case, it is impossible to draw general conclusions about the expected shape of the objective function, particularly because the model space in reservoir data assimilation is extremely highdimensional. It is conceivable—and even likely—that the objective function is far more complex than quadratic, potentially exhibiting multiple local and global minima. As a result, the posterior PDF may be multimodal.

A well-known example of reservoir data assimilation objective function with multiple minima is the Fault Problem introduced by Tavassoli et al. [433]. This problem involves a cross-sectional model of a reservoir with intercalated highand low-permeability layers and a single fault. By varying the fault throw and the permeability values, the authors obtained a datamismatch objective function with a very irregular shape and multiple minima. Zhang et al. [479] also examined the shape of the objective function for a problem involving the estimation of a single channel’s position based on pressure data. They concluded that the resulting objective function has multiple minima and is non-differentiable at some locations. Additional examples of multimodal posterior PDFs for synthetic reservoir problems are provided by [293, 480].

A common aspect in these cases is that all examples with multimodal posteriors involve problems with relatively few model parameters. There is limited discussion on the shape of the objective function in cases where reservoir parameters vary on a gridblock-by-gridblock basis. One of the few attempts to explore this is presented in Oliver et al. [334, Chap. 8]. They analyzed a two-dimensional model on an 11 × 11 grid operating in a five-spot geometry and generated multiple posterior models by assimilating pressure data. By interpolating between distinct posterior models, they observed that the objective function exhibited two minima. Further analysis, however, revealed that these minima were connected by an elongated curved valley with relatively low objective function values.

The non-Gaussian nature of the posterior PDF, including the potential presence of multiple modes, clearly challenges the effectiveness of ensemble methods. This issue is readily demonstrated in low-dimensional toy problems; for example, Fig. 5.4 in Section 5.3.4 shows how applying ES-MDA fails to capture the two modes of the posterior distribution. This limitation stems from the method’s formulation, which is optimal only for Gaussian distributions. In low dimensions, however, this limitation can be partially addressed through strategies involving multiple ensembles. For example, Zhang et al. [480] proposed the iterative local updating ensemble smoother (ILUES), which updates each ensemble member with a sub-ensemble of the closest realizations, enabling it to capture multiple distribution modes effectively in low-dimensional cases. A similar approach is explored by Moyen and Gentilhomme [310]. In small dimensions, even simple reweighting steps, such as importance sampling, are often sufficient to correct the sampling. The main challenge lies in high dimensions, where these techniques yield only marginal improvements over standard iterative ES implementations. Nonetheless, it is unclear that the PDFs generated by real reservoir problems are sufficiently non-Gaussian to render ensemble-based results unreliable. On the contrary, there is ample evidence that ensemble methods provide valuable results in practical reservoir applications.

# D.12 Reservoir Applications

# D.12.1 Petroleum Reservoirs

Petroleum reservoirs are among the areas with the most extensive application of ensemble methods for data assimilation. Oil and gas companies have been utilizing reservoir simulation models for more than 50 years. As a result, data assimilation—commonly referred to as “history matching” in the petroleum industry—has long been a critical component of reservoir management and decision-making processes.

The literature on assisted history matching methods is extensive and diverse, but the introduction of the EnKF to the petroleum field by Nævdal et al. [313] sparked a surge of research activity. This led to a significant number of publications, primarily focused on evaluating the method in synthetic problems. The first documented field application of the EnKF for reservoir data assimilation was presented by Skjervheim et al. [399]. Additional field applications were later reported by Bianco et al. [36], Evensen et al. [144], Haugen et al. [188], and Emerick and Reynolds [127]. An influential review paper on the EnKF for petroleum reservoirs was published by Aanonsen et al. [3], which outlined the key challenges of the method. This review significantly shaped the research agenda in the years that followed, providing

Despite these promising results, the limitations of the EnKF formulation for practical reservoir applications became increasingly apparent. A key issue was the sequential data assimilation scheme, which often introduced inconsistencies between model parameters and states, undermining the method’s effectiveness and increasing the computational cost of the process [435, 459].

Skjervheim et al. [400] proposed using the ES instead of the EnKF for reservoir applications. Although initial attempts with standard ES proved ineffective in subsequent studies [78, 132], this work spurred the development of iterative ES variants [78, 79, 132, 413, 279, 354]. Today, iterative ES methods are widely used for data assimilation in petroleum reservoirs, with both in-house and commercial software integrating these techniques. In addition to proprietary solutions, several open-source tools have gained prominence, with the most notable being the ERT [1]. There are also some Python open-source codes, including PET [2], resmda [383], and pyESMDA [91].

The number of publications reporting field applications of iterative forms of ES in petroleum reservoirs has become quite large. Some examples include [133, 80, 118, 297, 344, 371, 46, 6, 143, 273, 475, 11, 124, 125].

# D.12.2 Groundwater Hydrology

Another field with extensive use of ensemble methods for data assimilation is hydrology, particularly in applications related to groundwater flow and contaminant transport. The earliest applications of ensemble data assimilation in hydrology were introduced by Reichle et al. [360], who used the EnKF to estimate soil moisture profiles. In a subsequent study, Reichle et al. [361] compared the EKF with the EnKF, highlighting the advantages of the ensemble-based approach. The first documented application of the EnKF for groundwater flow calibration was likely presented by Chen and Zhang [82], who used it to calibrate conductivity fields with hydraulic head data. Subsequent studies further explored the potential of the EnKF across a range of groundwater flow and contaminant transport problems [264, 205, 153, 485, 314, 167, 470].

Similar to the early developments in petroleum reservoirs, the EnKF was initially the preferred method for hydrogeology data assimilation. However, recent applications have shifted toward iterative forms of ES, with a significant number of publications evaluating the performance of these methods in a variety of scenarios.

For instance, Chen et al. [74] applied EnKF, ES, and the smoother version of EnRML to estimate the hydraulic conductivity field in the Hanford 300 Area [154] using tracer data. Their findings suggested that EnRML might be a superior alternative to both EnKF and ES for such applications. Kumar et al. [244] utilized an ES implementation to assimilate satellite data from the Gravity Recovery and Climate Experiment (GRACE) to monitor changes in total terrestrial water storage—comprising soil moisture, groundwater, surface waters, snow, ice, and wet biomass—across the United States. Building on this, Li et al. [255] extended the approach to a global scale, aiming to generate time series of groundwater storage for improved drought monitoring. Li et al. [258] also compared EnKF, ES, and iterative ES in a synthetic groundwater data assimilation problem and concluded that iterative ES outperformed standard ES and achieved results comparable to EnKF at a lower computational cost.

Lam et al. [248] compared ES-MDA and LM-EnRML in a synthetic case study for estimating log-hydraulic conductivity fields using transient hydraulic data. Their results showed that LM-EnRML outperformed ES-MDA using an ensemble size of 200. However, they also observed that the accuracy of ES-MDA improved consistently as the ensemble size increased, whereas LM-EnRML did not show the same level of improvement with larger ensembles.

Several studies have applied iterative ES methods for data assimilation in contaminant source identification and transport problems [172]. For example, Tso et al. [444] employed ES-MDA to estimate leak parameters using time-lapse electrical resistivity tomography data. Similarly, Chen et al. [86] used ES-MDA to jointly identify contaminant sources and hydraulic conductivities. In another study, Kang et al. [232] combined ES-MDA with a variational autoencoder to estimate the saturation of dense nonaqueous phase liquid (DNAPL) contamination. Additionally, Chen et al. [85] used ES-MDA to estimate the release history of a contaminant source.

Strategies for updating hydrogeological models generated with multiplepoint statistics using iterative ES methods have also been proposed [59, 249, 26, 434]. More recently, open-source data assimilation software for groundwater problems based on ES has emerged. Notable examples include PEST++ [465], DART-PFLOTRAN [216], and genES-MDA [440].

# D.12.3 Geological Carbon Storage

Geological carbon storage (GCS) is the main element of carbon capture and storage (CCS) and carbon capture, utilization and storage (CCUS) projects, offering a significant mechanism for reducing greenhouse gas emissions and helping to meet climate goals [366]. GCS involves the injection of CO 2 from industrial emissions or captured directly from the air into subsurface formations, such as saline aquifers [61, 155], depleted oil and gas reservoirs [185, 191], or as part of enhanced oil recovery (EOR) processes [180, 326], where it can be stored securely while also potentially enhancing hydrocarbon recovery.

GCS processes present additional challenges compared to petroleum and groundwater modeling. A key distinction is the longer forecast periods, often extending beyond 100 years, and the large-scale models required, both of which significantly increase computational costs. Moreover, GCS simulations must account for more complex physical processes, including near-wellbore effects, intricate fluid interactions, and thermal and geomechanical behavior. Adding to the complexity, GCS projects typically involve fewer wells and less available data than petroleum fields, resulting in higher uncertainties in long-term forecasts.

The existing literature on ensemble data assimilation for GCS focuses primarily on two areas. A set of studies evaluates the performance of these methods in synthetic problems [431, 173, 283, 67, 222, 68]. The second group explores strategies to reduce the computational cost of full-field GCS simulations, including the use of machine learning proxy techniques [427, 426, 385] and DSI schemes [469, 217].

# D.12.4 Geothermal Energy

Geothermal energy is a renewable resource that harnesses the Earth’s internal heat to provide a continuous, low-emission alternative to conventional energy sources. By extracting heated water from geological reservoirs, geothermal systems can generate electricity or provide direct heating.

The literature on data assimilation for geothermal reservoirs is relatively sparse compared to the extensive studies available for petroleum and groundwater hydrology. Most publications focus on evaluating data assimilation methods with different types of data for conditioning geothermal models. For instance, Marquart et al. [291] tested the EnKF for the assimilation of chemical tracer concentrations and temperature data. Wu et al. [466] explored the assimilation of tracer data using ES-MDA, while Oudshoorn et al. [339] examined the use of ES-MDA to assimilate electromagnetic data. Shariatinik et al. [392] tested the EnKF with electrical resistivity tomography. Békési et al. [32] investigated the use of ES-MDA to assimilate data

# D.12.5 Seismic Inversion

Seismic inversion is typically defined as the process of estimating subsurface properties such as acoustic impedance, velocity, and density from seismic reflection data. This process is closely related to rock-physics (or petrophysical) inversion, where the goal is to estimate reservoir characteristics like lithology, porosity, fluid content, and facies distribution from seismic data. The terms seismic inversion and rock-physics inversion are often used interchangeably. However, in practice, these processes are usually performed sequentially, with the results of seismic inversion serving as input for rockphysics inversion. That said, there are also joint inversion strategies [176].

The body of literature and the range of methods proposed for seismic inversion are extensive. These methods differ in their representation of rock physics and the inversion techniques employed, spanning from deterministic and stochastic optimization approaches to Monte Carlo methods. Grana et al. [176] presents a recent review of models and methodologies in this area.

Recently, ensemble methods have been investigated for seismic inversion problems. For example, Liu and Grana [265] applied ES-MDA to generate multiple realizations of reservoir properties, including seismic velocities, density, porosity, mineralogy, and saturation from seismic amplitude data. Moyen and Gentilhomme [310] used a modified EnRML implementation with sensitivities estimated from sub-ensembles to invert acoustic impedance data into porosity, shale fraction, and fluid saturation. Cao et al. [58] employed ES-MDA with correlation-based localization for joint seismic inversion, while Exterkoetter et al. [147] combined ES-MDA with a variational autoencoder to invert seismic amplitude data into facies. Spremić et al. [411] used the LETKF [207] to invert seismic AVO (amplitude-variation-withoffset) data to clay content and fluid saturation for a petroleum field in the North Sea.

Ensemble methods have also been considered for full waveform inversion (FWI). Unlike traditional seismic inversion, which uses only parts of the seismic data, such as amplitudes or traveltimes, FWI leverages the entire seismic waveform to produce more accurate and detailed subsurface representations [451]. FWI typically employs a forward model based on the finite difference method and involves iteratively adjusting the subsurface model until the predicted seismic waveforms closely match the recorded seismic signals, making the inversion process computationally intensive. As a result,

# References

- [1] Ensemble based reservoir tool (ERT). Software. URL https://ert. readthedocs.io/en/latest/ .
- [2] Python ensemble toolbox (PET). Software. URL https://github. com/Python-Ensemble-Toolbox/PET .
- [3] Aanonsen, S. I., Nævdal, G., Oliver, D. S., Reynolds, A. C., and Vallès, B. Review of ensemble Kalman filter in petroleum engineering. SPE Journal , 14(3):393–412, 2009. DOI: 10.2118/117274-PA .
- [4] Aanonsen, S. I., Tveit, S., and Alerini, M. Using Bayesian model probability for ranking different prior scenarios in reservoir history matching. SPE Journal , 24(4), 2019. DOI: 10.2118/194505-PA .
- [5] Aanonsen, S. I., Fossum, K., and Mannseth, T. Bayesian model evaluation for multiple scenarios. Computational Geosciences , 27, 2023. DOI: 10.1007/s10596-023-10241-2 .
- [6] Abadpour, A., Adejare, M., Chugunova, T., Mathieu, H., and Haller, N. Integrated geo-modeling and ensemble history matching of complex fractured carbonate and deep offshore turbidite fields, generation of several geologically coherent solutions using ensemble methods. In Proceedings of the Abu Dhabi International Petroleum Exhibition &amp; Conference, Abu Dhabi, UAE, 12–15 November , number SPE-193028MS, 2018. DOI: 10.2118/193028-MS .
- [7] Alabert, F. G. Stochastic imaging of spatial distributions using hard and soft information. Master’s thesis, Stanford University, 1987. URL https://pangea.stanford.edu/departments/ere/dropbox/scrf/ documents/Theses/SCRF-Theses/1980-1989/1987_MS_Alabert. pdf .
- [8] Alcolea, A., Carrera, J., and Medina, A. Pilot points method incorporating prior information for solving the groundwater flow inverse problem. Advances in Water Resources , 29:1678–1689, 2006. DOI: 10.1016/j.advwatres.2005.12.009 .
- [9] Alfonzo, M. A. and Oliver, D. S. Seismic data assimilation with an imperfect model. Computational Geosciences , 24:889–905, 2020. DOI: 10.1007/s10596-019-09849-0 .


[10] Allam, F. A., El-Banbi, A. H., Bustami, S. S., Saada, T. H., and Fahmy, I. I. History match tuning through different upscaling algorithms. In Proceedings of the SPE Annual Technical Confer-

ence and Exhibition, Houston, Texas , number SPE-90292-MS, 2004. DOI: 10.2118/90292-MS .

- [11] Alqallabi, S., Gacem, M. T., Al-Jenaibi, F., Tahir, S., Ameri, S. M., Ouzzane, D. E., Adli, M., Malla, L., Cornejo, V. O. S., Almarzooqi, A., Sunagatullin, R., Hidayati, S. R., Voleti, D. K., Messabi, F. A., Montani, H., Shibasaki, T., Tani, K., Mohamed, F., Sankararaj, R., Ducroux, S., Wojnar, K., and Gourc, L. Key learnings from application of ensemble-based modelling on three giant carbonate oilfields for optimal economic decisions under static and dynamic uncertainties. In Proceedings of the ADIPEC, Abu Dhabi, UAE, October , number SPE-211409-MS, 2022. DOI: 10.2118/211409-MS .
- [12] Amaefule, J. O., Altunbay, M., Tiab, D., Kersey, D. G., and Keelan, D. K. Enhanced reservoir description: Using core and log data to identify hydraulic (flow) units and predict permeability in uncored intervals/wells. In Proceeding of the SPE Annual Technical Conference and Exhibition, Houston, Texas, October , number SPE-26436-MS, 1993. DOI: 10.2118/26436-MS .
- [13] Anderson, J. L. An ensemble adjustment Kalman filter for data assimilation. Monthly Weather Review , 129(12):2884–2903, 2001. DOI: 10.1175/1520-0493(2001)129&lt;2884:AEAKFF&gt;2.0.CO;2 .
- [14] Anderson, J. L. Exploring the need for localization in ensemble data assimilation using a hierarchical ensemble filter. Physica D: Nonlinear Phenomena , 230(1–2):99–111, 2007. DOI: 10.1016/j.physd.2006.02.011 .
- [15] Anderson, J. L. and Anderson, S. L. A Monte Carlo implementation of the nonlinear filtering problem to produce ensemble assimilations and forecasts. Monthly Weather Review , 127(12):2741–2758, 1999. DOI: 10.1175/1520-0493(1999)127&lt;2741:AMCIOT&gt;2.0.CO;2 .
- [16] Anterion, F., Karcher, B., and Eymard, R. Use of parameter gradients for reservoir history matching. In Proceedings of the 10th SPE Reservoir Simulation Symposium, Houston, Texas, 6–8 February , number SPE-18433-MS, 1989. DOI: 10.2118/18433-MS .
- [17] Armstrong, M., Galli, A., Beucher, H., Loc’h, G. L., Renard, D., Doligez, B., Eschard, R., and Geffroy, F. Plurigaussian simulations in geosciences . Springer-Verlag Berlin Heidelberg, 2nd edition, 2011. DOI: 10.1007/978-3-642-19607-2 .
- [18] Armstrong, M., Vincent, A., Galli, A. G., and Méheut, C. Genetic algorithms and scenario reduction. Journal of The Southern African Institute of Mining and Metallurgy , 114(3):237–244, 2014.
- [19] Arroyo-Negrete, E., Devegowda, D., Datta-Gupta, A., and Choe, J. Streamline-assisted ensemble Kalman filter for rapid and continuous reservoir model updating. SPE Reservoir Evaluation &amp; Engineering , 11(6):1046–1060, 2008. DOI: 10.2118/104255-PA .
- [20] Avansi, G. D. and Schiozer, D. J. UNISIM-I: synthetic model for reservoir development and management applications. International Journal of Modeling and Simulation for the Petroleum Industry ,


- 9(1):21–30, 2015. URL http://www.ijmspi.org/ojs/index.php/ ijmspi/article/view/152 .
- [21] Aziz, K. and Settari, A. Petroleum reservoir simulation . Elsevier Applied Science Publishers, London, 1979.
- [22] Babin, V., Iaubatyrov, R., Ushmaev, O., Garcia, D. K., Golitsyna, M., Semenikhin, A., and Ciaurri, D. E. A variant of particle swarm optimization for uncertainty quantification. In Proceedings of the SPE Reservoir Characterisation and Simulation Conference and Exhibition, Abu Dhabi, UAE, 8–10 May , number SPE-186024-MS, 2017. DOI: 10.2118/186024-MS .
- [23] Bahrami, P., Moghaddam, F. S., and James, L. A. A review of proxy modeling highlighting applications for reservoir engineering. Energies , 15(14), 2022. DOI: 10.3390/en15145247 .
- [24] Bai, X., Wang, Y., and Zhang, W. Applying physics informed neural network for flow data assimilation. Journal of Hydrodynamics , 32, 2020. DOI: 10.1007/s42241-020-0077-2 .
- [25] Bai, Z. D. and Yin, Y. Q. Convergence to the semicircle law. The Annals of Probability , 16(2), 1988. URL http://www.jstor.org/ stable/2243844 .
- [26] Bao, J., Li, L., and Redoloza, F. Coupling ensemble smoother and deep learning with generative adversarial networks to deal with nonGaussianity in flow and transport data assimilation. Journal of Hydrology , 590, 2020. DOI: 10.1016/j.jhydrol.2020.125443 .
- [27] Bao, J., Lee, J., and Yoon, H. Enhanced geothermal site characterization using generative adversarial network and ensemble method. In ARMA-2024-0579, editor, Proceedings of the 58th U.S. Rock Mechanics/Geomechanics Symposium, Golden, Colorado, USA , 2024. DOI: 10.56952/ARMA-2024-0579 .
- [28] Bardsley, J. M., Solonen, A., Haario, H., and Laine, M. Randomizethen-optimize: a method for sampling from posterior distributions in nonlinear inverse problems. SIAM Journal on Scientific Computing , 36(4):A1895–A1910, 2014. DOI: 10.1137/140964023 .
- [29] Barker, J. W. and Dupouy, P. An analysis of dynamic pseudo-relative permeability methods for oil-water flows. Petroleum Geoscience , 5: 385–394, 1999. DOI: 10.1144/petgeo.5.4.38 .
- [30] Bastian, P., Kraus, J., Scheich, R., and Wheeler, M., editors. Simulation of Flow in Porous Media: Applications in Energy and Environment . Series on Computational and Applied Mathematics Book 12. De Gruyter, 2013. ISBN 978-3110282245.
- [31] Batzle, M. and Wang, Z. Seismic properties of pore fluids. Geophysics , 57(11):1396–1408, 1992. DOI: 10.1190/1.1443207 .
- [32] Békési, E., Struijk, M., Bonté, D., Veldkamp, H., Limberger, J., Fokker, P. A., Vrijlandt, M., and van Wees, J.-D. An updated geothermal model of the dutch subsurface based on inversion of temperature data. Geothermics , 88, 2020. DOI: 10.1016/j.geothermics.2020.101880 .


- [33] Bellman, R. E. Dynamic Programming . Princeton University Press, 1957.
- [34] Bertino, L., Evensen, G., and Wackernagel, H. Sequential data assimilation techniques in oceanography. International Statistical Review , 71(2), 2003. DOI: 10.1111/j.1751-5823.2003.tb00194.x .
- [35] Beucher, H. and Renard, D. Truncated Gaussian and derived methods. Mathematical Geology , 348(7), 2016. DOI: 10.1016/j.crte.2015.10.004 .
- [36] Bianco, A., Cominelli, A., Dovera, L., Nævdal, G., and Vallès, B. History matching and production forecast uncertainty by means of the ensemble Kalman filter: A real field application. In Proceedings of the EAGE/EUROPEC Conference and Exhibition, London, U.K., 11–14 June , number SPE-107161-MS, 2007. DOI: 10.2118/107161-MS .
- [37] Bishop, C. H. and Hodyss, D. Flow-adaptive moderation of spurious ensemble correlations and its use in ensemble-based data assimilation. Quarterly Journal of the Royal Meteorological Society , 133(629): 2029–2044, 2007. DOI: 10.1002/qj.169 .
- [38] Bishop, C. H. and Hodyss, D. Ensemble covariances adaptively localized with ECO-RAP. part 1: tests on simple error models. Tellus , 61: 84–96, 2009. DOI: 10.1111/j.1600-0870.2008.00371.x .
- [39] Bishop, C. H., Etherton, B. J., and Majumdar, S. J. Adaptive sampling with the ensemble transform Kalman filter. Part I: Theoretical aspects. Monthly Weather Review , 129:420–436, 2001. DOI: 10.1175/15200493(2001)129&lt;0420:ASWTET&gt;2.0.CO;2 .
- [40] Bissell, R. Calculating optimal parameters for history matching. In Proceedings of the 4th European Conference on the Mathematics of Oil Recovery (ECMOR IV), 07 June , 1994. DOI: 10.3997/22144609.201411181 .
- [41] Bjarkason, E. K., Maclaren, O. J., Nicholson, R., Yeh, A., and O’Sullivan, M. J. Uncertainty quantification of highly-parameterized geothermal reservoir models usingensemble-based methods. In Proceedings World Geothermal Congress 2020+1 , 2021. URL https: //hdl.handle.net/2292/65029 .
- [42] Bocquet, M. and Sakov, P. Combining inflation-free and iterative ensemble Kalman filters for strongly nonlinear systems. Nonlinear Processes in Geophysics , 19(3), 2012. DOI: 10.5194/npg-19-383-2012 .
- [43] Boisvert, J. B. Geostatistics with locally varying anisotropy . PhD thesis, University of Alberta, 2010.
- [44] Bortz, D. M. and Kelley, C. T. The simplex gradient and noisy optimization problems. In Borggaard, T., J. Burns, E. C., and Schreck, S., editors, Computational Methods for Optimal Design and Control . Birkhäuser Boston, 1998. ISBN 978-1461217800. DOI: 10.1007/9781-4612-1780-0_5 .
- [45] Boser, B. E., Guyon, I. M., and Vapnik, V. N. A training algorithm for optimal margin classifiers. In COLT ’92 Proceedings of the fifth annual workshop on Computational learning theory Pittsburgh, Pennsylvania, USA, July 27–29 , pages 144–152, 1992. DOI: 10.1145/130385.130401 .


- [46] Breslavich, I. D., Sarkisov, G. G., and Makarova, E. S. Experience of MDA ensemble smoother practice for Volga-Ural oilfield. In Proceedings of the SPE Russian Petroleum Technology Conference held in Moscow, Russia, 16–18 October , number SPE-187800-MS, 2017. DOI: 10.2118/187800-MS .
- [47] Bruhn, C. H. L., Gomes, J. A. T., Luchesse, C. D., and Johann, P. R. S. Campos Basin: Reservoir charactertization and management – historical overview and future challenges. In Proceedings of the Offshore Technology Conference, Houston, Texas , number OTC 15220, 2003. DOI: 10.4043/15220-MS .
- [48] Bruyelle, J. and Guérillot, D. Neural networks and their derivatives for history matching and reservoir optimization problems. Computational Geosciences , 18(3–4):549–561, 2014. DOI: 10.1007/s10596-013-9390-y .
- [49] Brynjarsdóttir, J. and O’Hagan, A. Learning about physical parameters: the importance of model discrepancy. Inverse Problems , 30, 2014. DOI: 10.1088/0266-5611/30/11/114007 .
- [50] Buckley, S. E. and Leverett, M. C. Mechanism of fluid displacement in sands. Transactions of the AIME , 146(1):107–116, 1942. DOI: 10.2118/942107-G .
- [51] Burgers, G., van Leeuwen, P., and Evensen, G. Analysis scheme in the ensemble Kalman filter. Monthly Weather Review , 126(6):1719–1724, 1998. DOI: 10.1175/1520-0493(1998)126&lt;1719:ASITEK&gt;2.0.CO;2 .
- [52] Burgess, P. M. Regional Geology and Tectonics: Principles of Geologic Analysis , chapter A brief review of developments in stratigraphic forward modelling, 2000–2009, pages 378–404. Elsevier, 2012. ISBN 978-0444530424. DOI: https://doi.org/10.1016/B978-0444-53042-4.00014-5 .
- [53] Caers, J. Bayesianism in the Geosciences. In Handbook of Mathematical Geosciences: Fifty Years of IAMG , pages 527–566. Springer International Publishing, 2018. DOI: 10.1007/978-3-319-78999-6_27 .
- [54] Camacho, A., Talavera, A., Emerick, A. A., Pacheco, M. A., and Zannia, J. Uncertainty quantification in reservoir simulation models with polynomial chaos expansions: Smolyak quadrature and regression method approach. Journal of Petroleum Science and Engineering , 153: 203–211, 2017. DOI: 10.1016/j.petrol.2017.03.046 .
- [55] Canchumuni, S. W. A., Emerick, A. A., and Pacheco, M. A. C. History matching geological facies models based on ensemble smoother and deep generative models. Journal of Petroleum Science and Engineering , 177:941–958, 2019. DOI: 10.1016/j.petrol.2019.02.037 .
- [56] Canchumuni, S. W. A., Emerick, A. A., and Pacheco, M. A. C. Towards a robust parameterization for conditioning facies models using deep variational autoencoders and ensemble smoother. Computers &amp; Geosciences , 128:87–102, 2019. DOI: 10.1016/j.cageo.2019.04.006 .
- [57] Canchumuni, S. W. A., Castro, J. D. B., Potratz, J., Emerick, A. A., and Pacheco, M. A. C. Recent developments combining ensemble smoother and deep generative networks for facies history matching.


- Computational Geosciences , 25(433–466), 2021. DOI: 10.1007/s10596020-10015-0 .
- [58] Cao, Y., Zhou, H., Yu, B., Wei, S., Chen, H., and Tian, Y. The estimation of petrophysical parameters based on ensemble smoother with correlation localization. IEEE Transactions on Geoscience and Remote Sensing , 62, 2024. DOI: 10.1109/TGRS.2024.3403663 .
- [59] Cao, Z., Li, L., and Chen, K. Bridging iterative ensemble smoother and multiple-point geostatistics for better flow and transport modeling. Journal of Hydrology , 565, 2018. DOI: 10.1016/j.jhydrol.2018.08.023 .
- [60] Carrassi, A., Bocquet, M., Bertino, L., and Evensen, G. Data assimilation in the geosciences: An overview of methods, issues, and perspectives. WIREs Climate Change , 9(8), 2018. DOI: 10.1002/wcc.535 .
- [61] Celia, M. A., Bachu, S., Nordbotten, J. M., and Bandilla, K. W. Status of CO 2 storage in deep saline aquifers with emphasis on modeling approaches and practical simulations. Water Resources Research , 51 (9), 2015. DOI: 10.1002/2015WR017609 .
- [62] Chan, S. and Elsheikh, A. H. Parametrization and generation of geological models with generative adversarial networks. arXiv:1708.01810v1 [stat.ML] , 2017. URL https://arxiv.org/abs/ 1708.01810 .
- [63] Chan, S. and Elsheikh, A. H. Parametric generation of conditional geological realizations using generative neural networks. Computational Geosciences , 23:925–952, 2019. DOI: 10.1007/s10596-019-09850-7 .
- [64] Chang, H., Zhang, D., and Lu, Z. History matching of facies distributions with the EnKF and level set parameterization. Journal of Computational Physics , 229:8011–8030, 2010. DOI: 10.1016/j.jcp.2010.07.005 .
- [65] Chang, Y., Stordal, A. S., and Valestran, R. Facies parameterization and estimation for complex reservoirs – the Brugge field. In Proceedings of the SPE Bergen One Day Seminar, Bergen, Norway, 22 April , number SPE-173872-MS, 2015. DOI: 10.2118/173872-MS .
- [66] Chassagne, R., Obidegwu, D., Dambrine, J., and MacBeth, C. Binary 4D seismic history matching, a metric study. Computers &amp; Geosciences , 96, 2016. DOI: 10.1016/j.cageo.2016.08.013 .
- [67] Chen, B., Harp, D. R., Lu, Z., and Pawar, R. J. Reducing uncertainty in geologic CO 2 sequestration risk assessment by assimilating monitoring data. International Journal of Greenhouse Gas Control , 94, 2020. DOI: 10.1016/j.ijggc.2019.102926 .
- [68] Chen, B., Morales, M. M., Ma, Z., Kang, Q., and Pawar, R. J. Assimilation of geophysics-derived spatial data for model calibration in geologic CO 2 sequestration. SPE Journal , 29(7), 2024. DOI: 10.2118/212975-PA .
- [69] Chen, C., Gao, G., Honorio, J., Gelderblom, P., Jimenez, E., and Jaakkola, T. Integration of principal-component-analysis and streamline information for the history matching of channelized reservoirs. In Proceedings of the SPE Annual Technical Conference and Exhibition,


- Amsterdam, The Netherlands, 27–29 October , number SPE-170636MS, 2014. DOI: 10.2118/170636-MS .
- [70] Chen, C., Gao, G., Ramirez, B. A., Vink, J. C., and Girardi, A. M. Assisted history matching of channelized models using pluri-principal component analysis. In Proceedings of the SPE Reservoir Simulation Symposium, Houston, Texas, USA, 23–25 February , number SPE173192-MS, 2015. DOI: 10.2118/173192-MS .
- [71] Chen, C., Gao, G., Gelderblom, P., and Jimenez, E. Integration of cumulative-distribution-function mapping with principalcomponent analysis for the history matching of channelized reservoirs. SPE Reservoir Evaluation &amp; Engineering , 19(2):278–293, 2016. DOI: 10.2118/170636-PA .
- [72] Chen, C., Deng, Y., Ma, H., Kang, X., Ma, L., and Qian, J. Deep learning-based inversion framework by assimilating hydrogeological and geophysical data for an enhanced geothermal system characterization and thermal performance prediction. Energy , 302, 2024. DOI: 10.1016/j.energy.2024.131713 .
- [73] Chen, W. H., Gavalas, G. R., Seinfeld, J. H., and Wasserman, M. L. A new algorithm for automatic history matching. SPE Journal , 14(6): 593–608, 1974. DOI: 10.2118/4545-PA .
- [74] Chen, X., Hammond, G. E., Murray, C. J., Rockhold, M. L., Vermeul, V. R., and Zachara, J. M. Application of ensemble-based data assimilation techniques for aquifer characterization using tracer data at hanford 300 area. Water Resources Research , 49(10), 2013. DOI: 10.1002/2012WR013285 .
- [75] Chen, Y. Keynote geologically consistent history matching using the ensemble based methods. In Proceedings of the Petroleum Geostatistics, Biarritz, France, 7–11 September , 2015. DOI: 10.3997/22144609.201413627 .
- [76] Chen, Y. and Oliver, D. S. Ensemble-based closed-loop optimization applied to Brugge field. SPE Reservoir Evaluation &amp; Engineering , 13 (1):56–71, 2010. DOI: 10.2118/118926-PA .
- [77] Chen, Y. and Oliver, D. S. Cross-covariance and localization for EnKF in multiphase flow data assimilation. Computational Geosciences , 14 (4):579–601, 2010. DOI: 10.1007/s10596-009-9174-6 .
- [78] Chen, Y. and Oliver, D. S. Ensemble randomized maximum likelihood method as an iterative ensemble smoother. Mathematical Geosciences , 44(1):1–26, 2012. DOI: 10.1007/s11004-011-9376-z .
- [79] Chen, Y. and Oliver, D. S. Levenberg-Marquardt forms of the iterative ensemble smoother for efficient history matching and uncertainty quantification. Computational Geosciences , 17:689–703, 2013. DOI: 10.1007/s10596-013-9351-5 .
- [80] Chen, Y. and Oliver, D. S. History matching of the Norne full-field model with an iterative ensemble smoother. SPE Reservoir Evaluation &amp; Engineering , 17(2), 2014. DOI: 10.2118/164902-PA .


- [81] Chen, Y. and Oliver, D. S. Localization and regularization for iterative ensemble smoothers. Computational Geosciences , 21(1):13–30, 2017. DOI: 10.1007/s10596-016-9599-7 .
- [82] Chen, Y. and Zhang, D. Data assimilation for transient flow in geologic formations via ensemble Kalman filter. Advances in Water Resources , 29(8):1107–1122, 2006. DOI: 10.1016/j.advwatres.2005.09.007 .
- [83] Chen, Y., Oliver, D. S., and Zhang, D. Efficient ensemble-based closedloop production optimization. SPE Journal , 14(4):634–645, 2009. DOI: 10.2118/112873-PA .
- [84] Chen, Z., Huan, G., and Ma, Y. Computational Methods for Multiphase Flows in Porous Media . SIAM, 2006. ISBN 978-0898718942. DOI: 10.1137/1.9780898718942.fm .
- [85] Chen, Z., Xu, T., Gómez-Hernández, J. J., Zanini, A., and Zhou, Q. Reconstructing the release history of a contaminant source with different precision via the ensemble smoother with multiple data assimilation. Journal of Contaminant Hydrology , 252, 2023. DOI: 10.1016/j.jconhyd.2022.104115 .
- [86] Chen, Z., Zong, L., Gómez-Hernández, J. J., Xu, T., Jiang, Y., Zhou, Q., Yang, H., Jia, Z., and Mei, S. Contaminant source and aquifer characterization: An application of ES-MDA demonstrating the assimilation of geophysical data. Advances in Water Resources , 181, 2023. DOI: 10.1016/j.advwatres.2023.104555 .
- [87] Chrysikopoulos, C. Artificial tracers for geothermal reservoir studies. Environmental Geology , 22, 1993. DOI: 10.1007/BF00775286 .
- [88] Cipra, B. A. The best of the 20th Century: editors name top 10 algorithms. SIAM News , 33(4), 2000.
- [89] Cojan, I., Olivier Fouché, S. L., and Rivoirard, J. Geostatistics Banff 2004 , chapter Process-based Reservoir Modelling in the Example of Meandering Channel, pages 611–619. Springer, Dordrecht, 2004. ISBN 978-1402036101. DOI: 10.1007/978-1-4020-3610-1_62 .
- [90] Coley, D. A. An introduction to genetic algorithms for scientists and engineers . World Scientific, 1999. ISBN 978-9810236021. DOI: 10.1142/3904 .
- [91] Collet, A. pyESMDA – Python ensemble smoother with multiple data assimilation. Software. URL https://pypi.org/project/pyesmda/ .
- [92] Conn, A. R., Scheinberg, K., and Vicente, L. N. Introduction to derivative free optimization . SIAM, Philadelphia, PA, 2009. DOI: 10.1137/1.9780898718768 .
- [93] Costa, L. A. N., Maschio, C., and Schiozer, D. J. Application of artificial neural networks in a history matching process. Journal of Petroleum Science and Engineering , 123, 2014. DOI: 10.1016/j.petrol.2014.06.004 .
- [94] Coutinho, E. J., Emerick, A. A., Li, G., and Reynolds, A. C. Conditioning multi-layered gelogic models to well test and production logging data using the ensemble Kalman filter. In Proceedings of the SPE


- Annual Technical Conference and Exhibition, Florence, Italy, 19–22 September , number SPE-134542-MS, 2010. DOI: 10.2118/134542-MS .
- [95] Coutinho, E. J. R., Dall’Aqua, and Gildin, E. Physics-aware deeplearning-based proxy reservoir simulation model equipped with state and well output prediction. Frontiers in Applied Mathematics and Statistics , 7, 2021. DOI: 10.3389/fams.2021.651178 .
- [96] Craig, P. S., Goldstein, M., Seheult, A. H., and Smith, J. A. Pressure matching for hydrocarbon reservoirs: A case study in the use of bayes linear strategies for large computer experiments. In Case Studies in Bayesian Statistics. Lecture Notes in Statistics , volume 121. Springer, 1997. DOI: 10.1007/978-1-4612-2290-3_2 .
- [97] Cruz, N. M., Cruz, J. M., Teixeira, L. M., da Costa, M. M., de Oliveira, L. B., Urasaki, E. N., Bispo, T. P., de Sá Jardim, M., Grochau, M. H., and Maul, A. Tupi nodes pilot: A successful 4D seismic case for Brazilian presalt reservoirs. The Leading Edge , 40(12):886–896, 2021. DOI: 10.1190/tle40120886.1 .
- [98] Custódio, A. L. and Vicente, L. N. Using sampling and simplex derivatives in pattern search methods. SIAM Journal on Optimization , 18: 537–555, 2007. DOI: 10.1137/050646706 .
- [99] Dasgupta, A., Hostache, R., Ramsankaran, R., Grimaldi, S., Matgen, P., Chini, M., Pauwels, V. R., and Walker, J. P. Earth observation and hydraulic data assimilation for improved flood inundation forecasting. In Schumann, G. J.-P., editor, Earth Observation for Flood Applications . Elsevier, 2021. DOI: 10.1016/B978-0-12-819412-6.00012-2 .
- [100] Davolio, A. and Schiozer, D. J. Probabilistic seismic history matching using binary images. Journal of Geophysics and Engineering , 15(1), 2018. DOI: 10.1088/1742-2140/aa99f4 .
- [101] de Marsily, G., Lavedan, G., Boucher, M., and Fasanino, G. Interpretation of interference tests in a well field using geostatistical techniques to fit the permeability distribution in a reservoir model. In Verly, G., David, M., Journel, A. G., and Marechal, A., editors, Geostatistics for Natural Resources Characterization, Proceedings of the NATO Advanced Study Institute , pages 831–849. Dordrecht, Holland, Dordrecht, Holland, 1984. DOI: 10.1007/978-94-009-3701-7_16 .
- [102] de Moraes, R. J., Rodrigues, J. R. P., Hajibeygi, H., and Jansen, J.-D. Multiscale gradient computation for flow in heterogeneous porous media. Journal of Computational Physics , 336, 2017. DOI: 10.1016/j.jcp.2017.02.024 .
- [103] de Moraes, R. J., de Zeeuw, W., Rodrigues, J. R. P., Hajibeygi, H., and Jansen, J.-D. Iterative multiscale gradient computation for heterogeneous subsurface flow. Advances in Water Resources , 129, 2019. DOI: 10.1016/j.advwatres.2019.05.016 .
- [104] Deutsch, C. V. Geostatistical reservoir modeling . Oxford University Press, 2002.


- [105] Deutsch, C. V. and Journel, A. G. GSLIB: Geostatistical software library and user’s guide . Oxford University Press, New York, 1992. ISBN 978-0195073928.
- [106] Deutsch, C. V. and Journel, A. G. GSLIB: Geostatistical software library and user’s guide . Oxford University Press, New York, 2nd edition, 1997. ISBN 978-0195100150.
- [107] Deutsch, C. V. and Wang, L. Hierarchical object-based stochastic modeling of fluvial reservoirs. Mathematical Geology , 28(7):857–880, 1996. DOI: 10.1007/BF02066005 .
- [108] Devegowda, D., Arroyo-Negrete, E., Datta-Gupta, A., and Douma, S. G. Efficient and robust reservoir model updating using ensemble Kalman filter with sensitivity-based covariance localization. In Proceedings of the SPE Reservoir Simulation Symposium, Houston, Texas, USA 26–28 February , number SPE-106144-MS, 2007. DOI: 10.2118/106144-MS .
- [109] Ding, Z. and Li, Q. Ensemble Kalman inversion: mean – field limit and convergence analysis. Statistics and Computing , 31(9), 2021. DOI: 10.1007/s11222-020-09976-0 .
- [110] Do, S. T. and Reynolds, A. C. Theoretical connections between optimization algorithms based on an approximate gradient. Computational Geosciences , 17(6):959–973, 2013. DOI: 10.1007/s10596-013-9368-9 .
- [111] Dong, Y. and Oliver, D. S. Quantitative use of 4D seismic data for reservoir description. SPE Journal , 10(1):51–65, 2005.
- [112] Donoho, D. L. and Johnstone, I. M. Ideal spatial adaptation by wavelet shrinkage. Biometrika , 81(3):425–455, 1994. DOI: 10.1093/biomet/81.3.425 .
- [113] Donoho, D. L. and Johnstone, I. M. Adapting to unknown smoothness via wavelet shrinkage. Journal of the American Statistical Association , 90:1200–1224, 1995. DOI: 10.1080/01621459.1995.10476626 .
- [114] Doucet, A., de Freitas, N., and Gordon, N., editors. Sequential Monte Carlo methods in practice . Springer-Verlag, 2000. ISBN 9781475734379. DOI: 10.1007/978-1-4757-3437-9 .
- [115] Dupont, E., Zhang, T., Tilke, P., Liang, L., and Bailey, W. Generating realistic geology conditioned on physical measurements with generative adversarial networks. arXiv:1802.03065v3 [stat.ML] , 2018. URL https://arxiv.org/abs/1802.03065 .
- [116] Durlofsky, L. J. Use of higher moments for the description of upscaled, process independent relative permeabilities. SPE Journal , 2 (4):474–484, 1997. DOI: 10.2118/37987-PA .
- [117] Elsheikh, A. H., Hoteit, I., and Wheeler, M. F. Efficient bayesian inference of subsurface flow models using nested sampling and sparse polynomial chaos surrogates. Computer Methods in Applied Mechanics and Engineering , 269, 2014. DOI: 10.1016/j.cma.2013.11.001 .
- [118] Emerick, A. A. Analysis of the performance of ensemblebased assimilation of production and seismic data. Jour-


- nal of Petroleum Science and Engineering , 139:219–239, 2016. DOI: 10.1016/j.petrol.2016.01.029 .
- [119] Emerick, A. A. Estimating uncertainty bounds in field production using ensemble-based methods. Journal of Petroleum Science and Engineering , 145:648–656, 2016. DOI: 10.1016/j.petrol.2016.06.037 .
- [120] Emerick, A. A. Investigation on principal component analysis parameterizations for history matching channelized facies models with ensemble-based data assimilation. Mathematical Geosciences , 49(1): 85–120, 2017. DOI: 10.1007/s11004-016-9659-5 .
- [121] Emerick, A. A. Deterministic ensemble smoother with multiple data assimilation as an alternative for history matching seismic data. Computational Geosciences , 22(5):1175–1186, 2018. DOI: 10.1007/s10596018-9745-5 .
- [122] Emerick, A. A. Analysis of geometric selection of the data-error covariance inflation for ES-MDA. Journal of Petroleum Science and Engineering , 182, 2019. DOI: 10.1016/j.petrol.2019.06.032 .
- [123] Emerick, A. A. Practical considerations in the application of ensemble smoother for assimilating production and 4D seismic data. In Proceedings of th European Conference for Mathematics of Geological Reservoirs ECMOR, September 2-5, Olso, Norway , 2024. DOI: 10.3997/2214-4609.202437027 .
- [124] Emerick, A. A. and Neto, G. M. S. Investigation on the production data frequency for assimilation with ensemble smoother. Geoenergy Science and Engineering , 231, 2023. DOI: 10.1016/j.geoen.2023.212356 .
- [125] Emerick, A. A. and Neto, G. M. S. Projection of 4D seismic onto the ensemble observation subspace for data assimilation. Geoenergy Science and Engineering , 237, 2024. DOI: 10.1016/j.geoen.2024.212835 .
- [126] Emerick, A. A. and Reynolds, A. C. Combining the ensemble Kalman filter with Markov chain Monte Carlo for improved history matching and uncertainty characterization. In Proceedings of the SPE Reservoir Simulation Symposium, The Woodlands, Texas, USA, 21–23 February , number SPE-141336-MS, 2011. DOI: 10.2118/141336-MS .
- [127] Emerick, A. A. and Reynolds, A. C. History matching a field case using the ensemble Kalman filter with covariance localization. SPE Reservoir Evaluation &amp; Engineering , 14(4):423–432, 2011. DOI: 10.2118/141216-PA .
- [128] Emerick, A. A. and Reynolds, A. C. Combining sensitivities and prior information for covariance localization in the ensemble Kalman filter for petroleum reservoir applications. Computational Geosciences , 15 (2):251–269, 2011. DOI: 10.1007/s10596-010-9198-y .
- [129] Emerick, A. A. and Reynolds, A. C. History matching timelapse seismic data using the ensemble Kalman filter with multiple data assimilations. Computational Geosciences , 16(3):639–659, 2012. DOI: 10.1007/s10596-012-9275-5 .


- [130] Emerick, A. A. and Reynolds, A. C. Combining the ensemble Kalman filter with Markov chain Monte Carlo for improved history matching and uncertainty characterization. SPE Journal , 17(2):418–440, 2012. DOI: 10.2118/141336-PA .
- [131] Emerick, A. A. and Reynolds, A. C. Investigation of the sampling performance of ensemble-based methods with a simple reservoir model. Computational Geosciences , 17(2):325–350, 2013. DOI: 10.1007/s10596-012-9333-z .
- [132] Emerick, A. A. and Reynolds, A. C. Ensemble smoother with multiple data assimilation. Computers &amp; Geosciences , 55:3–15, 2013. DOI: 10.1016/j.cageo.2012.03.011 .
- [133] Emerick, A. A. and Reynolds, A. C. History matching of production and seismic data for a real field case using the ensemble smoother with multiple data assimilation. In Proceedings of the SPE Reservoir Simulation Symposium, The Woodlands, Texas, USA, 18–20 February , number SPE-163675-MS, 2013. DOI: 10.2118/163675-MS .
- [134] Emerick, A. A., Moraes, R. J., and Rodrigues, J. R. P. History matching 4D seismic data with efficient gradient based methods. In Proceedings of the EUROPEC/EAGE Conference and Exhibition, 11-14 June, London, U.K. , number SPE-107179-MS, 2007. DOI: 10.2118/107179MS .
- [135] Evans, M. and Swartz, T. Methods for approximating integrals in statistics with special emphasis on Bayesian integration problems. Statistical Science , 10(3), 1995. DOI: 10.1214/ss/1177009938 .
- [136] Evensen, G. Sequential data assimilation with a nonlinear quasigeostrophic model using Monte Carlo methods to forecast error statistics. Journal of Geophysical Research , 99(C5):10143–10162, 1994. DOI: 10.1029/94JC00572 .
- [137] Evensen, G. The ensemble Kalman filter: theoretical formulation and practical implementation. Ocean Dynamics , 53:343–367, 2003. DOI: 10.1007/s10236-003-0036-9 .
- [138] Evensen, G. Sampling strategies and square root analysis schemes for the EnKF. Ocean Dynamics , 54(6):539–560, 2004. DOI: 10.1007/s10236-004-0099-2 .
- [139] Evensen, G. Data assimilation: the ensemble Kalman filter . Springer, Berlin, 2007. ISBN 978-3540383000. DOI: 10.1007/978-3-642-03711-5 .
- [140] Evensen, G. Analysis of iterative ensemble smoothers for solving inverse problems. Computational Geosciences , 2018. DOI: 10.1007/s10596-018-9731-y .
- [141] Evensen, G. Accounting for model errors in iterative ensemble smoothers. Computational Geosciences , 23, 2019. DOI: 10.1007/s10596-019-9819-z .
- [142] Evensen, G. On the formulation of the ensemble history-matching problem. In Proceedings of the SPE Reservoir Simulation Conference, Galveston, Texas, USA, March 2023 , number SPE-212232-MS, 2023. DOI: 10.2118/212232-MS .


- [143] Evensen, G. and Eikrem, K. S. Conditioning reservoir models on rate data using ensemble smoothers. Computational Geosciences , 22(1): 1–20, 2018. DOI: 10.1007/s10596-018-9750-8 .
- [144] Evensen, G., Hove, J., Meisingset, H. C., Reiso, E., Seim, K. S., and Espelid, Ø. Using the EnKF for assisted history matching of a North Sea reservoir model. In Proceedings of the SPE Reservoir Simulation Symposium, Houston, Texas, 26–28 February , number SPE-106184MS, 2007. DOI: 10.2118/106184-MS .
- [145] Evensen, G., Raanes, P. N., Stordal, A. S., and Hove, J. Efficient implementation of an iterative ensemble smoother for data assimilation and reservoir history matching. Frontiers in Applied Mathematics and Statistics , 3, 2019. DOI: 10.3389/fams.2019.00047 .
- [146] Exterkoetter, R., Dutra, G. R., de Figueiredo, L. P., Bordignon, F., Neto, G. M. S., and Emerick, A. A. Feature extraction in time-lapse seismic using deep learning for data assimilation. SPE Journal , 1, 2023. DOI: 10.2118/212196-PA .
- [147] Exterkoetter, R., de Figueiredo, L. P., Bordignon, F. L., Emerick, A. A., Roisenberg, M., and Rodrigues, B. B. Ensemble smoother with fully convolutional VAE for seismic facies inversion. Computers &amp; Geosciences , 189, 2024. DOI: 10.1016/j.cageo.2024.105619 .
- [148] Federico, G. D. and Durlofsky, L. J. Latent diffusion models for parameterization and data assimilation of facies-based geomodels. arXiv:2406.14815v3 [cs.CV] , 2024. DOI: 10.48550/arXiv.2406.14815 .
- [149] Fletcher, R. and Reeves, C. M. Function minimization by conjugate gradient. Computer Journal , 7:149–154, 1964. DOI: 10.1093/comjnl/7.2.149 .
- [150] Floris, F. J. T., Bush, M. D., Cuypers, M., Roggero, F., and Syversveen, A. R. Methods for quantifying the uncertainty of production forecasts: a comparative study. Petroleum Geoscience , 7(SUPP): 87–96, 2001. DOI: 10.1144/petgeo.7.S.S87 .
- [151] Fonseca, R. M., Chen, B., Jansen, J. D., and Reynolds, A. C. A stochastic simplex approximate gradient (StoSAG) for optimization under uncertainty. International Journal For Numerical Methods in Engineering , 109(13):1756–1776, 2017. DOI: 10.1002/nme.5342 .
- [152] Fonseca, R. M., Rossa, E. D., Emerick, A. A., Hanea, R. G., and Jansen, J. D. Introduction to the special issue: Overview of OLYMPUS optimization benchmark challenge. Computational Geosciences , 24: 1933–1941, 2020. DOI: 10.1007/s10596-020-10003-4 .
- [153] Franssen, H. J. H., Kaiser, H. P., Kuhlmann, U., Bauser, G., Stauffer, F., Müller, R., and Kinzelbach, W. Operational real-time modeling with ensemble kalman filter of variably saturated subsurface flow including stream-aquifer interaction and parameter updating. Water Resources Research , 47(2), 2011. DOI: 10.1029/2010WR009480 .
- [154] Freshley, M. D. 300 area integrated field-scale subsurface research challenge (IFRC) field site management plan. Technical report, Pacific


- Northwest National Laboratory, 2008. URL https://www.pnnl.gov/ publications .
- [155] Furre, A.-K., Ola Eiken, H. A., Vevatne, J. N., and Kiær, A. F. 20 years of monitoring CO 2 -injection at Sleipner. Energy Procedia , 114: 3916–3926, 2017. DOI: 10.1016/j.egypro.2017.03.1523 .
- [156] Furrer, R. and Bengtsson, T. Estimation of high-dimensional prior and posterior covariance matrices in Kalman filter variants. Journal of Multivariate Analysis , 98(2):227–255, 2007. DOI: 10.1016/j.jmva.2006.08.003 .
- [157] Galli, A., Beucher, H., Le Loc’h, G., Doligez, B., and Group, H. The pros and cons of the truncated Gaussian method , pages 217–233. Springer Netherlands, Dordrecht, 1994. DOI: 10.1007/978-94-0158267-4_18 .
- [158] Gao, G. and Reynolds, A. C. An improved implementation of the LBFGS algorithm for automatic history matching. SPE Journal , 11 (1):5–17, 2006. DOI: 10.2118/90058-PA .
- [159] Gao, G., Li, G., and Reynolds, A. C. A stochastic algorithm for automatic history matching. SPE Journal , 12(2):196–208, 2007. DOI: 10.2118/90065-PA .
- [160] Gao, G., Vink, J. C., Chen, C., Alpak, F. O., and Du, K. Enhanced reparameterization and data-integration algorithms for robust and efficient history matching of geologically complex reservoirs. In Proceedings of the SPE Annual Technical Conference and Exhibition, Houston, Texas, USA, 28–30 September , number SPE-175039-MS, 2015. DOI: 10.2118/175039-MS .
- [161] Garud, S. S., Karimi, I. A., and Kraft, M. Design of computer experiments: A review. Computers and Chemical Engineering , 106, 2017. DOI: 10.1016/j.compchemeng.2017.05.010 .
- [162] Gaspari, G. and Cohn, S. E. Construction of correlation functions in two and three dimensions. Quarterly Journal of the Royal Meteorological Society , 125(554):723–757, 1999. DOI: 10.1002/qj.49712555417 .
- [163] Gassmann, F. Elastic waves through a packing of spheres. Geophysics , 16:673–685, 1951. DOI: 10.1190/1.1437718 .
- [164] Gavalas, G. R., Shah, P. C., and Seinfeld, J. H. Reservoir history matching by Bayesian estimation. SPE Journal , 16(6):337–350, 1976. DOI: 10.2118/5740-PA .
- [165] Gavish, M. and Donoho, D. L. The optimal hard threshold for singular values is 4 / √ 3. IEEE Transactions on Information Theory , 60(8): 5040–5053, 2014. DOI: 10.1109/TIT.2014.2323359 .
- [166] Geyer, C. J. Handbook of Markov Chain Monte Carlo , chapter Introduction to Markov chain Monte Carlo. Chapman &amp; Hall/CRC, 2011.
- [167] Gharamti, M. E., Hoteit, I., and Valstar, J. Dual states estimation of a subsurface flow-transport coupled model using ensemble Kalman filtering. Advances in Water Resources , 60, 2013. DOI: 10.1016/j.advwatres.2013.07.011 .


- [168] Gineste, M. and Eidsvik. Batch seismic inversion using the iterative ensemble Kalman smoother. Computational Geosciences , 25, 2021. DOI: 10.1007/s10596-021-10043-4 .
- [169] Gineste, M., Eidsvik, J., and Zheng, Y. Ensemble-based seismic inversion for a stratified medium. Geophysics , 85, 2020. DOI: 10.1190/geo2019-0017.1 .
- [170] Golub, G. H. and van Loan, C. F. Matrix computations . The Johns Hopkins University Press, Baltimore, 3rd edition, 1989. ISBN 9780801854149.
- [171] Gómez-Hernández, J. J. and Journel, A. G. Joint sequential simulation of multigaussian fields. In Soares, A., editor, Geostatistics Tróia ’92 , pages 133–144. 1992. DOI: 10.1007/978-94-011-1739-5_8 .
- [172] Gómez-Hernández, J. J. and Xu, T. Contaminant source identification in aquifers: A critical view. Mathematical Geosciences , 54, 2021. DOI: 10.1007/s11004-021-09976-4 .
- [173] González-Nicolás, A., Baú, D., and Alzraiee, A. Detection of potential leakage pathways from geological carbon storage by fluid pressure data assimilation. Advances in Water Resources , 86, 2015. DOI: 10.1016/j.advwatres.2015.10.006 .
- [174] Gosselin, O., Aanonsen, S., Aavatsmark, I., Cominelli, A., Gonard, R., Kolasinski, M., Ferdinandi, F., Kovacic, L., and Neylon, K. History matching using time-lapse seismic (HUTS). In Proceedings of the SPE Annual Technical Conference and Exhibition, Denver, Colorado, 5–8 October , number SPE-84464-MS, 2003. DOI: 10.2118/84464-MS .
- [175] Grana, D., Mukerji, T., and Doyen, P. Seismic Reservoir Modeling: Theory, Examples, and Algorithms . John Wiley &amp; Sons, 2021. ISBN 978-1119086185.
- [176] Grana, D., Azevedo, L., de Figueiredo, L., Connolly, P., and Mukerji, T. Probabilistic inversion of seismic data for reservoir petrophysical characterization: Review and examples. Geophysics , 87(5), 2022. DOI: 10.1190/geo2021-0776.1 .
- [177] Gross, H., Settgast, R. R., Aronson, R. M., Borio, A., Bui, Q. M., Castelletto, N., Corbett, B. C., Cordier, P., Cremon, M. A., Cusini, M., Frambati, S., Franc, J., Gazzola, T., Hamon, F., Huang, J., Kachuma, D., Karimi-Fard, M., Klevtsov, S., Lapene, A., Magri, V. A. P., Mazuyer, A., N’diaye, M., Osei-Kuffuor, D., Sherman, C. S., Tchelepi, H. A., Tobin, W. R., Tomin, P., Wen, X., and White, J. A. GEOS: Exascale, multiphysics, open-source simulation for CCS. In Proceedings of the European Conference for Mathematics of Geological Reservoirs ECMOR, September 2-5, Olso, Norway , 2024. DOI: 10.3997/22144609.202437054 .
- [178] Gu, Y. and Oliver, D. S. An iterative ensemble Kalman filter for multiphase fluid flow data assimilation. SPE Journal , 12(4):438–446, 2007. DOI: 10.2118/108438-PA .
- [179] Guardiano, F. B. and Srivastava, R. M. Multivariate geostatistics: Beyond bivariate moments. In Soares, A., editor, Geostatistics Tróia ’92 ,


- volume 5 of Quantitative Geology and Geostatistics , pages 133–144. Springer Netherlands, 1993.
- [180] Guo, J.-X., Huang, C., Wang, J.-L., and Meng, X.-Y. Integrated operation for the planning of CO 2 capture path in CCS-EOR project. Journal of Petroleum Science and Engineering , 186, 2020. DOI: 10.1016/j.petrol.2019.106720 .
- [181] Guo, Z., Chen, C., Gao, G., Cao, R., Li, R., and Liu, C. EUR assessment of unconventional assets using machine learning and distributed computing techniques. In Proceedings of the SPE/AAPG/SEG Unconventional Resources Technology Conference, Austin, Texas, USA , 24–26 July , number URTEC-2659996-MS, 2017. DOI: 10.15530/URTEC-2017-2659996 .
- [182] Hadamard, J. Sur les problémes aux dérivées partielles et leur signification physique. Princeton University Bulletin , 13:49–52, 1902.
- [183] Hamill, T. M., Whitaker, J. S., and Snyder, C. Distance-dependent filtering of background error covariance estimates in an ensemble Kalman filter. Monthly Weather Review , 129(11):2776–2790, 2001. DOI: 10.1175/1520-0493(2001)129&lt;2776:DDFOBE&gt;2.0.CO;2 .
- [184] Hanke, M. A regularizing Levenberg-Marquardt scheme, with applications to inverse groundwater filtration problems. Inverse Problems , 13(1):79–95, 1997. DOI: 10.1088/0266-5611/13/1/007 .
- [185] Hannis, S., Lu, J., Chadwick, A., Hovorka, S., Kirk, K., Romanak, K., and Pearce, J. CO 2 storage in depleted or depleting oil and gas fields: What can we learn from existing projects? Energy Procedia , 114, 2017. DOI: 10.1016/j.egypro.2017.03.1707 .
- [186] Hansen, N. and Ostermeier, A. Completely derandomized selfadaptation in evolution strategies. Evolutionary Computation , 9(2), 2001. DOI: 10.1162/106365601750190398 .
- [187] Hastings, W. K. Monte Carlo sampling methods using Markov chains and their applications. Biometrika , 57(1):97–109, 1970. DOI: 10.2307/2334940 .
- [188] Haugen, V., Nævdal, G., rgen Natvik, L.-J., Evensen, G., Berg, A. M., and Flornes, K. M. History matching using the ensemble Kalman filter on a North Sea field case. SPE Journal , 13(4):382–391, 2008. DOI: 10.2118/102430-PA .
- [189] He, J., Sarma, P., and Durlofsky, L. J. Reduced-order flow modeling and geological parameterization for ensemble-based data assimilation. Computers &amp; Geosciences , 55:54–69, 2013. DOI: 10.1016/j.cageo.2012.03.027 .
- [190] He, Q., Barajas-Solano, D., Tartakovsky, G., and Tartakovsky, A. M. Physics-informed neural networks for multiphysics data assimilation with application to subsurface transport. Advances in Water Resources , 141, 2020. DOI: 10.1016/j.advwatres.2020.103610 .
- [191] Heidarabad, R. G. and Shin, K. Carbon capture and storage in depleted oil and gas reservoirs:the viewpoint of wellbore injectivity. Energies , 17(5), 2024. DOI: 10.3390/en17051201 .


- [192] Hill, A. D. Production Logging: Theoretical and Interpretive Elements . Society of Petroleum Engineers, second edition, 2021. ISBN 978-1613999073. DOI: 10.2118/9781613998243 .
- [193] Hoeting, J. A., Madigan, D., Raftery, A. E., and Volinsky, C. T. Bayesian model averaging: a tutorial. Statistical Science , 14(4), 1999. URL http://www.jstor.org/stable/2676803 .
- [194] Hoffimann, J. GeoStats.jl – high-performance geostatistics in Julia. The Journal of Open Source Software , 2018. DOI: 10.21105/joss.00692 .
- [195] Holland, J. H. Adaptation in Natural and Artificial System . The MIT Press, 1992. ISBN 978-0262581110.
- [196] Horn, R. A. The Hadamard product. In Matrix Theory and Applications , pages 87–170. American Mathematical Society, 1990. DOI: 10.1090/psapm/040/1059485 .
- [197] Houtekamer, P. L. and Mitchell, H. L. Data assimilation using an ensemble Kalman filter technique. Monthly Weather Review , 126(3):796–811, 1998. DOI: 10.1175/15200493(1998)126&lt;0796:DAUAEK&gt;2.0.CO;2 .
- [198] Houtekamer, P. L. and Mitchell, H. L. A sequential ensemble Kalman filter for atmospheric data assimilation. Monthly Weather Review , 129(1):123–137, 2001. DOI: 10.1175/15200493(2001)129&lt;0123:ASEKFF&gt;2.0.CO;2 .
- [199] Houtekamer, P. L. and Mitchell, H. L. Ensemble Kalman filtering. Quarterly Journal of the Royal Meteorological Society , 131:3269–3289, 2005. DOI: 10.1256/qj.05.135 .
- [200] Houtekamer, P. L. and Zhang, F. Review of the ensemble Kalman filter for atmospheric data assimilation. Monthly Weather Review , 144, 2016. DOI: 10.1175/MWR-D-15-0440.1 .
- [201] Houtekamer, P. L., Mitchell, H. L., Pellerin, G., Buehner, M., Charron, M., Spacek, L., and Hansen, B. Atmospheric data assimilation with an ensemble Kalman filter: Results with real observations. Monthly Weather Review , 133(3):604–620, 2005. DOI: 10.1175/MWR-2864.1 .
- [202] Howard, A. D. and Knutson, T. R. Sufficient conditions for river meandering: A simulation approach. Water Resources Research , 20 (11), 1984. DOI: 10.1029/WR020i011p01659 .
- [203] Hu, L. Y. Gradual deformation and iterative calibration of Gaussianrelated stochastic models. Mathematical Geology , 32(1):87–108, 2000. DOI: 10.1023/A:1007506918588 .
- [204] Hu, L. Y., Le Ravalec, M., Blanc, G., Roggero, F., Noetinger, B., Haas, A., and Corre, B. Reducing uncertainties in production forecasts by constraining geological modeling to dynamic data. In Proceedings of the SPE Annual Technical Conference and Exhibition, Houston, Texas, USA, 3–6 October , number SPE-56703-MS, 1999. DOI: 10.2118/56703-MS .
- [205] Huang, C., Hu, B. X., Li, X., and Ye, M. Using data assimilation method to calibrate a heterogeneous conductivity field and improve solute transport prediction with an unknown contamination source.


- Stochastic Environmental Research and Risk Assessment , 23, 2009. DOI: 10.1007/s00477-008-0289-4 .
- [206] Huang, X., Will, R., Khan, M., and Stanley, L. Reservoir characterization by integration of time-lapse seismic and production data. In Proceedings of the SPE Annual Technical Conference and Exhibition, San Antonio, Texas, 5–8 October , number SPE-38695-MS, 1997.
- [207] Hunt, B. R., Kostelich, E. J., and Szunyogh, I. Efficient data assimilation for spatiotemporal chaos: a local ensemble transform Kalman filter. Physica D , 230:112–26, 2007. DOI: 10.1016/j.physd.2006.11.008 .
- [208] Iglesias, M. and Yang, Y. Adaptive regularisation for ensemble Kalman inversion. Inverse Problems , 37(2), 2021. DOI: 10.1088/13616420/abd29b .
- [209] Iglesias, M. A. and Dawson, C. The regularizing Levenberg-Marquardt scheme for history matching of petroleum reservoirs. Computational Geosciences , 17(6):1033–1053, 2013. DOI: 10.1007/s10596-013-9373-z .
- [210] Iglesias, M. A., Law, K. J. H., and Stuart, A. M. Ensemble Kalman methods for inverse problems. Inverse Problems , 29(4), 2013. DOI: 10.1088/0266-5611/29/4/045001 .
- [211] Jaber, A. K., Al-Jawad, S. N., and Alhuraishawy, A. K. A review of proxy modeling applications in numericalreservoir simulation. Arabian Journal of Geosciences , 12, 2019. DOI: 0.1007/s12517-019-4891-1 .
- [212] Jafarpour, B. and Khodabakhshi, M. A probability conditioning method (PCM) for nonlinear flow data integration into multipoint statistical facies simulation. Mathematical Geosciences , 43(2):133–164, 2011. DOI: 10.1007/s11004-011-9316-y .
- [213] Jafarpour, B. and McLaughlin, D. B. History matching with an ensemble Kalman filter and discrete cosine parameterization. Computational Geosciences , 12(2):227–244, 2008. DOI: 10.1007/s10596-008-9080-3 .
- [214] Jeffreys, H. An invariant form for the prior probability in estimation problems. Proceedings of the Royal Society A , 186(1007):453–461, 1946. DOI: 10.1098/rspa.1946.0056 .
- [215] Jeong, H., Sun, A. Y., Jeon, J., Min, B., and Jeong, D. Efficient ensemble-based stochastic gradient methods for optimization under geological uncertainty. Frontiers in Earth Science , 8, 2020. DOI: 10.3389/feart.2020.00108 .
- [216] Jiang, P., Chen, X., Chen, K., Anderson, J., Collins, N., and Gharamti, M. E. DART-PFLOTRAN: an ensemble-based data assimilation system for estimating subsurface flow and transport model parameters. Environmental Modelling and Software , 142, 142. DOI: 10.1016/j.envsoft.2021.105074 .
- [217] Jiang, S. and Durlofsky, L. J. History matching for geological carbon storage using data-space inversion with spatio-temporal data parameterization. International Journal of Greenhouse Gas Control , 134, 2024. DOI: 10.1016/j.ijggc.2024.104124 .
- [218] Jiang, S., Hui, M.-H., and Durlofsky, L. J. Data-space inversion with a recurrent autoencoder for naturally fractured sys-


- tems. Frontiers in Applied Mathematics and Statistics , 7, 2021. DOI: 10.3389/fams.2021.686754 .
- [219] Jin, L., Alpak, F., van den Hoek, P., Pirmez, C., Fehintola, T., Tendo, F., and Olaniyan, E. A comparison of stochastic data-integration algorithms for the joint history matching of production and time-lapseseismic data. SPE Reservoir Evaluation &amp; Engineering , 15(4), 2012. DOI: 10.2118/146418-PA .
- [220] Jin, Q. On a regularized Levenberg-Marquardt method for solving nonlinear inverse problems. Numerische Mathematik , 115, 2010. DOI: 10.1007/s00211-009-0275-x .
- [221] Johann, P., Sansonowski, R., Oliveira, R., and Bampi, D. 4D seismic in heavy-oil, turbidite reservoir offshore Brazil. The Leading Edge , 28 (6):718–729, June 2009. DOI: 10.1190/1.3148415 .
- [222] Joon, S., Dawuda, I., Morgan, E., and Srinivasan, S. Rock physicsbased data assimilation of integrated continuous active-source seismic and pressure monitoring data during geological carbon storage. SPE Journal , 27(4), 2022. DOI: 10.2118/209585-PA .
- [223] Joosten, G. J., Altintas, A., Essen, G. V., Doren, J. V., van den Hoek, P. G. P., and Foreste, K. Reservoir model maturation and assisted history matching based on production and 4D seismic data. In Proceedings of the SPE Annual Technical Conference and Exhibition, Amsterdam, The Netherlands, 27–29 October , number SPE-170604-MS, 2014. DOI: 10.2118/170604-MS .
- [224] Journel, A. G. and Deutsch, C. V. Entropy and spatial disorder. Mathematical Geology , 25(3):329–355, 1993. DOI: 10.1007/BF00901422 .
- [225] Kahrobaei, S., van Essen, G. M., Doren, J. F. V., den Hof, P. M. V., and Jansen, J. D. Adjoint-based history matching of structural models using production and time-lapse seismic dat. In Proceedings of the SPE Reservoir Simulation Symposium, The Woodlands, Texas , number SPE-163586-MS, 2013. DOI: 10.2118/163586-MS .
- [226] Kaipio, J. P. and Somersalo, E. Statistical and Computational Inverse Problems . Springer New York, 2005. DOI: 10.1007/b138659 .
- [227] Kaleta, M. P., Hanea, R. G., Heemink, A. W., and Jansen, J.-D. Model-reduced gradient-based history matching. Computational Geosciences , 15, 2011. DOI: 10.1007/s10596-010-9203-5 .
- [228] Kalman, R. E. A new approach to linear filtering and prediction problems. Transactions of the ASME, Journal of Basic Engineering , 82: 35–45, 1960. DOI: 10.1115/1.3662552 .
- [229] Kalman, R. E. and Bucy, R. S. New results in linear filtering and prediction theory. Journal of Basic Engineering , 83(1), 1961. DOI: 10.1115/1.3658902 .
- [230] Kam, D., Han, J., and Datta-Gupta, A. Streamline-based rapid history matching of bottomhole pressure and three-phase production data. In Proceedings of the SPE Improved Oil Recovery Conference, Tulsa, Oklahoma, USA, 11–13 April , number SPE-179549-MS, 2016. DOI: 10.2118/179549-MS .


- [231] Kam, D., Han, J., and Datta-Gupta, A. Streamline-based history matching of bottomhole pressure and three-phase production data using a multiscale approach. Journal of Petroleum Science and Engineering , 154, 2017. DOI: 10.1016/j.petrol.2017.04.022 .
- [232] Kang, X., Kokkinaki, A., Kitanidis, P. K., Shi, X., Lee, J., Mo, S., and Wu, J. Hydrogeophysical characterization of nonstationary DNAPL source zones by integrating a convolutional variational autoencoder and ensemble smoother. Water Resources Research , 57(2), 2021. DOI: 10.1029/2020WR028538 .
- [233] Karsli, H. and Dondurur, D. A procedure to reduce side lobes of reflection wavelets: A contribution to low frequency information. Journal of Applied Geophysics , 96, 2013. DOI: 10.1016/j.jappgeo.2013.07.002 .
- [234] Kennedy, J. and Eberhart, R. Particle swarm optimization. In Proceedings IEEE international conference on neural networks, IV. IEEE Service Ceneter, Piscataway, NJ , pages 1942–1948, 1995. DOI: 10.1109/ICNN.1995.488968 .
- [235] Kennedy, M. C. and O’Hagan, A. Bayesian calibration of computer models. Journal of The Royal Statistical Society: Series B , 63:425–464, 2001. DOI: 10.1111/1467-9868.00294 .
- [236] Keppenne, C. L. and Rienecker, M. M. Assimilation of temperature into an isopycnal ocean general circulation model using a parallel ensemble Kalman filter. Journal of Marine Systems , 40–41:363–380, 2003. DOI: 10.1016/S0924-7963(03)00025-3 .
- [237] Khaninezhad, M. M., Jafarpour, B., and Li, L. Sparse geologic dictionaries for subsurface flow model calibration: Part i. inversion formulation. Advances in Water Resources , 39:106–121, 2012. DOI: 10.1016/j.advwatres.2011.09.002 .
- [238] Kirkpatrick, S., Jr., C. D. G., and Vecchi, M. P. Optimization by simulated annealing. Science , 220(4598):671–680, 1983. DOI: 10.1126/science.220.4598.671 .
- [239] Kitanidis, P. K. Quasi-linear geostatistical theory for inversing. Water Resources Research , 31(10):2411–2419, 1995. DOI: 10.1029/95WR01945 .
- [240] Kovachki, N. B. and Stuart, A. M. Ensemble Kalman inversion: a derivative-free technique for machine learning tasks. Inverse Problems , 35, 2019. DOI: 10.1088/1361-6420/ab1c3a .
- [241] Kragh, E. and Christie, P. Seismic repeatability, normalized RMS, and predictability. The Leading Edge , 21(7), 2002. DOI: 10.1190/1.1497316 .
- [242] Krige, D. G. A statistical approach to some mine valuations and allied problems at the Witwatersrand. Master’s thesis, University of the Witwatersrand, Faculty of Engineering, 1951.
- [243] Krogstad, S., Lie, K.-A., Moyner, O., Nilsen, H. M., Raynaud, X., and Skaflestad, B. MRST-AD – an open-source framework for rapid prototyping and evaluation of reservoir simulation problems. In Proceedings


- of the SPE Reservoir Simulation Symposium, Houston, Texas, USA , 2015. DOI: 10.2118/173317-MS .
- [244] Kumar, S. V., Zaitchik, B. F., Peters-Lidard, C. D., Rodell, M., Reichle, R., Li, B., Jasinski, M., Mocko, D., Getirana, A., Lannoy, G. D., Cosh, M. H., Hain, C. R., Anderson, M., Arsenault, K. R., Xia, Y., and Ek, M. Assimilation of gridded GRACE terrestrial water storage estimates in the north american land data assimilation system. Journal of Hydrometeorology , 17(7), 2016. DOI: 10.1175/JHM-D-15-0157.1 .
- [245] Lacerda, J. M., Emerick, A. A., and Pires, A. P. Methods to mitigate loss of variance due to sampling errors in ensemble data assimilation with non-local model parameters. Journal of Petroleum Science and Engineering , 172:690–706, 2019. DOI: 10.1016/j.petrol.2018.08.056 .
- [246] Laloy, E., Hérault, R., Jacques, D., and Linde, N. Inversion using a new low-dimensional representation of complex binary geological media based on a deep neural network. Advances in Water Resources , 110:387–405, 2017. DOI: 10.1016/j.advwatres.2017.09.029 .
- [247] Laloy, E., Hérault, R., Jacques, D., and Linde, N. Training-image based geostatistical inversion using a spatial generative adversarial neural network. Water Resources Research , 54(1):381–406, 2018. DOI: 10.1002/2017WR022148 .
- [248] Lam, D.-T., Kerrou, J., Renard, P., Benabderrahmane, H., and Perrochet, P. Conditioning multi-gaussian groundwater flow parameters to transient hydraulic head and flowrate data with iterative ensemble smoothers: A synthetic case study. Frontiers in Earth Science , 2020. DOI: 10.3389/feart.2020.00202 .
- [249] Lam, D.-T., Renard, P., Straubhaar, J., and Kerrou, J. Multiresolution approach to condition categorical multiple-point realizations to dynamic data with iterative ensemble smoothing. Water Resources Research , 56(2), 2020. DOI: 10.1029/2019WR025875 .
- [250] LaVenue, A. M. and Pickens, J. F. Application of a coupled adjoint sensitivity and kriging approach to calibrate a groundwater flow model. Water Resources Research , 28(6):1543–1569, 1992. DOI: 10.1029/92WR00208 .
- [251] Lawson, W. G. and Hansen, J. A. Implications of stochastic and deterministic filters as ensemble-based data assimilation methods in varying regimes of error growth. Monthly Weather Review , 132(8):1966–1981, 2004. DOI: 10.1175/1520-0493(2004)132&lt;1966:IOSADF&gt;2.0.CO;2 .
- [252] Le, D. H., Younis, R., and Reynolds, A. C. A history matching procedure for non-Gaussian facies based on ES-MDA. In Proceedings of the SPE Reservoir Simulation Symposium, Houston, Texas, USA, 23–25 February , number SPE-173233-MS, 2015. DOI: 10.2118/173233-MS .
- [253] Le, D. H., Emerick, A. A., and Reynolds, A. C. An adaptive ensemble smoother with multiple data assimilation for assisted history matching. SPE Journal , 21(6):2195–2207, 2016. DOI: 10.2118/173214-PA .
- [254] Leeuwenburgh, O. and Arts, R. Distance parameterization for efficient seismic history matching with the ensemble Kalman filter. Computa-


- tional Geosciences , 18(3–4):535–548, 2014. DOI: 10.1007/s10596-0149434-y .
- [255] Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., Goncalves, L. G., Cossetin, C., Bhanja, S., Mukherjee, A., Tian, S., Tangdamrongsub, N., Long, D., Nanteza, J., Lee, J., Policelli, F., Goni, I. B., Daira, D., Bila, M., Lannoy, G., Mocko, D., Steele-Dunne, S. C., Save, H., and Bettadpur, S. Global GRACE data assimilation for groundwater and drought monitoring: Advances and challenges. Water Resources Research , 55(9), 2019. DOI: 10.1029/2018WR024618 .
- [256] Li, G. and Reynolds, A. C. Iterative ensemble Kalman filters for data assimilation. SPE Journal , 14(3):496–505, 2009. DOI: 10.2118/109808PA .
- [257] Li, G. and Reynolds, A. C. Uncertainty quantification of reservoir performance predictions using a stochastic optimization algorithm. Computational Geosciences , 15(3):451–462, 2011. DOI: 10.1007/s10596010-9214-2 .
- [258] Li, L., Puzel, R., and Davis, A. Data assimilation in groundwater modelling: ensemble Kalman filter versus ensemble smoothers. Hydrological Processes , 32(13), 2018. DOI: 10.1002/hyp.13127 .
- [259] Li, R., Reynolds, A. C., and Oliver, D. S. History matching of three-phase flow production data. SPE Journal , 8(4):328–340, 2003. DOI: 10.2118/87336-PA .
- [260] Li, X. and Zhang, D. A backward automatic differentiation framework for reservoir simulation. Computational Geosciences , 18, 2014. DOI: 10.1007/s10596-014-9441-z .
- [261] Lie, K.-A. An Introduction to Reservoir Simulation Using MATLAB/GNU Octave – User Guide for the MATLAB Reservoir Simulation Toolbox (MRST) . Cambridge University Press, 2019. DOI: 10.1017/9781108591416 .
- [262] Liem, M., Matthai, S. K., and Jenny, P. Estimation of fracture aperture in naturally fractured reservoirs using an ensemble smoother with multiple data assimilation. In Proceedings of the European Conference for Mathematics of Geological Reservoirs ECMOR, September 5-7, The Hague, The Netherlands , 2022. DOI: 10.3997/2214-4609.202244068 .
- [263] Lima, M. M., Emerick, A. A., and Ortiz, C. E. P. Data-space inversion with ensemble smoother. Computational Geosciences , 24(3): 1179–1200, 2020. DOI: 10.1007/s10596-020-09933-w .
- [264] Liu, G., Chen, Y., and Zhang, D. Investigation of flow and transport processes at the MADE site using ensemble Kalman filter. Advances in Water Resources , 31(7):975–986, 2008. DOI: 10.1016/j.advwatres.2008.03.006 .
- [265] Liu, M. and Grana, D. Stochastic nonlinear inversion of seismic data for the estimation of petroelastic properties using the ensemble smoother and data reparameterization. Geophysics , 83(3), 2018. DOI: 10.1190/geo2017-0713.1 .


- [266] Liu, N. and Oliver, D. S. Evaluation of Monte Carlo methods for assessing uncertainty. SPE Journal , 8(2):188–195, 2003. DOI: 10.2118/84936-PA .
- [267] Liu, N. and Oliver, D. S. Critical evaluation of the ensemble Kalman filter on history matching of geologic facies. In Proceedings of the SPE Reservoir Simulation Symposium , number SPE-92867-MS, 2005. DOI: 10.2118/92867-MS .
- [268] Liu, Y., Sun, W., and Durlofsky, L. J. A deep-learning-based geological parameterization for history matching complex models. Mathematical Geosciences , 51:725–766, 2019. DOI: 10.1007/s11004-019-09794-9 .
- [269] Lomeland, F., Ebeltoft, E., and Thomas, W. H. A new versatile relative permeability correlation. In International Symposium of the Society of Core Analysts, Toronto, Canada, 21–25 August , 2005. URL jgmaas.com/SCA/2005/SCA2005-32.pdf .
- [270] Lorenc, A. C. The potential of the ensemble Kalman filter for NWP—a comparison with 4D-Var. Quarterly Journal of the Royal Meteorological Society , 129(595):3183–3203, 2003. DOI: 10.1256/qj.02.132 .
- [271] Lorentzen, R. J., Berg, A. M., Nævdal, G., and Vefring, E. H. A new approach for dynamic optimization of waterflooding problems. In Proceedings of the SPE Intelligent Energy Conference and Exhibition , number SPE-99690-MS, 2006. DOI: 10.2118/99690-MS .
- [272] Lorentzen, R. J., Flornes, K., and Nævdal, G. History channelized reservoirs using the ensemble Kalman filter. SPE Journal , 17(1): 137–151, 2012. DOI: 10.2118/143188-PA .
- [273] Lorentzen, R. J., Luo, X., Bhakta, T., and Valestrand, R. History matching the full norne field model using seismic and production data. SPE Journal , 24(4):1452–1467., 2019. DOI: 10.2118/194205-PA .
- [274] Lorentzen, R. J., Bhakta, T., Grana, D., Luo, X., Valestrand, R., and Nævdal, G. Simultaneous assimilation of production and seismic data: application to the norne field. Computational Geosciences , 24:907–920, 2020. DOI: 10.1007/s10596-019-09900-0 .
- [275] Lorentzen, R. J., Bhakta, T., Fossum, K., Haugen, J. A., Lie, E. O., Ndingwan, A. O., and Straith, K. R. Ensemble-based history matching of the Edvard Grieg field using 4D seismic data. Computational Geosciences , 28, 2024. DOI: 10.1007/s10596-024-10275-0 .
- [276] Lorenz, E. N. and Emanuel, K. A. Optimal sites for supplementary weather observations: Simulation with a small model. Journal of the Atmospheric Sciences , 55(3), 1998. DOI: 10.1175/15200469(1998)055&lt;0399:OSFSWO&gt;2.0.CO;2 .
- [277] Lu, M. and Chen, Y. Improved estimation and forecast through model error estimation – norne field example. In Proceedings of the International Petroleum Technology Conference, Beijing, China, 26–28 March , number IPTC-19142-MS, 2019. DOI: 10.2523/IPTC-19142MS .


- [278] Luo, X. and Bhakta, T. Automatic and adaptive localization for ensemble-based history matching. Journal of Petroleum Science and Engineering , 184, 2020. DOI: 10.1016/j.petrol.2019.106559 .
- [279] Luo, X., Stordal, A. S., Lorentzen, R. J., and Nævdal, G. Iterative ensemble smoother as an approximate solution to a regularized minimum-average-cost problem: Theory and applications. SPE Journal , 20(5), 2015. DOI: 10.2118/176023-PA .
- [280] Luo, X., Bhakta, T., and Nævdal, G. Correlation-based adaptive localization with applications to ensemble-based 4D-seismic history matching. SPE Journal , 23(2):396–427, 2018. DOI: 10.2118/185936-PA .
- [281] Luo, X., Lorentzen, R. J., Valestrand, R., and Evensen, G. Correlationbased adaptive localization for ensemble-based history matching: Applied to the Norne field case study. SPE Reservoir Engineering , 22(3): 1084–1109, 2018. DOI: 10.2118/191305-PA .
- [282] Luo, X., Lorentzen, R. J., and Bhakta, T. Accounting for model errors of rock physics models in 4D seismic history matching problems: A perspective of machine learning. Journal of Petroleum Science and Engineering , 196, 2021. DOI: 10.1016/j.petrol.2020.107961 .
- [283] Ma, W., Jafarpour, B., and Qin, J. Dynamic characterization of geologic CO 2 storage aquifers from monitoring data with ensemble Kalman filter. International Journal of Greenhouse Gas Control , 81, 2019. DOI: 10.1016/j.ijggc.2018.10.009 .
- [284] Ma, X. and Bi, L. A robust adaptive iterative ensemble smoother scheme for practical history matching applications. Computational Geosciences , First Online, 2019. DOI: 10.1007/s10596-018-9786-9 .
- [285] Mahalanobis, P. C. On the generalised distance in statistics. In Proceedings of the National Institute of Sciences of India , volume 2, pages 49–55, 1936.
- [286] Mahjour, S. K., Santos, A. A. S., and Manuel G. Correia, D. J. S. Developing a workflow to select representative reservoir models combining distance-based clustering and data assimilation for decision making process. Journal of Petroleum Science and Engineering , 190, 2020. DOI: 10.1016/j.petrol.2020.107078 .
- [287] Mannseth, T. Relation between level set and truncated pluri-Gaussian methodologies for facies representation. Mathematical Geosciences , 46 (6):711–731, 2014. DOI: 10.1007/s11004-013-9507-9 .
- [288] Mannseth, T. Comparison of five different ways to assimilate data for a simplistic weakly nonlinear parameter estimation problem. Computational Geosciences , 19(4):791–804, 2015. DOI: 10.1007/s10596-0159490-y .
- [289] Mariethoz, G. Handbook of Mathematical Geosciences: Fifty Years of IAMG , chapter When Should We Use Multiple-Point Geostatistics? Springer International Publishing, 2018. DOI: 10.1007/978-3319-78999-6_31 .


- [290] Mariethoz, G. and Caers, J. Multiple-point geostatistics – Stochastic modeling with training images . John Wiley &amp; Sons, Ltd., 2014. ISBN 978-1118662939.
- [291] Marquart, G., Vogt, C., Klein, C., and Widera, A. Estimation of geothermal reservoir properties using the ensemble Kalman filter. Energy Procedia , 40, 2013. DOI: 10.1016/j.egypro.2013.08.015 .
- [292] Maschio, C. and Schiozer, D. J. Bayesian history matching using artificial neural network and Markov chain Monte Carlo. Journal of Petroleum Science and Engineering , 123, 2014. DOI: 10.1016/j.petrol.2014.05.016 .
- [293] Maschio, C. and Schiozer, D. J. A new methodology for Bayesian history matching using parallel interacting Markov chain Monte Carlo. Inverse Problems in Science and Engineering , 26(4), 2018. DOI: 10.1080/17415977.2017.1322078 .
- [294] Maschio, C., Neto, G. M. S., Davolio, A., and Vinicius S. Rios, D. J. S. Performance assessment of an iterative ensemble smoother with local analysis to assimilate big 4D seismic datasets applied to a complex pre-salt-like benchmark case. Journal of Geophysics and Engineering , 21(1), 2024. DOI: 10.1093/jge/gxad099 .
- [295] Matheron, G. The theory of regionalized variables and its applications. Technical Report No. 5, Les Cahiers du Centre de Morphologie Mathématique de Fontainebleau, 1971. URL http://cg.ensmp.fr/ bibliotheque/public/MATHERON_Ouvrage_00167.pdf .
- [296] Matheron, G., Beucher, H., de Fouquet, C., Galli, A., Guerillot, D., and Ravenne, C. Conditional simulation of the geometry of fluvio-deltaic reservoirs. In Proceedings of the SPE Annual Technical Conference and Exhibition , number SPE-16753-MS, 1987. DOI: 10.2118/16753-MS .
- [297] Maucec, M., Ravanelli, F. M. D. M., Lyngra, S., Zhang, S. J., Alramadhan, A. A., Abdelhamid, O. A., and Al-Garni, S. A. Ensemble-based assisted history matching with rigorous uncertainty quantification applied to a naturally fractured carbonate reservoir. In Proceedings of the SPE Annual Technical Conference and Exhibition, Dubai, UAE, 26–28 September , number SPE-181325-MS, 2016. DOI: 10.2118/181325-MS .
- [298] Mavko, G., Mukerji, T., and Dvorkin, J. The Rock Physics Handbook: Tools for Seismic Analysis of Porous Media . Cambridge University Press, 2nd edition, 2009. ISBN 978-0511626753. DOI: 10.1017/CBO9780511626753 .
- [299] McGrayne, S. B. The Theory that Would Not Die: How Bayes’ Rule Cracked the Enigma Code, Hunted Down Russian Submarines, and Emerged Triumphant from Two Centuries of Controversy . Yale University Press, 2011.
- [300] McHargue, T., Pyrcz, M. J., Sullivan, M. D., Clark, J. D., Fildani, A., Romans, B. W., Covault, J. A., Levy, M., Posamentier, H. W., and Drinkwater, N. J. Architecture of turbidite channel systems on the continental slope: Patterns andpredictions. Marine and Petroleum Geology , 28:728–243, 2011. DOI: 10.1016/j.marpetgeo.2010.07.008 .


- [301] McKay, M. D., Beckman, R. J., and Conover, W. J. A comparison of three methods for selecting values of input variables in the analysis of output from a computer code. Technometrics , 21(2), 1979. DOI: 10.2307/1268522 .
- [302] Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H., and Teller, E. Equations of state calculations by fast computing machines. Journal of Chemical Physics , 21:1087–1092, 1953. DOI: 10.1063/1.1699114 .
- [303] Mezghani, M., Fornel, A., Langlais, V., and Lucet, N. History matching and quantitative use of 4D seismic data for an improved reservoir characterization. In Proceedings of the SPE Annual Technical Conference and Exhibition, Houston, Texas, 26–29 September , number SPE-90420-MS, 2004. DOI: 10.2118/90420-MS .
- [304] Moreno, D. L. and Aanonsen, S. I. Continuous facies updating using the ensemble Kalman filter and the level set method. Mathematical Geosciences , 43(8):951–970, 2011. DOI: 10.1007/s11004-011-9347-4 .
- [305] Moreno, D. L., Aanonsen, S. I., Evensen, G., and Skjervheim, J.A. Channel facies estimation based on Gaussian perturbations in the EnKF. In Proceedings of the 11th European Conference on the Mathematics of Oil Recovery (ECMOR XI) , 2008. DOI: 10.3997/22144609.20146403 .
- [306] Morozov, V. Methods for Solving Incorrectly Posed Problems . SpringerVerlag New York, 1984. DOI: 10.1007/978-1-4612-5280-1 .
- [307] Morris, M. D. Factorial sampling plans for preliminary computational experiments. Technometrics , 33(2), 1991. DOI: 10.2307/1269043 .
- [308] Mosser, L., Dubrule, O., and Blunt, M. J. DeepFlow: History matching in the space of deep generative models. arXiv:1905.05749v1 [cs.LG] , 2019. DOI: 10.48550/arXiv.1905.05749 .
- [309] Motaei, E. and Ganat, T. Smart proxy models art and future directions in the oil and gas industry:a review. Geoenergy Science and Engineering , 227, 2023. DOI: 10.1016/j.geoen.2023.211918 .
- [310] Moyen, R. and Gentilhomme, T. Adaptive ensemble-based optimisation for petrophysical inversion. Mathematical Geosciences , 53, 2021. DOI: 10.1007/s11004-020-09900-2 .
- [311] Moyner, O. JutulDarcy.jl a fully differentiable high-performance reservoir simulator based on automatic differentiation. In Proceedings of the European Conference for Mathematics of Geological Reservoirs ECMOR, September 2-5, Olso, Norway , 2024. DOI: 10.3997/22144609.202437111 .
- [312] Myers, M., Stalker, L., Pejcic, B., and Ross, A. Tracers – past, present and future applications in CO 2 geosequestration. Applied Geochemistry , 30, 2013. DOI: 10.1016/j.apgeochem.2012.06.001 .
- [313] Nævdal, G., Mannseth, T., and Vefring, E. H. Near-well reservoir monitoring through ensemble Kalman filter. In Proceedings of the SPE/DOE Improved Oil Recovery Symposium, 13–17 April , number SPE-75235-MS, 2002. DOI: 10.2118/75235-MS .


- [314] Nan, T. and Wu, J. Groundwater parameter estimation using the ensemble Kalman filter with localization. Hydrogeology Journal , 19, 2011. DOI: 10.1007/s10040-010-0679-9 .
- [315] Neal, R. M. Sampling from multimodal distributions using tempered transitions. Statistics and Computing , 6(4):353–366, 1996. DOI: 10.1007/BF00143556 .
- [316] Neal, R. M. Annealed importance sampling. Statistics and Computing , 11(2), 2001. DOI: 10.1023/A:1008923215028 .
- [317] Nelder, J. A. and Mead, R. A simplex method for function minimization. The Computer Journal , 7(4), 1965. DOI: 10.1093/comjnl/8.1.27 .
- [318] Nelsen, R. B. An Introduction to Copulas . Springer New York, NY, second edition, 2007. DOI: 10.1007/0-387-28678-0 .
- [319] Neto, G. M. S., Rios, V. S., Davolio, A., and Schiozer, D. J. Improving fluid modeling representation for seismic data assimilation in compositional reservoir simulation. Journal of Petroleum Science and Engineering , 194, 2020. DOI: 10.1016/j.petrol.2020.107446 .
- [320] Neto, G. M. S., Davolio, A., and Schiozer, D. J. Assimilating timelapse seismic data in the presence of significant spatially correlated model errors. Journal of Petroleum Science and Engineering , 207, 2021. DOI: 10.1016/j.petrol.2021.109127 .
- [321] Neto, G. M. S., Soares, R. V., Davolio, G. E. A., and Schiozer, D. J. Subspace ensemble randomized maximum likelihood with local analysis for time-lapse-seismic-data assimilation. SPE Journal , 26(2): 1011–1031, 2021. DOI: 10.2118/205029-PA .
- [322] Nilsen, M. M., Stordal, A. S., Raanes, P. N., Lorentzen, R. J., and Eikrem, K. S. Non-gaussian ensemble optimization. Mathematical Geosciences , 2024. DOI: 10.1007/s11004-024-10148-3 .
- [323] Nóbrega, D. V., de Moraes, F. S., and Emerick, A. A. Data assimilation of a legacy 4D seismic in a brown field. Journal of Geophysics and Engineering , 15(6), 2018. DOI: 10.1088/1742-2140/aadd68 .
- [324] Nocedal, J. Updating quasi-Newton matrices with limited storage. Mathematics of Computation , 35(151):773–782, 1980. DOI: 10.2307/2006193 .
- [325] Nocedal, J. and Wright, S. J. Numerical Optimization . Springer, New York, 2006. ISBN 978-0387303031. DOI: 10.1007/978-0-387-40065-5 .
- [326] Nunes, J. P. P., Seabra, G. S., and de Sousa Junior, L. C. A review of CO 2 -injection projects in the Brazilian pre-salt – storage capacity and geomechanical constraints. International Journal of Greenhouse Gas Control , 137, 2024. DOI: 10.1016/j.ijggc.2024.104232 .
- [327] Obidegwu, D., Chassagne, R., and MacBeth, C. Seismic assisted history matching using binary maps. Journal of Natural Gas Science and Engineering , 42, 2017. DOI: 10.1016/j.jngse.2017.03.001 .
- [328] Oliver, D. S. Minimization for conditional simulation: Relationship to optimal transport. Journal of Computational Physics , 265:1–15, 2014. DOI: 10.1016/j.jcp.2014.01.048 .


- [329] Oliver, D. S. Information content in 4D seismic data: Effect of correlated noise. Journal of Petroleum Science and Engineering , 208, 2022. DOI: 10.1016/j.petrol.2021.109728 .
- [330] Oliver, D. S. and Alfonzo, M. Calibration of imperfect models to biased observations. Computational Geosciences , 22:145–161, 2018. DOI: 10.1007/s10596-017-9678-4 .
- [331] Oliver, D. S. and Chen, Y. Recent progress on reservoir history matching: a review. Computational Geosciences , 15(1):185–221, 2011. DOI: 10.1007/s10596-010-9194-2 .
- [332] Oliver, D. S., He, N., and Reynolds, A. C. Conditioning permeability fields to pressure data. In Proceedings of the 5th European Conference on the Mathematics of Oil Recovery (ECMOR V), 03 September , 1996. DOI: 10.3997/2214-4609.201406884 .
- [333] Oliver, D. S., Reynolds, A. C., Bi, Z., and Abacioglu, Y. Integration of production data into reservoir models. Petroleum Geoscience , 7 (SUPP):65–73, 2001. DOI: 10.1144/petgeo.7.S.S65 .
- [334] Oliver, D. S., Reynolds, A. C., and Liu, N. Inverse Theory for Petroleum Reservoir Characterization and History Matching . Cambridge University Press, Cambridge, UK, 2008. ISBN 978-0511535642. DOI: 10.1017/CBO9780511535642 .
- [335] Oliver, D. S., Chen, Y., and Nævdal, G. Updating Markov chain models using the ensemble Kalman filter. Computational Geosciences , 15:325–344, 2011. DOI: 10.1007/s10596-010-9220-4 .
- [336] Oliver, D. S., Fossum, K., Bhakta, T., Sandø, I., Nævdal, G., and Lorentzen, R. J. 4D seismic history matching. Journal of Petroleum Science and Engineering , 207, 2021. DOI: 10.1016/j.petrol.2021.109119 .
- [337] OpenGoSim. PFLOTRAN-OGS. Software, 2024. URL https:// docs.opengosim.com/manual/introduction/ .
- [338] Otsuka, S., Kotsuki, S., and Miyoshi, T. Nowcasting with data assimilation: A case of global satellite mapping of precipitation. Weather and Forecasting , 31:1409–1416, 2016. DOI: 10.1175/WAF-D-16-0039.1 .
- [339] Oudshoorn, C., Werthmüller, D., Slob, E., and Voskov, D. Numerical experiment on data assimilation for geothermal doublets using production data and electromagnetic observations. Geophysics , 0(11), 2024. DOI: 10.1190/geo2023-0463.1 .
- [340] Owen, A. B. Orthogonal arrays for computer experiments, integration and visualization. Statistica Sinica , 2(2), 1992. URL https://www. jstor.org/stable/24304869 .
- [341] Paola, C. Quantitative models of sedimentary basin filling. Sedimentology , 47, 2000. DOI: 10.1046/j.1365-3091.2000.00006.x .
- [342] Patidar, A. K., Joshi, D., Dristant, U., and Choudhury, T. A review of tracer testing techniques in porous media specially attributed to the oil and gas industry. Journal of Petroleum Exploration and Production Technology , 12, 2022. DOI: 10.1007/s13202-022-01526-w .


- [343] Pebesma, E. J. Multivariable geostatistics in S: the gstat package. Computers &amp; Geosciences , 30(7), 2004. DOI: 10.1016/j.cageo.2004.03.012 .
- [344] Perrone, A., Pennadoro, F., Tiani, A., Rossa, E. D., and Sætrom, J. Enhancing the geological models consistency in ensemble based history matching an integrated approach. In Proceedings of the SPE Reservoir Characterisation and Simulation Conference and Exhibition, Abu Dhabi, UAE , 8–10 May , number SPE-186049-MS, 2017. DOI: 10.2118/186049-MS .
- [345] Peters, E., Chen, Y., Leeuwenburgh, O., and Oliver, D. S. Extended Brugge benchmark case for history matching and water flooding optimization. Computers &amp; Geosciences , 50:16–24, 2013. DOI: 10.1016/j.cageo.2012.07.018 .
- [346] Peters, L., Arts, R., Brouwer, G., Geel, C., Cullick, S., Lorentzen, R. J., Chen, Y., Dunlop, N., Vossepoel, F. C., Xu, R., Sarma, P., Alhuthali, A. H., and Reynolds, A. Results of the Brugge benchmark study for flooding optimisation and history matching. SPE Reservoir Evaluation &amp; Engineering , 13(3):391–405, 2010. DOI: 10.2118/119094-PA .
- [347] Ping, J. and Zhang, D. History matching of channelized reservoirs with vector-based level-set parameterization. SPE Journal , 19(3):514–529, 2014. DOI: 10.2118/169898-PA .
- [348] Powell, M. J. D. An efficient method for finding the minimum of a function of several variables without calculating derivatives. The Computer Journal , 7(2), 1964. DOI: 10.1093/comjnl/7.2.155 .
- [349] Powell, M. J. D. The NEWUOA software for unconstrained optimization without derivatives. In Pillo, G. and Roma, M., editors, Large-Scale Nonlinear Optimization. Nonconvex Optimization and Its Applications , volume 83. Springer, 2006. DOI: 10.1007/0-387-300651_16 .
- [350] Press, W. H., Teukolsky, S. A., Vetterling, W. T., and Flannery, B. P. Numerical Recipes: The Art of Scientific Computing . Cambridge University Press, Cambridge, England, 3rd edition, 2007. ISBN 9780521880688.
- [351] Ptak, T., Piepenbrink, M., and Martac, E. Tracer tests for the investigation of heterogeneous porous media and stochastic modelling of flow and transport-a review of some recent developments. Journal of Hydrology , 294, 2003. DOI: 10.1016/j.jhydrol.2004.01.020 .
- [352] Pyrcz, M. J., Sech, R. P., Covault, J. A., Willis, B. J., Sylvester, Z., and Sun, T. Stratigraphic rule-based reservoir modeling. Bulletin of Canadian Petroleum Geology , 63(4), 2015. DOI: 10.2113/gscpgbull.63.4.287 .
- [353] Raanes, P. N., Bocquet, M., and Carrassi, A. Adaptive covariance inflation in the ensemble Kalman filter by gaussian scale mixtures. Quarterly Journal of the Royal Meteorological Society , 145(718):53–75, 2019. DOI: 10.1002/qj.3386 .


- [354] Raanes, P. N., Stordal, A. S., and Evensen, G. Revising the stochastic iterative ensemble smoother. Nonlinear Processes in Geophysics , 26 (3), 2019. DOI: 10.5194/npg-2019-10 .
- [355] Raanes, P. N., Stordal, A. S., and Lorentzen, R. J. Review of ensemble gradients for robust optimisation. arXiv:2304.12136v1 [math.OC] , 2023. DOI: 10.48550/arXiv.2304.12136 .
- [356] Rafiee, J. and Reynolds, A. C. Theoretical and efficient practical procedures for the generation of inflation factors for ES-MDA. Inverse Problems , 33(11):115003, 2017. DOI: 10.1088/1361-6420/aa8cb2 .
- [357] RamaRao, B. S., LaVenue, A. M., de Marsily, G., and Marietta, M. G. Pilot point methodology for automated calibration of an ensemble of conditionally simulated transmissivity fields: 1. theory and computational experiments. Water Resources Research , 31(3):475–493, 1995. DOI: 10.1029/94WR02258 .
- [358] Ranazzi, P. H., Luo, X., and Sampaio, M. A. Improving pseudo-optimal Kalman-gain localization using the random shuffle method. Journal of Petroleum Science and Engineering , 215, 2022. DOI: 10.1016/j.petrol.2022.110589 .
- [359] Rasmussen, A. F., Sandve, T. H., Bao, K., Lauser, A., Hove, J., Skaflestad, B., Klöfkorn, R., Blatt, M., Rustad, A. B., vareid, O. S., Lie, K.-A., and Thune, A. The open porous media flow reservoir simulator. Computers and Mathematics with Applications , 81, 2020. DOI: 10.1016/j.camwa.2020.05.014 .
- [360] Reichle, R. H., McLaughlin, D. B., and Entekhabi, D. Hydrologic data assimilation with the ensemble Kalman filter. Monthly Weather Review , 130(1):103–114, 2002. DOI: 10.1175/15200493(2002)130&lt;0103:HDAWTE&gt;2.0.CO;2 .
- [361] Reichle, R. H., Walker, J. P., Koster, R. D., and Houser, P. R. Extended versus ensemble Kalman filtering for land data assimilation. Journal of Hydrometeorology , 3(6), 2002. DOI: 10.1175/15257541(2002)003&lt;0728:EVEKFF&gt;2.0.CO;2 .
- [362] Remy, N., Boucher, A., and Wu, J. Applied Geostatistics with SGeMS – A User’s Guide . 2009.
- [363] Reynolds, A. C., He, N., Chu, L., and Oliver, D. S. Reparameterization techniques for generating reservoir descriptions conditioned to variograms and well-test pressure data. SPE Journal , 1(4):413–426, 1996. DOI: 10.2118/30588-PA .
- [364] Reynolds, A. C., Zafari, M., and Li, G. Iterative forms of the ensemble Kalman filter. In Proceedings of 10th European Conference on the Mathematics of Oil Recovery, Amsterdam, 4–7 September , 2006. DOI: 10.3997/2214-4609.201402496 .
- [365] Ringrose, P. and Bentley, M. Reservoir Model Design . Springer Netherlands, 2015. DOI: 10.1007/978-94-007-5497-3 .
- [366] Ringrose, P. S. and Meckel, T. A. Maturing global CO 2 storage resources on offshore continental margins to achieve 2DS emissions re-


- ductions. Scientific Reports , 9(17944), 2019. DOI: 10.1038/s41598019-54363-z .
- [367] Rodrigues, J. R. P. Calculating derivatives for automatic history matching. Computational Geosciences , 10(1):119–136, 2006. DOI: 10.1007/s10596-005-9013-3 .
- [368] Roggero, F. and Hu, L. Y. Gradual deformation of continuous geostatistical models for history matching. In Proceedings of the SPE Annual Technical Conference and Exhibition, New Orleans, Louisiana, 27–30 September , number SPE-49004-MS, 1998. DOI: 10.2118/49004-MS .
- [369] Rommelse, J. Data Assimilation in Reservoir Management . Ph.D. thesis, Technical University of Delft, Delft, The Netherlands, 2009.
- [370] Rosa, D. R., Schiozer, D. J., and Davolio, A. Data assimilation of production and multiple 4D seismic acquisitions in a deepwater field using ensemble smoother with multiple data assimilation. SPE Reservoir Evaluation &amp; Engineering , 26(4), 2023. DOI: 10.2118/215812-PA .
- [371] Sætrom, J., Morell, E., Ravari, R. R., Maitre, C. L., and Seldal, M. Fast integrated reservoir modelling on the Gjøa field offshore Norway. In Proceedings of the Abu Dhabi International Petroleum Exhibition &amp; Conference, Abu Dhabi, UAE, 13–16 November , number SPE-188557MS, 2017. DOI: 10.2118/188557-MS .
- [372] Sakov, P. and Bertino, L. Relation between two common localisation methods for the EnKF. Computational Geosciences , 15(2):225–237, 2011. DOI: 10.1007/s10596-010-9202-6 .
- [373] Sakov, P. and Oke, P. R. Implications of the form of the ensemble transformation in the ensemble square root filters. Monthly Weather Review , 136:1042–1053, 2008. DOI: 10.1175/2007MWR2021.1 .
- [374] Sakov, P. and Oke, P. R. A deterministic formulation of the ensemble Kalman filter: an alternative to ensemble square root filters. Tellus A , 60(2):361–371, 2008. DOI: 10.1111/j.1600-0870.2007.00299.x .
- [375] Sakov, P., Counillon, F., Bertino, L., Lisæter, K. A., Oke, P. R., and Korablev, A. TOPAZ4: an ocean-sea ice data assimilation system for the North Atlantic and Arctic. Ocean Science , 8(4), 2012. DOI: 10.5194/os-8-633-2012 .
- [376] Sakov, P., Oliver, D. S., and Bertino, L. An iterative EnKF for strongly nonlinear systems. Monthly Weather Review , 140:1988–2004, 2012. DOI: 10.1175/MWR-D-11-00176.1 .
- [377] Sarma, P. and Chen, W. H. Generalization of the ensemble Kalman filter using kernel for non Gaussian random fields. In Proceedings of the SPE Reservoir Simulation Symposium, The Woodlands, Texas, 2-4 February , number SPE-119177-MS, 2009. DOI: 10.2118/119177-MS .
- [378] Sarma, P., Durlofsky, L. J., and Aziz, K. Kernel principal component analysis for efficient differentiable parameterization of multipoint geostatistics. Mathematical Geosciences , 40(1):3–32, 2008. DOI: 10.1007/s11004-007-9131-7 .
- [379] Satija, A. and Caers, J. Direct forecasting of subsurface flow response from non-linear dynamic data by linear least-squares in canonical func-


- tional principal component space. Advances in Water Resources , 77: 69–81, 2015. DOI: 10.1016/j.advwatres.2015.01.002 .
- [380] Satija, A. and Caers, J. Direct forecasting of reservoir performance using production data without history matching. Computational Geosciences , 21(2):315–333, 2017. DOI: 10.1007/s10596-017-9614-7 .
- [381] Scheidt, C., Renard, P., and Caers, J. Prediction-focused subsurface modeling: Investigating the need for accuracy in flow-based inverse modeling. Mathematical Geosciences , 47(2):173–191, 2015. DOI: 10.1007/s11004-014-9521-6 .
- [382] Schneider, T., Stuart, A. M., and Wu, J.-L. Learning stochastic closures using ensemble Kalman inversion. Transactions of Mathematics and Its Applications , 5(1), 2021. DOI: 10.1093/imatrm/tnab003 .
- [383] Seabra, G. S. and Vossepoel, F. C. resmda. Software. URL https: //tuda-geo.github.io/resmda/ .
- [384] Seabra, G. S., de Hoop, S., Voskov, D., and Vossepoel, F. C. Understanding of naturally fractured geothermal reservoirs using data assimilation. In Proceedings of the 48th Workshop on Geothermal Reservoir Engineering, Stanford University, Stanford, California , 2023.
- [385] Seabra, G. S., Mücke, N. T., Silva, V. L. S., Voskov, D., and Vossepoel, F. C. AI enhanced data assimilation and uncertainty quantification applied to geological carbon storage. International Journal of Greenhouse Gas Control , 136, 2024. DOI: 10.1016/j.ijggc.2024.104190 .
- [386] Sebacher, B., Hanea, R., and Stordal, A. S. An adaptive plurigaussian simulation model for geological uncertainty quantification. Journal of Petroleum Science and Engineering , 158, 2017. DOI: 10.1016/j.petrol.2017.08.038 .
- [387] Sebacher, B. M., Hanea, R., and Heemink, A. A probabilistic parametrization for geological uncertainty estimation using the ensemble Kalman filter (EnKF). Computational Geosciences , 17(5):813–832, 2013. DOI: 10.1007/s10596-013-9357-z .
- [388] Sebacher, B. M., Stordal, A. S., and Hanea, R. Bridging multipoint statistics and truncated Gaussian fields for improved estimation of channelized reservoirs with ensemble methods. Computational Geosciences , 19(2):341–369, 2015. DOI: 10.1007/s10596-014-9466-3 .
- [389] Seiler, A., Aanonsen, S. I., Evensen, G., and Reivenæs, J. C. Structural uncertainty modeling and updating using the ensemble Kalman filter. SPE Journal , 15(4):1062–1076, 2010. DOI: 10.2118/125352-PA .
- [390] Shah, P. C., Gavalas, G. R., and Seinfeld, J. H. Error analysis in history matching: The optimum level of parameterization. SPE Journal , 18(6):219–228, 1978. DOI: 10.2118/6508-PA .
- [391] Shahkarami, A., Mohaghegh, S. D., Gholami, V., and Haghighat, S. A. Artificial intelligence (AI) assisted history matching. In Proceedings of the SPE Western North American and Rocky Mountain Joint Meeting, Denver, Colorado , number SPE-169507-MS, 2014. DOI: 10.2118/169507-MS .


- [392] Shariatinik, B., Gloaguen, E., Raymond, J., Boutin, L.-C., and FabienOuellet, G. ERT data assimilation to characterize aquifer hydraulic conductivity heterogeneity through a heat-tracing experiment. Near Surface Geophysics , 22(3), 2023. DOI: 10.1002/nsg.12288 .
- [393] Shirangi, M. G. History matching production data and uncertainty assessment with an efficient TSVD parameterization algorithm. Journal of Petroleum Science and Engineering , 113:54–71, 2013. DOI: 10.1016/j.petrol.2013.11.025 .
- [394] Shirangi, M. G. and Durlofsky, L. J. A general method to select representative models for decision making and optimization under uncertainty. Computers &amp; Geosciences , 96:109–123, 2016. DOI: 10.1016/j.cageo.2016.08.002 .
- [395] Shirangi, M. G. and Emerick, A. A. An improved TSVD-based Levenberg-Marquardt algorithm for history matching and comparison with Gauss-Newton. Journal of Petroleum Science and Engineering , 143:259–271, 2016. DOI: 10.1016/j.petrol.2016.02.026 .
- [396] Silva, T. M., Pesco, S., and Jr., A. B. Influences of the inflation factors generation in the main parameters of the ensemble smoother with multiple data assimilation. Journal of Petroleum Science and Engineering , 203, 2021. DOI: 10.1016/j.petrol.2021.108648 .
- [397] Silva, V. L. S., Cardoso, M. A., Oliveira, D. F. B., and de Moraes, R. J. Stochastic optimization strategies applied to the OLYMPUS benchmark. Computational Geosciences , 24, 2020. DOI: 10.1007/s10596019-09854-3 .
- [398] Skjaeveland, S. M., Siqveland, L. M., Kjosavik, A., Thomas, W. L. H., and Virnovsky, G. A. Capillary pressure correlation for mixed-wet reservoirs. SPE Reservoir Evaluation &amp; Engineering , 23(1), 2000. DOI: 10.2118/60900-PA .
- [399] Skjervheim, J.-A., Evensen, G., Aanonsen, S. I., Ruud, B. O., and Johansen, T.-A. Incorporating 4D seismic data in reservoir simulation models using ensemble Kalman filter. SPE Journal , 12(3):282–292, 2007. DOI: 10.2118/95789-PA .
- [400] Skjervheim, J.-A., Evensen, G., Hove, J., and Vabø, J. G. An ensemble smoother for assisted history matching. In Proceedings of the SPE Reservoir Simulation Symposium, The Woodlands, Texas, USA, 21–23 February , number SPE-141929-MS, 2011. DOI: 10.2118/141929-MS .
- [401] Skjervheim, J.-A., Heanea, R. G., and Evensen, G. Fast model update coupled to an ensemble based closed loop reservoir management. In Proceedings of the Petroleum Geostatistics, Biarritz, France, 7–11 September , 2015. DOI: 10.3997/2214-4609.201413629 .
- [402] Slowik, A. and Kwasnicka, H. Evolutionary algorithms and their applications to engineering problems. Neural Computing and Applications , 32, 2020. DOI: 10.1007/s00521-020-04832-8 .
- [403] Smola, A. J. and Schölkopf, B. A tutorial on support vector regression. Statistics and Computing , 14(3):199–222, 2004. DOI: 10.1023/B:STCO.0000035301.49549.88 .


- [404] Smolen, J. J. and Litsey, L. R. Formation evaluation using wireline formation tester pressure data. Journal of Petroleum Technology , 31, 1979. DOI: 10.2118/6822-PA .
- [405] Soares, R. V., Luo, X., Evensen, G., and Bhakta, T. Handling big models and big data sets in history-matching problems through an adaptive local analysis scheme. SPE Journal , 26(2), 2021. DOI: 10.2118/204221-PA .
- [406] Sobol’, I. M. Global sensitivity indices for nonlinear mathematical models and their Monte Carlo estimates. Mathematics and Computers in Simulation , 55(1-3), 2001. DOI: 10.1016/S0378-4754(00)00270-6 .
- [407] Soper, H. E. On the probable error of the correlation coefficient to a second approximation. Biometrika , 9(1/2), 1913. DOI: 10.2307/2331802 .
- [408] Sousa, E. P. S. and Reynolds, A. C. Adaptive least squares support vector regression for history matching and Markov chain Monte Carlo uncertainty quantification. TUPREP research report, The University of Tulsa, 2018.
- [409] Spall, J. C. Multivariate stochastic approximation using a simulataneous perturbation gradient approximation. IEEE Transactions on Automatic Control , 37(3):332–341, 1992. DOI: 10.1109/9.119632 .
- [410] Spall, J. C. Implementation of the simultaneous perturbation algorithm for stochastic optimization. IEEE Transactions on Aerospace and Electronic Systems , 34(3):817–823, 1998. DOI: 10.1109/7.705889 .
- [411] Spremić, M., Eidsvik, J., and Avseth, P. Bayesian rock-physics inversion using a localized ensemble-based approach – with an application to the alvheim field. Geophysics , 89(2), 2024. DOI: 10.1190/geo20220764.1 .
- [412] Srivastava, R. M. Handbook of Mathematical Geosciences: Fifty Years of IAMG , chapter The Origins of the Multiple-Point Statistics (MPS) Algorithm. Springer International Publishing, 2018. DOI: 10.1007/978-3-319-78999-6_32 .
- [413] Stordal, A. S. Iterative Bayesian inversion with Gaussian mixtures: finite sample implementation and large sample asymptotics. Computational Geosciences , 19(1):1–15, 2014. DOI: 10.1007/s10596-014-94449 .
- [414] Stordal, A. S. and Elsheikh, A. H. Iterative ensemble smoothers in the annealed importance sampling framework. Advances in Water Resources , 86:231–239, 2015. DOI: 10.1016/j.advwatres.2015.09.030 .
- [415] Stordal, A. S. and Lorentzen, R. J. An iterative version of the adaptive Gaussian mixture filter. Computational Geosciences , 18(3–4):579–595, 2014. DOI: 10.1007/s10596-014-9402-6 .
- [416] Stordal, A. S., Karlses, H. A., Nævedal, G., Skaug, H. J., and Vallés, B. Bridging the ensemble Kalman filter and particle filters: the adaptive Gaussian mixture filter. Computational Geosciences , 15(2):293–305, 2011. DOI: 10.1007/s10596-010-9207-1 .


- [417] Strebelle, S. Conditional simulation of complex geological structures using multiple-point statistics. Mathematical Geology , 34(1):1–21, 2002. DOI: 10.1023/A:1014009426274 .
- [418] Sun, L., Seidou, O., Nistor, I., and Liu, K. Review of the Kalman-type hydrological data assimilation. Hydrological Sciences Journal , 61(13), 2016. DOI: 10.1080/02626667.2015.1127376 .
- [419] Sun, W. and Durlofsky, L. J. A new data-space inversion procedure for efficient uncertainty quantification in subsurface flow problems. Mathematical Geosciences , 49:679–715, 2017. DOI: 10.1007/s11004016-9672-8 .
- [420] Sun, W. and Durlofsky, L. J. Data-space approaches for uncertainty quantification of CO 2 plume location in geological carbon storage. Advances in Water Resources , 123, 2019. DOI: 10.1016/j.advwatres.2018.10.028 .
- [421] Sun, W., Hui, M.-H., and Durlofsky, L. J. Production forecasting and uncertainty quantification for naturally fractured reservoirs using a new data-space inversion procedure. Computational Geosciences , Online, 2017. DOI: 10.1007/s10596-017-9633-4 .
- [422] Sun, W., Vink, J. C., and Gao, G. A practical method to mitigate spurious uncertainty reduction in history matching workflows with imperfect reservoir models. In Proceedings of the SPE Reservoir Simulation Conference, Montgomery, Texas, USA, 20-22 February , number SPE-182599-MS, 2017. DOI: 10.2118/182599-MS .
- [423] Suykens, J. A. K. and Vandewalle, J. Least squares support vector machine classifiers. Neural Processing Letters , 9(3):293–300, 1999. DOI: 10.1023/A:1018628609742 .
- [424] Sylvester, Z., Pirmez, C., and Cantelli, A. A model of submarine channel-levee evolution based on channel trajectories: Implications for stratigraphic architecture. Marine and Petroleum Geology , 28(3), 2011. DOI: 10.1016/j.marpetgeo.2010.05.012 .
- [425] Szunyogh, I., Kostelich, E. J., Gyarmati, G., Patil, D. J., Hunt, B. R., Kalnay, E., Ott, E., and Yorke, J. A. Assessing a local ensemble Kalman filter: perfect model experiments with the national centers for environmental prediction global model. Tellus A , 57:528–545, 2005. DOI: 10.1111/j.1600-0870.2005.00136.x .
- [426] Tang, H., Fu, P., Sherman, C. S., Zhang, J., Ju, X., ois Hamon, F., Azzolina, N. A., Burton-Kelly, M., and Morris, J. P. A deep learningaccelerated data assimilation and forecasting workfow for commercialscale geologic carbon storage. International Journal of Greenhouse Gas Control , 112, 2021. DOI: 10.1016/j.ijggc.2021.103488 .
- [427] Tang, M., Liu, Y., and Durlofsky, L. J. A deep-learningbased surrogate model for data assimilation in dynamic subsurface flow problems. Journal of Computational Physics , 413, 2020. DOI: 10.1016/j.jcp.2020.109456 .


- [428] Tarantola, A. Inverse Problem Theory and Methods for Model Parameter Estimation . SIAM, Philadelphia, USA, 2005. ISBN 9780898715729.
- [429] Tavakoli, R. and Reynolds, A. C. History matching with parameterization based on the SVD of a dimensionless sensitivity matrix. SPE Journal , 15(12):495–508, 2010. DOI: 10.2118/118952-PA .
- [430] Tavakoli, R. and Reynolds, A. C. Monte Carlo simulation of permeability fields and reservoir performance predictions with SVD parameterization in RML compared with EnKF. Computational Geosciences , 15(1):99–116, 2011. DOI: 10.1007/s10596-010-9200-8 .
- [431] Tavakoli, R., Yoon, H., Delshad, M., ElSheikh, A. H., Wheeler, M. F., and Arnold, B. W. Comparison of ensemble filtering algorithms and null-space monte carlo for parameter estimation and uncertainty quantification using CO 2 sequestration data. Water Resources Research , 49(12), 2013. DOI: 10.1002/2013WR013959 .
- [432] Tavakoli, R., Srinivasan, S., and Wheeler, M. F. Rapid updating of stochastic models by use of an ensemble-filter approach. SPE Journal , 19(3):500–513, 2014. DOI: 10.2118/163673-PA .
- [433] Tavassoli, Z., Carter, J. N., and King, P. R. An analysis of history matching errors. Computational Geosciences , 9, 2005. DOI: 10.1007/s10596-005-9001-7 .
- [434] Tetteh, M., Li, L., and Davis, A. Leveraging deep learning with progressive growing GAN and ensemble smoother with multiple data assimilation for inverse modeling. Advances in Water Resources , 187, 2024. DOI: 10.1016/j.advwatres.2024.104680 .
- [435] Thulin, K., Li, G., Aanonsen, S. I., and Reynolds, A. C. Estimation of initial fluid contacts by assimilation of production data with EnKF. In Proceedings of the SPE Annual Technical Conference and Exhibition, Anaheim, California, 11–14 November , number SPE-109975-MS, 2007. DOI: 10.2118/109975-MS .
- [436] Thurin, J., Brossier, R., and Métivier, L. Ensemble-based uncertainty estimation in full waveform inversion. Geophysical Journal International , 219, 2019. DOI: 10.1093/gji/ggz384 .
- [437] Tian, X., Volkov, O., and Voskov, D. An advanced inverse modeling framework for efficient and flexible adjoint-based history matching of geothermal fields. Geothermics , 116, 2024. DOI: 10.1016/j.geothermics.2023.102849 .
- [438] Tillier, E., Veiga, S. D., and Derfoul, R. Appropriate formulation of the objective function for the history matching of seismic attributes. Computers &amp; Geosciences , 51, 2013. DOI: 10.1016/j.cageo.2012.07.031 .
- [439] Tippett, M. K., Anderson, J. L., Bishop, C. H., Hamill, T. M., and Whitaker, J. S. Ensemble square-root filters. Monthly Weather Review , 131:1485–1490, 2003. DOI: 10.1175/15200493(2003)131&lt;1485:ESRF&gt;2.0.CO;2 .
- [440] Todaro, V., D’Oria, M., Tanda, M. G., and Gómez-Hernández, J. J. genES-MDA: a generic open-source software package to solve inverse


- problems via the ensemble smoother with multiple data assimilation. Computers and Geosciences , 167, 2022. DOI: 10.1016/j.cageo.2022.105210 .
- [441] Tolstukhin, E., Lyngnes, B., and Sudan, H. H. Ekofisk 4D seismic – seismic history matching workflow. In Proceedings of the SPE Europec/EAGE Annual Conference, 4-7 June, Copenhagen, Denmark , number SPE-154347-MS, 2012. DOI: 10.2118/154347-MS .
- [442] Torczon, V. On the convergence of pattern search algorithms. SIAM Journal on Optimization , 7(1), 1997. DOI: 10.1137/S1052623493250780 .
- [443] Trani, M., Arts, R., and Leeuwenburgh, O. Seismic history matching of fluid fronts using the ensemble Kalman filter. SPE Journal , 18(1), 2012. DOI: 10.2118/163043-PA .
- [444] Tso, C.-H. M., Johnson, T. C., Song, X., Chen, X., Kuras, O., Wilkinson, P., Uhlemann, S., Chambers, J., and Binley, A. Integrated hydrogeophysical modelling and data assimilation for geoelectrical leak detection. Journal of Contaminant Hydrology , 234, 2020. DOI: 10.1016/j.jconhyd.2020.103679 .
- [445] Tversky, A. and Kahneman, D. Judgment under uncertainty: Heuristics and biases. Science , 185(4157):1124–1131, 1974. DOI: 10.1126/science.185.4157.1124 .
- [446] van Essen, G. M., Jimenez, E. A., Przybysz-Jarnut, J. P., Horesh, L., Douma, S. G., van den Hoek, P. J., Conn, A., and Mello, U. T. Adjoint-based history-matching of production and time-lapse seismic data. In Proceedings of the SPE Europec/EAGE Annual Conference, Copenhagen, Denmark , number SPE-154375-MS, 2012. DOI: 10.2118/154375-MS .
- [447] van Leeuwen, P. J. A consistent interpretation of the stochastic version of the ensemble Kalman filter. Quarterly Journal of the Royal Meteorological Society , 146(731):2815–2825, 2020. DOI: 10.1002/qj.3819 .
- [448] van Leeuwen, P. J. and Evensen, G. Data assimilation and inverse methods in terms of a probabilistic formulation. Monthly Weather Review , 124:2898–2913, 1996. DOI: 10.1175/15200493(1996)124&lt;2898:DAAIMI&gt;2.0.CO;2 .
- [449] Vasco, D. W., Yoon, S., and Datta-Gupta, A. Integrating dynamic data into high-resolution reservoir models using streamline-based analytic sensitivity coefficients. SPE Journal , 4(4):389–399, 1999. DOI: 10.2118/59253-PA .
- [450] Vink, J. C., Gao, G., and Chen, C. Bayesian style history matching: Another way to under-estimate forecast uncertainty? In Proceedings of the SPE Annual Technical Conference and Exhibition, Houston, 28-30 September , number SPE-175121-MS, 2015. DOI: 10.2118/175121-MS .
- [451] Virieux, J. and Operto, S. An overview of full-waveform inversion in exploration geophysics. Geophysics , 76(6), 2009. DOI: 10.1190/1.3238367 .


- [452] Vishny, D., Morzfeld, M., Gwirtz, K., Bach, E., Dunbar, O. R. A., and Hodyss, D. High-dimensional covariance estimation from a small number of samples. Journal of Advances in Modeling Earth Systems , 16(9), 2024. DOI: 10.1029/2024MS004417 .
- [453] Vo, H. X. and Durlofsky, L. J. A new differentiable parameterization based on principal component analysis for the low-dimensional representation of complex geological models. Mathematical Geosciences , 46 (7):775–813, 2014. DOI: 10.1007/s11004-014-9541-2 .
- [454] Vono, M., Dobigeon, N., and Chainais, P. High-dimensional Gaussian sampling: A review and a unifying approach based on a stochastic proximal point algorithm. SIAM Review , 64(1), 2022. DOI: 10.1137/20M1371026 .
- [455] Voskov, D., Saifullin, I., Novikov, A., Wapperom, M., Orozco, L., Seabra, G. S., Chen, Y., Khait, M., Lyu, X., Tian, X., de Hoop, S., and Palha, A. Open Delft advanced research terra simulator (open-DARTS). The Journal of Open Source Software , 9(99), 2024. DOI: 10.21105/joss.06737 .
- [456] Wackernagel, H. Multivariate Geostatistics: An Introduction with Applications . Springer Verlag, 3rd edition, 2003. DOI: 10.1007/978-3662-05294-5 .
- [457] Waggoner, J. R., Cominelli, A., and Seymour, R. H. Improved reservoir modeling with time-lapse seismic in a Gulf of Mexico gas condensate reservoir. In SPE Annual Technical Conference and Exhibition, San Antonio, Texas, 29 September–2 October , number SPE-77514-MS, 2002. DOI: 10.2118/77514-MS .
- [458] Wang, Y. and Kovscek, A. R. Streamline approach for history matching production data. SPE Journal , 5(4):353–362, 2000. DOI: 10.2118/58350-PA .
- [459] Wang, Y., Li, G., and Reynolds, A. C. Estimation of depths of fluid contacts by history matching using iterative ensemble-Kalman smoothers. SPE Journal , 15(2), 2010. DOI: 10.2118/119056-PA .
- [460] Watanabe, S., Han, J., Hetz, G., Datta-Gupta, A., King, M. J., and Vasco, D. W. Streamline-based time-lapse-seismic-data integration incorporating pressure and saturation effects. SPE Journal , 22(4), 2017. DOI: 10.2118/166395-PA .
- [461] Webb, S. J., Bayless, J. S., and Dunlop, K. N. B. Enabling the “big loop” – ensuring consistency of geological and reservoir simulation models. In Proceedings of the AAPG Annual Convention and Exhibition, Long Beach, California, April , 2007.
- [462] Wen, X.-H. and Gómez-Hernández, J. J. Upscaling hydraulic conductivities in heterogeneous media: An overview. Journal of Hydrology , 183. DOI: 10.1016/S0022-1694(96)80030-8 .
- [463] Whitaker, J. S. and Hamill, T. M. Ensemble data assimilation without perturbed observations. Monthly Weather Review , 130(7):1913–1924, 2002. DOI: 10.1175/1520-0493(2002)130&lt;1913:EDAWPO&gt;2.0.CO;2 .


- [464] Whitaker, J. S., Hamill, T. M., Wei, X., Song, Y., and Toth, Z. Ensemble data assimilation with the NCEP global forecast system. Monthly Weather Review , 136:463–482, 2008. DOI: 10.1175/2007MWR2018.1 .
- [465] White, J. T. A model-independent iterative ensemble smoother for efficient history-matching and uncertainty quantification in very high dimensions. Environmental Modelling and Software , 109, 2018. DOI: 10.1016/j.envsoft.2018.06.009 . URL https://github.com/ dwelter/pestpp .
- [466] Wu, H., Fu, P., Hawkins, A. J., Tang, H., and Morris, J. P. Predicting thermal performance of an enhanced geothermal system from tracer tests in a data assimilation framework. Water Resources Research , 57 (12), 2021. DOI: 10.1029/2021WR030987 .
- [467] Wu, Z., Reynolds, A. C., and Oliver, D. S. Conditioning geostatistical models to two-phase production data. SPE Journal , 3(2):142–155, 1999.
- [468] Xiao, C., Leeuwenburgh, O., Lin, H. X., and Heemink, A. Nonintrusive subdomain POD-TPWL for reservoir history matching. Computational Geosciences , 23, 2019. DOI: 10.1007/s10596-018-9803z .
- [469] Xiao, C., Zhang, S., Ma, X., Zhou, T., Hou, T., and Chen, F. Deep-learning-generalized data-space inversion and uncertainty quantification framework for accelerating geological CO 2 plume migration monitoring. Geoenergy Science and Engineering , 224, 2023. DOI: 10.1016/j.geoen.2023.211627 .
- [470] Xu, T. and Gómez-Hernández, J. J. Joint identification of contaminant source location, initial release time, and initial solute concentration in an aquifer via ensemble Kalman filtering. Water Resources Research , 52(8), 2016. DOI: 10.1002/2016WR019111 .
- [471] Xu, W., Tran, T. T., Srivastava, R. M., and Journel, A. G. Integrating seismic data in reservoir modeling: the collocated cokriging approach. In Proceedings of the SPE Annual Technical Conference and Exhibition , number SPE-24742-MS, 1992. DOI: 10.2118/24742-MS .
- [472] Yao, Y., Vehtari, A., Simpson, D., and Gelman, A. Using stacking to average Bayesian predictive distributions (with discussion). Bayesian Analysis , 13(3), 2018. DOI: 10.1214/17-BA1091 .
- [473] Yeh, W. W.-G. Review of parameter identification in groundwater hydrology: The inverse problem. Water Resources Research , 22(2): 95–108, 1986. DOI: 10.1029/WR022i002p00095 .
- [474] Yeung, Y.-H., Barajas-Solano, D. A., and Tartakovsky, A. M. Physics-informed machine learning method for large-scale data assimilation problems. Water Resources Research , 58(5), 2022. DOI: 10.1029/2021WR031023 .
- [475] Yin, Z., Feng, T., and MacBeth, C. Fast assimilation of frequently acquired 4D seismic data for reservoir history matching. Computers &amp; Geosciences , 128:30–40, 2019. DOI: 10.1016/j.cageo.2019.04.001 .


- [476] Zachariassen, E., Skjervheim, J.-A., Vabø, J. G., Lunt, I., Hove, J., and Evensen, G. Integrated work flow for model update using geophysical monitoring data. In Proceedings of the 73rd EAGE Conference &amp; Exhibition, Vienna, Austria, 23–26 May , 2011. DOI: 10.3997/22144609.20149329 .
- [477] Zemel, B. Tracers in the Oil Field . Elsevier, first edition, 1995. ISBN 978-0444541512.
- [478] Zhang, F., Reynolds, A. C., and Oliver, D. S. Evaluation of the reduction in uncertainty obtained by conditioning a 3D stochastic channel to multiwell pressure data. Mathematical Geology , 34(6):713–740, 2002. DOI: 10.1023/A:1019805310025 .
- [479] Zhang, F., Reynolds, A. C., and Oliver, D. S. The impact of upscaling errors on conditioning a stochastic channel to pressure data. SPE Journal , 8(1):13–21, 2003. DOI: 10.2118/83679-PA .
- [480] Zhang, J., Li, G. L. W., Wu, L., and Zeng, L. An iterative local updating ensemble smoother for estimation and uncertainty assessment of hydrologic model parameters with multimodal distributions. Water Resources Research , 54(3):1716–1733, 2018. DOI: 10.1002/2017WR020906 .
- [481] Zhang, X.-L., Michelén-Ströfer, C., and Xiao, H. Regularized ensemble Kalman methods for inverse problems. Journal of Computational Physics , 416, 2020. DOI: 10.1016/j.jcp.2020.109517 .
- [482] Zhang, Y. and Oliver, D. S. Improving the ensemble estimate of the Kalman gain by bootstrap sampling. Mathematical Geosciences , 42: 327–345, 2010. DOI: 10.1007/s11004-010-9267-8 .
- [483] Zhang, Y., Stordal, A. S., and Lorentzen, R. J. A natural Hessian approximation for ensemble based optimization. Computational Geosciences , 27, 2023. DOI: 10.1007/s10596-022-10185-z .
- [484] Zhao, Y., Reynolds, A. C., and Li, G. Generating facies maps by assimilating production data and seismic data with the ensemble Kalman filter. In Proceedings of the SPE Improved Oil Recovery Symposium, Tulsa, Oklahoma, 20–23 April , number SPE-113990-MS, 2008. DOI: 10.2118/113990-MS .
- [485] Zhou, H., Gómez-Hernández, J. J., Franssen, H.-J. H., and Li, L. An approach to handling non-gaussianity of parameters and state variables in ensemble Kalman filtering. Advances in Water Resources , 34 (7), 2011. DOI: 10.1016/j.advwatres.2011.04.014 .
- [486] Zhu, Y. and Zabaras, N. Bayesian deep convolutional encoderdecoder networks for surrogate modeling and uncertainty quantification. Journal of Computational Physics , 366, 2018. DOI: 10.1016/j.jcp.2018.04.018 .
- [487] Zubarev, D. I. Pros and cons of applying proxy-models as a substitute for full reservoir simulations. In Proceedings of the SPE Annual Technical Conference and Exhibition, New Orleans, Louisiana, 4–7 October , number SPE-124815-MS, 2009. DOI: 10.2118/124815-MS .


# Index

<table>
  <tr>
    &lt;th&gt;Symbols 4D (time-lapse) seismic 11, 24, 169, 172,</th>
    &lt;th&gt;cumulative density function 48, 100, 316 curse of dimensionality 52, 87, 233</th>
  </tr>
  <tr>
    &lt;td&gt;229, 252–254, 256, 270, 275, 345, 347</td>
    &lt;td&gt;D</td>
  </tr>
  <tr>
    &lt;td&gt;A</td>
    &lt;td&gt;Darcy’s law 6 data-error covariance 25, 31, 245, 254</td>
  </tr>
  <tr>
    &lt;td&gt;a posteriori 14 a priori 9 adjoint method 36, 72, 348</td>
    &lt;td&gt;data-mismatch objective function 269 data-space inversion 348</td>
  </tr>
  <tr>
    &lt;td&gt;annealed importance sampling 148 assisted history matching 22, 351</td>
    &lt;td&gt;design of experiments 79 deterministic ensemble Kalman filter</td>
  </tr>
  <tr>
    &lt;td&gt;B</td>
    &lt;td&gt;168, 340 deterministic ensemble smoother with multiple data assimilation 168</td>
  </tr>
  <tr>
    &lt;td&gt;batch-EnRML 342</td>
    &lt;td&gt;discrete cosine transform 100, 346 distance-based localization 200, 202,</td>
  </tr>
  <tr>
    &lt;td&gt;Bayes’ rule 14, 19, 26, 27, 39, 114, 115, 117, 120, 121, 147, 148, 329, 330 Bayesian estimator 114</td>
    &lt;td&gt;204 domain localization 214, 215, 344</td>
  </tr>
  <tr>
    &lt;td&gt;best guess approach 233 big-loop 101, 234</td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;Broyden-Fletcher-Goldfarb-Shanno 68, 69</td>
    &lt;td&gt;ensemble adjustment Kalman filter 340 ensemble Kalman filter 15, 103, 122,</td>
  </tr>
  <tr>
    &lt;td&gt;Brugge case 156, 177, 342, 349, 352 C</td>
    &lt;td&gt;133, 339 ensemble Kalman inversion 349</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;ensemble randomized maximum likelihood 16, 175, 341 ensemble smoother 16, 139, 342</td>
  </tr>
  <tr>
    &lt;td&gt;capillary pressure 237, 241 Cholesky decomposition 41–43, 169, 238, 301</td>
    &lt;td&gt;ensemble smoother with multiple data assimilation 140, 142, 342</td>
  </tr>
  <tr>
    &lt;td&gt;conjugate gradient method 64 cookie-cutter approach 237</td>
    &lt;td&gt;ensemble square root filter 137, 340 ensemble transform Kalman filter 340</td>
  </tr>
  <tr>
    &lt;td&gt;Corey model 239 correlation-based localization 209, 211, 344</td>
    &lt;td&gt;ensemble-based optimization 349 evolutionary algorithm 74 extended Kalman filter 121, 339</td>
  </tr>
  <tr>
    &lt;td&gt;cosine similarity 266 covariance inflation 194</td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;covariance localization 196, 215 covariance matrix adaptation evolution</td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;facies 10, 100, 237, 336, 342, 346 facies overlap coefficient 267 faults 241</td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;forward model 9, 20, 252</th>
    &lt;th&gt;35, 50, 71, 79, 183,</th>
    &lt;th&gt; </th>
    &lt;th&gt; </th>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;355</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;pseudo-optimal taper</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;238,</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;correlation function 200,</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;Gaspari-Cohn 204, 235, 345 Gauss-Newton 66, 175,</td>
    &lt;td&gt;341</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;generative adversarial</td>
    &lt;td&gt;network 347</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;347 73–75</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;genetic algorithm geological carbon storage geological reservoirs</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;geostatistics 11, 13, 258, 331, 333–335</td>
    &lt;td&gt;1, 2, 4, 10, 11 47, 169, 233, 235,</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;gradual deformation gradzone 99</td>
    &lt;td&gt;95, 348</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;grid parameters 234,</td>
    &lt;td&gt;237, 241</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;H</td>
    &lt;td&gt;345 nonlinear conjugate gradient 65, 67</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;341</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;half-iteration EnKF hard data 47, 235, 236, history matching 11,</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;I</td>
    &lt;td&gt;22, 351</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;importance sampling</td>
    &lt;td&gt;148, 233, 351</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;integrated workflows inverse problem 8</td>
    &lt;td&gt;234</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;iterative adaptive</td>
    &lt;td&gt;Gaussian mixture</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;342 ensemble</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;351</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;K</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;104, 112, 121 110, 114, 217</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;Kalman gain 107, Kalman gain localization 228, 230, 271, 282</td>
    &lt;td&gt;196, 199, 217,</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;component analysis</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;331, 334, 335</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;342 objective function 22, 27, 44, 175, 182</td>
    &lt;td&gt;normalized variance numerical weather 340</td>
    &lt;td&gt;31, 267 prediction 122, 137,</td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;sampling 80, 348</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;100, 346</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;level-set function Levenberg-Marquardt</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
</table>


<table>
  <tr>
    &lt;th&gt;observation ocean bottom optimal hard optimization optimization-based analysis</th>
    &lt;th&gt;coverage 261 nodes 275 threshold 225, 35, 51 principal 100</th>
    &lt;th&gt; </th>
    &lt;th&gt; </th>
    &lt;th&gt; </th>
    &lt;th&gt; </th>
  </tr>
  <tr>
    &lt;td&gt;P parametrization particle filter particle swarm</td>
    &lt;td&gt;92, 99, 101, 342 optimization</td>
    &lt;td&gt;231 73, 76, 348</td>
    &lt;td&gt; </td>
    &lt;td&gt;theorem analysis 213 data assimilation 341 Gaussian simulation</td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;correlation 89, 320, 321 1, 3, 4, 6, 7, 10, observations model 253, 254</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;petroelastic pilot-point 94 porosity 1, 4, posterior covariance 144, 170, prediction-focused pressure transient</td>
    &lt;td&gt;6, 10, 234, 236 30, 33, 189, 191, 267 analysis analysis</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;principal component prior covariance probability 35, 40, 43, 122, 123,</td>
    &lt;td&gt;analysis 26, 97, 177, density function 47, 49, 54, 96, 144, 147, 190,</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;328, 331, 332 maps 100, 346 mass function modeling 337 data 243 tools 257</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;production-logging proxy modeling PUNQ-S3 case Q quasi-Newton</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt;R randomized rank deficiency</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;187 Levenberg-Marquardt minimum-average-cost permeability 4, 6, 285 testers 257 models 287</td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
    &lt;td&gt; </td>
  </tr>
  <tr>
    &lt;td&gt; </td>
    &lt;td&gt;modeling 101, 337 197</td>
    &lt;td&gt; </td>
    &lt;td&gt;V variational variogram</td>
    &lt;td&gt; </td>
    &lt;td&gt;347 346</td>
  </tr>
</table>


# W Z

water-alternating-gas 256, 275 zonation 93

![](<ensemble_data_assimilation_e-book_version_images/imageFile63.png>)

![](<ensemble_data_assimilation_e-book_version_images/imageFile64.png>)

