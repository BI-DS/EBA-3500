import numpy as np
import matplotlib.pylab as plt

n = 5
c = np.linspace(0, 1, 100)
plt.clf()
plt.plot(c, c**2/n + (1-c)**2)
plt.show()
