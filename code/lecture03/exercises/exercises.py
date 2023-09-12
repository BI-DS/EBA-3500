# Exericse 13.1

# The “µ ± a few σ” rule. Most of the probability mass of a
# random variable is within a few standard deviations from its expectation.

# U(−1, 1), U(−a, a), N(0, 1), N(µ, σ2), Par (3), Geo(1/2).

rng = np.random.default_rng(seed=313)
n = 100000

randoms = [
  rng.uniform(-1, 1, n),
  rng.uniform(-2, np.pi, n),
  rng.normal(0, 1, n),
  rng.normal(1, 2, n),
  rng.pareto(3, n),
  rng.geometric(0.5, n)]
  
means = [np.mean(x) for x in randoms]
stdevs = [np.std(x) for x in randoms]

def prob(k, x, mean, std):
  """ Approximate P(|X-mean|<k*std)."""
  return (np.abs(x - mean) < k * std).mean() 

k = 1
[prob(k, x, mean, std) for x, mean, std in zip(randoms, means, stdevs)]

def probs(k):
  """ List of approximate probabilities."""
  return [prob(k, x, mean, std) for x, mean, std in zip(randoms, means, stdevs)]

np.array([probs(k) for k in [1, 2, 3, 4]])

# Chebyshev's inequality: P(|Y-\mu|<k*std) >= 1-1/k^2

[round(1-1/k**2, 3) for k in [1, 2, 3, 4]]


# Exercise 13.2
# (a) Either integrate or use wikipedia. mean = (b+a) / 2, 


# Exercise 14.1 

# CLT: Use that the sum has mean approximate 144 * 2 and variance approximately
# 144 * 4 (so standard deviation sqrt(144) * 2)
from scipy.stats import norm
norm.pdf(144, 144 * 2, np.sqrt(144) * 2)

# The uniform distribution on [a,b] has variance
# (b-a)^2/12 = 4 and mean (b+a)/2 = 2. We can solve the first to get
# b = -4a. Then the second equation yields 5^2 a^2 / 12 = 4, so that
# 12 * 4 / 25 = a^2, with b = -4a. It follows that a = - (2 * sqrt(12)) / 5

import numpy as np
rng = np.random.default_rng(seed=313)
a = -2 * np.sqrt(12) / 5
b = -4 * a

# Verify
x = rng.uniform(a, b, 100000)
x.var()
x.mean()

# Simulate
y = rng.uniform(a, b, (144, 100000))
sums = y.sum(axis=0)
(sums > 144).mean()
