# One-Month Deep Dive

> Goal: leave with a researcher-level grasp of all five programmes, the adjacent appendix, and the synthesis arguments — having read multiple papers per programme, run all five notebooks, and written a 1-page proposal addressing one Open Problem. Four weekends of ~6 hours each, with light weekday reading in between.

---

## Week 1 — Programmes 01 and 02

**Weekend.** Use the [`one-weekend-intro.md`](one-weekend-intro.md) plan for Programmes 01 and 02 (Saturday's content). Both notebooks. The synthesis essay [`compression-and-superposition.md`](../essays/compression-and-superposition.md).

**Weekday reading (3–5 hours).**

- Delétang et al. 2023 (*Language Modeling is Compression*, [arXiv:2309.10668](https://arxiv.org/abs/2309.10668)) in full, including the audio/image experiments.
- Park, Choe, Veitch 2023 (*The Linear Representation Hypothesis and the Geometry...*, [arXiv:2311.03658](https://arxiv.org/abs/2311.03658)) — focus on the formal LRH statement.
- Cunningham et al. 2023 (*Sparse Autoencoders Find Highly Interpretable Features*, [arXiv:2309.08600](https://arxiv.org/abs/2309.08600)). The SAE methodology section.

**Optional.** MacKay, *Information Theory, Inference, and Learning Algorithms*, Chapter 1 (the predictor↔compressor identity at textbook level). 90 min, but useful.

## Week 2 — Programme 03

**Weekend.** Saturday afternoon's content from [`one-weekend-intro.md`](one-weekend-intro.md), expanded:

- *Mathematical Framework for Transformer Circuits* (Elhage et al. 2021) in full.
- *In-context Learning and Induction Heads* (Olsson et al. 2022) in full.
- *Interpretability in the Wild — Circuit for IOI* (Wang et al. 2022, [arXiv:2211.00593](https://arxiv.org/abs/2211.00593)). The paradigm case for end-to-end circuit analysis.
- Notebook 03.

**Weekday reading (4–6 hours).**

- *Towards Automated Circuit Discovery* (Conmy et al. 2023, [arXiv:2304.14997](https://arxiv.org/abs/2304.14997)).
- *Progress Measures for Grokking via Mechanistic Interpretability* (Nanda et al. 2023, [arXiv:2301.05217](https://arxiv.org/abs/2301.05217)).
- *Open Problems in Mechanistic Interpretability* (Sharkey et al. 2025, [arXiv:2501.16496](https://arxiv.org/abs/2501.16496)). Skim; mark 2–3 problems that interest you.

**Optional but high-value.** The [ARENA 3.0](https://github.com/callummcdougall/ARENA_3.0) interpretability chapter — pick one notebook and do it. It is where most working MI researchers actually got their hands trained.

## Week 3 — Programme 04 and Adjacent

**Weekend.** Sunday morning's content from [`one-weekend-intro.md`](one-weekend-intro.md), expanded:

- Xie et al. 2022 in full.
- von Oswald et al. 2023 ([arXiv:2212.07677](https://arxiv.org/abs/2212.07677)) in full.
- Notebook 04.
- Synthesis essay [`circuits-and-icl-bayes.md`](../essays/circuits-and-icl-bayes.md).

**Weekday reading (4–6 hours).**

- Akyürek et al. 2022 ([arXiv:2211.15661](https://arxiv.org/abs/2211.15661)) — the algorithm-identification methodology.
- Bai et al. 2023 ([arXiv:2306.04637](https://arxiv.org/abs/2306.04637)) — algorithm selection as the next-step generalization.
- Panwar et al. 2023 ([arXiv:2306.04891](https://arxiv.org/abs/2306.04891)) — where the Bayesian frame succeeds and fails on natural-data ICL.
- Singh et al. 2023 ([arXiv:2311.08360](https://arxiv.org/abs/2311.08360)) — transient ICL.

**Adjacent skim.** [`programmes/adjacent-programmes.md`](../programmes/adjacent-programmes.md). At minimum, the Singular Learning Theory and Platonic Representation sections.

## Week 4 — Programme 05, Synthesis, and a Proposal

**Saturday.** All of Programme 05's reading-path-intermediate content:

- Wei et al. 2022 ([arXiv:2206.07682](https://arxiv.org/abs/2206.07682)).
- Schaeffer et al. 2023 ([arXiv:2304.15004](https://arxiv.org/abs/2304.15004)).
- Power et al. 2022 ([arXiv:2201.02177](https://arxiv.org/abs/2201.02177)).
- Snell et al. 2024 ([arXiv:2408.03314](https://arxiv.org/abs/2408.03314)).
- DeepSeek-R1 ([arXiv:2501.12948](https://arxiv.org/abs/2501.12948)).
- s1 (Muennighoff et al. 2025, [arXiv:2501.19393](https://arxiv.org/abs/2501.19393)).
- Notebook 05.

**Sunday.** Synthesis and writing.

- The essay [`emergence-vs-reasoning-models.md`](../essays/emergence-vs-reasoning-models.md).
- The methodological essay [`how-to-falsify-an-llm-theory.md`](../essays/how-to-falsify-an-llm-theory.md).
- **Write a 1-page proposal** addressing one of the Open Problems from any programme.
  - Use the structure: *Open problem (verbatim), why it is open, what experiment / argument would close it, why you think the experiment is tractable.*
  - Save it for yourself. If it survives a week of reflection, consider proposing it on an issue or following the [research-track.md](research-track.md) workflow.

## What you should leave knowing, after one month

- The hard cores, contested edges, and current statuses of all five programmes.
- Several papers per programme, read in original, not in summary.
- The major synthesis arguments and their open questions.
- One Open Problem you have thought about long enough to propose a starting experiment.
- Where the adjacent appendix is and what it covers.

## What you should leave knowing you don't know

- The literature that has appeared *since* the canonical papers per programme — the current frontier is not what is in this repo's reading list.
- The hands-on craft of doing the experiments. Reading is not training. Do ARENA, or pair with a researcher, or pick a problem and actually run it.
- The ongoing internal-to-Anthropic / internal-to-DeepMind work that is not in the public literature. Some of the most important work on these programmes is currently published as blog posts on lab websites; we link to it where we can, but the lab-internal version is more advanced than the public version.

## After one month: what next?

[`research-track.md`](research-track.md). You are ready for it.
