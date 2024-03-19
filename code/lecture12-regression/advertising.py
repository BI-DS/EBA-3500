import numpy as np
import pandas as pd
import statsmodels as sm
import statsmodels.formula.api as smf

advertising = pd.read_csv("code/lecture12-regression/Advertising.csv")
advertising.head()

model = smf.ols("sales ~ TV + radio + newspaper", data = advertising)
fit = model.fit()
fit.summary()

model = smf.ols("sales ~ TV + radio", data = advertising)
fit = model.fit()
fit.summary()

def ols(y, x):
    """ Returns the parameters a, b, estimated by simple OLS."""
    y_bar = y.mean()
    x_bar = x.mean()
    beta1 = ((x-x_bar) * (y-y_bar)).sum() / ((x-x_bar)**2).sum()
    beta0 = y_bar - beta1 * x_bar
    return (beta0, beta1)
  
x = advertising.TV
y = advertising.sales
ols(y, x)
model = smf.ols("sales ~ TV", data = advertising)
fit = model.fit()
fit.params

import pandas as pd
import statsmodels as sm
import statsmodels.formula.api as smf

advertising = pd.read_csv("code/lecture12-regression/Advertising.csv")
advertising.head()
model = smf.ols("sales ~ TV", data = advertising)
fit = model.fit()
fit.params

model = smf.ols("sales ~ TV + radio + newspaper", data = advertising)
fit = model.fit()
fit.rsquared_adj

model = smf.ols("sales ~ TV + radio", data = advertising)
fit = model.fit()
fit.rsquared_adj
