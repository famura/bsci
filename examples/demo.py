"""
This scripts allows to play with the 4 parameters of the backlash model.

Based on matplotlib's interactive slider demo

.. seealso::
    https://matplotlib.org/3.1.1/gallery/widgets/slider_demo.html
"""
import itertools

import matplotlib.pyplot as plt
import numpy as np

from bsci import compute_interval

if __name__ == "__main__":
    np.random.seed(0)

    # Here we use the mean as the statistic of interest
    stat_fcn = np.mean

    # Generate some data
    mean, std = 2, 3
    num_samples = 40
    num_bs_repetitions = [100, 1000]
    alphas = [0.05, 0.1]
    data = mean + std * np.random.randn(num_samples)

    for num_reps in num_bs_repetitions:

        num_rows, num_cols = 2, 2
        fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 10))

        for idx, (alpha, bias_correction) in enumerate(itertools.product(alphas, (True, False))):
            stat_emp = stat_fcn(data)
            stat_ret, ci_lo, ci_up = compute_interval(
                data, stat_fcn, num_reps=num_reps, alpha=alpha, ci_sides=2, bias_correction=bias_correction, seed=0
            )

            n, bins, patches = axs[idx // num_cols, idx % num_cols].hist(
                data, num_samples // 5, density=True, alpha=0.7
            )

            axs[idx // num_cols, idx % num_cols].axvline(stat_emp, label="empirical stat", c="k", ls="--", lw=2)
            axs[idx // num_cols, idx % num_cols].axvline(ci_lo, label=f"ci lower = {ci_lo[0]:.5f}", c="C1")
            axs[idx // num_cols, idx % num_cols].axvline(stat_ret, label=f"bs stat = {stat_ret[0]:.5f}", c="C2")
            axs[idx // num_cols, idx % num_cols].axvline(ci_up, label=f"ci upper = {ci_up[0]:.5f}", c="C3")

            axs[idx // num_cols, idx % num_cols].grid(True)
            plt.get_current_fig_manager().canvas.manager.set_window_title(
                f"{num_samples} data samples, {num_reps} bootstrap repetitions"
            )
            axs[idx // num_cols, idx % num_cols].set_title(f"alpha {alpha}, bias_correction {bias_correction}")
            axs[idx // num_cols, idx % num_cols].legend()

    plt.show()
