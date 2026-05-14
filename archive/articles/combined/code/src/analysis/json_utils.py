"""
JSON serialization utilities for converting numpy types to Python natives.

Prevents "TypeError: Object of type X is not JSON serializable"
"""
import numpy as np
from typing import Any, Dict, List


def to_python_type(obj: Any) -> Any:
    """
    Recursively convert numpy types to Python native types.

    Parameters
    ----------
    obj : any
        Object to convert (can be scalar, array, dict, list, etc.)

    Returns
    -------
    converted : any
        Python-native version (float, int, bool, list, dict)
    """
    # Numpy scalars → Python scalars
    if isinstance(obj, (np.integer,)):
        return int(obj)
    elif isinstance(obj, (np.floating,)):
        return float(obj)
    elif isinstance(obj, (np.bool_,)):
        return bool(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()

    # Recursively handle containers
    elif isinstance(obj, dict):
        return {k: to_python_type(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [to_python_type(item) for item in obj]

    # Pass through native types
    elif obj is None or isinstance(obj, (int, float, bool, str)):
        return obj

    # Handle NaN/Inf specially
    elif isinstance(obj, float):
        if np.isnan(obj):
            return None  # or keep as float('nan') if you prefer
        elif np.isinf(obj):
            return None  # or keep as float('inf')
        return obj

    # Fallback: try to convert or return as-is
    else:
        try:
            return float(obj)
        except (TypeError, ValueError):
            return str(obj)


def sanitize_for_json(data: Dict) -> Dict:
    """
    Sanitize a dictionary for JSON serialization.

    Converts all numpy types to Python natives and handles NaN/Inf.

    Parameters
    ----------
    data : dict
        Dictionary potentially containing numpy types

    Returns
    -------
    sanitized : dict
        Dictionary with only JSON-serializable types
    """
    return to_python_type(data)
