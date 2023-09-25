import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

plt.clf()
rng = np.random.default_rng(seed=313)
x = rng.exponential(2, (1000, 100))
medians = np.median(x, axis = 1)
sns.histplot(medians, stat="density")
plt.show()

rng = np.random.default_rng(seed=313)
x = rng.exponential(2, 100)
n = x.size
n_reps = 1000
boots = rng.choice(x, (n, n_reps))
median_boots = np.median(boots, axis = 0)
sns.histplot(median_boots, stat="density")
plt.show()

import pandas as pd
supermarket = pd.read_csv("supermarket_sales.csv")
supermarket.describe()

sns.histplot(supermarket.Quantity)
plt.show()
supermarket.Quantity.describe()

rng = np.random.default_rng(seed=313)
x = supermarket.Quantity
n = x.size
n_reps = 1000
boots = rng.choice(x, (n, n_reps))
std_boots = np.std(boots, axis = 0)
sns.histplot(std_boots, stat="density")
plt.show()
