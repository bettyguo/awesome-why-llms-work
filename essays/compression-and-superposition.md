# Compression and Superposition: Two Aspects of One Phenomenon?

> If compression-as-intelligence (Programme 01) is the right *target* for what pretraining optimizes toward, and superposition (Programme 02) is the right *mechanism* by which a fixed-size network reaches that target, then the two programmes are not competing — they are the same explanation at different levels of analysis. This essay argues that case, identifies where the unification is empirically active, and proposes a specific test that would falsify it.

---

## The thesis in one paragraph

A trained language model is, *up to a constant*, a lossless compressor of the text distribution. The compressor is bounded by a fixed parameter count. If the underlying text distribution has more *features* (semantically meaningful sources of variance) than the network has neurons, the network has no choice but to encode features in overlapping linear combinations — superposition. **Therefore: compression-as-intelligence predicts superposition under finite-capacity constraints, and superposition mechanistically supplies what compression-as-intelligence asserts at the I/O level.** The two programmes are vertically integrated rather than horizontally competing.

---

## What each programme says, sharply

**Programme 01.** The cleanest empirical anchor is Huang et al. (2024) — average benchmark score is approximately linear in bits-per-byte across model families. The cleanest theoretical anchor is the predictor↔compressor identity made literal by Delétang et al. (2023): arithmetic-coding with an LM produces lossless compression of text, audio, and images at competitive rates. The *thing the model is doing*, in the sharpest defensible reading, is fitting a distribution as tightly as it can.

**Programme 02.** The cleanest empirical anchor is the SAE literature (Cunningham et al. 2023, Bricken et al. 2023): sparse autoencoders applied to LM activations recover dictionaries whose atoms behave as monosemantic features at scale. The cleanest theoretical anchor is Elhage et al. 2022 (toy models of superposition): a network with too few neurons for the implied feature count encodes features as overlapping directions in approximately polytope-shaped geometries. The *thing the model is doing*, in the sharpest defensible reading, is packing many features into too-small an activation space using superposition.

These read as different stories. They are not.

---

## The bridge: feature count, parameter budget, and information

Consider a hypothetical generative process producing tokens conditioned on a *latent* state $\theta$ that ranges over a complex set of "features" (concepts, syntactic structures, latent topics, the country someone was born in, ...). For the model to predict next tokens *Bayes-optimally* under this process, it must represent — at every position — the posterior over $\theta$ given the prefix. If $\theta$ has $n$ binary features and the activation space has $d < n$ neurons, the posterior cannot be encoded one-feature-per-neuron. The information-theoretic lower bound on how many features must coexist in the activation is $\Omega(n/d)$; under additional sparsity assumptions, the model can pack much more.

This is *exactly* the toy-superposition setting of Elhage et al., re-framed in compression language. The "bottleneck" of the toy is the parameter budget of the real LM. The "synthetic features" of the toy are the latents of the natural-text-generating process. The "sparsity" of the toy is the empirical sparsity of features in natural language (most features are not present in most tokens). Toy superposition then *predicts* that real LMs will encode many features per neuron, with the polytope-shaped geometries collapsing into something more elaborate at scale but with the same logic.

Programme 01's central claim — capability tracks bits-per-byte — is, on this reading, *equivalent to* Programme 02's central claim — the model packs as much feature content as possible into a fixed activation budget — because bits-per-byte is exactly the metric that asks whether the packing is efficient.

---

## Where the unification is empirically active

Several lines of work are already living at this boundary, even if they don't always describe themselves this way:

- **Scaling Monosemanticity** (Anthropic 2024 follow-up to *Towards Monosemanticity*): when you scale up the SAE width and the underlying model together, the SAE recovers more and finer-grained features. The "right number of features" question turns out to depend on the parameter budget of the model — exactly what the compression-superposition unification predicts.
- **SAE-based compression** (working hypothesis, increasingly explored): if the model's features form a sparse, mostly-monosemantic dictionary, then *that dictionary itself* is a candidate for an explicit description-length account of what the model knows. "MDL of the SAE" becomes a (partial) measure of what the model has compressed.
- **Cross-model universality** as a *prediction* of the unification: if compression of the *same* world produces convergent representations (the Platonic Representation Hypothesis), and superposition is the mechanism behind those representations, then SAE-feature universality across models should be a robust empirical phenomenon. Anthropic's preliminary evidence (and the Platonic paper itself, Huh et al. 2024) is consistent with this.

---

## Why the unification is not trivial

It is tempting to dismiss this as "obviously, the model has to put information *somewhere*." The non-trivial content is:

