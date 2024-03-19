import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pprint

boston = pd.read_csv("Boston.csv", na_values="?")
boston.drop(boston.columns[0], axis = 1, inplace = True)

boston.info()
boston.describe()

# (a) Ok
covariates = set(boston.columns.values.tolist()) - set(["crim"])
formulas = ["crim ~ " + x for x in covariates]
fits = [smf.ols(formula, data = boston).fit() for formula in formulas]

pp = pprint.PrettyPrinter(indent=4)
pp.pprint([(i, formulas[i], fit.rsquared.round(2), fit.pvalues[1].round(3)) for i, fit in enumerate(fits)])

plt.clf()
plt.scatter(boston.rad, boston.crim)
plt.plot(boston.rad, fits[10].params[0] + fits[10].params[1] * boston.rad)
plt.show()

plt.clf()
plt.scatter(boston.tax, boston.crim)
plt.plot(boston.tax, fits[2].params[0] + fits[2].params[1] * boston.tax)
plt.show()

# (b) 
formula = "crim" + "~" + "+".join(boston.columns.difference(["crim"]))
fit = smf.ols(formula, boston).fit()
fit.summary()

np.corrcoef(boston.tax, boston.rad)

# (c)
uni = sorted([(formulas[i], fit.params[1]) for i, fit in enumerate(fits)])
uni = [x for (i,x) in uni]
multi = fit.params[1:]

plt.clf()
plt.scatter(uni, multi)
plt.show()

# (d) Strange question. You know there is no-linearity, the cubic regression
# does not answer it.
formulas = ["crim ~ " + x for x in covariates]
fits = [smf.ols(formula, data = boston).fit() for formula in formulas]

formulas3 = [f"crim ~ {x} + I({x}**2) + I({x}**3)" for x in covariates]
fits2 = [smf.ols(formula, data = boston).fit() for formula in formulas3]
pp.pprint([(i, formulas[i], fit.rsquared_adj.round(2), fit.pvalues[3].round(3)) for i, fit in enumerate(fits2)])

pp.pprint([(i, formulas[i], fit.rsquared_adj.round(2) - fits[i].rsquared_adj.round(3)) for i, fit in enumerate(fits2)])

