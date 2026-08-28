![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile1.png>)

Check for updates

AGU

ADVANCING

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile2.png>)

EARTH AND

SPACE SCIENCES

# JGR Solid Earth

# RESEARCH ARTICLE

10.1029/2024JB030470

# Trans‐Conceptual Sampling: Bayesian Inference With Competing Assumptions

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile2.png>)

# Key Points:

• Bayesian sampling is extended to cases where the model dimension, type of model bases, noise statistics and forward physics may all vary

• Algorithms for Markov chain Monte Carlo sampling across models with differing conceptual assumptions are derived, and illustrated on real and synthetic data

• Trans‐conceptual inversion is shown to be a generalization of trans‐ dimensional inversion, and leads to samplers that may be automated

# Correspondence to:

M. Sambridge, Malcolm.Sambridge@anu.edu.au

# Citation:

Sambridge, M., Valentine, A. P., &amp; Hauser, J. (2025). Trans‐conceptual sampling: Bayesian inference with competing assumptions. Journal of Geophysical Research: Solid Earth , 130 , e2024JB030470. https://doi.org/10.1029/ 2024JB030470

Received 9 OCT 2024 Accepted 31 JUL 2025

# Author Contributions:

Conceptualization: Malcolm Sambridge, Andrew P. Valentine, Juerg Hauser Data curation: Juerg Hauser Formal analysis: Malcolm Sambridge, Andrew P. Valentine, Juerg Hauser Funding acquisition: Malcolm Sambridge Investigation: Malcolm Sambridge, Andrew P. Valentine, Juerg Hauser Methodology: Malcolm Sambridge, Andrew P. Valentine, Juerg Hauser Resources: Malcolm Sambridge, Andrew P. Valentine, Juerg Hauser Software: Malcolm Sambridge, Andrew P. Valentine, Juerg Hauser Validation: Malcolm Sambridge, Andrew P. Valentine, Juerg Hauser Visualization: Malcolm Sambridge Writing – original draft: Malcolm Sambridge

© 2025. The Author(s). This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

Malcolm Sambridge 1 , Andrew P. Valentine 2 , and Juerg Hauser 3

1 Research School of Earth Sciences, Australian National University, Canberra, ACT, Australia, 2 Department of Earth Sciences, Durham University, Durham, UK, 3 Mineral Resources, CSIRO, Acton, ACT, Australia

Abstract Trans‐dimensional Bayesian sampling has been applied to subsurface imaging and other inference problems across the Earth Sciences. A particular style of Markov chain Monte Carlo (McMC) method, known as reversible‐jump has been used almost universally in such studies. This algorithm allows sampling across variably dimensioned model parameterizations. However, for practical reasons, it is limited to cases where the number of free parameters differ in a regular sequence between alternate models, usually by addition or subtraction of a single variable. Furthermore, jumps between model dimensions rely on bespoke mathematical transformations, which are bespoke to each class of application. As a result, implementations are dependent on the choice of model parameterization employed. A framework for Trans‐conceptual Bayesian sampling, which is a generalization of trans‐dimensional sampling, is presented. Trans‐C Bayesian sampling allows exploration across a finite, but arbitrary, set of conceptual models, that is ones where the number of variables, the type of model basis function, nature of the forward problem, and assumptions on the measurement noise statistics, may all vary independently. The new framework avoids parameter transformations and thereby lends itself to development of automatic McMC algorithms, that is where the details of the sampler do not require knowledge of the parameterization. Algorithms implementing Bayesian conceptual model sampling are presented and illustrated with examples drawn from geophysics, using real and synthetic data. Comparison with reversible‐jump illustrates that trans‐C sampling produces statistically identical results for situations where the former is applicable, but also allows sampling in situations where trans‐D would be impractical to implement.

Plain Language Summary To learn about the Earth's interior one must use indirect observations collected at or above the surface. Geoscientists often proceed by either constructing models of the Earth that satisfy observation plus other criteria, or by generating an ensemble of plausible models. The sampling approach has become popular with the growth of computational resources. All results of such studies involve assumptions, for example about the type of Earth characteristics expected. For two decades sampling approaches have been employed that let the number of parameters be variable. However, other conceptual assumptions persist, for example on choice of mathematical representation, the type of data noise present, and the approximations concerning the physics involved. All results are then dependent on these choices, which may themselves be uncertain. Here a new approach is proposed which allows model sampling to be extended to any type of conceptual assumptions and their support tested against the data simultaneously. Versatile algorithms for implementing “Trans‐conceptual” Bayesian sampling are proposed and illustrated using real and synthetic data examples. Results show that trans‐C sampling is able to match results of current methods, but may also be applied to a much a wider class of problems which have not been tractable to date.

# 1. Introduction

Many physical systems are not amenable to direct observation. In the Earth Sciences, for example, most data sets are collected at, or above, the Earth's surface. They only provide indirect constraints on properties of interest, which are either at depth or in the past, and hence one must use some form of inference process to learn about the interior. The field of inverse theory, which was initially a somewhat esoteric area of mathematics, came to embody the set of principles, tools and computational methods that are routinely used to derive quantitative results from indirect observations. For many decades now, earth scientists have applied these ideas to situations where the relationship between measurements and the sought after Earth properties is complex, typically governed by a set of differential equations, or other physical or chemical systems.

AGU

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile4.png>)

ADVANCING EARTH

AND SPACE SCIENCES

# Journal of Geophysical Research: Solid Earth

Writing – review &amp; editing: Malcolm Sambridge, Andrew

P. Valentine, Juerg Hauser

Geophysicists have been particularly active in this endeavor, using methods of inverse theory (Parker, 1994 ; Tarantola, 2005 ; Valentine &amp; Sambridge, 2023 ) to place quantified constraints on properties of the subsurface from scales of meters to the whole Earth. Two styles of approach are common. In the first, one seeks an optimal mathematical model representing interior properties, that satisfies the available data and usually some other chosen criteria (Aster et al., 2018 ; Menke, 2018 ). In the second, a probabilistic setting is invoked, and one seeks many such models that characterize both the constraint placed on the Earth by the data and any pre‐conceptions again represented probabilistically (Mosegaard &amp; Sambridge, 2002 ; Mosegaard &amp; Tarantola, 1995 ). Both approaches have their merits and weaknesses and involve implicit assumptions. One common assumption is that the physical quantity of interest, within the Earth, may be represented at any location by a finite set of basis functions, with their number and mathematical form chosen in advance by the practitioner. An example would be assuming that the seismic wavespeed within the Earth varies only with depth and can also be adequately represented by a fixed number of layers, perhaps with variable thickness. Such assumptions are necessarily incorrect, but expedient. All inferences made from analysis of the data, are then dependent, or “conditional” on such assumptions, and it can become difficult to untangle the influence of the data from that of the assumptions on the conclusions drawn in any study.

Within the probabilistic framework for inference, the situation began to change with the work of Malinverno ( 2000 , 2002 ) who introduced some recent advances from the Bayesian statistics community into geophysics, enabling multiple sets of assumptions, each possibly involving a different number of unknowns, to be considered together. This was significant as it provided a formal procedure to let the data decide not only what values of the unknowns were supported, but also which sets of underlying assumptions were as well. Again this was all couched within a Bayesian probabilistic framework and led to what is known today as trans‐dimensional Bayesian inversion, or sampling. Practitioners then sought to sample Earth models of variable dimension, in a probabilistic manner, with each class of model representation being based on a differing set of assumptions. Trans‐D sampling, as it became known, has since enjoyed considerable popularity and been applied to a wide variety of inference problems across the geosciences and beyond (Bodin &amp; Sambridge, 2009 ; R. C. Brodie &amp; Sambridge, 2012 ; Bodin et al., 2012 ; Burdick &amp; Lekic, 2017 ; Charvin et al., 2009 ; Cipta et al., 2018 ; Dettmer et al., 2010 , 2012 , 2014 ; Gallagher, 2012 ; Gallagher et al., 2011 ; Gao &amp; Lekic, 2018 ; Ghalenoei et al., 2022 ; Guo et al., 2020 ; Hawkins &amp; Sambridge, 2015 ; Hawkins et al., 2017 ; Hopcroft et al., 2007 ; Jasra et al., 2006 ; Malinverno, 2002 ; Magrini et al., 2023 ; Marignier et al., 2023 ; Minsley, 2011 ; Piana Agostinetti et al., 2015 , 2021 ; Ray &amp; Key, 2012 , 2014 , 2018 ; Stephenson et al., 2006 ; Sambridge et al., 2006 ; Sambridge et al., 2013 ; Tomita et al., 2021 ).

Underpinning all this work is an approach developed by Green ( 1995 ), known as “reversible‐jump Markov chain Monte Carlo” (rj‐McMC). Implementing this depends on detailed knowledge of the relationships between the different model representations: how do we “translate” a model from one representation to another? This restricts the range of settings in which trans‐D sampling can realistically be employed, and application to each new class of problem typically necessitates bespoke analysis and software. Apart from being tedious and time‐consuming, this encourages reliance on straightforward, but unsophisticated, Monte Carlo strategies such as the Metropolis‐ Hastings algorithm. Thus, researchers are left unable to benefit from the vastly improved efficiency of modern techniques such as Hamiltonian McMC (Betancourt, 2017 ), imposing further limits on the scale of problem that can be reliably addressed.

In this paper, we present an alternative strategy to trans‐D sampling that does not rely on rj‐McMC. This builds on work by Carlin and Chib ( 1995 ), which (to our knowledge) has not previously been recognized within the geophysics community. In this framework, each set of conceptual assumptions (or “state”) is treated in isolation; we therefore describe it as a “trans‐conceptual” or “trans‐C” sampler, and it can be employed in a wide range of settings that are not amenable to rj‐McMC. Two states may differ in model dimension, in the class of basis function used, in the assumptions made about data noise, and even in the physical laws that underpin the data‐ model relationship.

To illustrate these concepts, Figure 1 shows a comparison of a fixed dimensional ensemble of Earth models, a trans‐dimensional one, and a trans‐conceptual ensemble, for a problem involving inference of earth properties, for example of seismic wavespeed. In the fixed‐D ensemble, the profile is represented by three layers, with layer thickness and property varying between members of the ensemble. The trans‐D ensemble also consists of layers with variable properties and thickness, but here the number of layers is also variable. The trans‐conceptual

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile5.png>)

ADVANCING EARTH

AND SPACE SCIENCES

$$
= p d | m ( k ) , I k ) p m ( k ) | I k ) p ( I k ) p ( d | I ) ( 8 )
$$

where p ( d | I ) = ∑ k p ( I k ) p ( d | I k ) , and p ( I k ) is the prior for the k th state, and we have made use of Bayes' theorem for the k th state,

$$
p ( I k | d ) = p ( d | I k ) p ( I k ) p ( d | I ) . ( 9 )
$$

In Equation 9 the ratio p ( d | I k ) p ( d | I ) is the relative evidence of the k ‐th state.

In a McMC context, sampling of Equation 6 can be tackled through generation of an ensemble of ( m ( k ) , I k ) pairs according to this distribution. The remainder of the paper is concerned with this problem. For completeness, we note that our prior on z becomes

$$
p ( z ) = ∑ K k = 1 p ( I k ) ∫ M ( k ) p z | m ( k ) , I k ) p m ( k ) | I k ) d m ( k ) ( 10 )
$$

where p ( I k ) represents our prior beliefs about the suitability of each state, and p ( m ( k ) | I k ) is the usual prior distribution for parameters within each state. In principle, these within ‐ state priors should be tuned so that p ( z ) accurately describes our beliefs; in practice, one inevitably chooses convenient within ‐ state priors and accepts an implicitly defined p ( z ) . Nevertheless, it is important to consider the compatibility—or otherwise—of the choices made across different states.

# 2.1. Reversible‐Jump McMC

One route forward lies in the reversible‐jump algorithm of Green ( 1995 ). This is a Markov chain where at each step a move is proposed, ( m ( k ) , I k ) → ( m ʹ ( k ʹ ) , I k ʹ ) . This may occur within‐state ( k = k ʹ ) or between ‐ state ( k ≠ k ʹ ) , and then accepted with probability α , according to the Metropolis‐Hastings‐Green (MHG) acceptance condition (Green, 1995 ; Hastings, 1970 ; Metropolis et al., 1953 )

