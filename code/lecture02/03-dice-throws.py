import numpy as np

rng = np.random.default_rng(seed=313)
throws = rng.integers(1, 7, size=(10000, 2))
# throws contains 10000 rows of two dice throws.

totals = throws.sum(axis=1)
maxs = throws.max(axis=1)
totals
maxs

# What is the approximate probabiltiy of obtaining a sum of 7?
(totals == 7).mean()

# What is the approximate probabiltiy that the max is 6?
(maxs == 6).mean()

# What is the probability that the total is 7 OR the max is 6?
x = np.logical_or(totals == 7, maxs == 6)
x.mean()

# What is the probability that the total is 7 AND the max is 6?
x = np.logical_and(totals == 7, maxs == 6)
x.mean()

# True probability: 2 * (1/6 * 1/6)


def prob(rng, n_reps=10000):
    throws = rng.integers(1, 7, size=(n_reps, 2))
    totals = throws.sum(axis=1)
    maxs = throws.max(axis=1)
    return np.logical_or(totals == 7, maxs == 6).mean()


prob(rng)

rng1 = np.random.default_rng(seed=313)
rng2 = np.random.default_rng(seed=313)
prob(rng1)
prob(rng2)
