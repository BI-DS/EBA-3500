import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

rng = np.random.default_rng(seed=313)

x_100 = rng.exponential(2, (10000, 100))
x_200 = rng.exponential(2, (10000, 200))

x_100.var()

var_100 = x_100.mean(axis=1).var(ddof = 1)
var_200 = x_200.mean(axis=1).var(ddof = 1)