$$
α = 1 ∧ { p d | mʹ ( k ʹ ) , I k ʹ ) p mʹ ( k ʹ ) | I k ʹ ) p ( I k ʹ ) q m ( k ) , I k | mʹ ( k ʹ ) , I k ʹ ) p ( d | m ( k ) , I k ) p ( m ( k ) | I k ) p ( I k ) q ( mʹ ( k ʹ ) , I k ʹ | m ( k ) , I k ) | J kk ʹ | } . ( 11 )
$$

Here q ( m ʹ ( k ʹ ) , I k ʹ | m ( k ) , I k ) is the probability for the proposed move ( m ( k ) , I k ) → ( m ʹ ( k ʹ ) , I k ʹ ) ; and | J kk ʹ | is the determinant of the Jacobian of the transformation between the two states. If k = k ʹ then | J kk ʹ | = 1.

By accepting moves randomly with probability α the Markov chain satisfies what is known as detailed balance, and will asymptotically converge to the desired target distribution (Equation 8 ). However, it can only be employed in situations where we can write down an expression for the transformation between states, and hence compute the Jacobian. This is a severe limitation, and in practice usually restricts the use of rj‐McMC to situations where the various states I 1 ⋯ K all share the same core theoretical assumptions, and differ only in the number of model parameters that are free to vary. This has become known as “trans‐dimensional inference,” and in this context rj‐McMC has been applied extensively within the geosciences over the past two decades, as noted above.

The efficiency of any McMC algorithm is usually characterized by the average acceptance rate for proposed moves, ¯ α . Much effort has been devoted to designing proposal distributions, q , that maximize this quantity and enable efficient sampling of the target PDF for particular classes of problems (Brooks et al., 2011 ). In the reversible‐jump algorithm moves must also be performed between models in different states ( k ≠ k ʹ ) , which creates additional complexities. As with the Jacobian calculation, this tends to be problem dependent, and can be quite complex to implement. For this reason, authors typically further limit transitions to a restricted set of model states, where a single model parameter is added or subtracted, within the same basis class. An example might be a regression problem where the model parameters are coefficients of a polynomial with each state increasing in

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile6.png>)

ADVANCING EARTH

AND SPACE SCIENCES

Moreover, fixed‐dimensional (i.e., within ‐ state , k = k ʹ ) McMC sampling has been the subject of a large body of research for more than three decades (see Brooks et al., 2011 ; Hanada &amp; Matsuura, 2022 , for a summary of some advances), and a number of these more advanced sampling algorithms have also been translated into generic user‐ friendly software packages that are available via modern code sharing platforms. However, due to the bespoke nature of reversible‐jump implementations, it is often not convenient—perhaps not even possible—to employ these techniques. As a result reversible‐jump implementations generally rely upon simple algorithms such as Metropolis‐Hastings or Gibbs samplers, which have often been found to be very inefficient compared to state‐of‐ the‐art methods.

# 2.2. The Product Space Formulation

About the same time as the reversible‐jump algorithm appeared, Carlin and Chib ( 1995 ) proposed an alternative approach for sampling Equation 8 . Their idea was to combine one realization from each state, m ( k ) , into a single model vector, m , with dimension N = ∑ K k = 1 N k , where N k is the number of dimensions of parameter space k . This exists within a “product” space M = M ( 1 ) × M ( 2 ) × ⋯ × M ( K ) , and is merely a concatenation of the model vectors from the individual states,

$$
m = ⎛ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎝ m ( 1 ) m ( 2 ) ⋮ m ( K ) ⎞ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎠ . ( 12 )
$$

Carlin and Chib ( 1995 ) then proposed to construct the following probability density function defined in an (N + 1)‐dimensional space (comprising the product space, and a state index k ):

$$
π ( m , k | d , I ) = p d | m ( k ) , I k ) p m ( k ) | I k ) p ( I k ) ϕ ( m ) ϕk ( m ( k ) ) . ( 13 )
$$

Here ϕ ( m ) ≡ Π K k = 1 ϕ k ( m ( k ) ) , and ϕ k ( m ( k ) ) is a quantity that we will refer to as the pseudo‐prior for the k th state. We will discuss these pseudo‐priors in more detail below; for present purposes, they can be regarded as arbitrary —but normalized—PDFs, such that

$$
∫ M ( k ) ϕk m ( k ) ) d m ( k ) = 1, k = 1… K . ( 14 )
$$

The first three terms of Equation 13 are the Likelihood times the priors for the k th state, as in Equation 8 ; the ratio ϕ ( m ) / ϕ k ( m ( k ) ) ≡ ∏ j ≠ k ϕ j ( m ( j ) ) represents the pseudo‐priors for the remaining K − 1 states. Figure 2 shows an illustration of how the product space PDF, π ( m , k | d , I ) , varies with state indicator k . The state vectors, m ( j ) , in the pink boxes along the diagonal are referred to as “active” because they correspond to j = k , whereas those in the gray boxes are labeled “inactive” because j ≠ k . It will be convenient to introduce a “state selection operator,” S i , which extracts the part of m corresponding to state i , such that S i ( m ) = m ( i ) .

Given π is an unnormalized PDF in a fixed dimension space, it is straightforward to generate samples from it (i.e., an ensemble of ( m , k ) pairs), using any McMC algorithm. If we assume we have such an ensemble, then two key

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile7.png>)

ADVANCING EARTH

AND SPACE SCIENCES

# Journal of Geophysical Research: Solid Earth

| |p(dfm(1) , 1) X p(m(1)| | |@4(m(4))| |
|---|---|---|---|---|---|
|2|(m(1))|p(m(2)) 1(2),2)|03 (m(3))|04(m(4))|05 (m(5)|
|3|(m(1) )|(m(2))|p(dlm ,3) p(m(3))|04 (m(4))|05 [ (m(5))|
|5|01 (m(1) )| | | | |


Figure 2. A schematic visualization of the product space for a problem with 5 states. Each row represents the components of π , in Equation 13 , for a value of the state indicator k shown in the first column. Each column represents the model space for a state. Boxes along the diagonal (pink) contain the unnormalized posterior times prior for each state, while the off diagonal boxes (gray) contain the relevant pseudo‐priors. π is given by the product of terms in each column for a given k value designated by the row. The blue outlined boxes illustrate the four terms involved in the Metropolis‐Hastings balance condition when a move from k = 1 to k ʹ = 3 is proposed.

properties of π are revealed. The first is seen by asking, “What distribution do the active state vectors m ( k ) follow?” By definition, the answer to this is found by computing the marginal of π over the inactive state vectors, m ( j ) , where j ≠ k :

$$
∫ ∫ ⋯ ∫ M ( j ) π ( m , k | d , I ) ∏ K j = 1 j ≠ k d m ( j ) = p d | m ( k ) , I k ) p m ( k ) | I k ) p ( I k ) ∏ K j = 1 j ≠ k ∫ M ( j ) ϕj m ( j ) ) d m ( j ) ( 15 )
$$

$$
= p d | m ( k ) , I k ) p m ( k ) | I k ) p ( I k ) ( 16 )
$$

where the second line follows directly from the normalization of the pseudo‐priors (Equation 14 ). Since this is the same as the numerator in Equation 8 , it is clear that the active state model vectors follow the posterior PDF of their state. That is samples in each of the pink boxes along the diagonal of Figure 2 follow their respective within‐state posteriors. The second key property of π is seen by asking, “In what proportion does a sampler of π visit the active states?” This is found by marginalizing π over the entire product space. Using Equation 16 and the definition of conditional probability, we obtain

$$
∫ M π ( m , k | d , I ) d m = ∫ M ( k ) p d | m ( k ) , I k ) p m ( k ) | I k ) p ( I k ) d m ( k ) ( 17 )
$$

$$
= p ( d | I k ) p ( I k ) ( 18 )
$$

$$
= p ( I k | d ) p ( d ) ( 19 )
$$

Hence the number of times a sampler of π visits each active state is proportional to p ( I k | d ) , that is the support that the data offers for that state. This is identical to how an rj‐McMC sampler would visit each state in a trans‐ dimensional problem.

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile8.png>)

ADVANCING EARTH

AND SPACE SCIENCES

Together, these two properties of π enable construction of samples distributed according to the trans‐state posterior. If one samples π to obtain an ensemble of ( m , k ) pairs, they may be straightforwardly converted into an ensemble of ( S k ( m ) , I k ) pairs—and then further transformed into an ensemble of samples z I k ( S k ( m ) ) distributed according to p ( z | d , I ) , as in Equation 1 . This ensemble can be used to answer questions about the target property, taking into account the range of possibilities encapsulated by the various states I 1 ⋯ I K . This has been achieved via Markov chain Monte Carlo sampling in a fixed‐dimensional space, which can be implemented using any convenient algorithm—including state‐of‐the‐art “black‐box” methods.

# 2.3. Sampling Over Conceptual States

Despite its simplicity, the product space sampling framework of Carlin and Chib ( 1995 ) has not been widely adopted, and indeed it seems to be largely unknown within the geophysical community. Presumably, one reason for this is that it requires sampling to be conducted in a much larger‐dimension space than would otherwise be necessary—and in this respect, the reversible‐jump algorithm of Green ( 1995 ) is more appealing. However, it turns out that this issue can be circumvented, and we suggest that Carlin and Chib's idea merits re‐examination. In what follows, we discuss three “flavors” of sampling algorithm that each allow sampling across conceptual model states, building on the theory developed above.

# 2.3.1. The Product‐Space Sampler

The first approach, which we call “the product‐space sampler,” is to implement exactly what has been described above: Markov chain Monte Carlo sampling of the un‐normalized ( N + 1 ) ‐dimensional PDF π ( m , k | d ) . As has already been highlighted, this is a standard sampling problem in a fixed‐dimension space, and it can be tackled using a wide range of techniques. In particular, one may employ one of the various black‐box sampling packages that are readily available: in the examples below, we use the Python package emcee (Foreman‐Mackey et al., 2013b ) which implements the Affine‐Invariant sampler of Goodman and Weare ( 2010 ), among others. As is the case with many generic software packages, one simply needs to provide a function that can compute the logarithm of π at any point ( m , k ) , which is straightforwardly given by

$$
log π ( m , k | d ) = log p d | m ( k ) , I k ) + log p m ( k ) | I k ) + log p ( I k ) + ∑ K j = 1 j ≠ k log ϕj m ( j ) ) . ( 20 )
$$

One small complication is that the state index, k , is an integer rather than a real variable. Strictly speaking, this requires an McMC algorithm that accommodates mixed integer and real‐variable inputs; for the examples below, we instead work with a real variable k r defined such that 1 ≤ k r &lt; K + 1, and map this to the integer below, k = ⌊ k r ⌋.

# 2.3.2. The State‐Jump Sampler

While the product‐space sampler is straightforward, the dimension of the product space grows rapidly with the number of states. This has both computational cost and memory implications, as convergence is required in large dimensional spaces. Potentially then the product‐space sampler will be impractical for large geophysical applications. In order to identify alternative strategies, we consider the MHG acceptance condition for a Markov chain exploring π , with a proposed step ( m , k ) → ( m ʹ , k ʹ ) .

$$
α = 1 ∧ { π ( m ʹ , k ʹ | d ) q ( m , k | m ʹ , k ʹ ) π ( m , k | d ) q ( m ʹ , k ʹ | m , k ) } ( 21 )
$$

$$
= 1 ∧ { p ( d | S k ʹ ( m ʹ ) , I k ʹ ) p ( d | Sk ( m ) , I k ) ⋅ p ( S k ʹ ( m ʹ ) | I k ʹ ) p ( Sk ( m ) | I k ) ⋅ p ( I k ʹ ) p ( I k ) ⋅ ϕ ( m ʹ ) ϕ ( m ) ⋅ ϕk ( Sk ( m )) ϕ k ʹ ( S k ʹ ( m ʹ )) ⋅ q ( m , k | m ʹ , k ʹ ) q ( m ʹ , k ʹ | m , k ) } ( 22 )
$$

