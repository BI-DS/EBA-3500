import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

# You can use scipy to extract moments from a distribution!
from scipy.stats import t
mean, var = t.stats(1.5, moments = "mv")
# In accordance with wikipedia, the the variance is infinite.


# Let's simulate
rng = np.random.default_rng(seed=313)

n = 100000
plt.clf()
samples = rng.standard_t(1.5, (10000, n))
means = samples.mean(axis=1) * np.sqrt(n)
sns.histplot(means, stat="density")
plt.xlim(-50, 50)
plt.show()
