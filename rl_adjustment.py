"""
Reinforcement Learning–Inspired Adjustment Module (reference implementation).

Update rule:
    w_{t+1} = w_t * (1 + eta * r_t)

Then enforce non-negativity and normalize to sum to 1.

- `reward_signal` can be a scalar (portfolio-level reward) or a vector aligned
  with `weights` (asset-level signals).
"""
from __future__ import annotations
import numpy as np

def rl_adjust_weights(weights, reward_signal, eta: float = 0.01, clip_min: float = 1e-12):
    """
    Parameters
    ----------
    weights : array-like, shape (n,)
        Current weights (must be non-negative and sum to 1). Will be coerced to float array.
    reward_signal : float or array-like
        Scalar reward or per-asset vector signal. If a vector is provided, it must
        be broadcastable to the shape of `weights`.
    eta : float, default=0.01
        Learning rate / sensitivity to reward.
    clip_min : float, default=1e-12
        Minimum floor to avoid negative/zero-collapse during clipping.

    Returns
    -------
    new_weights : ndarray, shape (n,)
        Updated, non-negative, L1-normalized weights.
    """
    w = np.asarray(weights, dtype=float)
    if np.any(w < 0):
        raise ValueError("`weights` must be non-negative.")
    s0 = w.sum()
    if not np.isfinite(s0) or s0 <= 0:
        raise ValueError("`weights` must have positive finite sum.")
    w = w / s0  # ensure valid simplex input

    # multiplicative update
    new_w = w * (1.0 + eta * np.asarray(reward_signal, dtype=float))
    # clip and renormalize
    new_w = np.maximum(new_w, clip_min)
    s = new_w.sum()
    if not np.isfinite(s) or s <= 0:
        raise ValueError("Weights collapsed; try a smaller eta or valid reward_signal.")
    return new_w / s