We can now consider behavior in three special cases. If the proposed step involves a within ‐ state change only, that is k = k ʹ and S j ( m ʹ ) = S j ( m ) for all j ≠ k (so that only the active state vector is updated), we have

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile9.png>)

ADVANCING EARTH

AND SPACE SCIENCES

$$
α = 1 ∧ { p ( d | Sk ( m ʹ ) , I k ) p ( d | Sk ( m ) , I k ) ⋅ p ( Sk ( m ʹ ) | I k ) p ( Sk ( m ) | I k ) ⋅ q ( m | m ʹ ) q ( m ʹ | m ) } , ( 23 )
$$

$$
α = 1 ∧ { p d | mʹ ( k ) , I k ) p ( d | m ( k ) , I k ) ⋅ p mʹ ( k ) | I k ) p ( m ( k ) | I k ) ⋅ q m ( k ) | mʹ ( k ) ) q ( mʹ ( k ) | m ( k ) ) } ( 24 )
$$

which is simply the “standard” MHG condition used for implementing a Markov chain within a single state. In particular, it does not depend on the pseudo‐priors.

If, on the other hand, the proposed step involves an out ‐ of ‐ state change only, that is k ʹ = k and S k ( m ʹ ) = S k ( m ) (so that it is only the inactive states that are updated), we have

$$
α = 1 ∧ { ϕ ( m ʹ ) ϕ ( m ) ⋅ q ( m | m ʹ ) q ( m ʹ | m ) } . ( 25 )
$$

A sensible choice here would be to change only one inactive state per step, that is q ( m ʹ | m ) = q ( m ʹ ( j ) | m ( j ) ) . Since the composite pseudo function ϕ ( m ) is a product of independent pseudo prior PDFs, ϕ j , for each state, then this allows each inactive state to be considered independently. It follows that the acceptance condition for the j th inactive state is

$$
α = 1 ∧ { ϕj mʹ ( j ) ) ϕj ( m ( j ) ) ⋅ q m ( j ) | mʹ ( j ) ) q ( mʹ ( j ) | m ( j ) ) } , ( j ≠ k ) . ( 26 )
$$

so that inactive states are simply exploring the pseudo‐prior for their state. A further simplification occurs if we assume the pseudo‐prior function permits random sample generation, that is q ( m ʹ ( j ) | m ( j ) ) = ϕ j ( m ʹ ( j ) ) , and so α = 1 and, of course, then no McMC sampling is required over inactive states. This is the case in the examples below.

Finally, we can consider between‐state changes, where m ʹ = m but a different state becomes active, that is k ≠ k ʹ . In this case,

$$
α = 1 ∧ { p ( d | S k ʹ ( m ) , I k ʹ ) p ( d | Sk ( m ) , I k ) ⋅ p ( S k ʹ ( m ) | I k ʹ ) p ( Sk ( m ) | I k ) ⋅ p ( I k ʹ ) p ( I k ) ⋅ ϕk ( Sk ( m )) ϕ k ʹ ( S k ʹ ( m )) ⋅ q ( k | k ʹ ) q ( k ʹ | k ) } ( 27 )
$$

which reduces to

$$
α = 1 ∧ { p d | m ( k ʹ ) , I k ʹ ) p ( d | m ( k ) , I k ) ⋅ p m ( k ʹ ) | I k ʹ ) p ( m ( k ) | I k ) ⋅ p ( I k ʹ ) p ( I k ) ⋅ ϕk m ( k ) ) ϕ k ʹ ( m ( k ʹ ) ) ⋅ q ( k | k ʹ ) q ( k ʹ | k ) } ( 28 )
$$

It is instructive to compare this to the corresponding MHG acceptance condition for reversible‐jump (Equation 11 ). The Likelihood and prior ratios are identical between the two, but the proposal ratio between state vectors in Equation 11 has been replaced by a simple proposal ratio between state indicator variables in Equations 27 and 28 .

$$
q m ( k ) , I k | mʹ ( k ʹ ) , I k ʹ ) q ( mʹ ( k ʹ ) , I k ʹ | m ( k ) , I k ) ⇒ q ( k | k ʹ ) q ( k ʹ | k ) ( 29 )
$$

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile10.png>)

ADVANCING EARTH

AND SPACE SCIENCES

$$
| J kk ʹ | ⇒ ϕk m ( k ) ) ϕ k ʹ ( m ( k ʹ ) ) . ( 30 )
$$

Hence the two troublesome terms in the reversible‐jump acceptance criterion have been replaced with terms that do not require explicit knowledge of the details of the model parameterizations in either state. This is the key property which we argue makes the current framework attractive as an alternate to reversible‐jump, because it allows sampling to be performed across states of arbitrary character without the user having to worry about the details of the model parameterization in either state, proposal distributions, or the Jacobian.

A key property of the within‐state and out‐of‐state moves is that the acceptance ratios only depend upon the part of the model that is changing. Therefore, sampling algorithms can be built around these three classes of move that avoid the need to work directly in the product space. Instead—much as in the reversible‐jump algorithm—one has a set of K coupled random walk processes, of which only one needs to be updated at any one time. We will describe this class of sampler as a “state‐jump” sampler, to emphasize the connection to reversible‐jump. In cases where we have the ability to efficiently generate samples from the pseudo‐prior—for example, if it is chosen to be a multi‐ dimensional Gaussian—further simplification is possible. As noted above, instead of performing out ‐ of ‐ state sampling, we can simply generate a new out ‐ of ‐ state model vector each time a between ‐ state change is to be proposed. In this case, there is no need to even store the out ‐ of ‐ state model vectors, and the structure of the procedure becomes identical to that of reversible‐jump. Indeed, one could convert any existing reversible‐jump implementation into a state‐jump sampler by making the two substitutions shown in Equations 29 and 30 . Hence state‐jump sampling offers a “drop in” replacement of the MHG balance condition in reversible‐jump.

# 2.3.3. The Ensemble Resampler

Suppose that a posterior ensemble E ( k ) = { m ( k ) 1 ,…, m ( k ) E k } has been generated for each state individually, by sampling each fixed‐dimension posterior p ( m ( k ) | d , I k ) using any convenient McMC algorithm. We assume that the resulting Markov chains have been appropriately “thinned” (e.g., by their auto‐correlation time, see Goodman &amp; Weare, 2010 ), so that all samples can be treated as independent; and that values for the Likelihood, L ( k ) i = p ( d | m ( k ) i , I k ) , and prior, ρ ( k ) i = p ( m ( k ) i | I k ) were recorded for each sample during the sampling process. (As is usual with most McMC algorithms, we really only need to record the logs of these values).

We then fit some parametric model to each of the ensembles E ( k ) , such as a Gaussian mixture model or a normalizing flow, and adopt this as the pseudo‐prior. In principle, this could be used to implement a state‐jump sampler, but this would necessitate additional Likelihood evaluations. Alternatively, we can regard the ensembles E ( k ) —by construction—as offering a set of samples from the pseudo‐prior. We can therefore implement a discretized approximation to the state‐jump sampler, which we refer to as an “ensemble resampler.” Again, explicit out ‐ of ‐ state sampling is not required; when a between ‐ state move is proposed, we simply select a model i ʹ at random from the relevant ensemble and compute an acceptance probability

$$
α = 1 ∧ ⎧ ⎨ ⎩ L ( k ʹ ) i ʹ ρ ( k ʹ ) i ʹ L ( k ) i ρ ( k ) i ⋅ p ( I k ʹ ) p ( I k ) ⋅ ϕk ( m ( k ) i ) ϕ k ʹ ( m ( k ʹ ) i ʹ ) ⋅ q ( k | k ʹ ) q ( k ʹ | k ) ⎫ ⎬ ⎭ , ( 31 )
$$

where m ( k ) i denotes the i th model within the E ( k ) . A Markov chain for k would therefore consist of the following steps:

- 1. Select a state k for initial attention, and draw a state vector, m ( k ) i , at random from the k th ensemble. k ʹ q k ʹ k
- 2. Propose a new state using some distribution, ( | ) , which may be uniform. ( k ʹ )
- 3. Draw a state vector, m i ʹ , at random from the k ʹ th ensemble. 4. Accept k ʹ with probability α given by Equation 31 .


Accept k ʹ with probability α given by Equation 31.

5. Repeat from 2.

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile11.png>)

ADVANCING EARTH

AND SPACE SCIENCES

Since the ensemble resampler is a special case of the state‐jump sampler, it must visit each state in proportion to p ( k | d ) . As noted previously, a multi state ensemble is then easily created by drawing random state vectors (with replacement) from each ensemble in these proportions.

The reader will note that while values of Likelihood, prior and pseudo‐prior are required for all members of the ensembles (and in practice the logs of these quantities), the ensemble resampler involves no further Likelihood evaluations, and does not require the state vectors themselves. This may be convenient in situations where ensembles are large in number and high dimensional but where computer memory is limited, or cases where ensembles have been generated by a previous study and perhaps state vectors are no longer available. Like the product‐space sampler, the ensemble resampler may be used with any convenient McMC algorithm to pre‐ compute posterior ensembles, and as with both product‐space and state‐jump samplers, it does not require any transformations between model vectors in different states.

A further feature of the ensemble resampler is that while individual within ‐ state ensembles are each a comprehensive “solution” to the inverse problem within a given state, they also lend themselves to recycling. For example, if at some later time someone proposes yet another state, we just need to compute one more ensemble and can re‐run the inference with the already computed ensembles. In this way we let the data decide how well new states are supported relative to earlier states.

# 2.4. Choice of Pseudo Prior

The pseudo‐prior is a free choice, although its support must be equal to, or contain, that of the prior. Its primary role is to replace model vector transformations in the between‐state acceptance probability (Equation 27 ). A simple choice would be to use the prior, or some chosen distribution, for example a multi‐dimensional Gaussian in each state. These choices are illustrated in the examples below.

If we were able to use the normalized posterior as the pseudo‐prior, that is

$$
ϕk m ( k ) ) = p m ( k ) | d , I k ) = p d | m ( k ) , I k ) p m ( k ) | I k ) / p ( d | I k ) . ( 32 )
$$

we would find that (Equation 27 ) becomes

$$
α = 1 ∧ { p ( d | I k ʹ ) p ( d | I k ) ⋅ p ( I k ʹ ) p ( I k ) ⋅ q ( k | k ʹ ) q ( k ʹ | k ) } ( 33 )
$$

$$
= 1 ∧ { p ( I k ʹ | d ) p ( I k | d ) ⋅ q ( k | k ʹ ) q ( k ʹ | k ) } , ( 34 )
$$

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile12.png>)

ADVANCING EARTH

AND SPACE SCIENCES

Table 1 Feature Comparison of Reversible‐Jump With the Three Trans‐C Samplers

| |Reversible‐jump Product‐space|sampler State‐jump|sampler|Ensemble resampler|
|---|---|---|---|---|
|Problem solved Model space type|Trans‐D only Variable|Trans‐C Fixed|Trans‐C Variable|Trans‐C Fixed|
|Dimension N|i , ( i = 1,… , K ) 1|+ ∑ K i = 1 N i , N i , ( i|= 1,… , K )|1|
|Pseudo‐prior function|No Evaluate|density only Evaluate density|&amp; generate samples Evaluate|density for ensembles|
|Pre‐compute posterior samples|No Only|if used to build pseudo‐priors Only if used|to build pseudo‐priors|Yes|
|McMC details Typically|naive samplers &amp; Any 3rd|party Fixed‐D May embed|into existing rj‐McMC Any 3rd|party McMC plus 1D sampler|
|McMC details|MHG acceptance|McMC|software|Any 3rd party McMC plus 1D sampler|
|Jacobian calculation Est. state posterior|Yes Yes|No Yes|No Yes|No Yes|
|Caveats|Requires bespoke Large|space dimension Efficiency depends|on good choice of Dependent|on input posterior ensembles|
|Caveats|implementations|Large space dimension|pseudo‐prior|&amp; pseudo‐prior|


# 2.5. Recap of the Three Samplers

To recap, we have identified three types of McMC sampler, each of which performs trans‐C sampling across independently defined conceptual states, or if desired trans‐dimensional states, which are a special case. We have shown that they all follow from the product space formulation of Carlin and Chib ( 1995 ), and each may have advantages in different situations. A comparison of their requirements and properties is summarized in Table 1 .

