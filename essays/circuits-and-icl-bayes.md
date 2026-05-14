# Circuits and ICL-as-Bayes: Two Levels of One Explanation

> Circuit-level explanations of in-context learning (Programme 03) and Bayesian-mixture explanations (Programme 04) look incompatible at first glance — one is a story about discoverable graphs of attention heads, the other a story about implicit posterior inference. This essay argues they are *not* incompatible. They are the same explanation at different levels of abstraction, and the productive question is to identify where they disagree on predictions.

---

## The apparent tension

Read the two programmes at their surface and they pull in opposite directions.

Programme 03 (Circuits) says: ICL is implemented by specific, identifiable circuits — induction heads (Olsson et al. 2022), name-mover heads (Wang et al. 2022), task-vector compositions. The mode of explanation is *mechanistic*: this graph of attention heads, this pattern of QK and OV activations, produces the behavior. Causally validated.

Programme 04 (ICL-as-Bayes) says: ICL is, at the algorithmic level, approximate posterior inference over a distribution of latent tasks (Xie et al. 2022). The model is doing *Bayes-optimal prediction* under the implicit prior defined by the pretraining mixture; behavior tracks the Bayes-optimal predictor as context grows.

The first is a story about *what happens inside the box*. The second is a story about *what the box, as a function, approximates*. They appear to compete because:

- A circuit-level theorist may say: "Why posit a Bayesian abstraction when we have the actual circuit?"
- A Bayesian theorist may say: "Why dignify a particular implementation with the title 'explanation' when many circuits could implement the same Bayesian computation?"

Both objections are real. Neither requires giving up the other view.

---

## The reconciliation: levels of analysis, à la Marr

David Marr's three-level framework — *computational*, *algorithmic*, *implementational* — is helpful here. Bayes-optimal posterior inference is the *computational* description ("what is the system *for*?"). The induction-head circuit is part of the *implementational* description ("what physical mechanism realizes that"?). In between sits the *algorithmic* description — the specific algorithm the system runs (gradient descent on in-context examples? Bayesian update via attention-as-key-lookup?). The two programmes can be seen, respectively, as *implementation-level* (Programme 03) and *computational-level-plus-algorithm-sketch* (Programme 04) accounts.

This framing makes a useful prediction: **circuit-level findings should match Bayesian-frame predictions modulo implementation noise.** When they disagree, the disagreement should be at the algorithmic-or-below level, not at the computational level.

That is exactly what we observe:

- The *behavior* on synthetic mixture-of-HMM data tracks Bayes-optimal as context grows (Xie et al. 2022) — agreement at the computational level.
- The *mechanism* doing the tracking includes induction heads — implementation-level instantiation of part of the Bayesian computation.
- Discrepancies between Bayesian-predicted and observed ICL on real data (Panwar et al. 2023; surface-form sensitivities) are exactly where the implementation does *not* fully realize the computational ideal — algorithmic-level shortcuts taken by the actual circuit.

---

## Where the two programmes make *different* predictions

A useful synthesis is not one where the two programmes are reconciled into mush; it is one where their disagreements become sharper. Some examples:

### Surface-form sensitivity

Bayesian predictions are *invariant* under bijective relabelings of in-context examples (the prior assigns the same posterior to "input: x → output: y" and "INPUT: X → OUTPUT: Y" if the structure is identical). Circuit-level predictions are *not* invariant: induction heads care about specific tokens, and surface-form changes that perturb tokens perturb induction-head activations.

**Prediction:** if circuits dominate, ICL should be highly surface-form-sensitive. If the Bayesian abstraction is tight, ICL should be largely surface-form-invariant. The empirical reality is in between, leaning toward "more surface-form-sensitive than Bayesian-frame would predict" — evidence that the implementation level matters and is leaking through.

### Transient ICL

