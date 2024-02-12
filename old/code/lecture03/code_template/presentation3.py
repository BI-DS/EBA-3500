import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import scipy.stats as st

rng = np.random.default_rng(seed=313)
n = 9

# x = rng.uniform(0, 1, (10000, n))
# mu = 1/2
# sigma = np.sqrt(1/12)

x = rng.exponential(1, (10000, n))
mu = 1
sigma = 1

a = 1/2
b = 1
x = rng.gamma(a, b, (10000, n))
mu = a * b
sigma = np.sqrt(a) * b


sums = x.cumsum(axis=1)
sums.shape
ns = (np.arange(n) + 1)[: None]
means = sums / ns

rescaled = (means - mu) * np.sqrt(ns) / sigma

f, axes = plt.subplots(3, 3, figsize=(50, 50), sharex=True)
z = np.linspace(-3,3,100)
for i in range(n):
    ax = axes[i%3, i//3]
    sns.histplot(rescaled[:,i], stat="density",ax=ax)
    ax.plot(z, st.norm.pdf(z))
    ax.set_title(i + 1)
    ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)
    
plt.show()
