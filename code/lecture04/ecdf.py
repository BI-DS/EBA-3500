import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF
old_faithful = np.loadtxt("code/lecture04/ch16/old_faithful.dat", dtype=np.float64)

x = np.sort(old_faithful)
def ecdf(x):
  """ Returns the ECDF for the data x, only works for scalars."""
  def fun(y):
    return (x <= y).mean()
  return fun

f = ecdf(x)
f(100)
g = ECDF(x)
g(100)

def ecdf2(x):
  """ Returns the ECDF for the data x. The output function works for sorted and 
  vectorized data."""
  def fun(y):
    return (x <= y).mean()
  return fun


y = np.array([100, 200, 300])


def ecdf2(x):
  """ Returns the ECDF for the data x. The output function works for all vectors."""
  x_sorted = np.sort(x)  
  def fun(y):
    y_sorted = np.sort(y)
    digitized = np.digitize(x_sorted, y_sorted, right=True)
    values, counts = np.unique(digitized,return_counts=True)
    means = np.cumsum(counts[0:-1]) / x.size
    return means
  return fun

y = np.array([200, 100, 300])
g(y)

def ecdf3(x):
  """ Returns the ECDF for the data x. The output function works for all vectors."""
  x_sorted = np.sort(x)  
  def fun(y):
    indices = np.argsort(y)
    y_sorted = np.sort(y)
    digitized = np.digitize(x_sorted, y_sorted, right=True)
    values, counts = np.unique(digitized,return_counts=True)
    means = np.cumsum(counts[0:-1]) / x.size
    return means[indices]
    
  return fun


y = np.array([200, 100, 210, 300])
g(y)
ecdf3(x)(y)
