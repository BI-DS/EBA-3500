import scipy.stats as sp

sp.norm.ppf(0.99)

sp.t.ppf(0.975, 10 - 1)


def tinterval(x, alpha=0.05):
    mean = x.mean()
    std = x.std(ddof=1)
    n = x.size
    t = sp.t.ppf(1 - alpha / 2, n - 1)
