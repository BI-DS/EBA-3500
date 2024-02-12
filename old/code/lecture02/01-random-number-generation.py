import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

# Make a random number generator.

rng = np.random.default_rng(seed=313)
# rng

# Find its methods by writing dot! One of the main benefits of using
# e.g. VSCode instead of Jupyter notebooks.
# rng. explore.


# Random integers
rng.integers(0, 10, size=10)
rng.integers(0, 10, size=(2, 10))

# Uniform variables / also random
rng.uniform(0, 1, size=10)
rng.uniform(0, 1, size=(2, 10))

# See what it looks like:
x = rng.uniform(0, 3, size=10000)

import seaborn as sns
import matplotlib.pylab as plt

sns.histplot(x, stat="probability")
plt.show()

rng1 = np.random.default_rng(seed=313)
rng2 = np.random.default_rng(seed=313)

rng1.uniform(0, 1, size=(2, 2))
rng2.uniform(0, 1, size=(2, 2))

rng1 = np.random.default_rng()
rng2 = np.random.default_rng()
rng1.uniform(0, 1, size=(2, 2))
rng2.uniform(0, 1, size=(2, 2))

rng1 = np.random.default_rng(seed=313)
rng2 = np.random.default_rng(seed=313)
x = rng1.uniform(2, 5, size=(2, 2))  # starting at 2 and ending at 5,
y = rng2.uniform(0, 1, size=(2, 2))  # starting at 0 and ending at 1.

x
3 * y + 2

# Generate an array of uniformly distributed numbers on $[1,5]$ with
# $3$ rows and $4$ columns.

z = rng.uniform(1, 6, size=(3, 4))
