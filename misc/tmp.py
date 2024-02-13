import numpy as np
from quickBayes.fit_functions.gaussian import Gaussian as func
from quickBayes.functions.composite import CompositeFunction
from quickBayes.fitting.scipy_engine import ScipyFitEngine
from quickBayes.log_likelihood import loglikelihood
# generate some data
x = np.linspace(0,10, 100)
noise = 1 + 0.1 * (np.random.normal(0, .2, len(x)))
gauss = func()
ground_truth = gauss (x, 103, 4.2, .9)
y = ground_truth * noise
e = np.sqrt(y) # normal for count data
# construct fit functions
gauss_2 = func()
two_peaks = CompositeFunction()
two_peaks.add_function(gauss)
two_peaks.add_function(gauss_2)
# do fitting
engine = ScipyFitEngine(x, y, e, lower=[0, 0, 0], upper=[200, 10, 10], guess=[100, 5, 1.2])
engine.do_fit(x, y, e, g)
chi_2 = engine.get_chi_squared()
# calculate loglikelihood
beta = np.max(y) * (np.max(x) - np.min(x))
loglike = loglikelihood(len(x), chi_2, engine.get_covariance_matrix(), 1, beta)
# report results
print("one peak", engine.get_fit_parameters(), chi_2, loglike)

# for two peaks
engine.set_guess_and_bounds([100, 5, 1.2, 100, 5, 1.2], [0, 0, 0, 0, 0, 0], [200, 10, 10, 200, 10, 10])
engine.do_fit(x, y, e, two_peaks)
chi_2 = engine.get_chi_squared()
loglike = loglikelihood(len(x), chi_2, engine.get_covariance_matrix(), 1, beta)
print("two peaks", engine.get_fit_parameters(), chi_2, loglike)
