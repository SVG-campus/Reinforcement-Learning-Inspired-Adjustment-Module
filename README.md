# Reinforcement Learning–Inspired Adjustment Module (Paper 4)

This repository contains a minimal, production‑ready implementation of the **Reinforcement Learning–Inspired Adjustment Module** described in the accompanying paper. The module updates portfolio weights via a simple multiplicative rule linked to a reward signal and then re‑normalizes to maintain a valid probability simplex.

> Update rule: \(w_{t+1} = w_t \cdot (1 + \eta\, r_t)\), followed by positivity clipping and \(\ell_1\)-normalization.

---

## Quick start

```bash
# (optional) create venv
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate

pip install -r requirements.txt
pytest -q
python examples.py
```

---

## Usage

```python
import numpy as np
from rl_adjustment import rl_adjust_weights

w = np.array([0.4, 0.3, 0.3])
# reward can be a scalar (e.g., portfolio reward) or a vector per-asset
r_scalar = 0.02
w_next = rl_adjust_weights(w, r_scalar, eta=0.05)

r_vector = np.array([0.01, -0.02, 0.03])
w_next_vec = rl_adjust_weights(w, r_vector, eta=0.5)
```

Key properties:
- Always returns non‑negative weights that **sum to 1**.
- Accepts either a scalar **reward** (portfolio‑level) or a **vector** (asset‑level signal).
- Raises a helpful error if inputs would collapse the weight vector (e.g., extreme negative rewards with very large `eta`).

---

## Files included

- `rl_adjustment.py` — reference implementation with docstrings.
- `tests/test_rl_module.py` — unit tests validating invariants and behavior.
- `requirements.txt` — minimal Python dependencies.
- `.github/workflows/ci.yml` — CI for tests on push/PR.
- `.github/workflows/release.yml` — lightweight GitHub Release flow on tags (works with Zenodo’s GitHub integration).
- `CITATION.cff` — citation metadata (picked up by GitHub and reference managers).
- `.zenodo.json` — **Zenodo** deposition metadata (includes your ORCID).
- `examples.py` — tiny runnable example and sanity checks.
- `CHANGELOG.md` — version history.
- `LICENSE-CODE` (MIT) and `LICENSE-DOCS` (CC BY 4.0).

> The repository should also contain the paper PDF `Reinforcement_Learning_Inspired_Adjustment_Module.pdf` and the test companion `Tests/Reinforcement_Learning_Inspired_Adjustment_Module(Test).pdf` (as already present in your repo).

---

## ORCID & Zenodo integration (what’s already set up and what this adds)

- **ORCID**: Your ORCID iD is **https://orcid.org/0009-0004-9601-5617**. Once a **DOI** is minted (via Zenodo), add it to your ORCID **Works**. Zenodo will also push author/ORCID metadata automatically if `.zenodo.json` includes your iD (it does).
- **Zenodo ↔ GitHub**: With GitHub connected to Zenodo, **creating a GitHub release** will trigger a Zenodo deposition and mint a DOI. This repo includes:
  - `.zenodo.json` — to pre‑fill authorship (with ORCID), title, description, keywords, license, etc.
  - A `release.yml` workflow that creates a GitHub release whenever you push a tag like `v0.1.0`.

**Checklist to publish a citable version**  
1) Push all code, paper, and tests.  
2) Update version in `CHANGELOG.md` and `CITATION.cff`.  
3) Push a tag, e.g. `git tag v0.1.0 && git push --tags`.  
4) Zenodo will create a record with a **DOI**.  
5) Copy the DOI back into `README.md` (badge), `CITATION.cff` (`identifiers:` block), and (optionally) the repo description.  
6) Add the DOI to your **ORCID Works** if it doesn’t auto‑appear.

---

## Citing

See `CITATION.cff`. After the first Zenodo release, replace the placeholder DOI in the README badge and the BibTeX below.

```bibtex
@misc{rladjust2025,
  title        = {Reinforcement Learning–Inspired Adjustment Module},
  author       = {Villalobos-Gonzalez, Santiago de Jesus},
  year         = {2025},
  note         = {Code and preprint. DOI to be added after first Zenodo release.},
  howpublished = {GitHub + Zenodo}
}
```

---

## Licensing

- **Code**: MIT (see `LICENSE-CODE`).
- **Text/figures/PDFs**: CC BY 4.0 (see `LICENSE-DOCS`).  
  If you prefer a different license, update `LICENSE-DOCS` and `.zenodo.json` accordingly.

---

## Acknowledgements

This repository embeds and tests the method described in the paper **“Reinforcement Learning–Inspired Adjustment Module (Paper 4)”**. Unit tests include simple reward scenarios and sanity checks to help others reproduce the behavior and verify invariants.
