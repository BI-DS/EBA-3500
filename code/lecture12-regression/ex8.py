import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

auto = pd.read_csv("Auto.csv", na_values="?")
auto = auto.dropna()

model = smf.ols("mpg ~ horsepower", data = auto)
fit = model.fit()

fit.summary()

np.corrcoef(auto.mpg,auto.horsepower) ** 2
plt.clf()
plt.scatter(auto.horsepower, auto.mpg)

fit.params
plt.axline(xy1 = (0, fit.params[0]), slope = fit.params[1])
plt.show()


fig = sm.graphics.plot_regress_exog(fit, "horsepower")
fig.tight_layout(pad=1.0)


import seaborn as sns
sns.pairplot(auto)
plt.show()

auto.corr()

formula = "mpg" + "~" + "+".join(auto.columns.difference(["mpg", "name"]))
model = smf.ols(formula, data = auto)
fit = model.fit()
fit.summary()

fig = sm.graphics.plot_regress_exog(fit, "horsepower")

