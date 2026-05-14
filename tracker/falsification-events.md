# Falsification events log

> A chronological record of status changes. Every entry has a date, the affected
> claim, the move, and the citing paper. This file is appended to by
> status-change PRs; do not edit prior entries except to fix typos.

## Format

```
YYYY-MM-DD  CC-LL  <prior> → <new>   Citing: <Authors, "Title", venue, year, URL>
                                    <100–250 word rationale paragraph>
```

Where `CC-LL` is the claim ID (e.g., `01-D`, `04-E`) — programme code, dash, claim letter.

---

## Initial ledger (2026-05-14)

The initial statuses for all 27 tracked claims were set when this repo was
seeded. They are not "events" in the audit-trail sense, but for transparency
the assignments are listed below.

**2026-05-14  Initial statuses set across programmes 01–05.**  The ledger
reflects the literature as of this date. Notable initial verdicts:

- **05-A** strong Wei-style emergence: 🔴 *Refuted*. Citing: Schaeffer, Miranda, Koyejo, *Are Emergent Abilities of Large Language Models a Mirage?*, NeurIPS 2023, [arXiv:2304.15004](https://arxiv.org/abs/2304.15004). The metric-substitution argument is widely accepted; the strong-unpredictable form of Wei et al. 2022 does not survive it. The descriptive form (curves are sharp under exact-match) is retained as 🟢 supported under claim 05-B.

- **04-E** asymptotic-Bayes equilibrium for ICL: 🔴 *Refuted*. Citing: Singh, Chan, Moskovitz, Grant, Saxe, Hill, *The Transient Nature of Emergent In-Context Learning in Transformers*, 2023, [arXiv:2311.08360](https://arxiv.org/abs/2311.08360). ICL can emerge during training and then disappear in favor of in-weights learning, which is inconsistent with a strict reading of "ICL is the asymptotic equilibrium of next-token training on task-mixed data."

- All other claims start at 🟢 / 🟡 / ⚪ per the per-programme ledger tables.

---

## Events from 2026-05-15 onwards

_(none yet — this section will be populated by future status-change PRs)_

---

## Notes for contributors

- **Adding an event.** Use the [`status-change.md`](../.github/ISSUE_TEMPLATE/status-change.md) template; the PR that closes the issue should append to this file.
- **Editing prior events.** Only typos and broken links. If a prior status change was *wrong* (i.e., we now believe the move was unjustified), the right action is a *new* event reversing it, not editing the original.
- **Cross-references.** Each event should link to the issue thread that motivated it and to the affected programme file's ledger row.
