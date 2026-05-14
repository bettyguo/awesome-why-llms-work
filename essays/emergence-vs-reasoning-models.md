# Emergence vs. Reasoning Models: What Test-Time Compute Reopens, and What It Does Not

> The Schaeffer-style refutation (2023) largely closed the original emergence debate: under continuous metrics, the canonical Wei-et-al "emergent abilities" appear smooth, not sharp. But the reasoning-models wave (o1, DeepSeek-R1, s1) reopens the question along a different axis: capability that scales with *inference-time* compute. This essay argues that what these models show is not "emergence is real" but rather "there is a second compute axis we were ignoring," and identifies where the genuinely open empirical questions are.

---

## The two-stage history

**Stage 1 (2022).** Wei et al. propose that some capabilities of large language models are *emergent* in a strong sense: zero-or-near-zero performance below a critical scale, then a sharp transition to substantially-better performance. The claim is influential — it motivates "we cannot predict capabilities" rhetoric in both safety and capability-forecasting discussions.

**Stage 2 (2023).** Schaeffer, Miranda, Koyejo argue the apparent discontinuity is a *metric artifact*. Replace exact-match accuracy with a continuous metric (token-edit-distance, log-probability of the correct answer) and the curves go smooth across the same model families and the same tasks. The strong version of emergence — "the underlying capability is genuinely discontinuous" — is *refuted* in the cases Wei et al. originally cataloged.

The weaker descriptive claim survives ("under common metrics, some curves are sharp at scale, and this is operationally useful for forecasting") — but the philosophically interesting claim, that capability appears unpredictably out of thin air at some scale, does not.

**Stage 3 (2024–).** The reasoning-models wave. OpenAI's o1 (September 2024, blog post; no formal paper) demonstrates a model that scales capability *not by being a bigger model* but by spending more inference-time compute on each prompt — chain-of-thought sampling, search, self-consistency. DeepSeek-R1 (January 2025, [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)) replicates the recipe in the open with reinforcement learning on outcome-verified tasks. s1 (Muennighoff et al. 2025, [arXiv:2501.19393](https://arxiv.org/abs/2501.19393)) further compresses the recipe: 1,000 reasoning traces and a budget-forcing decoding rule are enough to match o1-preview on competition math.

Capability curves for reasoning models as a function of *training* compute look much like before — smooth or sharp depending on metric. Capability curves as a function of *inference* compute look different: there is a new axis along which capability scales, and it scales steeply on tasks where you can afford the wall-clock cost.

---

## What the reasoning-models wave does *not* show

It does not show that strong emergence (Stage 1) is real. The Schaeffer et al. critique still bites: where the *output* metric is continuous, capability gains from inference-time compute are smooth in compute, even when they look discontinuous in capability-per-prompt. The fact that you can sometimes turn a 0% exact-match into a 50% exact-match by spending 100× more inference compute is not "emergence"; it is "we were measuring capability per prompt instead of per compute budget."

It does not show that pretraining compute is the wrong axis. The base models in the reasoning-models wave are themselves the product of large pretraining runs; the inference-time scaling rests on a base capability that did *not* arise from inference-time compute. The right description is: capability is a function of (pretraining compute, inference compute, post-training procedure), and the field had previously been holding the second axis fixed.

It does not show that the underlying mechanism is mysterious. The s1 result — 1,000 reasoning traces + a decoding rule are sufficient to elicit competition-math performance — strongly constrains theories of *how* reasoning capability is acquired. The most defensible reading: reasoning capability is *latent in the base model* and is *elicited* by a small amount of targeted post-training, not *built up* by enormous reasoning-specific training. This is a much weaker claim than "emergence."

---

## What the reasoning-models wave *does* reopen

### Test-time-compute scaling laws

