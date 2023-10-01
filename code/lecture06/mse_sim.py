import numpy as np

rng = np.random.default_rng(seed=313)
n = 100
n_reps = 10000
lambda0 = 2
mse = lambda x: np.mean((x - lambda0)**2)
x = rng.exponential(1/lambda0, (n_reps, n))

lambda_1_hats = 1 / x.mean(axis = 1)
lambda_2_hats = np.log(2) / np.median(x, axis = 1)
lambda_3_hats = np.sqrt(1 / x.var(axis = 1))

mse(lambda_1_hats)
mse(lambda_2_hats)
mse(lambda_3_hats)
