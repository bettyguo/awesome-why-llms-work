# Research Track

> For PhD students, ML researchers, and others who want to *contribute* to one of the five programmes, not just read them. This path assumes you have completed [`one-month-deep-dive.md`](one-month-deep-dive.md) or its equivalent. It is structured around the *Open Problems* lists in each programme file and around the falsification ledger.

---

## How to use this document

This path is not linear. It is a menu of starter projects, ordered roughly by independence-of-prior-work. Pick *one*. Time-box it (8–12 weeks for a thorough first attempt). When you have a result, the [`falsification-events.md`](../tracker/falsification-events.md) is where it lands.

The criteria for "this is a good starter project" are:

- It targets a *specific* claim in the falsification ledger.
- It would, if successful, move the claim's status by at least one cell of the 🟢 / 🟡 / 🔴 / ⚪ taxonomy.
- A first-pass result is achievable on a budget of one researcher and ≤ 8 A100-equivalent-weeks of compute.
- The conclusion is interesting whether or not the result is "confirmation."

---

## Programme 01 — Compression-as-Intelligence

### Project 1.1: Reasoning-tuned cohort decoupling test

**Claim targeted:** 01-D (compression linearly predicts benchmark *across* model families, including reasoning-tuned).
**Operation:** Reproduce Huang et al. 2024's linear fit on a cohort that *includes* reasoning-finetuned model series (e.g., DeepSeek-R1 family, Qwen-2.5-Math, possibly o1 indirect estimates via released benchmark numbers). Compare against the matched base models.
**Predicted outcome under the strong programme:** the linear fit weakens but the qualitative ordering is preserved.
**Predicted outcome under a refutation:** the reasoning-tuned models systematically deviate above the line, breaking the relationship.
**Why it is tractable:** bits-per-byte and benchmark scores are computable in a few GPU-days per model.

### Project 1.2: Domain-specific decoupling

**Claim targeted:** 01-E (compression is sufficient for capability).
**Operation:** Construct a benchmark suite where compression of *general web text* should not predict performance (e.g., synthetic algorithmic reasoning where the right inductive bias is not "natural language pattern"). Re-run Huang et al.'s methodology and observe the fit weakening.
**Tractable starter:** the BIG-Bench subset of algorithmic tasks; cross with a fixed compression-corpus measurement.

## Programme 02 — Superposition and LRH

### Project 2.1: Cross-family SAE-feature universality

**Claim targeted:** 02-D (cross-family universality of features).
**Operation:** Train SAEs at a matched activation site across 4 base model families at matched scale (e.g., Pythia-410M, GPT-Neo-410M-equivalent, OPT-350M-equivalent, LLaMA-tiny-equivalent). Use the same SAE width and the same training recipe. Compare resulting dictionaries by:
- Top-K cosine-similarity matching across pairs of dictionaries.
- Behavioral causal-effect matching (feature ablation on the same input across models).
**Tractable starter:** stick to MLP-out SAEs at a single layer; do 5,000 features per dictionary.

### Project 2.2: Width-of-SAE as a model property

**Claim targeted:** 02-G (polysemanticity resolved at feature level).
**Operation:** Pick one model. Train SAEs at widths $\{2 \cdot d_{\text{model}}, 4 \cdot, 8 \cdot, 16 \cdot, 32 \cdot\}$. Track per-feature monosemanticity quality (manual rating on a sample) vs. width.
**Goal:** establish whether there is a *width-asymptote* of feature interpretability, or whether feature-splitting continues indefinitely.

## Programme 03 — Circuits and Biology

### Project 3.1: Cross-family replication of a canonical circuit

**Claim targeted:** 03-C (universality of circuit motifs).
**Operation:** Pick the IOI circuit (Wang et al. 2022). Replicate the analysis on at least 3 small open models from different families. Use ACDC (Conmy et al. 2023) for semi-automation. Compare the resulting circuits — same components in matching layers? Same functional classes?
**Tractable starter:** matched GPT-2-small, Pythia-160M, OPT-125M.

### Project 3.2: Feature-level circuits for ICL

**Claim targeted:** 03-G (circuits explain behavior on OOD inputs) plus the synthesis between programmes 02, 03, 04.
**Operation:** Train SAEs on a small base model. Pick a specific ICL task (e.g., simple arithmetic in-context). Identify the *feature-level* circuit for the task: which SAE features activate in sequence, what are the edges between them. Test predictivity on out-of-distribution variants of the task.
**Why it is high-leverage:** this is one of the cleanest cross-programme projects available. A clean result publishes well.

## Programme 04 — ICL as Bayes

### Project 4.1: Natural-data Bayes-gap measurement

**Claim targeted:** 04-D (ICL on natural data tracks Bayes-optimal).
**Operation:** Construct a benchmark where the Bayes-optimal predictor is *exactly computable or tightly upper-bounded* (e.g., very-restricted templated tasks where the true latent distribution can be specified). Run a frontier-class model on the benchmark. Measure the ICL-vs-Bayes gap as a function of context length.
**Predicted outcome:** the gap is non-trivial but shrinks with context. Magnitude of "non-trivial" is the open empirical question.

### Project 4.2: Transient-ICL at scale

**Claim targeted:** 04-E (asymptotic-Bayes equilibrium).
**Operation:** Reproduce the Singh et al. 2023 transient-ICL setup at modern scale. Is the transient regime an artifact of small-data/small-model settings, or does it persist in larger runs?
**Compute cost:** moderate; the original setup is small.

## Programme 05 — Emergence and Reasoning

### Project 5.1: Continuous-metric audit of the Wei catalog

**Claim targeted:** 05-A (strong emergence; already 🔴) — *and* the question of which of Wei's specific tasks are most resistant to the Schaeffer critique.
**Operation:** Take Wei et al.'s emergence catalog. For each task, identify the most natural continuous metric. Re-measure across a modern open-model family (e.g., Pythia × LLaMA-tiny × Qwen).
**Output:** a per-task table of "smooth under continuous metric / sharp even under continuous metric." The latter rows are the cases that *survive* Schaeffer and deserve mechanistic follow-up.

### Project 5.2: s1-style elicitation across base-model scales

**Claim targeted:** 05-F (reasoning is elicitable from small post-training).
**Operation:** Take the s1 recipe. Apply it to an earlier base model (e.g., Pythia-1.4B). Does it work? At what scale does elicitation start to fail?
**Goal:** determine where the latent reasoning capability is encoded in the base-model lineage.

---

## How to land a result

Once you have a result that would move a status:

1. **Open an issue using [`status-change.md`](../.github/ISSUE_TEMPLATE/status-change.md).** Include the cited paper (yours), the claim ID, the proposed new status, and a 100–250 word rationale.
2. **Add an entry to [`tracker/falsification-events.md`](../tracker/falsification-events.md)** with the date, the claim, and the change.
3. **Update the programme file's Falsification Status table.**

Two maintainers must approve 🟢 → 🔴 or 🔴 → 🟢 transitions. Smaller transitions need one. We do not block on unanimity; we block on *evidence*.

---

## Where to go beyond this list

- *Open Problems in Mechanistic Interpretability* (Sharkey et al. 2025, [arXiv:2501.16496](https://arxiv.org/abs/2501.16496)) is a 60+ page community-survey list. Many problems are concrete and unresolved.
- Programme files' "Open Problems" sections list ~7 problems each, more granular than the projects here.
- The transformer-circuits.pub thread for the latest from Anthropic.
- The ARENA curriculum for hands-on practice.

If you finish a starter project here, do not just publish — open a PR to this repo too. The status update is itself a contribution.
