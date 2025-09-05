import numpy as np
import pytest
from rl_adjustment import rl_adjust_weights

def test_simple_invariants():
    w = np.array([0.5, 0.3, 0.2])
    r = 0.1  # scalar reward
    w2 = rl_adjust_weights(w, r, eta=0.5)
    assert np.all(w2 >= 0)
    assert np.isclose(w2.sum(), 1.0)

def test_vector_reward_behaviour():
    w = np.array([0.4, 0.3, 0.3])
    r = np.array([0.1, -0.2, 0.0])
    w2 = rl_adjust_weights(w, r, eta=0.5)
    # asset 1 should get promoted relative to asset 2, all else equal
    assert w2[0] > w2[1]

def test_extreme_negative_reward_raises():
    w = np.array([0.6, 0.4])
    # very large negative reward with huge eta would collapse without clipping; function guards against that
    with pytest.raises(ValueError):
        rl_adjust_weights(w, reward_signal=-1e9, eta=1e9, clip_min=0.0)
