"""
Logging and diagnostics utilities for LIA simulations.

Provides:
- Consistent logging across all tiers
- Checkpoint saving/loading for debugging
- Diagnostic validation functions
"""

from __future__ import annotations
import logging
import sys
import json
from pathlib import Path
from typing import Any, Dict, Optional
from datetime import datetime
import numpy as np
import numpy.typing as npt

Array = npt.NDArray[np.float64]


# ----------------------------- Logging Setup -----------------------------

def setup_logger(
    name: str,
    log_file: Optional[Path] = None,
    level: int = logging.INFO,
    console: bool = True,
) -> logging.Logger:
    """
    Create a logger with consistent formatting.

    Parameters
    ----------
    name : str
        Logger name (typically __name__ or tier name).
    log_file : Optional[Path]
        If provided, write logs to this file in addition to console.
    level : int
        Logging level (logging.DEBUG, INFO, WARNING, ERROR).
    console : bool
        Whether to also log to console.

    Returns
    -------
    logger : logging.Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()  # Avoid duplicate handlers

    # Consistent format with timestamp, level, name, and message
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console handler
    if console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # File handler
    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# ----------------------------- Checkpointing -----------------------------

class Checkpoint:
    """
    Save/load intermediate results for debugging and reproducibility.

    Stores:
    - Configuration (JSON-serializable dict)
    - Arrays (via .npz)
    - Metadata (run info, timing, etc.)
    """

    def __init__(self, checkpoint_dir: Path, name: str):
        """
        Parameters
        ----------
        checkpoint_dir : Path
            Directory for checkpoints.
        name : str
            Checkpoint name (e.g., "tier1_q1.5_s0.01").
        """
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.name = name
        self.base_path = self.checkpoint_dir / name

    def save(
        self,
        config: Dict[str, Any],
        arrays: Dict[str, Array],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Save a checkpoint.

        Parameters
        ----------
        config : dict
            JSON-serializable configuration (params, hyperparams).
        arrays : dict
            Dictionary of named arrays to save.
        metadata : Optional[dict]
            Additional metadata (timing, git hash, etc.).
        """
        # Save config
        config_path = self.base_path.with_suffix('.config.json')
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)

        # Save arrays
        arrays_path = self.base_path.with_suffix('.npz')
        np.savez_compressed(arrays_path, **arrays)

        # Save metadata
        if metadata is None:
            metadata = {}
        metadata['timestamp'] = datetime.now().isoformat()
        metadata['checkpoint_name'] = self.name

        meta_path = self.base_path.with_suffix('.meta.json')
        with open(meta_path, 'w') as f:
            json.dump(metadata, f, indent=2)

    def load(self) -> tuple[Dict[str, Any], Dict[str, Array], Dict[str, Any]]:
        """
        Load a checkpoint.

        Returns
        -------
        config : dict
            Configuration dict.
        arrays : dict
            Dictionary of arrays.
        metadata : dict
            Metadata dict.
        """
        # Load config
        config_path = self.base_path.with_suffix('.config.json')
        with open(config_path, 'r') as f:
            config = json.load(f)

        # Load arrays
        arrays_path = self.base_path.with_suffix('.npz')
        arrays_npz = np.load(arrays_path)
        arrays = {k: arrays_npz[k] for k in arrays_npz.files}

        # Load metadata
        meta_path = self.base_path.with_suffix('.meta.json')
        with open(meta_path, 'r') as f:
            metadata = json.load(f)

        return config, arrays, metadata

    def exists(self) -> bool:
        """Check if checkpoint exists."""
        config_path = self.base_path.with_suffix('.config.json')
        arrays_path = self.base_path.with_suffix('.npz')
        return config_path.exists() and arrays_path.exists()


# ----------------------------- Diagnostics -------------------------------

