# Frequently asked questions

> Questions we expect readers to have, with honest answers. If your question is
> not here, open an issue — if we get it twice we add it.

---

### Why five programmes? Why not four, or six?

It is a curatorial judgement. The defense is in [DECISIONS.md](DECISIONS.md), ADR-0003. Five gave us five distinct hard cores with named proponents *and* named critics across the boundary; four collapsed Superposition and Circuits in ways the literature does not; six promoted Singular Learning Theory or Platonic Representation before they had developed evidence ledgers. The five-programme structure is not load-bearing: the [adjacent appendix](programmes/adjacent-programmes.md) names the candidates and the promotion criterion. We will move to six the moment one of the adjacent programmes meets the bar.

---

### Isn't your taxonomy a research claim, and isn't it contested?

Yes, and yes. We are explicit about it in the [methodological essay](essays/how-to-falsify-an-llm-theory.md). The right response is not to hide the taxonomy but to make it visible, defensible, and revisable. The synthesis essays do most of the work of showing that the five-programme structure is *productive* (it generates testable inter-programme predictions); the falsification ledger does most of the work of showing that it is *humble* (most claims are not at full confidence).

---

### How do I disagree with a status verdict?

Open a [status-change issue](.github/ISSUE_TEMPLATE/status-change.md). The bar is: a cited paper that supports the move plus a 100–250 word rationale. 🟢 ↔ 🔴 transitions require two maintainer approvals; smaller transitions need one. We do not block on unanimity; we block on evidence.

---

### Why isn't *scaling laws* a programme?

Scaling laws are a *measurement framework*, not a *theory*. They describe how loss / capability changes with parameters, data, and compute; they do not (by themselves) say *why* models work. Programmes 01 (Compression) and 05 (Emergence) both make heavy use of scaling-law machinery, but neither is reducible to scaling laws. If you read a "scaling-laws paper" carefully, it almost always rests on one of the five programmes' hard cores.

If you disagree, propose it as a new programme via the [new-programme issue template](.github/ISSUE_TEMPLATE/new-programme.md). The promotion criterion is real, not symbolic.

---

### Why isn't *RLHF / alignment / RLAIF* a programme?

Out of scope. This repo is about *why pretrained models work*, not *how to fine-tune them safely*. Alignment research is important and contiguous, but its hard cores and falsifiers are about *behavior shaping*, not *what the pretrained model has*. The reasoning-models wave (programme 05) intersects RLHF only because RL-on-outcome-rewards is the elicitation mechanism for capabilities that we argue are mostly latent in the base model.

---

### Why isn't *mesa-optimization* a programme?

We track it. It sits at the intersection of programmes 03 (circuits as internal optimizers) and 04 (ICL as in-context optimization). The von Oswald et al. (2023) line on "transformers learn in-context by gradient descent" is the empirical edge of mesa-optimization most directly. It is not its own programme today because (a) its strongest empirical content is already inside programme 04, and (b) the alignment-flavored framing of mesa-optimization (Hubinger et al. 2019) is about a hypothetical safety failure, not about *why models work*. If empirical work develops a distinct hard core, we will promote it.

---

### Notebooks: why are these so small?

Two reasons. (1) The notebooks are *teaching artifacts*, not research artifacts. The point is to develop intuition in 5 minutes, not to convince the reader of an empirical claim. (2) Each notebook has a "what this does *not* show" cell that is mandatory — we are loud about scale limitations to mitigate the obvious failure mode of overgeneralizing from a 4-model fit.

If you want the real evidence, the notebooks point to the canonical papers.

---

### Notebook X did not run in 5 minutes on my machine.

The "<5 min" target is for a free Colab T4. On a CPU, expect 20–40 min for notebook 01 (model downloads); on a slower GPU, expect 1–3× the times in the README. If the *T4 wall-clock* itself is wrong on your run, file an issue with the GPU type and the actual runtime — the target is verifiable.

---

### Why are some of the references blog posts and not papers?

Two categories of blog posts get cited:

- **The Anthropic transformer-circuits thread** is the canonical venue for several of programme 02 and programme 03's load-bearing results (e.g., *Toy Models of Superposition*, *Towards Monosemanticity*, *Circuit Tracing*). The format is a blog post; the content is research. We cite it the way the field does.
- **The OpenAI o1 blog post** (programme 05) is the only major release in the reasoning-models wave that does not have a formal companion paper at the time of writing. We cite the blog post and note the absence of a paper; DeepSeek-R1 and s1 are the corresponding peer-reviewed-or-arXiv-published reproductions, and we cite them too.

We do *not* cite SubStack threads, Twitter/X posts, or LessWrong shortform without an accompanying primary source.

---

### Do you have a paper I can cite?

No, the repo is the artifact. The BibTeX entry in the README is the citation. If you would like to write a paper that *uses* the repo's framing (e.g., "we evaluate against the five-programme map of …"), please get in touch — we are happy to contribute a methods paragraph for the repo's structure.

---

### Why are PRs so strict?

Because the repo's value collapses if entries become slop. The strict schema is what lets us claim, in good faith, that every entry is defensible. PRs that follow the schema and reflect actual reading get merged quickly. PRs that are AI-pasted abstracts get rejected. We are explicit about this in [CONTRIBUTING.md](CONTRIBUTING.md).

---

### How do I become a maintainer?

We invite 3 maintainers in the first 30 days from the most-engaged contributors (substantive issue replies, high-quality PRs, status-change rationales). After that, the same pattern. There is a 1-month probation period before merge rights. The criterion is editorial judgement, not contribution count.

---

### Why is the launch playbook in the repo?

Per [ADR-0005](DECISIONS.md): a research-curation repo's reputation depends on transparency about its process. Hiding the playbook signals defensiveness; publishing it signals confidence. The playbook itself is written to be readable by a stranger, and the rule is: if executing it embarrasses us, we revise the playbook, not the visibility.

---

### Why not just summarize a survey paper?

Surveys describe the literature. This repo *takes positions* on the literature. The two are not substitutes. Where a good survey exists per programme we link to it in the "Surveys and reviews" section of the programme file; the programme file's body is not a survey paraphrase but a falsification-anchored map.

---

### Where does the "biology of LLMs" framing come from?

Chris Olah and the Anthropic interpretability team use it deliberately: interpretability is *fieldwork inside an organism*, not deduction from architecture. The framing is methodological — it argues for careful empirical investigation of trained models the way a biologist investigates a creature, rather than reasoning purely from first principles about what the architecture *should* do. Programme 03 inherits the framing.

---

### Is the repo only about decoder-only transformers / autoregressive LLMs?

In its current scope, yes. The programmes are stated in language general enough to apply to encoder-decoders, masked LMs, and multimodal extensions, but the citation base is heavily autoregressive-LLM-centric because that is where the modern literature is. If you have specific encoder/multimodal evidence for or against a claim, the contribution is welcome.

---

### Why CC-BY-4.0 instead of CC0?

CC0 disclaims attribution. We want attribution — it is how curated work gets traced back and how downstream readers find the audit trail. CC-BY-4.0 is the lightest license that preserves attribution; commercial use is fully allowed.

---

### Is anything in this repo trying to be safety / alignment commentary?

No. The repo is about epistemics: which claims about *why models work* are supported, contested, refuted, or open. Many of the cited papers are safety-relevant, and the choice of programmes (especially Circuits and Superposition) reflects interpretability's heavy overlap with safety. But the editorial stance is descriptive, not advocacy: we describe what the literature supports, not what we wish were true. Programme files are deliberately silent on AGI timelines.
