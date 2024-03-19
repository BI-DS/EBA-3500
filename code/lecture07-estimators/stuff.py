import numpy as np
import matplotlib.pylab as plt

rng = np.random.default_rng(seed=313)
x = rng.exponential(1, 10)

l = lambda lamb: x.size * np.log(lamb) - lamb * x.sum()

lambs = np.linspace(0.001, 2, 100)
plt.clf()
plt.plot(lambs, l(lambs))
plt.axvline(x=1)
plt.show()


import numpy as np
import matplotlib.pylab as plt

rng = np.random.default_rng(seed=313)
x = rng.exponential(1, (10, 1000))
lambda_hats = 1/x.mean(axis = 0)
median_hat_ml = np.log(2) / lambda_hats
median_hat_samp = np.median(x, axis = 0)

mse = lambda x: np.mean((x - np.log(2))**2)

mse(median_hat_ml)
mse(median_hat_samp)

mse(median_hat_samp) / mse(median_hat_ml)


import matplotlib.pylab as plt

rng = np.random.default_rng(seed=313)
x = rng.uniform(-3, 2, (100, 1000))
true_variance = (-3 - 2)**2 / 12
mse = lambda x: np.mean((x - true_variance)**2)
hat_ml = (x.max(axis = 0) - x.min(axis = 0))**2 / 12
hat_samp = np.var(x, axis = 0)


mse(hat_samp)
mse(hat_ml)
mse(hat_samp) / mse(hat_ml)