Snell et al. (2024, [arXiv:2408.03314](https://arxiv.org/abs/2408.03314)) showed that, for fixed pretraining, allocating *test-time compute* optimally can outperform proportional increases in model size on a range of reasoning benchmarks. This is genuine new empirical content. It says:

- The right scalar to plot capability against is not just "params" or "training FLOPs" but something like "total FLOPs spent on the prompt, training + inference, in the right ratio."
- The trade-off between training and inference compute is task-dependent: some tasks benefit much more from extra inference compute than others.

Neither of these is a Stage-1-style strong-emergence claim. Both are open empirical questions with non-trivial implications for forecasting.

### Elicitation vs. construction

The s1 result suggests that, for at least one important class of capabilities (math reasoning), capability is *already in the model* and is being elicited rather than constructed. This raises a sharp question:

- **What else is latent in current base models?** Many of the dramatic "emergent" capabilities reported in 2022–2023 may turn out to be elicitable from earlier (smaller) base models given the right post-training. This is testable: take an early Pythia or LLaMA checkpoint, apply s1-style post-training on a target benchmark, see if capability is elicited.

If the answer is "yes, much of the apparent emergence was elicitation gap, not capacity gap," then the entire emergence debate gets re-interpreted: discontinuities at scale were partially discontinuities in *what was elicited from the base model*, not in *what the base model contained*.

### Process vs. outcome rewards

DeepSeek-R1 trained primarily on outcome rewards (the math answer is right or wrong) rather than process rewards (the reasoning steps are individually plausible). This is theoretically surprising: one might have expected process supervision to be necessary for reasoning capability. It was not. The mechanism is not yet well understood; the field is actively working on it.

### What this means for Programme 03 (Circuits)

Reasoning capability under inference-time-compute scaling is, mechanistically, an unanswered question. We do not yet have a "circuit for chain-of-thought" the way we have a "circuit for IOI" or a "circuit for induction." Until we do, the synthesis between this programme and the reasoning-models wave is open.

This is a high-value open problem; Programme 03's tooling (TransformerLens, SAELens, attribution patching) is ready for it.

---

## A specific question this essay does not resolve

The Krakauer, Krakauer, Mitchell 2025 paper ([arXiv:2506.11135](https://arxiv.org/abs/2506.11135)) brings a complex-systems-science definition of emergence to the LLM conversation: order parameter discontinuities; many-body interactions producing genuinely new phenomena at the collective level. Under that strict bar, almost nothing in the LLM literature currently qualifies as "emergent."

Is the strict bar the right one? Reasonable people disagree. The argument *for* the strict bar is that without it, "emergence" becomes a vague word that means "scaling produces capability" and loses analytic content. The argument *against* the strict bar is that it imports cross-field machinery (statistical mechanics phase-transition concepts) that may not be the right tools for understanding learned function approximators.

This essay does not take a position. It marks the question as genuinely open and as the right kind of question to be open: a definitional dispute with empirical consequences. Whoever produces a clean order-parameter measurement for a real LLM capability — whether that order parameter shows a discontinuity or not — moves the conversation.

---

## Bottom line

After Schaeffer et al., **strong emergence is refuted in its 2022 formulation**. The reasoning-models wave does not resurrect it. What the reasoning-models wave does is:

1. Reveal a second compute axis (inference-time) that had been ignored.
2. Suggest that much of what looked like "emergence" was in fact "elicitation," a different phenomenon with different implications.
3. Open new mechanistic questions about reasoning-as-elicited-capability.
4. Leave the *strict* definitional question (Krakauer et al.) open and important.

The five-programme map of this repo treats this synthesis carefully: Programme 05 lists strong emergence as 🔴 *refuted*, the descriptive form as 🟢 *supported*, and the test-time-compute axis as 🟡 *contested* in magnitude with high empirical activity. That is what the literature actually supports right now. We will update statuses as evidence comes in.

---

## Pointers

- *Are Emergent Abilities of Large Language Models a Mirage?* — Schaeffer, Miranda, Koyejo (2023). [arXiv:2304.15004](https://arxiv.org/abs/2304.15004).
- *Emergent Abilities of Large Language Models* — Wei et al. (2022). [arXiv:2206.07682](https://arxiv.org/abs/2206.07682).
- *Scaling LLM Test-Time Compute Optimally* — Snell et al. (2024). [arXiv:2408.03314](https://arxiv.org/abs/2408.03314).
- *DeepSeek-R1* — DeepSeek-AI (2025). [arXiv:2501.12948](https://arxiv.org/abs/2501.12948).
- *s1: Simple Test-Time Scaling* — Muennighoff et al. (2025). [arXiv:2501.19393](https://arxiv.org/abs/2501.19393).
- *Large Language Models and Emergence: A Complex Systems Perspective* — Krakauer, Krakauer, Mitchell (2025). [arXiv:2506.11135](https://arxiv.org/abs/2506.11135).
- Programme file: [`programmes/05-emergence-and-reasoning.md`](../programmes/05-emergence-and-reasoning.md).
- Notebook: [`notebooks/05-emergence-mirage-demo.ipynb`](../notebooks/05-emergence-mirage-demo.ipynb).
