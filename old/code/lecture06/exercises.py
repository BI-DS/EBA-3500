import numpy as np
import matplotlib.pylab as plt

true_variance = (-3 - 2)**2 / 12
mse = lambda x: np.mean((x - true_variance)**2)

def runner(n):
  """ Approximate the MSE of the variance for sample size n."""
  rng = np.random.default_rng(seed=313)
  x = rng.uniform(-3, 2, (n, 1000))
  hat_ml = (x.max(axis = 0) - x.min(axis = 0))**2 / 12
  hat_samp = np.var(x, axis = 0)
  return mse(hat_samp) / mse(hat_ml) 

runner(5)
runner(10)
runner(100)

ns = (5, 10, 50, 100, 500, 1000, 5000, 10000)
plt.clf()
plt.plot(ns, [runner(n) for n in ns])
plt.show()


x = 0.5
l = lambda delta: np.exp(-(x-delta)) * (x > delta)
deltas = np.linspace(0, 2, 100)
plt.clf()
plt.plot(deltas, l(deltas))
plt.show()
