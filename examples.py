from rl_adjustment import rl_adjust_weights
import numpy as np

if __name__ == "__main__":
    w = np.array([0.4, 0.3, 0.3])
    r = 0.02
    w_next = rl_adjust_weights(w, r, eta=0.1)
    print("w_next:", w_next)