The product‐space is quite convenient in that all trans‐D sampling is essentially “out‐sourced” to a fixed dimension sampler on the product space PDF, π , in Equation 13 . Its downside is that the dimension of the model space grows rapidly with number of states and length of the state vectors, thereby slowing convergence and increasing storage costs. The state‐jump sampler is a refinement of the product‐space which has structure, storage and compute demands similar to that of the reversible‐jump algorithm. It may be viewed as an alternate MHG acceptance condition to reversible‐jump that requires introduction of pseudo prior evaluations, but avoids problem‐specific transformations between model vectors in different states, as well as Jacobian calculations. The ensemble resampler is a special case of the state‐jump sampler, and the simplest of all, because it only involves sampling of a state indicator integer, pointing to existing posterior ensembles. It may be viewed as a form of “post‐ processing” following fixed dimension McMC sampling. In the next section we illustrate all three algorithms on problems ranging from sampling across multi‐dimensional Gaussians, to cases where both basis function class and forward modeling vary between states.

# 2.5.1. Laplace Integration

An alternative to the sampling based approaches introduced in this paper is direct calculation of the evidence within each state, p ( d | I k ) , via numerical integration. As is well known, this is equivalent to an integral over the model parameters in that state,

$$
p ( d | I k ) = ∫ M ( k ) p d | m ( k ) , I k ) p m ( k ) | I k ) d m ( k ) ( 35 )
$$

A trans‐C ensemble is then obtained by randomly choosing states in the ratio of the relative evidence multiplied by the prior for each state p ( d | I k ) p ( I k ) / p ( d | I ) , followed by drawing samples from the corresponding within‐ state posteriors. (See Sambridge et al., 2006 , for an example). A plethora of methods have been proposed for calculating integrals of the form Equation 35 . These include Importance Sampling (Brooks et al., 2011 ), Bayesian Model Averaging (Hoeting et al., 1998 ), Nested Sampling (Skilling, 2004 , 2006 ), and more recently the Learned Harmonic Mean estimator which has been developed in Cosmology (McEwen et al., 2021 ). Authors have applied these methods and many variants. For examples see Schöniger and Wöhling ( 2015 ) who compare nine such measures in use in Hydrology; Dettmer et al. ( 2010 ) who applied them to model selection in geoacoustics and Hauser et al. ( 2016 ) similarly in solid Earth geophysics. Each of these approaches are based on some underlying

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile13.png>)

ADVANCING EARTH

AND SPACE SCIENCES

A comprehensive comparison of integration based evidence estimators to the trans‐C samplers above is beyond the scope of this paper. However, for illustrative purposes, and where appropriate, in the examples below, we make use of Laplace integration as a comparator to Trans‐C. In this we follow (Raftery, 1996 ) and use their Equation 10.14 as an approximation to the evidence within each state

$$
p ( d | I k ) ≈ ( 2 π ) Nk / 2 | H | 1 / 2 p d | ˆ m ( k ) ) p ˆ m ( k ) ) , ( 36 )
$$

where H is the negative inverse Hessian of the log‐posterior PDF evaluated at its maximum, ˆ m ( k ) , which is often referred to as the MAP model.

# 3. Examples

We choose three examples to illustrate the trans‐C sampling. The first has three states with non‐consecutive dimensions, where no relationship exists between the variables of one state and another. This example provides an illustration of all three trans‐C samplers on a toy problem, where the performance of each can be compared to each other and known exact results. The second example involves real data in an Airborne EM Earth imaging. Here sampling is performed over 10 states, containing earth models with variable numbers of layers and thicknesses, as in the middle panel of Figure 1 . This is a trans‐dimensional sampling problem, which has previously been addressed with rj‐McMC, and so we are able to directly compare outcomes. The third example involves a synthetic 2D seismic tomography between boreholes, and is the most ambitious, in that it has 16 states with differing numbers of model parameters; differing basis function classes (one with local and one with global support); as well as two classes of forward model solvers. This example is not readily amenable to rj‐McMC, because transformations between model parameter coefficients with different bases would be unwieldily. In this case we show that the state‐jump and ensemble samplers are both able to identify the states containing the correct physics as well as the correct basis functions from limited data.

# 3.1. Example 1: Sampling Unnormalized Multi‐Dimensional Gaussians

The first (toy) example involves calculation of the normalization constant of three unnormalized Gaussians in 3, 5, and 10 dimensions respectively. We write these as

$$
f m ( k ) | I k ) = wk ( 2 π ) nk / 2 | Σ k | 1 / 2 exp { 1 2 m ( k ) ˆ m ( k ) ) T Σ 1 k m ( k ) ˆ m ( k ) )} , ( 37 )
$$

where ( w 1 , w 2 , w 3 ) take the values (0.56,0.3,0.14) respectively. Here there is no actual inverse problem, but the Equation 37 is akin to an unnormalized posterior, or prior, in each state with Gaussian shape. The task is then to find the normalization constants, w i , via trans‐C sampling and direct numerical integration. The three trans‐C algorithms, can be applied to the problem by replacing p ( d | m , I k ) p ( m | I k ) with f ( m ( k ) | I k ) in all expressions above. For a constant prior over states p ( I k ) = 1 / 3, ( k = 1,…,3 ) then all algorithms can be applied and we would expect to see the three states “visited” in proportion to w k , regardless of choices of the mean models ˆ m ( k ) and covariances, Σ k , ( k = 1,…,3 ) . While this problem is relatively simple and has an exactly known solution, it nevertheless provides a simple demonstration of convergence of all three samplers.

Figure 3 shows the results of applying all three trans‐C samplers. The same pseudo‐prior PDF was used in each case, and found by fitting a single component Gaussian mixture model to an ensemble of 32 × 10 3 model space samples constructed within each state using the McMC package emcee (Foreman‐Mackey et al., 2013b ).

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile14.png>)

ADVANCING EARTH

AND SPACE SCIENCES

Product-space sampler

State-jump sampler

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile15.png>)

1.0

1.0

0.8

0.8

1

0.6

0.6

0.4

0.4

0.2

0.2

0.0

0.0

log10 (chain step)

log10 (chain step)

Ensemble resampler

0.8

Ens resampler

State-jump

0.5

Product space

0.6

True

0.4

0.3

0.2

0.2

0.1

0.0

0.0

2

log1

State 1

State 2

State 3

10 (chain step)

Figure 3. Convergence of 32 chains of three trans‐C sampling algorithms applied to unnormalized Gaussian posteriors in 3, 5, and 10 dimensional parameter spaces. The y axis shows the relative number of times each walker visits each state. The upper left panel is for the product‐space sampler, the upper right panel the state‐jump sampler and the lower left panel for the ensemble resampler. Blue, yellow and green dots indicate the true normalization constants, w i for each state, respectively. The lower right panel shows a comparison of the estimated weights from each sampler with the truth.

# 3.1.1. Product‐Space Sampling

For the product‐space sampler we performed 10 5 steps for each of 64 chains in the 19 dimensional product space, and applied a thinning factor of 15 to the output, which produced the convergence plot show in Figure 3 (top left). The product‐space sampler also utilized the emcee package and achieved a healthy 28.6% acceptance rate with almost 70,000 successful state moves. Here the relative number of visits of the samplers to each state becomes the estimate of the normalizing constants w k . From the figure we see that the chains of this sampler have the largest spread of the three. Nevertheless the combined values of 0.554, 0.302, 0.144, for each state respectively, are accurate to two significant digits (see bottom right panel of Figure 3 ).

# 3.1.2. State‐Jump Sampling

For the state‐jump sampler we employed 32 chains in parallel, each for 10 5 steps. For within ‐ state steps, the model proposal distribution, q ( m ʹ | m ) , was an isotropic Gaussian, of the appropriate dimension, centered on the current model with standard deviation σ = 0 . 04 in all directions. For between‐state moves the proposed state was randomly chosen from the other two states, and a model generated using the pseudo‐prior for that state. This resulted in 58 . 7 % acceptance rate and 171,944 state moves. The chain convergence is shown in Figure 3 top right

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile16.png>)

ADVANCING EARTH

AND SPACE SCIENCES

# 3.1.3. Ensemble Sampling

For the ensemble resampler a simple one parameter integer McMC Metropolis algorithm was employed across 32 chains and run for 10 5 steps. Since this algorithm needs input posterior samples in each state, we generated these (again) with the emcee package using 32 chains and 5 × 10 4 steps. They were then thinned by sub‐sampling each chain using its integrated auto‐correlation time (see Goodman &amp; Weare, 2010 , for details of this calculation and further discussion). This resulted in ensembles with 79,996, 53,330, and 26,226 models in the 3, 5, and 10 dimensional states, respectively. The ensemble resampler had an acceptance rate of 58 . 1 % with 122,966 state moves. The chain convergence is shown in Figure 3 (bottom left panel), and is clearly the quickest of all three to converge. There also appears to be a healthy level of mixing resulting to w k estimates of 0.560, 0.300, and 0.140, which are accurate to within 3 significant figures.

# 3.1.4. Laplace Integration

To provide a comparison we also applied Laplace integration to directly estimate normalization coefficients, w i . Readers will note that since each integrand, f ( m ( k ) | I k ) , ( k = 1,…,3 ) are unnormalized Gaussians, then Laplace integration is exact to within the numerical error involved in estimating the Hessian of the target PDF Equation 37 . To be consistent with usual practice, H was estimated by numerical differentiation, even though it could be calculated exactly in this example. The evidence values recovered in this way were 0.560, 0.300, and 0.140 for the three states, which are effectively exact to machine precision.

# 3.1.5. Summary of Gaussian Example Results

All three trans‐C algorithms successfully sampled across these low dimensional independent states and recovered the correct relative normalization constant in each case. To give some indication of computational efficiency we report relative compute times of 1.0 for the product space‐sampler, 0.31 for the state‐jump sampler and 0.15 for the ensemble resampler, which itself was composed of 0.107 for the pre‐compute of “posteriors” in each ensemble and 0.046 for the across ensemble sampling for w k , ( k = 1,…,3 ) . Hence for this example, the state‐jump sampler was about 3 × faster than the product‐space, while the ensemble resampler 10 × faster. Note that all three samplers benefited from use of the pre‐sampling in fixed dimensions in constructions of pseudo‐priors. None of these calculations exploited parallelization. A key point to note here is that none of the trans‐C samplers, involve any proposals/jumps from models in one state to that of another. Hence no jump proposal, nor Jacobians, are required, as would be the case for reversible‐jump McMC. Indeed we have not had to specify any relationship whatsoever between the parameters of one state and that of another. In principle they could be control parameters of different classes of conceptual model, as in Figure 1 . Nevertheless successful sampling across these states has been performed.

# 3.2. Example 2: Trans‐D AEM Inversion—Comparison With Reversible‐Jump

Our second example is in the field of Airborne Electro‐Magnetic (AEM) inversion, and involves trans‐D sampling across 1‐D electrical resistivity models with variable numbers of layers. This problem has been previously studied by several authors using reversible‐jump McMC (R. C. Brodie &amp; Sambridge, 2012 ; Hawkins et al., 2017 ; Minsley, 2011 ). The aim here is to demonstrate that the ensemble resampler can be used to reproduce the same result as that obtained by a mature reversible‐jump implementation, and also illustrate how the ensemble resampler might be employed in practice with a real data set. The example is centered around the inversion of the inline and vertical component for a single fiducial (fiducial 4489.0 on flight line 1006601) of a TEMPEST (Lane et al., 2000 ) AEM survey that was acquired and inverted to characterize the regional groundwater system in the La Grange region to the south of Broome, Australia (Annetts et al., 2014 ; Paul et al., 2013 ).

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile17.png>)

ADVANCING EARTH

AND SPACE SCIENCES