1. **Compression-as-intelligence predicts *non-orthogonal* (overlapping) encodings.** A theory of representation that did not allow non-orthogonal encodings — and there were such proposals in the disentanglement era — would predict a hard cliff in capability when feature count exceeds neuron count. We do not observe that cliff. Superposition is a constructive explanation for the absence.
2. **Superposition without compression is a phenomenon without a *driver*.** Why would a trained network *want* to encode multiple features per neuron? The compression view supplies the driver: it is the optimization-bound consequence of trying to fit a feature-rich distribution under a parameter-count constraint. Without the compression view, superposition is "what we observe"; with it, superposition is "what we predict and then observe."
3. **The unification has falsifiable consequences distinct from either programme alone.** If the unification is right, then bits-per-byte and total dictionary size in a well-fitted SAE should be related — fitter compressors should have richer or finer-grained or denser SAEs. Cross-family. Across scales. Without the unification, there is no reason to expect this.

---

## A specific test that would falsify the unification

Construct two model checkpoints A and B such that bits-per-byte is held *constant* but the rest of the training (data mix, learning-rate schedule, regularization) differs. Train SAEs on matched activation sites with matched hyperparameters.

- **Prediction under the unification:** the SAEs should look strongly *similar*. The dictionaries should overlap substantially under best-matching alignment, and the per-feature interpretability should be of similar quality. Differences should be explainable by the data-mix differences in the pretraining.
- **Refutation:** if SAEs of A and B differ *as much as* SAEs of randomly initialized networks, despite identical bits-per-byte, then compression bits do not fix the feature dictionary — and the strong unification fails.

A subtler version: hold *bits-per-byte on the SAE training corpus* constant but train SAEs on a *different* domain corpus. Under the unification, the SAEs should still overlap on shared features. Under a non-unification view, the SAEs are free to differ.

These experiments are not, today, fully run at scale. They are tractable. Whoever runs them well writes a paper that pulls Programmes 01 and 02 either into a single programme or definitively apart.

---

## A subtler concern: the gap between bits-per-byte and feature richness

The cleanest version of the unification predicts that *every* bit of compression buys exactly one bit-equivalent of feature content. The empirical reality is closer to: bits-per-byte is *necessary* for capability but not *sufficient* — two models with the same bpb can still differ on downstream tasks (the open part of Programme 01, claim 01-E). On the unification view, this is a *post-superposition* effect: how the model *uses* the encoded features depends on circuit-level (Programme 03) and ICL-level (Programme 04) structures that bpb alone does not pin down.

The unification thus naturally embeds Programmes 01 and 02 as the *representational* layer, with Programmes 03 and 04 supplying the *computational* layer above it. This is a clean architectural picture and probably approximately correct; the synthesis essay on Programmes 03 and 04 ([`circuits-and-icl-bayes.md`](circuits-and-icl-bayes.md)) addresses the computational layer.

---

## What this essay is and is not arguing

This is not arguing that Programmes 01 and 02 are *identical*. They have distinct empirical content — compression is measured at the I/O of the model; superposition is measured inside the activation space. They have distinct refutation paths — compression-vs-capability can decouple without superposition being affected, and vice versa.

It *is* arguing that the two are not in tension and are, at the level of mechanism, two halves of one explanation. The right next step is to design experiments that test the unification directly rather than each programme separately. The "specific test" section above is one such design. Better ones welcome.

---

## Pointers

**Programme 01.**
- Delétang et al. 2023, [arXiv:2309.10668](https://arxiv.org/abs/2309.10668).
- Huang et al. 2024, [arXiv:2404.09937](https://arxiv.org/abs/2404.09937).
- [`programmes/01-compression-as-intelligence.md`](../programmes/01-compression-as-intelligence.md).

**Programme 02.**
- Elhage et al. 2022, [*Toy Models of Superposition*](https://transformer-circuits.pub/2022/toy_model/index.html).
- Park, Choe, Veitch 2023, [arXiv:2311.03658](https://arxiv.org/abs/2311.03658).
- Cunningham et al. 2023, [arXiv:2309.08600](https://arxiv.org/abs/2309.08600).
- [`programmes/02-superposition-linear-rep.md`](../programmes/02-superposition-linear-rep.md).

**Notebooks.**
- [`notebooks/01-compression-ratio-vs-benchmark.ipynb`](../notebooks/01-compression-ratio-vs-benchmark.ipynb).
- [`notebooks/02-toy-superposition.ipynb`](../notebooks/02-toy-superposition.ipynb).
