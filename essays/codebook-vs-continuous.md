# Codebook vs. Continuous: Is the Linear Representation Hypothesis Unique?

> The Linear Representation Hypothesis (LRH, [Programme 02](../programmes/02-superposition-linear-rep.md))
> asserts that features in trained language models are stored as approximately
> linear directions in activation space. Tamkin, Taufeeque, Goodman 2023
> ([arXiv:2310.17230](https://arxiv.org/abs/2310.17230)) proposed an alternative
> primitive — a *discrete codebook* of features — that interprets the same
> models without using continuous directions at all. This essay asks whether
> the two are notational variants or different theories, and proposes the
> experiment that would settle it.

---

## What the strong LRH says

The strong-LRH reading, sharpened in Park, Choe, Veitch 2023
([arXiv:2311.03658](https://arxiv.org/abs/2311.03658)):

> Features are points in a *continuous* representation space.
> Each feature's presence/absence/magnitude is encoded as a (generally
> unit-norm) direction; combinations of features are (approximately) linear
> combinations of these directions. The unembedding matrix induces a metric
> on this space that makes the linear-combination structure meaningful.

This is a strong, falsifiable statement. It says:

- The dictionary of features lives in a real vector space, not in a
  discrete set.
- "More of feature X" is a well-defined operation (scale along the X
  direction).
- Compositionality is approximately additive.

The empirical case for this is the SAE literature (Cunningham et al. 2023;
Bricken et al. 2023; Gao et al. 2024) plus the cross-feature transfer of
steering vectors and refusal directions.

---

## What codebook features say

Tamkin et al. propose:

> Quantize each layer's activations to a discrete codebook of $K$ codes
> via vector quantization (a learned dictionary plus a nearest-neighbor
> assignment). Pass the quantized representation forward. The codebook
> codes are the new unit of interpretability: each code is, by
> construction, monosemantic and discrete.

This is also a strong, falsifiable statement. It says:

- The useful description of "the feature this neuron is doing" is a *code
  index*, not a *direction*.
- Combinations are not additive; they are *concatenations of codes* across
  layers / heads.
- Continuous magnitude is not load-bearing; what matters is which code
  fired.

The empirical case is that codebook-replaced models retain non-trivial
performance and that the codes admit clean interpretability — a result
that, if continuous direction were the only useful primitive, should be
hard to obtain.

---

## Are they the same theory?

There are three readings on offer:

### Reading 1: notational variants

A continuous direction can be discretized into a code by quantization; a
codebook can be embedded into a continuous space by indicator vectors.
The two formalisms are equivalent under the right map.

This is correct as a mathematical statement and uninteresting as an
empirical one. The interesting question is whether *what the model uses*
is closer to one description or the other — and the same model can be
*described* either way without that telling us which description is
load-bearing for the model's actual computation.

### Reading 2: Continuous is right, codebook is a compression

The model's features really are continuous directions; codebooks just
discretize them at some loss. If you make the codebook large enough,
you recover the continuous picture; if you make it small, you destroy
information.

Empirically: this predicts that codebook accuracy should drop sharply as
$K$ decreases, and that the optimal $K$ should be roughly the SAE-derived
feature count for the layer.

### Reading 3: Codebook is right, continuous is a misleading idealization

The model's features really are discrete states (or finite-cardinality
mixtures), and the continuous-direction picture is an artifact of trying
to project onto a basis without realizing the underlying structure is
quantized. Continuous-direction methods (linear probes, SAE) succeed
*despite* this because they capture enough of the quantization for many
tasks; they fail *because* of this in subtle but predictable ways.

Empirically: this predicts that there should be tasks where codebook
features *causally beat* continuous features at predicting model
behavior — not just at describing it.

---

## A specific test that distinguishes the readings

Take a fixed base model. At a chosen layer, train both:

- A continuous SAE (any of the 2024–25 variants — gated, JumpReLU, top-K).
- A discrete codebook of the same effective capacity (e.g., $K$ codes
  matching the SAE's active-feature budget per token).

For the same set of downstream interpretability tasks (sparse probing,
activation steering, circuit faithfulness), measure:

1. **Reconstruction quality** of the layer's activations.
2. **Predictive power** of the recovered features for model output (linear
   probe accuracy and causal-intervention magnitude).
3. **Compositionality** of the recovered features under known compositions
   (e.g., the "Paris : France :: Berlin : ?" relational benchmark
   constructed by Merullo et al. 2023).

The predictions diverge:

| Reading | Reconstruction | Predictive power | Compositionality |
|---------|----------------|------------------|------------------|
| 1 (notational variants) | tie | tie | tie |
| 2 (continuous is fundamental) | continuous wins | continuous wins by small margin on relations | continuous wins decisively |
| 3 (codebook is fundamental) | tie at small $K$, codebook wins at large $K$ | codebook wins | codebook wins decisively |

This is a single, tractable experiment, and the result is genuinely
informative for [Programme 02](../programmes/02-superposition-linear-rep.md)'s claim 02-E
("Linear representation is the *unique* useful description"). At the time
of writing, the result has not been published cleanly; the experiment is
in the [Programme 02 Open Problems](../programmes/02-superposition-linear-rep.md#6-open-problems) list as item 5.

---

## Why this matters for the broader taxonomy

If Reading 1 is right, the programme map should not change — LRH continues
to be a productive frame and codebook features are a notation. If Reading
2 is right, programme 02 keeps its hard core. If Reading 3 is right, the
programme's hard core has to be re-stated: features are *discrete* states
that *look* linearly readable because of the projection geometry, and the
whole SAE methodology is suspect.

Reading 3 is the lowest-prior of the three but the one with the most at
stake. We mark its predictions, watch for the experiment, and update the
ledger if it lands.

---

## What this essay is not

It is not arguing for or against Tamkin et al.'s codebook framework. It
is arguing that the framework is *underexploited* — the literature has
not yet run the cross-comparison that would put one description on top.
Whoever runs that experiment publishes a paper that changes the per-claim
ledger for programme 02.

---

## Pointers

- Tamkin, Taufeeque, Goodman 2023 — [Codebook Features](https://arxiv.org/abs/2310.17230).
- Park, Choe, Veitch 2023 — [The Linear Representation Hypothesis and the Geometry of LLMs](https://arxiv.org/abs/2311.03658).
- Cunningham, Ewart, Riggs, Huben, Sharkey 2023 — [Sparse Autoencoders Find Highly Interpretable Features](https://arxiv.org/abs/2309.08600).
- Gao et al. 2024 — [Scaling and Evaluating Sparse Autoencoders](https://arxiv.org/abs/2406.04093).
- Merullo, Eickhoff, Pavlick 2023 — [LMs Implement Simple Word2Vec-style Vector Arithmetic](https://arxiv.org/abs/2305.16130).
- [Programme 02 file](../programmes/02-superposition-linear-rep.md) — full evidence ledger.
