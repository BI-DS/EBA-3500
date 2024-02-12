import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import scipy.stats as st

plt.clf()
rng = np.random.default_rng(seed=313)
x = rng.exponential(1, 10000)
means = np.cumsum(x) / (np.arange(len(x)) + 1)
plt.plot(means)
plt.axhline(y = 1)
plt.show()

# Infinite mean: You can use scipy to extract moments from a distribution!
mean, var = st.t.stats(2, moments = "mv")
# In accordance with wikipedia, the the variance is infinite.

plt.clf()
rng = np.random.default_rng(seed=313)
x = rng.standard_t(2, 10000)
means = np.cumsum(x) / (np.arange(len(x)) + 1)
plt.plot(means)
plt.axhline(y = 0)
plt.show()
