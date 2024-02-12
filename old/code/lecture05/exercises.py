import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import pandas as pd


## Exercise 1
supermarket = pd.read_csv("supermarket_sales.csv")
rng = np.random.default_rng(seed=313)

def bootstrap_means(x, rng, n_reps=1000):
  """ Bootstrap the means of some data. """
  n = x.size
  samples = np.random.choice(x, (n_reps, n))
  return x.mean() - samples.mean(axis=1)
  
sns.histplot(bootstrap_means(supermarket.Quantity, rng), stat = "density")
sns.histplot(bootstrap_means(supermarket["Unit price"], rng), stat = "density")
supermarket

## Exercise 2
import scipy.stats as st
x = supermarket["Unit price"]
n = x.size
plt.clf()
sns.histplot(bootstrap_means(x, rng), stat = "density")
z = np.linspace(-3, 3, 100)
plt.plot(z, st.norm.pdf(z, 0, x.std()/np.sqrt(n)))
plt.show()

## Exercise 17.1 / 17.2
# Look at the mean and spreads.

## Exercise 17.4
# (a) The mean; just use wikipedia or the book.
# (b) 

number = np.array([0, 1, 2, 3, 4, 5, 6, 7])
obs = np.array([229, 211, 93, 35, 7, 0, 0, 1])
mean = number @ obs / obs.sum()
plt.clf()
plt.plot(number, st.poisson.pmf(number, mean))
plt.bar(number, obs / obs.sum(), color = "orange")
plt.show()

## Exercise 18-1.
# If only distinct n values, n^n.
# But in this case 1 appears twice, there are only (n-1)^n

# No: (1,1,1,1,1,1) is more likely than (2, 2, 2, 2, 2, 2)

## Exercise 18-2
# There are 4^4 possibilities and only one yields (1,1,1,1). 
# The probabiltiy is 1/4^4.

# This happens if 6 is included in the data set. That's 1 - 3^4/4^4
samples = np.random.choice([1,3,4,6], (10000, 4))
np.mean(samples.max(axis = 1) == 6)

# This is the probability of sampling 1 exactly twice, i.e.,
# (1/4)**2 * (3/4)**2
samples.sort(axis=1)
((samples[:,0] == 1) * (samples[:,1] == 1) & (samples[:,2] != 1) & (samples[:,3] != 1)).mean()
