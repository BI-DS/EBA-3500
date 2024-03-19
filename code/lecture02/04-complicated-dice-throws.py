import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=666)

# Now let's simulate 100,000 throws.
n = 10**5
values = rng.integers(low=1, high=6 + 1, size=n)

# Let's count the number of 1s, 2s, 3s, et cetera.
uniques, counts = np.unique(values, return_counts=True)

# What happens to sums?
n = 10**5
values1 = rng.integers(low=1, high=6 + 1, size=n)
values2 = rng.integers(low=1, high=6 + 1, size=n)
values = values1 + values2

# Let's count the number of 1s, 2s, 3s, et cetera.
uniques, counts = np.unique(values, return_counts=True)

sns.barplot(data={"values": uniques, "counts": counts}, x="values", y="counts")
plt.show()


# What happens to maximas?
def maximum_throw_plot(m, n=10**6):
    """Makes barplot of the maximum of m throws. Simulated n times."""
    values = rng.integers(low=1, high=6 + 1, size=(n, m)).max(axis=1)
    uniques, counts = np.unique(values, return_counts=True)
    sns.barplot(data={"values": uniques, "counts": counts}, x="values", y="counts")
    plt.show()


maximum_throw_plot(1)
maximum_throw_plot(2)
maximum_throw_plot(100)
