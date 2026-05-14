# Contributing to `awesome-why-llms-work`

This is a curated repository with a strict schema, not an open paper dump. We accept PRs that *raise the standard of evidence*, not ones that increase entry count.

If your PR is rejected, it almost always falls into one of four buckets:

1. The citation could not be verified.
2. The annotation paraphrases the abstract instead of reflecting actual reading.
3. The proposed status change is not backed by a cited paper.
4. The paper is already implicitly covered and adding it would not change a status.

The rest of this document explains how to avoid those.

---

## What we accept

| Contribution type | Template | Reviewer SLA |
|-------------------|----------|--------------|
| Adding a paper to an existing programme | [`paper-suggestion.md`](.github/ISSUE_TEMPLATE/paper-suggestion.md) | 7 days |
| Changing a claim's status (🟢 / 🟡 / 🔴 / ⚪) | [`status-change.md`](.github/ISSUE_TEMPLATE/status-change.md) | 14 days |
| Proposing a new programme | [`new-programme.md`](.github/ISSUE_TEMPLATE/new-programme.md) | 30 days |
| Fixing a typo / dead link / broken notebook | PR directly | 7 days |
| Adding a synthesis essay | Open an issue first | n/a |
| Adding a notebook | Open an issue first | n/a |

Every issue gets a response within the SLA, even if the response is "won't fix; here's why." A repository where issues rot is a dead repository.

---

## Paper-entry schema (every paper entry follows this exactly)

```markdown
- **<Title>** (Year) — *<Authors short>*. [<venue or arXiv ID>](<url>).
  - **Programme**: <01 | 02 | 03 | 04 | 05 | Adjacent>
  - **Claim**: <one sentence — what does this paper claim about why LLMs work?>
  - **Status**: 🟢 Supported / 🟡 Contested / 🔴 Refuted / ⚪ Open
  - **Why it matters**: <≤ 80 words; specific, not abstract-paraphrase>
  - **Falsifies**: <none | "claim X in programme Y" with link>
  - **Reproduces**: <none | mini-notebook NN>
```

### Schema rules

- **Title** is the canonical published title. If preprint and venue title differ, use the venue title and note the arXiv ID.
- **Year** is the year of the *first* public release (arXiv first-version date if not formally published).
- **URL** is the arXiv abs page, OpenReview, ACL Anthology, or DOI — *never* a PDF link directly.
- **Claim** is *the paper's central claim about LLM behavior*, not a description of what the paper does. "Compression ratio linearly predicts benchmark score" — not "Evaluates 31 LLMs across 12 benchmarks."
- **Why it matters** is what we cannot derive from the abstract alone. If you cannot say anything specific, do not submit.
- **Status** must be defensible:
  - 🟢 Supported = at least two independent replications, or the original paper plus an accepted survey, with no published refutation.
  - 🟡 Contested = at least one named credentialed critic with a cited counter-paper.
  - 🔴 Refuted = a cited refuting paper accepted by the community (workshop or above).
  - ⚪ Open = a serious claim with no published replications or refutations yet.
- **Falsifies** lists *specific* claims this paper would falsify if accepted, by programme and short label. "Claim X in programme Y" must point to a heading in the programme file.

---

## Citation verification

Every URL in the repo is checked by [`scripts/verify_citations.py`](scripts/verify_citations.py) in CI. The script:

1. Pulls every `https://arxiv.org/abs/<id>` link.
2. Calls the arXiv API for each ID.
3. Checks that the paper exists, that the year matches the entry's `(Year)`, and that the first author's surname appears in the entry's `Authors short`.

If verification fails, CI blocks the PR. **Do not** disable this check.

DOIs and OpenReview links are validated by HTTP HEAD with a 200 response.

Non-arXiv references (Anthropic blog posts, distill.pub articles, etc.) are checked by [`scripts/check_links.py`](scripts/check_links.py).

---

## Annotation quality bar

Annotations are short on purpose — but they must be *specific*.

**Good** (specific, reflects reading):
> Argues that the "emergence" of CoT-style reasoning at scale disappears under continuous metrics like token-edit-distance; reproduces on three model families and four tasks. Its strongest version — that *all* claimed emergence is metric artifact — has not held up against discrete tasks where any continuous relaxation is contrived.

**Bad** (paraphrases the abstract):
> The authors investigate emergent abilities in LLMs and find that they may be artifacts of evaluation metrics. They propose a new framework.

The second example will be rejected.

---

## Status-change PRs (the most important contribution)

A status change is *the* high-leverage contribution. Every programme file's "Falsification status" section is a list of claim-status pairs; moving one of them requires:

1. A cited paper that supports the move. arXiv ID, OpenReview, or published DOI.
2. A 100–250 word rationale paragraph in the PR description.
3. A new entry in [`tracker/falsification-events.md`](tracker/falsification-events.md) with the date, the claim, the new status, and the citing paper.
4. A maintainer review. We will not merge unilateral status flips even when we agree with them; the public record matters.

Two maintainers must approve a 🟢 → 🔴 or 🔴 → 🟢 transition.

---

## Notebook contributions

If you want to add a notebook:

- Title must be a falsifiable claim. "Compression ratio predicts MMLU on five models" is fine. "Notebook for compression" is not.
- Must run on a free Colab T4 in **< 5 minutes wall-clock**. Test it.
- Pin all dependencies in the install cell.
- Set random seeds. Save figures to `notebooks/figures/<notebook-id>/`.
- Last cell is a 100-word interpretation: *what this shows, what this does not show, what would refute it*. The "does not show" sentence is mandatory.
- Pass `ruff check notebooks/ --select F,E,W,I` and `black --check notebooks/`.

We will close PRs that hand-wave on any of those.

---

## Synthesis essay contributions

A synthesis essay connects two or more programmes. The acceptance bar is high:

- It must propose a *specific* point of contact between the programmes — a shared mechanism, a shared prediction, or a point of disagreement that yields a different empirical prediction.
- It must address the strongest critique of the proposed connection.
- 1,500–4,000 words. Cite ≥ 10 papers across the connected programmes.

Open an issue describing the proposed thesis before writing.

---

## What we will not accept

- ❌ "Big list of papers about X." Send it to one of the [related repos](README.md#related-and-companion-repos) instead.
- ❌ AI-generated annotations passed off as editorial. AI-drafted-then-edited is fine and we use it; AI-pasted is rejected on sight (it usually paraphrases the abstract, which is its tell).
- ❌ Status changes without a cited paper.
- ❌ Promotional submissions of your own work without a status assignment and a falsifier.
- ❌ Anything ad-hominem or political in commentary. Stay on epistemics.

---

## Maintainer conventions

For maintainers and frequent contributors:

- Conventional Commits (`feat:`, `docs:`, `fix:`, `refactor:`, `chore:`).
- One programme = one PR; do not bundle multiple programmes in a single PR.
- Tag PRs with the affected programme label (`programme/01`..`programme/05` or `adjacent`).
- A weekly arxiv ingestion runs Mondays; it opens draft PRs that *we* triage.

---

## Code of Conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). It is short and not a joke. The fast version: argue with the strongest version of the other person's position; do not argue with strawmen or with the person.
