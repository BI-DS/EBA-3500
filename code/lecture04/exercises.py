import numpy as np

rng = np.random.default_rng(seed=313)
x = rng.normal(0, 1, (1000, 10))


### Exercise 1
def mad1(x):
    """Calculate mad for a single array."""
    return np.median(np.abs(x - np.median(x)))


### Exercise 2
def mad2(x, axis=None):
    """Calculate mad with axis argument (only 0 or 1)."""
    if axis is None:
        return mad1(x)
    if axis == 0:
        return [mad1(y) for y in x.T]
    if axis == 1:
        return [mad1(y) for y in x]


def mad3(x, axis=None):
    """Calculate mad with an axis argument (only 0 or 1), faster."""
    medians = np.median(x, axis=axis)
    if axis == 0:
        medians = medians[None, :]
    elif axis == 1:
        medians = medians[:, None]
    return np.median(np.abs(x - medians), axis=axis)


### Exercise 3


def ecdf(x):
    """Make an empirical CDF."""

    def fun(y):
        return np.mean(x <= y)

    return fun


ecdf_fun = ecdf(x[0, :])

import seaborn as sns
import matplotlib.pylab as plt
from statsmodels.distributions.empirical_distribution import ECDF

ecdf_fun_2 = ECDF(x[0, :])

ecdf_fun_2(0.3)
ecdf_fun(0.3)

## Plotting.

sns.ecdfplot(x=x[0, :])
y = np.sort(x[0, :])
plt.plot(y, [ecdf_fun(z) for z in y])
plt.show()


sns.ecdfplot(x=x[0, :])
y = np.sort(x[0, :])
plt.step(y, [ecdf_fun(z) for z in y], where="post")
plt.show()

## Exercise 4

data = np.array(
    [
        66,
        70,
        69,
        68,
        67,
        72,
        73,
        70,
        57,
        63,
        70,
        78,
        67,
        53,
        67,
        75,
        70,
        81,
        76,
        79,
        75,
        76,
        58,
    ]
)

plt.clf()
sns.histplot(data)
plt.show()

## 16.1
x = rng.normal(0, 1, 100)
quants = np.quantiles(x, (0.25, 0.37, 0.5, 0.75))
IQR = quants[-1] - quants[0]
median = quants[2]
q37 = quants[1]

# 16.6: Blackboard
