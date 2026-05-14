# Tools — the working stack for "why LLMs work" research

> An opinionated index of the libraries and services this repo's programmes are
> built on. Inclusion criterion: the tool is *load-bearing* for at least one
> programme's standard workflow. We are not trying to be comprehensive — the
> awesome-list competitors do that — we are trying to map *what the working
> researchers in each programme actually use*.

Last updated: 2026-05-14.

---

## At-a-glance

| Tool | Programme(s) | What it does | License |
|------|--------------|--------------|---------|
| [TransformerLens](#transformerlens) | 02 · 03 | White-box transformer analysis (hook into any layer, get activations, intervene). | MIT |
| [SAELens](#saelens) | 02 · 03 | Train, load, and analyze sparse autoencoders on pretrained models. | MIT |
| [nnsight](#nnsight) | 02 · 03 | Lazy-tensor remote-execution interface for inspecting and intervening on large LMs. | MIT |
| [Pyvene](#pyvene) | 03 | Causal-intervention DSL — patch, ablate, swap activations cleanly. | Apache-2.0 |
| [Neuronpedia](#neuronpedia) | 02 · 03 | Hosted interactive feature browser for SAEs on common open models. | hosted service |
| [Goodfire Ember](#goodfire-ember) | 02 · 03 | Commercial interpretability platform; feature-level controls for production LMs. | hosted service |
| [ACDC / EAP](#acdc-and-eap) | 03 | Automated circuit discovery (activation patching + edge-attribution-patching variants). | MIT |
| [circuit-tracer](#circuit-tracer) | 03 | Attribution-graph rendering on top of nnsight; companion to the Anthropic *Circuit Tracing* methodology. | open |
| [datasets / transformers](#hf-stack) | all | Hugging Face stack — loading the models and data that all of the above operate on. | Apache-2.0 |

---

## TransformerLens

- **Repo**: https://github.com/TransformerLensOrg/TransformerLens
- **Original author**: Neel Nanda; now community-maintained.
- **What it is**: A PyTorch library that wraps a wide range of pretrained transformers in a uniform `HookedTransformer` interface, with first-class hooks at every interesting tensor (residual stream, attention pattern, MLP pre- and post-activations, etc.).
- **What it is for**: The standard interpretability backbone. If a paper says "we use TransformerLens," they mean: (a) we loaded the model into a known-shape hook interface; (b) we can record any activation; (c) we can replace any activation; (d) the QK / OV / residual-stream vocabulary of the *Mathematical Framework* paper is built in.
- **Notebook 03** uses it.
- **Related**: [SAELens](#saelens), which builds on TransformerLens conventions.

## SAELens

- **Repo**: https://github.com/jbloomAus/SAELens
- **Original author**: Joseph Bloom; community-maintained.
- **What it is**: Training and analysis infrastructure for sparse autoencoders. Supports gated, JumpReLU, top-K, and vanilla L1 architectures. Loads pre-trained SAE collections from Hugging Face.
- **What it is for**: The standard SAE stack. Programme 02 work either uses SAELens directly or builds on its conventions.

## nnsight

- **Repo**: https://github.com/ndif-team/nnsight
- **Original authors**: Bau lab / NDIF (National Deep Inference Facility).
- **What it is**: A lazy-tensor abstraction for inspecting and intervening on large language models without the per-forward-pass GPU cost of doing it locally. Designed to scale from local Llama-3-8B inspections to remote inspection of frontier-class models hosted by NDIF.
- **What it is for**: When the model is bigger than your single-GPU budget but you still need clean, programmatic interventions.

## Pyvene

- **Repo**: https://github.com/stanfordnlp/pyvene
- **Original authors**: Stanford NLP (Atticus Geiger and collaborators).
- **What it is**: A DSL and library for *causal interventions* — clean syntax for "set this activation to that activation at this position on this layer, then measure that output."
- **What it is for**: When the experiment is "patch X to Y and measure Z" and you do not want to hand-roll the hook bookkeeping.

## Neuronpedia

- **Site**: https://neuronpedia.org
- **Maintained by**: Joseph Bloom, Curt Tigges, and contributors.
- **What it is**: An interactive feature browser for SAEs trained on a curated set of open models (GPT-2 small, Pythia, Gemma-Scope, Llama variants). Each feature has an activation panel, top-activating examples, and explanations.
- **What it is for**: Browsing the dictionary an SAE produced without retraining one yourself. The fastest way to develop intuition for what SAE features look like.

## Goodfire Ember

- **Site**: https://www.goodfire.ai
- **Maintained by**: Goodfire (commercial).
- **What it is**: A commercial interpretability platform offering feature-level control of production LMs via SAE-derived dictionaries plus an API.
- **What it is for**: Productionizing the *applied* end of programmes 02 and 03 — feature-conditioned generation, steering, monitoring. Free tier available at the time of writing.

## ACDC and EAP

- **Repos**:
  - ACDC: https://github.com/ArthurConmy/Automatic-Circuit-Discovery
  - EAP-IG: https://github.com/Aaquib111/edge-attribution-patching
- **What they are**: Algorithms for automated circuit discovery. ACDC (Conmy et al. 2023, [arXiv:2304.14997](https://arxiv.org/abs/2304.14997)) iteratively prunes the model's computation graph by activation patching. EAP-IG (Hanna, Pezzelle, Belinkov 2024, [arXiv:2403.17806](https://arxiv.org/abs/2403.17806)) adds integrated-gradient attribution to scale the methodology.
- **What they are for**: Replicating circuit discoveries without artisanal hand-work; scaling the methodology to larger models.

## circuit-tracer

- **Maintained on the transformer-circuits side**.
- **What it is**: The companion tooling for the Anthropic *Circuit Tracing* methodology (Lindsey et al. 2025). Constructs and renders attribution graphs over replacement models.
- **What it is for**: Reproducing or extending the 2025 attribution-graph case studies.

## HF stack

- **Repos**:
  - `huggingface/transformers`: https://github.com/huggingface/transformers
  - `huggingface/datasets`: https://github.com/huggingface/datasets
- **What it is for**: Loading the models and data. Notebook 01 and notebook 05 lean on the `transformers` API.

---

## Tools we deliberately do not list here

- **Generic ML stacks** (PyTorch, NumPy, scikit-learn). They underlie everything; listing them is noise.
- **Notebook UIs** (Jupyter, Colab). Same reason.
- **Probe libraries** as a category. Linear probing is a method, not a tool you depend on a specific library for.
- **One-off code releases** from individual papers. We cite the papers; if a release becomes a standard, we promote it.

If you think a tool belongs here, open an issue. The criterion is *load-bearing for at least one programme's standard workflow*.

---

## License notes

- TransformerLens, SAELens, ACDC, EAP-IG: MIT-licensed.
- Pyvene: Apache-2.0.
- Neuronpedia and Goodfire Ember: hosted services with their own terms; the open repositories where applicable use permissive licenses.

This index itself is CC-BY-4.0 (per [LICENSE-content](LICENSE-content)).
