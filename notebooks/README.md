# Notebooks — runtime, GPU, and reading order

Five teaching notebooks, one per programme. Each one is a *falsifiable claim in notebook form*: the title is the claim, the code either supports or refutes it, and the final cell says what the notebook does and does not show.

| # | Notebook | Claim | Programme | Runtime (T4) | GPU? |
|---|----------|-------|-----------|--------------|------|
| 01 | [`01-compression-ratio-vs-benchmark.ipynb`](01-compression-ratio-vs-benchmark.ipynb) | Bits-per-byte correlates with benchmark score across small open models. | [01](../programmes/01-compression-as-intelligence.md) | ~4 min | optional |
| 02 | [`02-toy-superposition.ipynb`](02-toy-superposition.ipynb) | A bottlenecked model packs more sparse features than dimensions. | [02](../programmes/02-superposition-linear-rep.md) | ~2 min | CPU OK |
| 03 | [`03-induction-head-discovery.ipynb`](03-induction-head-discovery.ipynb) | A small transformer trained on a copy task develops an induction-head signature. | [03](../programmes/03-circuits-and-biology.md) | ~3 min | recommended |
| 04 | [`04-icl-as-bayes-hmm-mixture.ipynb`](04-icl-as-bayes-hmm-mixture.ipynb) | On a synthetic mixture-of-HMMs, ICL tracks Bayes-optimal. | [04](../programmes/04-icl-as-bayes-meta-learning.md) | ~3 min | recommended |
| 05 | [`05-emergence-mirage-demo.ipynb`](05-emergence-mirage-demo.ipynb) | The same task looks emergent under exact-match and smooth under edit-distance. | [05](../programmes/05-emergence-and-reasoning.md) | ~3 min | optional |

## Reading order

If you have one weekend, run them in order 01 → 02 → 03 → 04 → 05. Each notebook builds on the conceptual vocabulary of the previous one without depending on its code.

## Reproducibility

- All notebooks set `numpy`, `torch`, and Python's `random` seeds.
- Versions are pinned in the install cell.
- Figures are saved to `figures/<notebook-id>/`.

## Local installation

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

A minimal `requirements.txt` with pinned versions is in this directory.

## What the notebooks are not

These are teaching artifacts at small scale. They are *not* meant to settle empirical questions about LLMs. The literature does that; the notebooks let you *feel* the phenomenon in 5 minutes so the literature is easier to read.

Each notebook has a final "What this does not show" cell. Read it.