def validate_array(
    arr: Array,
    name: str,
    expected_shape: Optional[tuple] = None,
    finite: bool = True,
    bounds: Optional[tuple[float, float]] = None,
    logger: Optional[logging.Logger] = None,
) -> bool:
    """
    Validate array properties and log issues.

    Parameters
    ----------
    arr : Array
        Array to validate.
    name : str
        Name for logging.
    expected_shape : Optional[tuple]
        If provided, check shape matches.
    finite : bool
        If True, check all values are finite (no NaN/Inf).
    bounds : Optional[tuple[float, float]]
        If provided, check values in [low, high].
    logger : Optional[logging.Logger]
        Logger for messages.

    Returns
    -------
    valid : bool
        True if all checks pass.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    valid = True

    # Shape check
    if expected_shape is not None:
        if arr.shape != expected_shape:
            logger.error(f"{name}: shape {arr.shape} != expected {expected_shape}")
            valid = False

    # Finite check
    if finite:
        n_nan = np.isnan(arr).sum()
        n_inf = np.isinf(arr).sum()
        if n_nan > 0:
            logger.error(f"{name}: {n_nan} NaN values detected")
            valid = False
        if n_inf > 0:
            logger.error(f"{name}: {n_inf} Inf values detected")
            valid = False

    # Bounds check
    if bounds is not None:
        low, high = bounds
        n_below = (arr < low).sum()
        n_above = (arr > high).sum()
        if n_below > 0:
            logger.warning(f"{name}: {n_below} values below {low}")
            valid = False
        if n_above > 0:
            logger.warning(f"{name}: {n_above} values above {high}")
            valid = False

    if valid:
        logger.debug(f"{name}: validation passed | shape={arr.shape} | range=[{arr.min():.3e}, {arr.max():.3e}]")

    return valid


def log_summary_stats(
    arr: Array,
    name: str,
    logger: Optional[logging.Logger] = None,
) -> None:
    """
    Log summary statistics for an array.

    Parameters
    ----------
    arr : Array
        Array to summarize.
    name : str
        Name for logging.
    logger : Optional[logging.Logger]
        Logger for output.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    stats = {
        'shape': arr.shape,
        'mean': float(np.mean(arr)),
        'std': float(np.std(arr)),
        'min': float(np.min(arr)),
        'max': float(np.max(arr)),
        'median': float(np.median(arr)),
    }

    logger.info(f"{name} summary: " + " | ".join(f"{k}={v}" for k, v in stats.items()))


def assert_positive(arr: Array, name: str, logger: Optional[logging.Logger] = None) -> None:
    """
    Assert array is positive (for divergences, bandwidths, etc.).

    Parameters
    ----------
    arr : Array
        Array to check.
    name : str
        Name for error message.
    logger : Optional[logging.Logger]
        Logger for messages.

    Raises
    ------
    ValueError
        If array has non-positive values.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    if np.any(arr <= 0):
        n_nonpos = (arr <= 0).sum()
        logger.error(f"{name}: {n_nonpos} non-positive values (min={arr.min():.3e})")
        raise ValueError(f"{name} must be positive")


def check_convergence(
    values: Array,
    name: str,
    rtol: float = 0.01,
    window: int = 5,
    logger: Optional[logging.Logger] = None,
) -> bool:
    """
    Check if a sequence has converged (for iterative methods).

    Parameters
    ----------
    values : Array
        Sequence of values (e.g., divergence over iterations).
    name : str
        Name for logging.
    rtol : float
        Relative tolerance for convergence.
    window : int
        Number of recent values to check for stability.
    logger : Optional[logging.Logger]
        Logger for messages.

    Returns
    -------
    converged : bool
        True if relative change < rtol over the last `window` values.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    if len(values) < window + 1:
        logger.debug(f"{name}: too few values ({len(values)}) to check convergence")
        return False

    recent = values[-window:]
    recent_change = np.abs(recent[-1] - recent[0]) / (np.abs(recent[0]) + 1e-12)

    converged = recent_change < rtol

    if converged:
        logger.info(f"{name}: converged (relative change {recent_change:.3e} < {rtol})")
    else:
        logger.debug(f"{name}: not converged (relative change {recent_change:.3e})")

    return converged
