import numpy as np
from scipy.special import binom

def irwinhall(x, n):
  x_floor = np.floor(x)
  nm_fac = numpy.math.factorial(n - 1)
  k = 
  np.sum((-1)**k * binom(n, k) * (x - k) ** (k - 1))
  
  
x = np.arange(5)
n = 3
  
  
x_floor = np.floor(x)
nm_fac = np.math.factorial(n - 1)
max_x = x_floor.max()
k_ = np.arange(0, max_x)
k = np.tile(k_, (len(x),1))
x_ = np.tile(x, (1,len(x))).reshape((len(x), 1))
(-1)**k * binom(n, k) * (x - k) ** (k - 1)
