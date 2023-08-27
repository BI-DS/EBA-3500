import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

rng = np.random.default_rng(seed=313)
x = rng.normal(0, 3, size=1000)
sns.histplot(x, stat="density")
plt.show()

x.mean()  # estimated mean
x.std(ddof=1)  # approximately unbiased standard error

y = np.linspace(-10, 10, 100)


def normal_density(x, mu, sigma):
    return np.sqrt(1 / (2 * np.pi * sigma**2)) * np.exp(
        -0.5 * ((x - mu) / sigma) ** 2
    )


sns.histplot(x, stat="density")
plt.plot(y, normal_density(y, x.mean(), x.std(ddof=1)))
plt.show()

### Simulating many means: The CLT.

x = rng.uniform(0, 1, size=(1000, 100))
means = x.mean(axis=1)
means.shape

sns.histplot(means, stat="density")
plt.show()

y = np.linspace(0.4, 0.6, 100)
sns.histplot(means, stat="density")
plt.plot(y, normal_density(y, means.mean(), means.std(ddof=1)))
plt.show()
