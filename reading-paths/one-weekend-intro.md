# One-Weekend Introduction

> Goal: leave with a working understanding of all five programmes, having read one canonical paper per programme and run all five notebooks. Two days, ~6 hours each. Pace deliberately; the notebooks are where the intuition lands.

---

## Saturday morning (3 hours) — Programmes 01 and 02

**Programme 01 — Compression-as-Intelligence.**

- Read the [programme file](../programmes/01-compression-as-intelligence.md), §§1–4 (Hard Core, Protective Belt, Positive Heuristic, Key Papers). 45 min.
- Read *Compression Represents Intelligence Linearly* (Huang et al. 2024, [arXiv:2404.09937](https://arxiv.org/abs/2404.09937)). First six pages plus the headline figure. 45 min.
- Run [`notebooks/01-compression-ratio-vs-benchmark.ipynb`](../notebooks/01-compression-ratio-vs-benchmark.ipynb). 30 min including model downloads.

**Programme 02 — Superposition and Linear Representations.**

- Read the [programme file](../programmes/02-superposition-linear-rep.md), §§1–4. 30 min.
- Skim the Anthropic blog post *Toy Models of Superposition* (Elhage et al. 2022). The first three sections. 30 min.
- Run [`notebooks/02-toy-superposition.ipynb`](../notebooks/02-toy-superposition.ipynb). 20 min.

Before lunch: read the synthesis essay [`compression-and-superposition.md`](../essays/compression-and-superposition.md). It will tie the two morning programmes together.

## Saturday afternoon (3 hours) — Programme 03

- Read the [programme file](../programmes/03-circuits-and-biology.md), §§1–4. 45 min.
- Read *In-context Learning and Induction Heads* (Olsson et al. 2022, [arXiv:2209.11895](https://arxiv.org/abs/2209.11895)). The executive summary and the first half. 45 min.
- Run [`notebooks/03-induction-head-discovery.ipynb`](../notebooks/03-induction-head-discovery.ipynb). 30 min.
- *Optional but recommended:* skim *A Mathematical Framework for Transformer Circuits* (Elhage et al. 2021) to anchor the QK/OV vocabulary you keep encountering. 30 min.

End of Saturday: you have the representational and computational levels of the picture. Sunday is about the inference-time computation and the scaling phenomenology.

## Sunday morning (3 hours) — Programme 04

- Read the [programme file](../programmes/04-icl-as-bayes-meta-learning.md), §§1–4. 45 min.
- Read *An Explanation of In-context Learning as Implicit Bayesian Inference* (Xie et al. 2022, [arXiv:2111.02080](https://arxiv.org/abs/2111.02080)). 60 min.
- Run [`notebooks/04-icl-as-bayes-hmm-mixture.ipynb`](../notebooks/04-icl-as-bayes-hmm-mixture.ipynb). 30 min.
- Read the synthesis essay [`circuits-and-icl-bayes.md`](../essays/circuits-and-icl-bayes.md). 30 min.

The synthesis essay is essential here; it is where the level-of-abstraction question (which made Programmes 03 and 04 look in tension) gets resolved.

## Sunday afternoon (3 hours) — Programme 05

- Read the [programme file](../programmes/05-emergence-and-reasoning.md), §§1–4. 45 min.
- Read *Emergent Abilities of Large Language Models* (Wei et al. 2022). Short. 20 min.
- Read *Are Emergent Abilities a Mirage?* (Schaeffer et al. 2023). The figures are the argument. 30 min.
- Run [`notebooks/05-emergence-mirage-demo.ipynb`](../notebooks/05-emergence-mirage-demo.ipynb). 25 min.
- Read the synthesis essay [`emergence-vs-reasoning-models.md`](../essays/emergence-vs-reasoning-models.md). 30 min.
- Pick up the s1 paper (Muennighoff et al. 2025, [arXiv:2501.19393](https://arxiv.org/abs/2501.19393)) — read the abstract and the budget-forcing section. 20 min.

## What you should leave knowing, after one weekend

- The hard core and falsification status of each of the five programmes.
- The shape of one canonical paper per programme, in the original.
- The hands-on intuition for what each programme is *about* — not just what it claims.
- The two main internal syntheses (compression↔superposition; circuits↔ICL-Bayes).
- The Schaeffer-et-al refutation of strong emergence and what test-time compute reopens.

## What you should leave knowing you don't know

- The literature *between* the canonical papers per programme. The reading-path tells you what to read; it does not pretend to be the literature.
- How any of these programmes performs at frontier scale (the canonical papers per programme are 2022–2023; the literature has continued).
- How to *do* research in any of these programmes. That is the research-track reading path.

## If you only have one day instead of two

- Saturday morning + Sunday afternoon. Programmes 01, 02, and 05. The two that frame the answer (compression and emergence) plus the mechanism layer (superposition). Skip 03 and 04; pick them up later.