The reversible‐jump algorithm, embodied in the public domain software package GA‐AEM (R. C. Brodie &amp; Richardson, 2015 ) was applied to this problem and serves as a comparison to the ensemble resampler. Using this software we also generated a posterior ensemble in each of the 10 fixed‐D states by setting the maximum and minimum number of layers to the same value. In each case, we ran a single Markov chain for 1 . 25 × 10 7 steps while retaining every 500th sample, giving 2 . 5 × 10 4 models in each ensemble. As noted previously, the ensemble resampler requires just the ensembles together with the log‐posterior probability density value for each model, and makes no further use of the forward model solver, or Likelihood evaluations.

To decide on a suitable pseudo‐prior function, we first inspected the input ensembles. Figure 4 shows a corner plot (Foreman‐Mackey, 2016 ) for the fifth ( k = 5 ) state, where the ensemble is projected onto every pair of depth and log‐conductivity parameters. In this example the prior PDF for all interface depths is a simple uniform density between 0 and 500 m. Similarly the prior for log‐conductivities in each layer is also a uniform density between bounds log 10 ( 0 . 001 ) and log 10 ( 5 . 0 ) log 10 S/m. In Figure 4 the (depth,log‐conductivity) parameters have been ordered by the layer boundary depth, so for example, depth 2 refers to the interface depth of the second shallowest layer which is always greater than depth 1 etc. This ordering influences the ensemble densities observed in Figure 4 , nevertheless it is clear that the distributions are far from Gaussian, even within the finite bounds for each parameter type. In these circumstances, the approach used in the previous example, that is of setting the pseudo‐ prior to a normalized Gaussian mixture model fit to the inputs ensembles, is inappropriate. In this case a simple and convenient normalized prior is a uniform distribution within bounds, that is we set the pseudo‐prior to the actual prior in each state, suitably normalized so that its integral within those bounds is unity. We have then

$$
ϕ m ( k ) ) = ( k 1 ) ! ( Δ Z ) k 1 ( Δ C ) k , ( k = 1,…10 ) , ( 38 )
$$

where Δ Z represents the depth range over which the interfaces are created (500 m), Δ C is the range in log‐ conductivities [ log 10 ( 0 . 001 ) ,log 10 ( 5 ) ] or [ − 3,0 . 69 ] log 10 S/m, and the factorial enters because there are ( k − 1 ) ! ways of ordering the interfaces. As an illustration, Figure 5 shows a corner plot of an ensemble of 10 5 random models generated from this pseudo‐prior for the fifth state. Comparison with Figure 4 shows that the samples provide reasonable coverage across the parameter space where the posterior densities are significant.

To find the posterior support for each of the 10 states we calculated the density of the pseudo‐prior for each model in the input ensembles and then supplied these together with those of the unnormalized posterior density to the ensemble resampler, which was run with 32 chains for 5 × 10 5 steps. The ensemble resampler had a respectable 21.6% acceptance rate and 827,623 state moves. Figure 6 shows the relative numbers of visits to each state by both the reversible‐jump and the ensemble resampler for both the prior and the posterior PDFs. Clearly they are close but not exact, which is likely due to sampling errors in both. With only samples and log‐posterior values for each state, there is no curvature information about a MAP model from which to estimate a Hessian for the Laplace estimator, and so we omit this calculation here.

A revealing comparison can be made by examining 1D density profiles recovered by trans‐D and trans‐C algorithms. These are shown as a depth versus resistivity plots in Figure 7 . Note resistivity, which is the inverse of conductivity, is used here so that results are comparable to earlier studies. For the reversible‐jump, a trans‐D ensemble is a direct output; for the ensemble resampler we randomly selected members of the posterior ensembles using the estimated posterior support for each state, p ( I k | d ) (Figure 6 ) as weights. Note that this fiducial is distant from the salt water intrusion and the main features may be interpreted as a resistivity jump below the shallow Cenozoic sediments and a transition at about 180 m between Broome sandstone and Jarlemai siltstone. These features dominate both posterior density plots. Inspection shows that the 5%, 50% and 95% credible intervals of the density plots are very close between figures, while the interface densities are also very similar. This verifies that the ensemble resampler has recovered virtually identical information as the reversible‐jump sampler.

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile18.png>)

ADVANCING EARTH

AND SPACE SCIENCES

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile3.png>)

200

4

400

100

480

240

~2.2

8

~2.8

8

8

~2.4

0

8

~2.4

8

8

2

40

0

100

~2.4

~2.5

~2.8

480

~2.2

240

200

cond 3

log

depth 1

depth 2

depth 3

depth 4

log cond 1

log cond 2

log cond 4

log cond 5

Figure 4. A corner density plot of posterior samples for the fifth model state with 4 layers and a half‐space, in the AEM example. This is one of 10 input ensembles used for the ensemble resampler. The first four parameters represent ordered interface depths and the remaining five represent the log‐conductivity in each layer. Both parameters classes exist within finite bounds and the posterior distributions within each state are far from Gaussian. Higher densities are indicated by darker shades, while samples in lower density areas are shown in purple. The diagonal shows 1D marginals.

# 3.3. Example 3: Sampling Conceptual Models in Seismic Tomography

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile20.png>)

ADVANCING EARTH

AND SPACE SCIENCES

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile4.png>)

400

;

100

;

;

g

;

8

400

100

100

100

100

400

400

depth 2

depth 3

depth 4

log cond 5

depth 1

log cond 1

log cond 2

log cond 4

cond 3

Figure 5. A corner density plot of random deviates generated according to the pseudo‐prior for the fifth state in the AEM example. Details same as in Figure 4 . The pseudo‐prior density is uniform within fixed bounds for depth variables, and uniform in log‐conductivity for other variables. The ordering of parameters by interface depth, creates a non uniform distribution in the plot, as seen in the first four columns and rows.

$$
s ( x , y ) = v 1 0 + ∑ nx 1 i = 0 ∑ ny 1 j = 0 s ij ψij ( x , y ) , ( 39 )
$$

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile22.png>)

ADVANCING EARTH

AND SPACE SCIENCES

# Journal of Geophysical Research: Solid Earth

0.200

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile23.png>)

Posterior

Prior

0.175

0.150

0.125

0.100

0.075

0.050

1

0.025

0.000

10

Number of layers

where the perturbation of the slowness field s ( x , y ) about the background v − 1 0 is a linear sum of basis functions, ψ ij ( x , y ) , with coefficients s ij , and v 0 = 2000m/s. Interchange between velocity and slowness fields is of course trivial, noting v ( x , y ) = s ( x , y ) − 1 . We choose four of the bases to have local support, consisting of a grid of n x × n y pixels with constant slowness s ij in the ij th pixel, and the remainder to have global support, consisting of products of n x × n y cosines across the 2D domain, given by

$$
ψij ( x , y ) = f i f j cos ( i π Lx x ) cos ( j π Ly y ) , ( i = 0,…, nx 1 ; j = 0,…, ny 1 ) ( 40 )
$$

where

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile24.png>)

Posterior

$$
f i = ⎧ ⎪ ⎪ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ 1 ̅̅̅̅ ̅ Lx √ if i = 0, ̅̅̅̅̅ 2 Lx √ otherwise, f j = ⎧ ⎪ ⎪ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ 1 ̅̅̅̅ ̅ Ly √ if j = 0, ̅̅̅̅̅ 2 Ly √ otherwise . ( 41 )
$$

0.175

Prior

0.150

0.125

0.100

1

Here L x = 20 m and L y = 30 m are the dimensions of the model region. In these experiments n x and n y take the values (4,5,6,7) and (6,8,9,10) respectively. We use labels PN and CN to identify each set of 2D basis functions, where N = n x × n y . The projection of the reference model (left panel of Figure 8 ) creates a “true” model within each bases, represented by a set of slowness coefficients s ij in Equation 39 . The middle and right panels of Figure 8 show these projected/true velocity models for the P70 and C70 bases respectively.

0.075

0.050

0.025

0.000

10

Number of layers

Figure 6. Prior and posterior distributions for the number of layers in 1D Earth models in the AEM inversion example. Upper panel shows results of the trans‐C ensemble resampler, while the lower panel is for trans‐D sampling with the reversible‐jump algorithm. The two sets of results are the same within sampling error.

First arrival seismic travel times are calculated for each of these, between 10 equi‐distant sources and receivers on either side of the region spanning 0– 20 m in x and 0–30 m in y . Raypaths and travel times are calculated using the Fast Marching method (Rawlinson &amp; Sambridge, 2004 ; Sethian &amp; Popo-

vici, 1999 ) with the seismic wavespeed model produced by B‐spline interpolation of a velocity field v ( x , y ) evaluated on a discrete grid. Here we use the implementation in the popular FMST software (de Kool et al., 2006 ; Rawlinson et al., 2008 ). Gaussian random noise was added to all travel times with standard deviation of 2.5% of the average travel time perturbation from the background velocity model. We therefore end up with multiple “ground truth” data sets, all of which are derived from the same physical scenario.

To add an additional feature to the experiments we consider two alternate classes of forward model based on different assumptions about the underlying physics. Specifically, for each type of basis function, we either kept rays fixed and straight between sources and receivers, that is no ray tracing, or updated via wavefront tracking for each new Likelihood evaluation. We distinguish these linear and nonlinear physics assumptions by appending an “L” or “N,” to the state label, that is P70‐L, P70‐N, where appropriate. This then doubles the number of states to 16. Examples of straight and wavefront tracked raypaths are shown in Figure 8 .

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile25.png>)

ADVANCING EARTH

AND SPACE SCIENCES

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile26.png>)

100

100

200

200

E

;

300

300

400

400

500

500

100

200

300

400

500

100

200

300

400

500

0

0

resistvity (02 m)

Figure 7. Results for the AEM inversion of a single fiducial for the La Grange data set. The left panel of each pair shows the density of resistivity profiles, while the right hand panel shows the density of the interface locations. The left pair of panels are based on 2 . 5 × 10 3 variably dimensioned profiles obtained using reversible‐jump. The right hand are the same plots for 10 5 models obtained by resampling the fixed dimension input ensembles using the posterior support values, p ( I k | d ) , ( k = 1,… ,10 ) , calculated by the ensemble resampler. Density percentiles are plotted at [5%, 50%, 95%] and in red, cyan and red respectively. Density shading is logarithmic with a minimum density cut off of 2%. The trans‐C sampler has reproduced the results of the rj‐mcmc sampler very well, however, the larger number of samples in the former creates smoother density plots.

Continuous reference model

2.5

7.5

10.0

12.5

15.0

17.5

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile5.png>)

P7O-L

25

15

15

2.5

17.5

12.5

20.0

5.0

0.0

10.0

15.0

20.0

0.0

2.5

5.0

C7O-N

2300

2200

2100

2000

m/s

1900

1800

1700

7.5

10.0

12.5

17.5

15.0

20.0

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile28.png>)

ADVANCING EARTH

AND SPACE SCIENCES

To continue, we define a Gaussian Likelihood and prior in the k th state as follows

$$
p d | m ( k ) ) = 1 ( 2 π ) n / 2 | Σ | 1 / 2 exp ( 1 2 d g m ( k ) )) T Σ 1 d g m ( k ) )) , ( 42 )
$$

and

$$
p m ( k ) ) = 1 ( 2 π ) N / 2 | Σ k | 1 / 2 exp ( 1 2 ̃ m ( k ) m ( k ) ) T Σ 1 k ̃ m ( k ) m ( k ) )) , ( 43 )
$$

where d is an n ‐vector of travel time data with noise covariance Σ, g ( m ( k ) ) are, as usual, the predicted data from the model, m ( k ) , and ( ̃ m ( k ) ,Σ k ) are the prior model and covariance in the k th state. In all experiments below the prior model covariance matrix, Σ k , is a discretzed approximation, in the appropriate basis, of a simple squared‐ exponential covariance function (cf. Tarantola and Nercessian ( 1984 ), or Equation 8b of Valentine and Sambridge ( 2020 )). Our prior corresponds to spatial correlation length 5.7 m and slowness standard deviation of 8 . 0 × 10 − 6 s/m for pixel coefficients and 1 . 4 × 10 − 4 s/m for cosine coefficients. These slowness standard deviations are up to 5 times the standard deviation of the true model coefficients (from background model) in each state, indicating that the prior is relatively weak. The prior model, ̃ m ( k ) , in each state is a reference background homogeneous model corresponding to 2,000 m/s.

