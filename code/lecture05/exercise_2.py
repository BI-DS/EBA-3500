import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd

supermarket = pd.read_csv("supermarket_sales.csv")

x = supermarket.Quantity
n = x.size
n_reps = 10000
rng = np.random.default_rng(seed = 313)
samples = rng.choice(x, (n_reps, n))
means = samples.mean(axis=1)

def bootstrapper(x, rng, n_reps = 1000):
  """ Bootstrap the means of x n_reps times. """
  n = x.size
  samples = rng.choice(x, (n_reps, n))
  return x.mean() - samples.mean(axis=1) 

sns.histplot(bootstrapper(supermarket.Quantity, rng))
sns.histplot(bootstrapper(supermarket["Unit price"], rng))
plt.show()

## Exercise 2
import scipy.stats as st
z = np.linspace(-3, 3, 100)
x = supermarket["Unit price"]
n = x.size()
plt.clf()
boots = bootstrapper(x, rng)
sns.histplot(boots, stat = "density")
plt.plot(z, st.norm.pdf(z, 0, x.std()/np.sqrt(n)))
plt.show()

boots.std()
x.std()/np.sqrt(n)



