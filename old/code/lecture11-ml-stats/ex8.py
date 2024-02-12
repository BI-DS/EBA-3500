import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pprint

default = pd.read_csv("Default.csv")
default.head()
default.default = (default.default == "Yes") * 1

model = smf.ols("default ~ balance", default).fit()
plt.clf()
plt.scatter(default.balance, default.default)
plt.plot(default.balance, model.predict())
plt.show()


model_logit = smf.logit("default ~ balance", default)
fit_logit= model_logit.fit()
model_probit = smf.probit("default ~ balance", default)
fit_probit = model_probit.fit()
plt.clf()
plt.scatter(default.balance, default.default)
plt.scatter(default.balance, fit_logit.predict())
plt.scatter(default.balance, fit_probit.predict())
plt.legend(["Data", "Logistic regression / Logit","Probit"], loc ="upper left", fontsize = "large", frameon=False) 
plt.show()

fit.summary()

model = smf.probit("default ~ balance", default)


default = pd.read_csv("Default.csv")
default.head()
default.default = (default.default == "Yes") * 1
model = smf.logit("default ~ balance + income + student", default).fit()
model.summary()

default = pd.read_csv("Default.csv")
default.head()
default.default = (default.default == "Yes") * 1
model_small = smf.logit("default ~ student", default).fit()
model_small.summary()

model_big = smf.logit("default ~ balance + student", default).fit()
model_big.summary()
model_big.predict({"student": "Yes", "balance": default.balance.mean()})
model_big.predict({"student": "No", "balance": default.balance.mean()})
model_big.predict({"student": ["Yes", "Yes"], "balance": [default.balance.min(), default.balance.max()]})

model_big.predict()


models = [smf.logit("default ~ balance + student + income", default).fit(),
smf.logit("default ~ balance + student", default).fit(),
smf.logit("default ~ balance + I(balance**2) + student", default).fit(),
smf.logit("default ~ balance", default).fit(),
smf.logit("default ~ balance + income", default).fit()]

models_probit = [smf.probit("default ~ balance + student + income", default).fit(),
smf.probit("default ~ balance + student", default).fit(),
smf.probit("default ~ balance + I(balance**2) + student", default).fit(),
smf.probit("default ~ balance", default).fit(),
smf.probit("default ~ balance + income", default).fit()]

[model.aic.round(2) for model in models_probit]

[model.prsquared.round(3) for model in models]
[model.aic.round(2) for model in models]
