import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
boston = pd.read_csv("Boston.csv", na_values="?")
boston.drop(boston.columns[0], axis = 1, inplace = True)

smf.ols("crim ~ zn", boston).fit().pvalues[1]
covariates = set(boston.columns.values.tolist()) - set(["crim"])
formulas = ["crim ~ " + x for x in covariates]
[(formula, smf.ols(formula, boston).fit().pvalues[1]) for formula in formulas]

lst = []

for formula in formulas:
  mod = smf.ols(formula, boston).fit()
  lst.append((formula, mod.rsquared.round(3)))
  
# rad: 0.391
# tax: 0.34

plt.clf()
fit = smf.ols("crim ~ rad", boston).fit()
plt.scatter(boston.rad, boston.crim)
plt.plot(boston.rad, fit.params[0] + fit.params[1] * boston.rad)
plt.show()
  
## (b)
formula = "crim" + "~" + "+".join(covariates)
pvalues_multi = smf.ols(formula, boston).fit().pvalues[1:]

## (c)
pvalues_uni = [(formula, smf.ols(formula, boston).fit().pvalues[1]) for formula in formulas]

plt.clf()
plt.scatter(pvalues_uni, pvalues_multi)
plt.show()

pvalues_uni = sorted(pvalues_uni)
pvalues_uni = [x for _, x in pvalues_uni]

pvalues_multi = pvalues_multi.sort_index()


formula = "crim ~ zn + I(zn**2) + I(zn**3)"

plt.scatter(pvalues_uni, pvalues_multi)
plt.show()



