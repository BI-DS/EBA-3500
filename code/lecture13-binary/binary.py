import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

hurr = pd.read_excel("hurricanes.xlsx").drop(["RowNames", "Number"], axis = 1)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
hurr.drop("Name", axis = 1).corr()

hurr["Type_new"] = (1 - 1 * (hurr["Type"] == 0))
sns.lmplot(hurr, x = "FirstLat", y = "Type_new", logistic = True)
plt.show()

import statsmodels.formula.api as smf

smf.logit("Type_new ~ FirstLat + MaxLat+ LastLon + MaxInt", data = hurr).fit().aic
smf.logit("Type_new ~ FirstLat + LastLon + MaxInt", data = hurr).fit().aic
smf.logit("Type_new ~ FirstLat + MaxLat+ LastLat + LastLon + MaxInt", data = hurr).fit().aic
smf.logit("Type_new ~ FirstLat + MaxLon + MaxLat+ LastLat + LastLon + MaxInt", data = hurr).fit().aic
smf.probit("Type_new ~ FirstLat + MaxLon + MaxLat+ LastLat + LastLon + MaxInt", data = hurr).fit().aic
smf.probit("Type_new ~ FirstLat + MaxLat+ LastLat + LastLon + MaxInt", data = hurr).fit().aic


import pandas as pd
url = "https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"
bank = pd.read_csv(url)
bank.head()
smf.logit("y ~ marital + job", data = bank).fit().summary()

set(bank.marital)
set(bank.job)

# Interpretation: Log-odds.
#  log(P(Y=1) / P(Y=0))
#  log(p) - log(1-p) = beta*x
#  log(p[x_i+1]) - log(1-p[x_i+1]) - (log(p[x]) - log(1-p[x])) = beta_i
#  log(p[x_i+1] / (1-p[x])) = beta_i


smf.logit("y ~ marital", data = bank).fit().aic
smf.logit("y ~ job", data = bank).fit().aic
smf.logit("y ~ marital + job", data = bank).fit().aic

import numpy as np
# 6 (a)
betas = [-6, 0.05, 1]
f = lambda x: np.exp(betas[0] + x[0] * betas[1] + x[1] * betas[2]) / (1 + np.exp(betas[0] + x[0] * betas[1] + x[1] * betas[2]))
f([93.94, 3.5])

(-betas[0] - betas[2] * 3.5) / betas[1]

(np.log(0.9/0.1) -betas[0] - betas[2] * 3.5) / betas[1]


boston = pd.read_csv("Boston.csv")
boston.info()
boston.corr().crime_new

smf.logit("crime_new ~ nox + dis + tax + indus", data = boston).fit().summary()

smf.logit("crime_new ~ nox + dis + tax + indus", data = boston).fit().aic
smf.logit("crime_new ~ nox + tax + indus", data = boston).fit().aic

boston["crime_new"] = 1 * (boston.crim >= np.median(boston.crim))
smf.logit("crime_new ~")

model = smf.ols("y ~ job + marital", data = bank).fit()

set(bank.marital)
set(bank.job)


model.predict({"marital": "divorced", "job": "admin."})


