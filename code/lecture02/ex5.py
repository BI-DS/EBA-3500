import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import scipy.stats as st

rng = np.random.default_rng(seed=313)


def sim_beta(a, b, n):
    """Simulate n beta(a,b) variables and plot a histogram."""
    x = rng.beta(a, b, n)
    obj = st.beta(a, b)
    z = np.linspace(0, 1, 10)
    sns.histplot(x, stat="density")
    plt.plot(z, obj.pdf(z))
    plt.show()


sim_beta(2, 7, 10000)
