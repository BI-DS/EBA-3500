import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import scipy.stats as st

rng = np.random.default_rng(seed=313)


def sum_throw(throw, rng, n_reps=10000):
    """Make barplot of sums of throw throws."""
    x = rng.integers(1, 7, (n_reps, throw))
    sums = x.sum(axis=1)
    uniques, counts = np.unique(sums, return_counts=True)
    sns.barplot(data=None, x=uniques, y=counts)
    plt.show()


sum_throw(7, rng)


def expected_sum_throw(throw, rng, n_reps=10000):
    """Make barplot of sums of throw throws."""
    x = rng.integers(1, 7, (n_reps, throw))
    sums = x.sum(axis=1)
    uniques, counts = np.unique(sums, return_counts=True)
    return uniques @ (counts / n_reps)


throw = 2
n_reps = 1000
x = rng.integers(1, 7, (n_reps, throw))
sums = x.sum(axis=1)
uniques, counts = np.unique(sums, return_counts=True)

uniques, counts = np.unique(sums, return_counts=True)