Singh et al. (2023, [arXiv:2311.08360](https://arxiv.org/abs/2311.08360)) showed that ICL can emerge during training and then *disappear* in favor of in-weights learning. The Bayesian story has trouble explaining the *disappearance* of an apparently optimal solution as training continues; the circuit-level story has a clean explanation — the induction-head circuit is overwritten by a parameter-storing alternative that achieves the same I/O behavior more cheaply for the training distribution. The implementation-level account explains the dynamics the computational-level account treats as anomalous.

**Prediction:** the disagreement should be observable. The model's I/O behavior should remain Bayes-optimal (or nearly so) *throughout* training; only the mechanism shifts. Singh et al. confirm partial Bayes-optimality is maintained as in-weights learning takes over.

### Algorithm selection (Bai-style)

Bai et al. (2023, [arXiv:2306.04637](https://arxiv.org/abs/2306.04637)) argue that transformers implement a *portfolio* of algorithms (OLS, ridge, etc.) and *select among them* based on the in-context examples. This is a *prediction at the algorithmic level* that is between the computational (Bayesian) and the implementational (circuit) levels. It makes a sharper prediction than either parent programme: there should be *multiple* circuits, each implementing a different algorithm, and a routing mechanism for choosing between them.

**Open question:** find the routing mechanism. It should be a circuit. Programme 03's tools — activation patching, ACDC — are the right ones for the job.

---

## A specific synthesis: feature-level circuits

Sparse autoencoders (Programme 02) give us *features*; circuit-discovery methods (Programme 03) give us *graphs over components*; Bayesian-frame reasoning (Programme 04) tells us *what the graph is computing*. A natural synthesis is:

> Discover the graph of *features* (not components) that implements the ICL computation; validate that the graph computes (approximately) the Bayes-optimal predictor on the in-context examples; identify where the feature-graph deviates from the ideal Bayes computation, and predict the deviations as algorithmic-level shortcuts.

This program is the active research frontier of feature-level circuits / sparse-feature circuits. The right tools exist (SAELens, ACDC variants for SAE features). The right theory exists (Bayesian frame as the computational specification). The empirical work is hard but tractable.

A paper that does this for *one* well-studied ICL task — say, IOI — would be the cleanest demonstration of the cross-programme synthesis and would settle several open questions at once.

---

## Why the synthesis matters for the broader repo

The five-programme structure of this repo is useful for navigation but it overstates the separation. The vertical-integration view above already absorbs Programmes 03 and 04 into a level-of-analysis pair; the [`compression-and-superposition.md`](compression-and-superposition.md) essay does the same for Programmes 01 and 02. A maximally aggressive synthesis would integrate all four into a single picture:

- **Programme 01 (Compression)** describes what the I/O is *for*.
- **Programme 02 (Superposition)** describes how the I/O target is stored in finite capacity.
- **Programme 03 (Circuits)** describes how the stored content is *computed with*.
- **Programme 04 (ICL-as-Bayes)** describes what the inference-time computation *approximates*.

Programme 05 (Emergence) is then a phenomenology question about how these layers come online during training and scaling — a question that depends on but is not itself one of the four core analysis levels.

This is a defensible position. The reason this repo does not adopt it as the *primary* framing is methodological: most of the field operates at a single level, and the five-programme structure forces explicit reckoning with the level-of-analysis question rather than papering it over. If the synthesis is right, this repo's structure should converge to it; the falsification ledgers across programmes are the mechanism by which that convergence happens publicly.

---

## A note on "is ICL really Bayesian?"

The honest answer is: **partially.** The Bayesian frame is a useful first-order model with non-trivial second-order deviations on real data; it is fully predictive in toy settings (Xie et al. 2022) and partially predictive on natural-language ICL (Panwar et al. 2023). The frame is *neither* refuted nor canonical; the synthesis essay's contribution is to reframe the question from "is ICL Bayesian?" to "where do the implementation-level shortcuts diverge from the computational-level ideal, and can we predict those divergences from circuit-level knowledge?"

That reframing is more productive than the head-on question because it points at experiments.

---

## Pointers

**Programme 03.**
- Olsson et al. 2022, [arXiv:2209.11895](https://arxiv.org/abs/2209.11895).
- Wang et al. 2022, [arXiv:2211.00593](https://arxiv.org/abs/2211.00593).
- Conmy et al. 2023, [arXiv:2304.14997](https://arxiv.org/abs/2304.14997).
- [`programmes/03-circuits-and-biology.md`](../programmes/03-circuits-and-biology.md).

**Programme 04.**
- Xie et al. 2022, [arXiv:2111.02080](https://arxiv.org/abs/2111.02080).
- von Oswald et al. 2023, [arXiv:2212.07677](https://arxiv.org/abs/2212.07677).
- Bai et al. 2023, [arXiv:2306.04637](https://arxiv.org/abs/2306.04637).
- Singh et al. 2023, [arXiv:2311.08360](https://arxiv.org/abs/2311.08360).
- Panwar et al. 2023, [arXiv:2306.04891](https://arxiv.org/abs/2306.04891).
- [`programmes/04-icl-as-bayes-meta-learning.md`](../programmes/04-icl-as-bayes-meta-learning.md).

**Notebooks.**
- [`notebooks/03-induction-head-discovery.ipynb`](../notebooks/03-induction-head-discovery.ipynb).
- [`notebooks/04-icl-as-bayes-hmm-mixture.ipynb`](../notebooks/04-icl-as-bayes-hmm-mixture.ipynb).