Apart from demonstrating the versatility of the new framework, a second objective in this example is to see whether trans‐C sampling can detect which class of basis function the data were generated from, and also which assumptions about the physics are supported by the data. As described above, for each experiment, travel times were calculated in the Gaussian anomaly model (Figure 8 ) after projection onto one of the eight model bases, local and global. In all cases “true” travel times were calculated using the nonlinear physics forward model, that is wavefront tracking.

Here the product‐space sampler would need to operate in a 189 dimensional space, which requires about 400 separate McMC chains in the Affine‐Invariant sampler of Goodman and Weare ( 2010 ). To simplify matters, we restrict attention to the state‐jump and ensemble samplers for this example. For the ensemble resampler, posterior ensembles are required in each state. Again we use the emcee package to perform standard McMC sampling within each of the 16 independent states, using 150 chains in parallel and 10 4 steps per chain. Each chain was then thinned by its respective auto‐correlation time, to produce final ensembles containing varying numbers (2,000– 5,000) of independent velocity models. The ensemble generation process is then repeated for each data set used in the tests discussed below.

For both samplers the pseudo‐prior function is again constructed by fitting a single component Gaussian mixture model to the ensemble of posterior samples within each state. This gives a convenient normalized pseudo‐prior PDF for each data set, j , in each state, k , that is N ( μ k , j ,Σ k , j ) . For the ensemble resampler the log of the pseudo‐ prior PDF amplitude is pre‐computed for all models in all ensembles.

Figure 9 shows results of an initial experiment using the ensemble algorithm to sample a weighted prior across 8 parametrization states (4 model and 4 cosine). We create unnormalized priors by multiplying each PDF by a weight in the ratio (1,2,3,4) for both basis classes. This is essentially a repeat of the experiment in Section 3.1 in much higher dimensions. For a successful outcome we would expect each chain to visit the states in the same ratio. Clearly the 32 McMC chains seen in Figure 9 all settle down by about 10 4 steps and visit each state in the correct proportions, indicated by colored dots. Figure 10 shows results of the same experiment for both state‐jump and ensemble sampling, together with Laplace posterior support estimator results. Here the latter is again accurate since the priors are Gaussian but in much higher dimensions compared to the earlier example. McMC acceptances rates for the state‐jump sampler were 90% for within state moves and about 70% for between state moves, for both

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile29.png>)

ADVANCING EARTH

AND SPACE SCIENCES

0.30

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile6.png>)

0.25

0.20

P7O &amp; C70

8

P54 &amp; C54

0.10

P4O &amp; C40

0.05

P24 &amp; C24

0.00

103

100

101

104

102

Chain step

Figure 9. Convergence of the ensemble algorithm sampling the prior in the tomography example. The y axis shows the relative cumulative number of visits of each random walker to each state. Here all pixel and cosine states are included (P24 to P70 and C24 to C70) and prior weights have been set in the ratio (1,2,3,4) for both sets. Labels indicate the state pairs corresponding to the chains. The 32 McMC chains of length 10 5 steps are used to sample the multi‐state prior with imposed weights indicated by the colored dots. Convergence is observed in all cases.

Figure 11 shows results of both the state‐jump and ensemble samplers across 12 separate experiments, including the relevant Likelihood. In each case we sample across 8 selected states as indicated by the labels. In all experiments the red dot indicates the basis in which the data were actually calculated, and the correct forward model in the Likelihood function, that is the one where wavefront tracking was performed. The height of each histogram represents the percentage of visits of the samplers across individual states, after thinning by a factor of 15. The state‐jump sampler results are all based on 32 McMC chains each of 10 4 steps, while the ensemble resampler on 32 chains on 10 5 steps each. Chain acceptance rates varied between 5% and 70% for the state‐jump sampler for within state moves, and about 1% for between state moves. For the ensemble resampler acceptance rates between states was typically 1% or less. This would normally suggest poor mixing of the McMC sampler, and possibly “stuck chains,” however, in all tests the initial state of the 32 chains is randomly assigned and so chains have simply moved from their random initial state to a single, (correct) state early on and remained there, thereby giving an apparently low acceptance rate for between state moves. Given that the prior sampling showed excellent

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile31.png>)

20

Ens resampler

State-jump

15

Laplace

;

True

10

5

P24

C24

P4O

C40

P7O

C70

P54

C54

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile32.png>)

ADVANCING EARTH

AND SPACE SCIENCES

All pixel model bases

All cosine model bases

Mixed pixellcosine model bases

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile33.png>)

100

Ens resampler

State-jump

Laplace

100

;

100

100

L N

L N

L N

L N

L N

L N

N

N

L

L

L

L

C70

C54

C70

P24

P4O

P54

P7O

C24

C40

C54

P24

P4O

Figure 11. Results of 12 experiments sampling across pixel and cosine bases in the cross borehole tomography example. In each case the red dot indicates the state used to generate synthetic “data” (i.e., corresponding to correct basis functions and physics). In each experiment the state‐jump and ensemble samplers are used to sample across eight independent states consisting of all pixel bases (left panel); all cosine bases (middle panel) and a mixture of pixel and cosine bases (right panel). The height of the bar represents the relative number of visits of the sampler to each state. For algorithmic details see main text. In all cases the samplers quickly converge on the state containing true basis class and physics, and then spend virtually all of their time there. The Laplace integration produce consistent results in the first two experiments but erroneous ones when pixel and cosine bases are mixed.

Looking at the details of each histogram, one can see that in the first two panels, where sampling is performed between either pixel only, or cosine only states, both samplers have spent nearly all of the time in a single state corresponding to the one generated by the data. Hence the trans‐C samplers have correctly identified the correct combination of parameterization and forward model. In the third panel, where pixel and cosine states are mixed, both algorithms have again converged on the correct state, where the parameterization and forward model was used to generate the synthetic data. Note that in all cases the histogram mode lies in the nonlinear version of each state pair, there is some variation for the state‐jump results in the cosine states C54 and C70. Given the ensemble resampler has correctly recovered the truth in these cases, this would appear to be due to some lack of convergence of the state‐jump, which likely requires longer chains.

We also directly estimated evidence, and hence posterior support, in each state via Laplace integration, results of which are shown in vanilla in each plot. Here we evaluated Equation 36 with Hessians calculated in two ways. The first is with a standard matrix approximation based on the Likelihood and prior in Equation 42 and Equation 43 that is

$$
H = G T k Σ 1 Gk + Σ 1 k ) 1 , ( 44 )
$$

where G k is the Jacobian of the forward model with respect to the model parameters in the k th state, and all terms are evaluated at the MAP model in the respective state, that is found by maximization of log‐posterior. The second approximation of the Hessian was with finite difference estimators of the second derivative of the log‐posterior about the MAP model. This is in principle more accurate as it takes account the dependence of the Jacobian on the model parameters. Results were found to be virtually identical for the all pixel experiment in Figure 11 , after which the latter was abandoned due to the extreme computational cost of the Hessian evaluation, being a factor of 10 5 greater, due to many repeated uses of Fast Marching within the Likelihood function in the four nonlinear

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile34.png>)

ADVANCING EARTH

AND SPACE SCIENCES

Overall then, we see that both trans‐C samplers have been able to use each data set to identify the correct basis class and forward model. Moreover, this example demonstrates the versatility of the new sampling framework in successfully sampling across model states based on entirely different conceptual assumptions.

# 4. Discussion and Conclusions

A framework has been presented, which allows Bayesian sampling across independent model states, each based on different conceptual assumptions. The three related McMC algorithms described are automated in the sense that they avoid the need for bespoke transformations of model parameters between states. This in turn obviates the need for calculation of Jacobians, thereby allowing considerable flexibility in the definition of model states, while retaining convergence to posterior distributions conditional on the data. This is made possible through use of a normalized pseudo prior PDF in each state, which is a free choice, but one upon which efficiency of the sampling depends. In contrast, the highly popular reversible‐jump framework relies on model transformations between state vectors and hence Jacobians to achieve the same outcome. Since such quantities depend on the mathematical details of the model basis functions used in each state, reversible‐jump requires the practitioner to derive appropriate balance conditions for each new class of application, which is avoided in the trans‐C framework.

It may be argued that adoption of the new approach, substitutes one problem dependent feature, that is model transformations and Jacobian calculations, for another, which is choice of pseudo prior PDFs. This is true, and here only simple methods for building pseudo priors have been examined. An alternative might be to define a pseudo‐prior equal to the posterior PDF produced by a Tarantola and Valette style linearized inversion. Another, more sophisticated approach, might be to exploit Machine Learning algorithms for PDF estimation. A promising direction in this regard, which has yet to be explored, are Normalizing Flows (Rezende &amp; Mohamed, 2015 ).

Another potential criticism of the trans‐C framework is that in applications which involve a large number of states with consecutive numbers of unknowns, not uncommon in geophysical applications, one may have to perform posterior sampling in each state separately, which would involve considerable computational effort. With no advanced knowledge of how posterior states are supported by the data, one might reasonably distribute such work according to the prior over the states, p ( I k ) , which may be uniform. A convergent reversible‐jump algorithm, on the other hand, visits each state in proportion to its posterior support from the data, p ( I k | d ) , and so distributes computational effort where its actually needed from the inference perspective. We note here that the pre‐ computation of ensembles within each state is “embarrassingly parallel,” in that no communication is required between samplers and so it is trivial to do so using parallelization. In addition, the posterior, p ( I k | d ) , being a marginal of the product space PDF, π ( m , I k | d ) , is likely to be highly correlated with k . Hence one could imagine applying any of the new samplers over a limited number of states spanning the desired range of unknowns, thereby limiting costs, and using the shape of the estimated posterior support for states, p ( I k | d ) , to decide whether further states are worth exploring, for example to resolve finer detail in p ( I k | d ) as a function of k , or whether a simple interpolation would suffice.

While the new framework expands the class of problem definition, this says nothing about efficiency of the resulting samplers compared to say a “finely tuned” reversible‐jump implementation. We have not addressed this issue here, either from a theoretical, or practical perspective through examples, and so make no claims of comparable efficiency with respect to reversible‐jump. Our experiments suggest that, in terms of relative efficiency, the ensemble resampler will likely require the least computational cost, the state‐jump next and the product‐space the least efficient on average. However, this will depend on the application, and relative efficiencies may vary with choice of pseudo‐prior, complexity of posterior and cost of forward modeling. At the same time, we note that the overall efficiency of the ensemble and product‐space samplers will be determined by that of the chosen fixed dimensional McMC algorithms, which do most of the work. A potential advantage of the trans‐C samplers presented is that they can utilize virtually any modern McMC fixed dimension sampling algorithm, either to sample the product space, individual states, or as the basis of pseudo‐prior construction.

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile35.png>)

ADVANCING EARTH

AND SPACE SCIENCES

A novel feature of the new framework, is the complete flexibility allowed in definition of the model states, that is different basis functions, data noise assumptions, and/or forward model approximations can be incorporated separately or together, and the data's support for each evaluated. Previously, in inversion studies, questions of which basis class to use, or which type of noise statistics were appropriate etc, largely had to be resolved prior to inference, while acknowledging that flexible parameterizations have been used, say, to allow spatial variably length scales in an Earth property, a sampling context, for example (Bodin &amp; Sambridge, 2009 ). In any Bayesian sampling strategy, one would not normally expect that real data would “choose a winner” and concentrate all posterior weight in a single type of basis, as was observed in the synthetic Tomography example. In general there is no winner. Rather, posterior weight would be distributed across multiple parameterization classes, just as is the case for a Trans‐dimensional sampling problem. The main point here as that by combining a wider range of states based on different choices, information on Earth properties is improved because the inference process is less dependent on restrictive choices. This point was made by Dettmer et al. ( 2014 ) in the context of trans‐dimensional versus fixed dimensional finite fault inversion of seismic sources. The same ideas are inherent in Bayesian Model Averaging (Hoeting et al., 1998 ).

How the flexibility provided by trans‐C sampling might be exploited in the future is an open question, although one possibility is in situations where uncertainty exists in the physical form of forward models or representations, such as in inversion of high pressure experimental measurements of mantle minerals for equations of state (Kennett &amp; Jackson, 2009 ). Here, trans‐C would allow competing forms of the equations of state to be considered simultaneously and tested against the data for support.

