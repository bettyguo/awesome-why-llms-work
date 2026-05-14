# 30-Minute Overview

> Goal: leave with a working mental model of why each of the five programmes exists, what its central claim is, and where it is contested. No code, no full-paper reading.

---

## Minute 0–5: the README five-programme table

Read the [top-level README](../README.md) — specifically the *Five Programmes — at a glance* table. It is one screen. Look at each row's *Hard core* column.

You should be able, after this, to say in one sentence each:

- Programme 01 is about... *the linear coupling between compression performance and benchmark performance.*
- Programme 02 is about... *features as overcomplete linear directions in activation space.*
- Programme 03 is about... *small identifiable graphs of attention heads that implement specific behaviors.*
- Programme 04 is about... *in-context learning as approximate posterior inference over a latent-task variable.*
- Programme 05 is about... *whether capability appears sharply at scale and (now) about test-time compute as a second compute axis.*

## Minute 5–10: the falsification ledger summary

Same README, the *Falsification ledger summary* section. Note:

- 🟢 *Supported*: ~7 claims, well-distributed across programmes.
- 🟡 *Contested*: ~8 claims. These are the live ones.
- 🔴 *Refuted*: ~2 claims. **One of them is the strong form of emergence (Wei et al. 2022, refuted by Schaeffer et al. 2023).** Internalize this; it is the highest-leverage update relative to popular discourse.
- ⚪ *Open*: ~10 claims. These are the projects available to research.

## Minute 10–15: one figure, three captions

Look at [`taxonomy.svg`](../taxonomy.svg) (or [`taxonomy.png`](../taxonomy.png)). Read the captions on:

- The "implies" arrow between Programme 01 (Compression) and Programme 02 (Superposition).
- The "implies" arrow between Programme 02 (Superposition) and Programme 03 (Circuits).
- The "in tension with" edge between Programme 04 (ICL-as-Bayes) and the surface-form-sensitivity findings cited in [`programmes/04`](../programmes/04-icl-as-bayes-meta-learning.md).

## Minute 15–25: skim the synthesis essays

You will not have time to read them fully. Read the executive paragraphs of:

- [`compression-and-superposition.md`](../essays/compression-and-superposition.md). The thesis-in-one-paragraph and the falsification-test sections.
- [`emergence-vs-reasoning-models.md`](../essays/emergence-vs-reasoning-models.md). The "Stage 1 / 2 / 3" section.

You should leave with the (correct) intuition that the strong-emergence claim is dead and the test-time-compute axis is alive.

## Minute 25–30: pick the next entry point

You have three sensible next steps, depending on your background:

1. **You are a researcher.** Open [`reading-paths/research-track.md`](research-track.md) and pick an Open Problem from your programme of choice.
2. **You are a practitioner.** Open [`reading-paths/one-weekend-intro.md`](one-weekend-intro.md), pick the programme that matches your work, and plan a weekend.
3. **You want depth.** Open [`reading-paths/one-month-deep-dive.md`](one-month-deep-dive.md). Block 4 weekends in your calendar.

## What you should leave knowing

- The five programmes by name and one-sentence claim.
- That strong emergence is refuted; weak/operational emergence and test-time-compute are alive.
- That circuits and Bayesian-frame ICL are not in tension, just at different levels of abstraction.
- That superposition is the candidate *mechanism* and compression-as-intelligence is the candidate *target*; the two are coupled.
- Where to go next.

## What this is not

A substitute for reading any of the cited papers. 30 minutes buys orientation, not knowledge.
