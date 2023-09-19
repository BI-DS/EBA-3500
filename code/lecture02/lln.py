import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import seaborn as sns

rng = np.random.default_rng(seed=313)
x = rng.uniform(0, 1, 10000)
means = np.cumsum(x) / (np.arange(len(x)) + 1)
