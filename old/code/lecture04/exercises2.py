import numpy as np

def mad(x):
    """ Calculate the mad for one array."""
    return np.median(np.abs(x - np.median(x)))

rng = np.random.default_rng(seed=313)
x = rng.normal(0, 1, (1000, 10))

x.mean(axis=0)
x.mean(axis=1)
x.mean()

def mad2(x,axis=None):
    """ Calculate the MAD with an axis argument."""
    if axis is None:
        return mad(x)
    if axis == 0:
        return [mad(y) for y in x.T]
    if axis == 1:
        return [mad(y) for y in x]
    
len(mad2(x, axis=1))
x.mean(axis=1).size
mad(x[:,0])

## 15.1

x = np.array([66, 70, 69, 68, 67, 72, 73, 70, 57, 63, 70, 78,
67, 53, 67, 75, 70, 81, 76, 79, 75, 76, 58])

np.quantile(x, (0.2, 0.4))

import seaborn as sns
import matplotlib.pylab as plt
sns.histplot(x)