Another might be in situations where two competing theories exist for a forward model. One which is approximate and computationally cheap, and an alternate which is more accurate but computationally expensive. Does it suffice to use the convenient simple theory, or must we use the complex one? In principle a trans‐C study could be performed to quantitatively assess what support a data set has for each theory, in any given experiment. This might justify future use of simple theories, or guide the need for more complex ones.

A third example, is in geophysical imaging, where user choices on model basis and regularization type can be influential on subsequent interpretations, and thereby render comparison of results between studies, based on different choices, problematic (Valentine &amp; Trampert, 2015 ). In all cases, separate states need only be constructed based on competing assumptions and trans‐C sampling will let the data decide. In this regard the new framework is only limited by the scope of competing theoretical assumptions that one might wish to consider in any particular problem. By expanding capability, in this way, trans‐C sampling can help reduce the influence of parameterization and other choices, and thereby lessen epistemic uncertainty in the inference process.

An important characteristic of all McMC samplers is how efficiently they move around within and between states, as measured by the acceptance rate of transitions. Details of acceptance rates were given in each of the examples presented and were reasonable in those cases. However, in general one might expect that as states differ significantly, for example in basis function type, then acceptance rates may decline. A powerful tool to improve acceptance rates in such cases is Parallel Tempering (PT) (Falcioni &amp; Deem, 1999 ; Geyer, 1991 ), which replaces a single chain sampling a target PDF with multiple chains each raised to a “temperature.” This feature facilitates transitions between Markov chains and increases acceptance rates for between ‐ state changes (see Sambridge, 2014 , for some examples). While PT has not been used in the present study, it may be an area for further study, for example in conjunction with the ensemble resampler, at least, as its use would not involve any further Likelihood evaluations and hence it could be employed with minimal computational cost.

We conclude by noting that the key insight of Carlin and Chib ( 1995 ) is to transform a multi‐state sampling problem to one of fixed dimension, which immediately leads to both the product‐space and state‐jump samplers. The ensemble resampler is a special case of the latter, which we argue has some attractive features for physics based forward models. It is in essence, posterior sampling within each state, followed by estimation of p ( I k | d ) with a simple integer Markov chain. Awareness of the product space framework seems very limited, and to our knowledge unknown in the geosciences. We have argued that there are several benefits of the trans‐C framework, not least of which is that the three McMC samplers discussed are each applicable to trans‐D problems, and represent an automatic alternative to reversible‐jump, in that parameter transformations between states are avoided. The flexibility afforded by the new framework also allows extension of across state Bayesian sampling to a much wider class of problem. This may be of particular benefit in geoscience applications where conceptual

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile36.png>)

ADVANCING EARTH

AND SPACE SCIENCES

assumptions are commonplace and to date there has been no comparable way to evaluate the data's support across such models. We hope that this will lead to new applications across the physical sciences.

# Data Availability Statement

Numerical experiments in this study were conducted using the open‐source software emcee as introduced by Foreman‐Mackey et al. ( 2013a ), for McMC posterior sampling in fixed dimensional spaces; Fast‐Marching software pyfm2d , used here is available at Hauser et al. ( 2025 ); Reversible‐jump McMC calculations on the La Grange data set were performed with software supplied by R. Brodie ( 2016 ). A Python library implementing the three trans‐C samplers with notebook examples is available at Sambridge et al. ( 2025 ), which includes the inline and vertical component for the single fiducial from the La Grange AEM survey analyzed in this study.

# Acknowledgments

This work received support from Australian Research Council Discovery Project DP200100053, and CSIRO's Deep Earth Imaging Future Science Platform. The authors have benefited from discussions with InLab team members Jiawen He, Fabrizio Magrini and Auggie Marignier on this work. Comments from two anonymous reviewers were helpful in refining earlier versions of this manuscript. Open access publishing facilitated by Australian National University, as part of the Wiley ‐ Australian National University agreement via the Council of Australian University Librarians.

# References

Annetts, D., Munday, T., Ibrahim, T., Calhill, K., &amp; Davis, A. (2014). The application of AEM to mapping the aquifer and groundwater characteristics of the La Grange groundwater area, WA: Milestone 1 report (Tech. Rep. No. EP145055). CSIRO . CSIRO. Parameter estimation and inverse problems

Aster, R., Borchers, B., &amp; Thurber, C. (2018). . Elsevier Science.

Betancourt, M. (2017). A conceptual introduction to Hamiltonian Monte Carlo. arXiv:1701.02434v1. Pattern recognition and machine learning

Bishop, C. (2006). . Springer.

Bodin, T., &amp; Sambridge, M. (2009). Seismic tomography with the reversible jump algorithm. Geophysical Journal International , 178 (3), 1411– 1436. https://doi.org/10.1111/j.1365‐246X.2009.04226.x

Bodin, T., Sambridge, M., Tkalčić, H., Arroucau, P., Gallagher, K., &amp; Rawlinson, N. (2012). Transdimensional inversion of receiver functions and surface wave dispersion. Journal of Geophysical Research , 178 (B2), B02301. https://doi.org/10.1029/2011JB008560 Zenodo

Brodie, R. (2016). GA‐AEM: Source code repository [Software]. . Retrieved from https://zenodo.org/records/15598056 ASEG‐PESA 24th

Brodie, R. C., &amp; Richardson, M. (2015). Open source software for 1D airborne electromagnetic inversion. In International Geophysics Conference and Exhibition, Extended Abstracts (Vol. 1, pp. 1–3). https://doi.org/10.1071/aseg2015ab197 ASEG 22nd International Geophysics

Brodie, R. C., &amp; Sambridge, M. (2012). Transdimensional Monte Carlo inversion of AEM data. In Conference and Exhibition, Extended Abstracts (Vol. 1, pp. 1–4). https://doi.org/10.1071/aseg2012ab095 Handbook of Markov chain Monte Carlo

Brooks, S., Gelman, A., Jones, G. L., &amp; Meng, X. E. (2011). . Chapman &amp; Hall/CRC.

Burdick, S., &amp; Lekic, V. (2017). Velocity variations and uncertainty from transdimensional p‐wave tomography of North America. Geophysical Journal International , 209 (2), 1337–1351. https://doi.org/10.1093/gji/ggx091 Journal of the Royal Statistical Society B 57

Carlin, B. P., &amp; Chib, S. (1995). Bayesian model choice via Markov chain Monte Carlo. , (3), 473–484. https://doi.org/10.1111/j.2517‐6161.1995.tb02042.x

Charvin, K., Gallagher, K., Hampson, G., &amp; Labourdette, R. (2009). A Bayesian approach to inverse modelling of stratigraphy, part 1: Method. Basin Research , 21 (1), 5–25. https://doi.org/10.1111/j.1365‐2117.2008.00369.x

Cipta, A., Cummins, P., Dettmer, J., Saygin, E., Irsyam, M., Rudyanto, A., &amp; Murjaya, J. (2018). Seismic velocity structure of the Jakarta Basin, Indonesia, using trans‐dimensional Bayesian inversion of horizontal‐to‐vertical spectral ratios. Geophysical Journal International , 215 (1), 431–449. https://doi.org/10.1093/gji/ggy289

de Kool, M., Rawlinson, N., &amp; Sambridge, M. (2006). A practical grid‐based method for tracking multiple refraction and reflection phases in three‐dimensional heterogeneous media. Geophysical Journal International , 167 (1), 253–270. https://doi.org/10.1111/j.1365‐246X.2006. 03078.x Bayesian methods for nonlinear classification and regression

Denison, D. G. T., Holmes, C., Mallick, B., &amp; Smith, A. F. M. (2002). . John Wiley &amp; Sons. Geophysical Journal Interna-

Dettmer, J., Benavente, R., Cummins, P. R., &amp; Sambridge, M. (2014). Trans‐dimensional finite‐fault inversion. tional , 199 (2), 735–751. https://doi.org/10.1093/gji/ggu280 Journal of the Acoustical Society of America 128

Dettmer, J., Dosso, S. E., &amp; Holland, C. (2010). Trans‐dimensional geoacoustic inversion. , (6), 3393–4005. https://doi.org/10.1121/1.3500674

Dettmer, J., Molnar, S., Steininger, G., Dosso, S. E., &amp; Cassidy, J. F. (2012). Trans‐dimensional inversion of microtremor array dispersion data with hierarchical autoregresive error models. Geophysical Journal International , 188 (2), 719–734. https://doi.org/10.1111/j.1365‐246x.2011. 05302.x

Dinh, L., Sohl‐Dickstein, J., &amp; Bengio, S. (2017). Density estimation using real NVP. arXiv. https://doi.org/10.48550/arXiv.1605.08803 Journal of Chemical Physics 110

Falcioni, M., &amp; Deem, M. W. (1999). A biased Monte Carlo scheme for zeolite structure solution. , (3), 1754– 1766. https://doi.org/10.1063/1.477812 Journal of Open Source Software 1

Foreman‐Mackey, D. (2016). corner.py: Scatterplot matrices in python. , (2), 24. https://doi.org/10.21105/joss. 00024

Foreman‐Mackey, D., Hogg, D. W., Lang, D., &amp; Goodman, J. (2013a). emcee [Software]. Retrieved from https://emcee.readthedocs.io/en/stable Publications of the Astronomical Society of

Foreman‐Mackey, D., Hogg, D. W., Lang, D., &amp; Goodman, J. (2013b). emcee: The MCMC hammer. the Pacific , 125 (925), 306–312. https://doi.org/10.1086/670067 Journal of Geophysical Research

Gallagher, K. (2012). Transdimensional inverse thermal history modelling for quantitative thermochronology. , 117 , B02408. https://doi.org/10.1029/2011JB008825

Gallagher, K., Bodin, T., Sambridge, M., Weiss, D., Kylander, M., &amp; Large, D. (2011). Inference of abrupt changes in noisy geochemical records using transdimensional changepoint models. Earth and Planetary Science Letters , 311 (1–2), 182–194. https://doi.org/10.1016/j.epsl.2011. 09.015

Gao, C., &amp; Lekic, V. (2018). Consequences of parametrization choices in surface wave inversion: Insights from transdimensional Bayesian methods. Geophysical Journal International , 215 , 1037–1063. https://doi.org/10.1093/gji/ggy310 Computing Science and Statistics: Proceedings of the 23rd Symposium on

Geyer, C. J. (1991). Markov chain Monte Carlo maximum likelihood. In the Interface (pp. 156–163). American Statistical Association.

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile37.png>)

ADVANCING EARTH

AND SPACE SCIENCES

Geyer, C. J., &amp; Møller, J. (1994). Simulation procedures and likelihood inference for spatial point processes. Scandinavian Journal of Statistics , 21 , 359–373.

Ghalenoei, E., Dettmer, J., Ali, M. Y., &amp; Kim, J. W. (2022). Trans‐dimensional gravity and magnetic joint inversion for 3‐D earth models. Geophysical Journal International , 230 (1), 363–376. https://doi.org/10.1093/gji/ggac083 Communications in Applied Mathematics and Computational

Goodman, J., &amp; Weare, J. (2010). Ensemble samplers with affine invariance. Science , 5 (1), 65–80. https://doi.org/10.2140/camcos.2010.5.65 Biometrika 82

Green, P. J. (1995). Reversible jump Markov chain Monte Carlo computation and Bayesian model determination. , (4), 711–732. https://doi.org/10.1093/biomet/82.4.711 Highly Structured

Green, P. J. (2003). Trans‐dimensional Markov chain Monte Carlo. In N. L. Green, P. J. Hjort, &amp; S. Richardson (Eds.), Stochastic Systems (pp. 179–198). O. U. P. Geophysical

Guo, P., Visser, G., &amp; Saygin, E. (2020). Bayesian trans‐dimensional full waveform inversion: Synthetic and field data application. Journal International , 222 (1), 610–627. https://doi.org/10.1093/gji/ggaa201 MCMC from scratch: A practical introduction to Markov Chain Monte Carlo

Hanada, M., &amp; Matsuura, S. (2022). . Springer Nature. Retrieved from https://books.google.com.au/books?id = VCow0AEACAAJ Towards automatic reversible jump Markov chain Monte Carlo (Unpublished doctoral dissertation)

