import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

auto = pd.read_csv("Auto.csv", na_values="?")
auto = auto.dropna()

model = smf.ols("mpg ~ horsepower", auto)
fit = model.fit()
fit.summary()

plt.clf()
plt.scatter(auto.horsepower, auto.mpg)
plt.plot(auto.horsepower, fit.params[0] + fit.params[1] * auto.horsepower )
plt.show()

### Exericse 9

import seaborn as sns

sns.pairplot(auto)
plt.show()
auto.corr()

# Linear regression
formula = "mpg" + "~" + "+".join(auto.columns.difference(["mpg", "name"]))
model = smf.ols(formula, auto)
fit = model.fit()
fit.summary() # 0.816

rem = ["mpg", "name", "cylinders", "horsepower", "acceleration"]
formula2 = "mpg" + "~" + "+".join(auto.columns.difference(rem))
model2 = smf.ols(formula2, data = auto)
fit2 = model2.fit() # 0.816

rem = ["mpg", "name", "cylinders", "horsepower", "acceleration", "displacement"]
formula3 = "mpg" + "~" + "+".join(auto.columns.difference(rem))
model3 = smf.ols(formula3, data = auto)
fit3 = model3.fit() # 0.816

