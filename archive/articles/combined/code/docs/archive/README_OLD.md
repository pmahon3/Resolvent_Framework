# LIA Numerical Demonstrations

Code for validating the Least-Information Action (LIA) framework through numerical simulations.

## Structure

```
code/
├── common_utils.py      # Core utilities (divergences, IACT, bootstrap, local linear, plotting)
├── logging_utils.py     # Logging, checkpointing, diagnostics
├── test_utils.py        # Validation tests for all components
├── tier1_scalar.py      # Tier 1: One-dimensional controlled dynamics
├── tier3_henon.py       # Tier 3: Hénon map with delay embedding (TODO)
├── tier6_exponents.py   # Tier 6: Dynamical exponents link (TODO)
├── figures/             # Output figures
└── configs/             # Configuration JSONs and checkpoints

```

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Or with conda
conda install numpy scipy matplotlib
```

## Quick Start

### 1. Run validation tests
```python
python -c "
from logging_utils import setup_logger
from test_utils import run_all_tests
import common_utils
import logging

logger = setup_logger('validation', level=logging.INFO)
rng = common_utils.make_rng(42)
results = run_all_tests(common_utils, logger, rng)
"
```

### 2. Run Tier 1 simulation
```bash
python tier1_scalar.py --q 1.5 --sigma 0.01 --seed 42
```

## Tier 1: One-dimensional Controlled Dynamics

**System:** `y_{t+1} = sign(y_t)|y_t|^q + noise`, clamped to [-1,1]

**Goal:** Verify locality exponent η ≈ 2s and learning exponent ζ ≈ 2s/(2s+1)

**Parameters:**
- q ∈ {1.2, 1.5, 2.0, 2.5} (smoothness s ≈ q)
- σ ∈ {0, 0.01, 0.03, 0.1} (noise level)

**Outputs:**
- Learning curves: A(n) vs n_eff
- Locality curves: A(h) vs h
- Fitted slopes η and ζ
- Checkpoints in `configs/`

## Logging

All simulations use consistent logging format:
```
YYYY-MM-DD HH:MM:SS | LEVEL    | MODULE              | MESSAGE
```

Logs include:
- Configuration parameters
- Intermediate diagnostics
- Validation checks
- Timing information

## Checkpoints

Checkpoints save:
- Configuration (JSON)
- Arrays (NPZ compressed)
- Metadata (timing, git hash)

Load with:
```python
from logging_utils import Checkpoint
cp = Checkpoint("configs", "tier1_q1.5_s0.01")
config, arrays, metadata = cp.load()
```