Hastie, D. (2005). . Department of Mathematics, University of Bristol. Biometrika 57

Hastings, W. K. (1970). Monte Carlo sampling methods using Markov chain and their applications. , (1), 97–109. https://doi.org/10. 1093/biomet/57.1.97 Geophysics

Hauser, J., Gunning, J., &amp; Annetts, D. (2016). Probabilistic inversion of airborne electromagnetic data for basement conductors. , 81 (5), E389–E400. https://doi.org/10.1190/geo2016‐0128.1

Hauser, J., Sambridge, M., Marignier, A., Valentine, A. P., &amp; Rawlinson, N. (2025). pyfm2d: A python package for calculation of seismic wavefronts in 2D using fast marching version 1.0 [Software]. Zenodo . Retrieved from https://zenodo.org/records/15597985

Hawkins, R., Brodie, R. C., &amp; Sambridge, M. (2017). Trans‐dimensional Bayesian inversion of airborne electromagnetic data for 2D conductivity profiles. Exploration Geophysics , 49 (2), 134–147. https://doi.org/10.1071/EG1613 Geophysical Journal International 203

Hawkins, R., &amp; Sambridge, M. (2015). Geophysical imaging using trans‐dimensional trees. , (2), 972– 1000. https://doi.org/10.1093/gji/ggv326 Statistical Science 14

Hoeting, J. A., Madigan, D., Raftery, A. E., Volinsky, C. T., &amp; Hoeting, J. A. (1998). Bayesian model averaging. , (4), 77–83.

Hopcroft, P., Gallagher, K., &amp; Pain, C. (2007). Inference of past climate from borehole temperature data using Bayesian Reversible Jump Markov chain Monte Carlo. Geophysical Journal International , 171 (3), 1430–1439. https://doi.org/10.1111/j.1365‐246x.2007.03596.x

Jasra, A., Stephens, D., Gallagher, K., &amp; Holmes, C. (2006). Bayesian mixture modelling in geochemistry via Markov chain Monte Carlo. Mathematical Geology , 38 , 269–300. https://doi.org/10.1007/s11004‐005‐9109‐3

Kennett, B. L. N., &amp; Jackson, I. (2009). Optimal equations of state for mantle minerals from simultaneous non‐linear inversion of multiple datasets. Physics of the Earth and Planetary Interiors , 176 (1–2), 98–108. https://doi.org/10.1016/j.pepi.2009.04.005

Lane, R., Green, A., Golding, C., Owers, M., Pik, P., Plunkett, C., et al. (2000). An example of 3D conductivity mapping using the TEMPEST airborne electromagnetic system. Exploration Geophysics , 31 (2), 162–172. https://doi.org/10.1071/eg00162

Magrini, F., Kästle, E., Pilia, S., Rawlinson, N., &amp; De Siena, L. (2023). A new shear‐velocity model of continental Australia based on multi‐scale surface‐wave tomography. Journal of Geophysical Research: Solid Earth , 128 (7), e2023JB026688. https://doi.org/10.1029/2023JB026688 Geophysical Journal International 140

Malinverno, A. (2000). A Bayesian criterion for simplicity in inverse problem parametrization. , (2), 267– 285. https://doi.org/10.1046/j.1365‐246x.2000.00008.x Geophysical Journal

Malinverno, A. (2002). Parsimonious Bayesian Markov chain Monte Carlo inversion in a nonlinear geophysical problem. International , 151 (3), 675–688. https://doi.org/10.1046/j.1365‐246x.2002.01847.x The Open

Marignier, A., Kitching, T., McEwen, J. D., &amp; Ferreira, A. M. (2023). Sparse Bayesian mass‐mapping using trans‐dimensional MCMC. Journal of Astrophysics , 6 . https://doi.org/10.21105/astro.2211.13963

McEwen, J. D., Wallis, C. G. R., Price, M. A., &amp; Docherty, M. M. (2021). Machine learning assisted Bayesian model comparison: Learnt harmonic mean estimator. arXiv. https://doi.org/10.48550/ARXIV.2111.12720 Geophysical data analysis: Discrete inverse theory

Menke, W. (2018). . Elsevier Science.

Metropolis, N., Rosenbluth, M. N., Rosenbluth, A. W., Teller, A. H., &amp; Teller, E. (1953). Equation of state calculations by fast computing machines. Journal of Chemical Physics , 21 (6), 1087–1092. https://doi.org/10.1063/1.1699114

Minsley, B. J. (2011). A trans‐dimensional Bayesian Markov chain Monte Carlo algorithm for model assessment using frequency‐domain electromagnetic data. Geophysical Journal International , 187 (1), 252–272. https://doi.org/10.1111/j.1365‐246X.2011.05165.x Inverse Problems 18

Mosegaard, K., &amp; Sambridge, M. (2002). Monte Carlo analysis of inverse problems. , (3), R29–R54. https://doi.org/10.1088/ 0266‐5611/18/3/201 Journal of Geophysical Research 100

Mosegaard, K., &amp; Tarantola, A. (1995). Monte Carlo sampling of solutions to inverse problems. , (B7), 12431–12447. https://doi.org/10.1029/94jb03097 Geophysical inverse theory

Parker, R. L. (1994). . Princeton University Press. A review of the Broome sandstone

Paul, R., George, R. J., &amp; Gardiner, P. (2013). aquifer in the La Grange area (Tech. Rep. No. 387) . Department of Agriculture and Food.

Piana Agostinetti, N., Giacomuzzi, G., &amp; Malinverno, A. (2015). Local three‐dimensional earthquake tomography by trans‐dimensional Monte Carlo sampling. Geophysical Journal International , 201 (3), 1598–1617. https://doi.org/10.1093/gji/ggv084

Piana Agostinetti, N., Kotsi, M., &amp; Malcolm, A. (2021). Exploration of data space through trans‐dimensional sampling: A case study of 4D seismics. Journal of Geophysical Research: Solid Earth , 126 (12), e2021JB022343. https://doi.org/10.1029/2021JB022343 Markov chain Monte Carlo in practice

Raftery, A. E. (1996). Hypothesis testing and model selection. In . CRC Press. Markov chain Monte Carlo in practice

Raftery, A. E., &amp; Lewis, S. M. (1996). Implementing MCMC. In (pp. 115–130).

Rawlinson, N., Hauser, J., &amp; Sambridge, M. (2008). Seismic ray tracing and wavefront tracking in laterally heterogeneous media. Advances in Geophysics , 49 , 203–273. https://doi.org/10.1016/S0065‐2687(07)49003‐3

Rawlinson, N., &amp; Sambridge, M. (2004). Wavefront evolution in strongly heterogeneous layered media using the fast marching method. Geophysical Journal International , 156 (3), 631–647. https://doi.org/10.1111/j.1365‐246X.2004.02153.x

Ray, A., Kaplan, S., Washbourne, J., &amp; Albertin, U. (2018). Low frequency full waveform seismic inversion within a tree based Bayesian framework. Geophysical Journal International , 212 (1), 522–542. https://doi.org/10.1093/gji/ggx428 Geophysical Journal

Ray, A., &amp; Key (2012). Bayesian inversion of marine CSEM data with a trans‐dimensional self parametrizing algorithm. International , 191 (3), 1135–1151. https://doi.org/10.1111/j.1365‐246X.2012.05677.x

![](<Trans_Conceptual_Sampling_Bayesian_Inference_With_Competing_Assumptions_images/imageFile38.png>)

ADVANCING EARTH

AND SPACE SCIENCES

Ray, A., Key, K., Bodin, T., Myer, D., &amp; Constable, S. (2014). Bayesian inversion of marine CSEM data from the Scarborough gas field using a transdimensional 2‐D parametrization. Geophysical Journal International , 199 (3), 1847–1860. https://doi.org/10.1093/gji/ggu370 Proceedings of the 32nd In-

Rezende, D., &amp; Mohamed, S. (2015). Variational inference with normalizing flows. In F. Bach &amp; D. Blei (Eds.), ternational Conference on Machine Learning (Vol. 37, pp. 1530–1538). PMLR. Retrieved from https://proceedings.mlr.press/v37/rezende15. html Geophysical Journal Interna-

Sambridge, M. (2014). A parallel tempering algorithm for probabilistic sampling and multi‐modal optimization. tional , 196 (1), 357–374. https://doi.org/10.1093/gji/ggt342 Philosophical Transactions of the

Sambridge, M., Bodin, T., Gallagher, K., &amp; Tkalčić, H. (2013). Transdimensional inference in the geosciences. Royal Society of London, Series A: Physical Sciences and Engineering , 37 (1984), 20110547. https://doi.org/10.1098/rsta.2011.0547

Sambridge, M., Gallagher, K., Jackson, A., &amp; Rickwood, P. (2006). Trans‐dimensional inverse problems, model comparison and the evidence. Geophysical Journal International , 167 (2), 528–542. https://doi.org/10.1111/j.1365‐246x.2006.03155.x

Sambridge, M., Valentine, A. P., &amp; Hauser, J. (2025). pyTransC: A python package for trans‐conceptual Markov chain Monte Carlo sampling version 1.0 [Software]. Zenodo . Retrieved from https://zenodo.org/records/14854290

Schöniger, A., &amp; Wöhling, T. (2015). Finding the right balance between groundwater model complexity and experimental effort via Bayesian model selection. Journal of Hydrology , 531 , 96–110. https://doi.org/10.15496/publikation‐11850 Geophysics 64

Sethian, J. A., &amp; Popovici, A. M. (1999). 3‐D traveltime computation using the fast marching method. , (2), 516–523. https://doi.org/ 10.1190/1.1444558 Data analysis: A Bayesian tutorial

Sivia, D., &amp; Skilling, J. (2006). . OUP Oxford. Retrieved from https://books.google.com.au/books? id = lYMSDAAAQBAJ AIP Conference Proceedings 735

Skilling, J. (2004). Nested sampling. , (1), 395–405. https://doi.org/10.1063/1.1835238 Bayesian Analysis 1

Skilling, J. (2006). Nested sampling for general Bayesian computation. , (4), 833–860. https://doi.org/10.1214/06‐BA127

Stephenson, J., Gallagher, K., &amp; Holmes, C. C. (2006). Low temperature thermochronology and strategies for multiple samples 2: Partition Modelling for 2D/3D distributions with discontinuites. Earth and Planetary Science Letters , 241 (3–4), 557–570. https://doi.org/10.1016/j.epsl. 2005.11.027 Inverse problem theory and methods for model parameter estimation

Tarantola, A. (2005). . Siam. Geophysical

Tarantola, A., &amp; Nercessian, A. (1984). Three‐dimensional inversion without blocks. Journal of the Royal Astronomical Society , 76 (2), 299–306. https://doi.org/10.1111/j.1365‐246x.1984.tb05047.x Journal of

Tomita, F., Iinuma, T., Agata, R., &amp; Hori, T. (2021). Development of a trans‐dimensional fault slip inversion for geodetic data. Geophysical Research: Solid Earth , 126 (5), e2020JB020991. https://doi.org/10.1029/2020JB020991 RAS Techniques and In-

Turunçtur, B., Valentine, A., &amp; Sambridge, M. (2023). Overcomplete tomography: A novel approach to imaging. struments , 2 (1), 207–215. https://doi.org/10.1093/rasti/rzad010 Geophysical

Valentine, A. P., &amp; Sambridge, M. (2020). Gaussian process models I. A framework for probabilistic continuous inverse theory. Journal International , 220 (5), 1632–1647. https://doi.org/10.1093/gji/ggz520

Valentine, A. P., &amp; Sambridge, M. (2023). Emerging directions in geophysical inversion. In A. Ismail‐Zadeh, F. Castelli, D. Jones, &amp; S. Sanchez (Eds.), Applications of Data Assimilation and Inverse Problems in the Earth Sciences (pp. 9–26). Cambridge University Press. Geophysical Journal In-

Valentine, A. P., &amp; Trampert, J. (2015). The impact of approximations and arbitrary choices on geophysical images. ternational , 204 (1), 59–73. https://doi.org/10.1093/gji/ggv440

