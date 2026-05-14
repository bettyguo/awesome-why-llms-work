# Launch playbook

> Distribution plan for the public launch. **Lives in `_internal/` and is
> committed** per [ADR-0005](../DECISIONS.md). If the playbook embarrasses us
> when read by a stranger, the right fix is to revise the playbook, not hide it.

The launch is executed *after* technical readiness — see the Phase 4 reviewer
checklist in `MASTER_PROMPT_awesome-why-llms-work.md` and the QA tracking in
internal notes.

The strategy is **concentrate every channel inside a 48-hour window** to clear
the bar for trending-list eligibility, then sustain with monthly digests and
periodic synthesis essays.

---

## T-7 days

- Repo is private. All commits land here.
- Pre-share the repo with 5–10 high-trust readers (from `preseed_targets.md`'s
  trust list). Ask for:
  - critique of the five-programme structure,
  - status verdicts they would change,
  - papers we missed at the *consequential* level (not the comprehensive level).
- Solicit 2–3 endorsement quotes from people who actually read the repo (not
  promotional, just honest 1-sentence reactions). Optional — only if natural.
- Submit short pitches to 2–3 newsletters (Import AI, The Sequence, Interconnects).
  Use a 100-word pitch.

## T-2 days

- Make the repo public. **Do not post about it yet.**
- Configure GitHub Topics: `mechanistic-interpretability`, `llm`, `awesome-list`,
  `ai-safety`, `interpretability`, `transformers`, `awesome`, `awesome-llm`.
- Pre-write all launch copy (HN, Twitter/X, Reddit, LinkedIn). Save in
  `_internal/launch_copy.md` (this file does not exist yet — create it during
  the T-2 window).
- Schedule the launch for a **Tuesday or Wednesday, 14:00–16:00 UTC**. (Best
  observed time-of-day for engagement across HN + Twitter US/EU overlap.)

## T-0 launch day (Tuesday or Wednesday, 14:00–16:00 UTC)

Concentrate all channels within 2 hours.

| Time offset | Channel | What |
|-------------|---------|------|
| 00:00 | HN | "Show HN: A falsifiable-hypothesis map of why LLMs work" — title under 65 chars; one-sentence first comment with context. |
| +15 min | Twitter/X | 8–12 tweet thread with `taxonomy.png` in tweet 1. Tag pre-seeded researchers naturally where their work is cited. |
| +30 min | r/MachineLearning | Text post (not link). Title: "Why do LLMs work? I tried to map the five research programmes side-by-side with falsification status. Critique welcome." |
| +45 min | r/MLSafety + LessWrong | Cross-posts. LessWrong post should foreground the methodological essay. |
| +1 hr | LinkedIn | Long-form post. Less technical framing; emphasize the "what should I believe" angle. |
| +2 hr | Discord / Slack | Eleuther, MATS, AI Safety Camp — on-topic, substantive openings only. |
| Throughout T-0..T+6h | Respond | Reply substantively to every comment in the first 6 hours. Promise status updates for valid critiques and follow through. |

## T+1 to T+7 days

- Continue responding to comments. Quality of response in the first week
  determines whether the repo becomes a reference or fades.
- Triage incoming PRs. The first PRs are credibility-establishing; reject low-
  quality ones politely and link to `CONTRIBUTING.md`.
- File the first monthly digest if not yet filed (see `tracker/`).
- Identify the 5 most-engaged commenters; offer them maintainer roles with a
  1-month probation period.

## T+30 to T+90 days

- PR awareness: submit to `sindresorhus/awesome` and 3–5 niche `awesome-*`
  meta-lists.
- Publish the first quarterly synthesis essay (a new one, not one of the four
  seeded ones) — this is the trending-eligibility maintenance step.
- Continue weekly arXiv-ingest triage. Aim for 0 ingest PRs older than 14 days.

---

## Non-goals

- **Stars are not the goal.** The goal is to be *the canonical answer* to "why
  do LLMs work?" Stars are a side effect.
- **Newsletter coverage is not the goal.** Specific status changes appearing
  in *Import AI* because they made the news is a side effect.
- **Being "viral" is not the goal.** A reference repo is read repeatedly; a
  viral repo is read once.

---

## Failure modes and mitigations

| Mode | Mitigation |
|------|-----------|
| HN front-page traffic but few stars / few maintainers | Pre-seed the trust list; respond substantively for 6+ hours. |
| Twitter pile-on over a specific status verdict | Open the `status-change.md` template; respond by inviting the critique into the process; do not get into a fight. |
| Researcher feels misrepresented by an annotation | Take it seriously; the annotation is the contestable part. Open a paper-suggestion issue with the corrected annotation and merge it visibly. |
| Maintainer burnout | Bring on 3 maintainers in the first 30 days. The repo cannot be one person's hobby; it is editorial work. |
| Politicization (AGI timelines, safety doom) | Stay on epistemics. The repo is about *why* models work, not whether they are dangerous. Decline politely. |

---

## Honest closing point

This is a marketing document. The repo's actual value is the *content*. If the
content is good, the marketing matters less. If the content is not good, the
marketing should not paper over it. The Phase 4 reviewer pass exists to make
sure the content is defensible before this playbook fires.

If the playbook ever feels uncomfortable to execute, that is the signal to
slow down and check the content rather than to push harder on the marketing.
