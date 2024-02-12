ddef boot(indices):
    """Generate a single bootstrap sample using the indices in "indices"."""
    fit = smf.logit("default ~ income + balance", data=default.iloc[[indices]]).fit()
    print(fit)
    print(1)
    return fit


boot([1, 2, 3, 4, 5, 6, 7, 8, 9])

indices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fit = smf.logit("default ~ income + balance", data=default.iloc[indices]).fit()
fit.params
