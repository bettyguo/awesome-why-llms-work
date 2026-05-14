# Singular Learning Theory and Grokking: A Programme-Bridge

> Singular Learning Theory (SLT, Watanabe's algebraic-statistical
> framework) lives in the [adjacent appendix](../programmes/adjacent-programmes.md#singular-learning-theory).
> Grokking lives inside [Programme 05](../programmes/05-emergence-and-reasoning.md) and is mechanistically
> explained inside [Programme 03](../programmes/03-circuits-and-biology.md). This essay argues that the
> three are *the same picture* at three levels of description, and identifies
> the experiment that would either promote SLT to a full programme or refute the
> bridge.

---

## The setup in three sentences

- **Grokking** is the empirical observation that some networks fit the training
  set to near-zero loss but stay at chance on the test set, then *abruptly*
  generalize much later in training (Power et al. 2022,
  [arXiv:2201.02177](https://arxiv.org/abs/2201.02177)).
- **Mechanistic interpretability** answered "what changed?" for at least one
  case: Nanda et al. 2023 ([arXiv:2301.05217](https://arxiv.org/abs/2301.05217))
  showed that a small transformer learning modular addition smoothly builds a
  Discrete-Fourier-Transform-based algorithm in the weights while a memorization
  algorithm dominates the loss, then phase-transitions to the DFT solution.
- **Singular Learning Theory** says: that is exactly what we should expect
  for an under-parameterized region of a singular loss landscape; phase
  transitions in training correspond to transitions between regions of
  different *learning coefficient* (RLCT / $\lambda$).

These three statements are about the same phenomenon. The interesting
content is in the *bridge*.

---

## The bridge

SLT's central technical claim is that, in singular models, the
generalization-controlling quantity is not parameter count but a quantity
$\lambda$ — the Real Log Canonical Threshold — which is an algebraic-geometric
invariant of the loss landscape's degeneracies. The free energy
$F_n \sim n L^* + \lambda \log n$ controls how much data a region of
parameter space "needs"; transitioning between regions during training
shows up as a change in $\lambda$.

The empirical handle the alignment-flavored SLT community has developed —
estimating $\hat\lambda$ during training via stochastic-gradient-Langevin
or related methods — gives a *progress measure* in Nanda et al.'s sense:
a number you can plot against training step that anticipates the
transition before the loss curves do.

This is the bridge:

> **A grokking phase transition is a transition between two regions of the
> loss landscape with different learning coefficients; mechanistic
> interpretability tells us *which algorithms* the two regions implement;
> SLT tells us *why* the network leaves one for the other.**

The two stories are not redundant. MI tells us the *content* of each phase
(memorization vs. DFT for Nanda et al.; refusal-circuit vs. refusal-direction
for Arditi et al.; in-context-learning circuit vs. in-weights memorization
for Singh et al.); SLT tells us the *thermodynamics* of the move (which
phase wins as a function of data, prior, regularization).

---

## What this bridge would predict

Three concrete predictions, if the bridge is right and not just an analogy:

### Prediction 1: $\hat\lambda$ anticipates grokking transitions on tasks beyond modular arithmetic

Run grokking-style experiments on tasks for which we have *separately* an
MI walkthrough (Nanda et al. modular addition; potentially Wang et al.
IOI on a controlled curriculum; the induction-head phase change observed
by Olsson et al.). Estimate $\hat\lambda$ across training. The bridge
predicts $\hat\lambda$ will *drop* in advance of the test-loss
transition, in proportion to the algorithmic complexity of the two phases.

This is partially confirmed for modular arithmetic; cross-task replication
is the open empirical question.

### Prediction 2: the loss-landscape geometry constrains *which* MI explanations are possible

If two algorithms both fit the training set perfectly, SLT says the one
with the lower $\lambda$ wins asymptotically. MI says the algorithm in
the weights is the algorithm we read off. The bridge predicts these
agree: the algorithm MI finds at the end of training should be the
*lower-$\lambda$* algorithm at the loss minimum.

There is no general theorem of this form. A clean test: take a problem
where two qualitatively distinct algorithms both achieve zero loss, train
both to convergence with different inductive biases, and check that the
ranked-by-$\lambda$ ordering matches the ranked-by-MI-success ordering.

### Prediction 3: the elicitation result for reasoning is SLT-flavored

The s1 result (Muennighoff et al. 2025) — 1,000 reasoning traces are
enough to elicit competition-math performance from a base model — is, under
the bridge view, a *phase selection* result. The base model contains
*multiple* loss-minima for the reasoning task; pre-training settles on a
non-reasoning one (memorization-flavored); post-training on the small
traces dataset selects a lower-$\lambda$ reasoning-flavored one without
much weight motion. The fact that 1,000 examples suffice is not surprising
if the two phases share most of their parameters and differ only in a
*low-rank* basin transition.

This is, to our knowledge, untested. A clean experiment: estimate
$\hat\lambda$ around the pre-fine-tuning and post-fine-tuning weights;
predict the elicitability of reasoning from the gap.

---

## What would falsify the bridge

The bridge is genuinely refutable. It fails if:

- For grokking tasks beyond modular arithmetic, $\hat\lambda$ does *not*
  track the phase transition — i.e., the MI-identified algorithm change
  has no corresponding signature in the SLT-estimated quantity.
- The MI-final-algorithm and the SLT-lowest-$\lambda$ algorithm
  systematically *disagree* on tasks where both are computable.
- The elicitation regime (s1, reasoning) shows phase-selection signatures
  *incompatible* with SLT's predictions about basin geometry.

Any of these would mean the SLT story is a productive analogy without
empirical bite for transformers. That would not be a tragedy — analogies are
useful — but it would close the case for promoting SLT from adjacent
to core programme.

---

## Why the bridge matters for this repo's taxonomy

Right now SLT is in the [adjacent appendix](../programmes/adjacent-programmes.md#singular-learning-theory)
with the promotion criterion of "≥ 5 verifiable claims with non-trivial
evidence ledgers, including ≥ 1 🔴 or 🟡, and ≥ 1 named credentialed
critic." The three predictions above are the start of such a ledger.

If those predictions all confirm cleanly, SLT becomes a sixth programme.
If they all fail, SLT remains adjacent and the bridge is documented as a
productive-but-failed unification attempt. Either outcome is a real update.

The synthesis essays in this repo are not in the business of being right
about the future of the field; they are in the business of *committing the
field to falsifiable predictions*, so that future readers can audit which
predictions held.

---

## Pointers

**On the empirical side.**
- Power, Burda, Edwards, Babuschkin, Misra 2022 — [Grokking](https://arxiv.org/abs/2201.02177).
- Nanda, Chan, Lieberum, Smith, Steinhardt 2023 — [Progress Measures for Grokking via Mechanistic Interpretability](https://arxiv.org/abs/2301.05217).
- Singh, Chan, Moskovitz, Grant, Saxe, Hill 2023 — [The Transient Nature of Emergent ICL](https://arxiv.org/abs/2311.08360).
- Muennighoff et al. 2025 — [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393).

**On the SLT side.**
- Watanabe, *Algebraic Geometry and Statistical Learning Theory* (2009).
- Sharkey et al. 2025 — [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496) (Murfet & Hoogland are SLT-side authors).
- The alignment-community SLT writeups by Daniel Murfet, Edmund Lau, and
  Jesse Hoogland on LessWrong / Alignment Forum (linked from the
  [adjacent-programmes file](../programmes/adjacent-programmes.md#singular-learning-theory)).

**Programme files this essay touches.**
- [Programme 03 — Circuits and Biology](../programmes/03-circuits-and-biology.md)
- [Programme 05 — Emergence and Reasoning](../programmes/05-emergence-and-reasoning.md)
- [Adjacent — Singular Learning Theory](../programmes/adjacent-programmes.md#singular-learning-theory)
