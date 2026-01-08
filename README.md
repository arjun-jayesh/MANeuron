[![DOI](https://zenodo.org/badge/1129907660.svg)](https://doi.org/10.5281/zenodo.18181278)

# Project MA

**Project MA: A Deterministic, Energy-Constrained Framework for Probabilistic Cognitive Modeling**

Author: Arjun Jayesh  
ORCID: https://orcid.org/0009-0001-8057-3225  

---

## Overview

Project MA is an experimental cognitive architecture designed to explore how complex, self-organizing behavior can emerge from **local metabolic and entropic constraints**, rather than global loss minimization.

Unlike conventional Artificial Neural Networks trained via backpropagation, Project MA models cognition as a population of autonomous units (MA-Neurons) that operate under:
- Energy budgets
- Entropic uncertainty
- Structural plasticity
- Deterministic event-driven execution

The system is intended as a **research testbed**, not a production AI model.

---

## Core Concepts

### MA-Neuron
Each MA-Neuron maintains an internal state consisting of:
- Metabolic energy
- Entropic uncertainty
- Novelty pressure
- Confidence estimation
- Short-term activation history
- Long-term structural memory (graph)

Learning occurs via **structural plasticity**, not just weight updates.

---

## Execution Phases

### Wake Mode
- Constraint-dominant execution
- Energy-aware signal propagation
- Conservative structural plasticity
- Optimized for stability and survival

### Dream Mode
- Constraint-relaxed internal simulation
- Controlled stochastic noise injection
- Memory consolidation
- Structural rebalancing

Phase separation enables both robustness and adaptability.

---

## Architecture Highlights

- **Event-driven execution** (no global clock)
- **Deterministic replay** via seeded RNG
- **Sparse dynamic graphs**
- **Hebbian LTP + heterosynaptic LTD**
- **Automatic structural pruning**
- **Single-threaded causal scheduling**

All experiments are **fully reproducible**.

---

## Repository Structure
```
project-ma/
├── src/ # Core simulation engine (Rust)
│ ├── neuron/ # MA-Neuron implementation
│ ├── plasticity/ # Learning rules
│ ├── scheduler/ # Event queue & execution
│ └── metrics/ # Entropy, energy, confidence
│
├── scripts/ # Utility and plotting helpers
├── data/ # (Optional) Local experiment outputs
├── Cargo.toml # Rust project configuration
├── README.md # This file
└── LICENSE # Code license

```

(Exact layout may evolve as the project matures.)

---

## Reproducibility

- Deterministic RNG seed: **2026**
- RNG algorithm: **ChaCha20**
- Single-threaded execution
- Ordered event queue
- Per-step CSV logging

Given identical parameters, simulations are **bitwise reproducible** across platforms.

---

## Datasets

All experimental datasets and plotting scripts used in the associated paper are archived separately on Zenodo.

See the dataset record for:
- Raw CSV outputs
- Plot generation scripts
- Detailed dataset README

---

## License

### Code
Choose one (recommended):
- **MIT License** or **Apache 2.0**

### Paper & Datasets
- **Creative Commons Attribution 4.0 (CC BY 4.0)**

Licenses are intentionally permissive to support open research.

---

## Citation

If you use this code, model, or associated datasets in academic work, please cite:

> Jayesh, A. *Project MA: A Deterministic, Energy-Constrained Framework for Probabilistic Cognitive Modeling*. Preprint.

(Use the Zenodo or arXiv DOI once available.)

---

## Scientific Scope

This project does **not** claim:
- Consciousness
- Sentience
- Artificial General Intelligence

Terms such as “confidence”, “dream”, or “novelty” are **mathematical metaphors** for internal state variables.

---

## Contact

- Email: arjunjayesh500@gmail.com  
- ORCID: https://orcid.org/0009-0001-8057-3225
