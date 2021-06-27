from typing import Callable

import numpy as np
import pytest

import bsci


@pytest.mark.parametrize("stat_fcn", [np.mean, np.std], ids=["mean", "std"])
@pytest.mark.parametrize("sample", [np.array([30, 37, 36, 43, 42, 43, 43, 46, 41, 42])])
@pytest.mark.parametrize("seed", [1, 12, 123], ids=["seed1", "seed1", "seed123"])
def test_boostrap_methods(stat_fcn: Callable, sample: np.ndarray, seed: int):
    # Empirical bootstrap
    m_bs, ci_bs_lo, ci_bs_up = bsci.compute_interval(sample, stat_fcn, num_reps=20, alpha=0.1, ci_sides=2, seed=seed)

    # Percentile bootstrap
    # Add one to the seed because with the MD5 seed calculation and so on, the lower quantiles are actually equal by
    # chance. This seems to be the one-in-a-million case for this.
    np.random.seed(seed + 1)
    resampled = np.random.choice(sample, (sample.shape[0], 20), replace=True)
    means = np.apply_along_axis(np.mean, 0, resampled)
    ci_lo, ci_up = np.percentile(means, [5, 95])

    # You should operate on the deltas (empirical bootstrap) and not directly on the statistic from the resampled data
    # (percentile bootstrap)
    assert ci_lo != ci_bs_lo
    assert ci_up != ci_bs_up


@pytest.mark.parametrize(
    "data",
    [np.random.normal(10, 1, (40,)), np.random.normal((1, 7, 13), (1, 1, 1), (40, 3))],
    ids=["1dim-data", "3dim-data"],
)
@pytest.mark.parametrize("num_reps", [100, 1000, 10000], ids=["100reps", "1000reps", "10000reps"])
@pytest.mark.parametrize("seed", [1, 12, 123], ids=["seed1", "seed12", "seed123"])
def test_bootsrapping(data: np.ndarray, num_reps: int, seed: int):
    # Fully-fledged example
    bsci.compute_interval(
        data, np.mean, num_reps, alpha=0.05, ci_sides=2, studentized=True, bias_correction=True, seed=seed
    )

    m, ci_lo, ci_up = bsci.compute_interval(
        data, np.mean, num_reps, alpha=0.05, ci_sides=2, studentized=False, bias_correction=False, seed=seed
    )
    assert np.all(m >= ci_lo)
    assert np.all(m <= ci_up)

    m_bc, ci_lo, ci_up = bsci.compute_interval(
        data, np.mean, num_reps, alpha=0.05, ci_sides=2, studentized=False, bias_correction=True, seed=seed
    )
    assert np.all(m_bc != m)

    m, ci_lo, ci_up = bsci.compute_interval(
        data, np.mean, num_reps, alpha=0.05, ci_sides=1, studentized=False, seed=seed
    )
    m_t, ci_lo_t, ci_up_t = bsci.compute_interval(
        data, np.mean, num_reps, alpha=0.05, ci_sides=1, studentized=True, seed=seed
    )
    assert m == pytest.approx(m_t)
    assert np.all(m_t >= ci_lo_t)
    assert np.all(m_t <= ci_up_t)
    # Bounds are different (not generally wider) when assuming a t-distribution
    assert np.all(ci_lo != ci_lo_t)
    assert np.all(ci_up != ci_up_t)
