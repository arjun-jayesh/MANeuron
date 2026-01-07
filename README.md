give this readme cntnt as is, but the formatting bee perfect- ready to copy paste# Project MA – Experimental Datasets (v1.0) 

This archive contains the raw experimental datasets and plotting scripts associated with the paper:

**Project MA: A Deterministic, Energy-Constrained Framework for Probabilistic Cognitive Modeling**  
Author: Arjun Jayesh  
ORCID: https://orcid.org/0009-0001-8057-3225  

These datasets were generated using a deterministic, event-driven cognitive simulation implemented in Rust and are provided to enable full reproducibility of the experimental results reported in the paper.

---

## Repository Structure


maneuron/
├── src/                      # Rust Source Code (v1.0 Hardened)
│   ├── main.rs               # Simulation Entry Point & Experiment Runner
│   ├── brain.rs              # Event-Driven Orchestrator & Memory Manager
│   ├── neuron.rs             # MA-Neuron Logic (Entropy, Hebbian, Bias)
│   ├── interfaces.rs         # Reality & Meta-Regulator Interfaces
│   ├── config.rs             # Simulation Constants (Energy, Learning Rates)
│   ├── types.rs              # Data Structures (Signal, Hypothesis)
│   └── experiments.rs        # Scientific Experiment Modules
├── datasets/                 # Raw Experimental Data (CSV)
│   ├── results_overload.csv  # Exp 1: Saturation Data
│   ├── results_scaling.csv   # Exp 2: Scaling Data
│   └── results_ablation.csv  # Exp 3: Stability Data
├── scripts/
│   └── generate_plots.py     # Python Plotting Script (Reproducibility)
├── Cargo.toml                # Rust Dependencies & Build Config
├── LICENSE                   # MIT License (Code)
└── README.md                 # Project Documentation


## Dataset Descriptions

### 1. results_overload.csv
**Purpose:** System saturation experiment (Experiment 1)

This dataset records queue dynamics and entropy behavior under progressively increasing input load.

**Columns:**
- `step` — Simulation timestep (integer)
- `queue_len` — Length of the global event queue
- `mean_ent` — Mean normalized Shannon entropy across all neurons

**Used in:** Figure 1 (System Saturation Behavior)

---

### 2. results_scaling.csv
**Purpose:** Network scaling and emergent resonance (Experiment 2)

This dataset captures average firing activity across different network sizes.

**Columns:**
- `n` — Number of neurons in the network
- `mean_firing_rate` — Mean firing rate (Hz), averaged across neurons

**Used in:** Figure 2 (Emergent Activity vs. Scale)

---

### 3. results_ablation.csv
**Purpose:** Structural stability and plasticity ablation (Experiment 3)

This dataset compares connection counts over time between a plastic network and a fixed-topology control.

**Columns:**
- `step` — Simulation timestep
- `links_control` — Total number of connections with plasticity enabled
- `links_ablated` — Total number of connections with plasticity disabled

**Used in:** Figure 3 (Short-Term Structural Stability)

---

## Plotting Script

### generate_plots.py
Python script used to generate all figures reported in the paper directly from the CSV files.

**Dependencies:**
- Python ≥ 3.8
- pandas
- matplotlib

**Usage:**
```bash
python generate_plots.py

This will generate:

figure_1_overload.png

figure_2_scaling.png

figure_3_ablation.png

No smoothing, aggregation, or post-processing is applied.

Reproducibility Notes

All datasets were generated using a fixed deterministic seed (2026).

Pseudo-randomness is implemented via ChaCha20 using Rust’s rand::StdRng.

The simulation is single-threaded and event-driven, ensuring invariant execution order.

Outputs are logged per simulation step directly to CSV.

Under identical parameters, results are bitwise reproducible across platforms.

License

This dataset is licensed under the
Creative Commons Attribution 4.0 International License (CC BY 4.0).

You are free to use, share, and adapt the data for any purpose, provided appropriate credit is given.

License text:
https://creativecommons.org/licenses/by/4.0/

Citation

If you use this dataset in academic work, please cite the associated paper:

Jayesh, A. Project MA: A Deterministic, Energy-Constrained Framework for Probabilistic Cognitive Modeling. Preprint.


Contact

Email: arjunjayesh500@gmail.com

ORCID: https://orcid.org/0009-0001-8057-3225
