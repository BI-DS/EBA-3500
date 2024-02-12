import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels as sm
auto = pd.read_csv(
    "solutions/applied/data/Auto.csv", na_values="?", index_col="name"
).dropna()
auto.replace({"origin": {1: "American", 2: "European", 3: "Japanese"}}, inplace=True)
auto.head()

fit = smf.ols("mpg~horsepower", data=auto).fit()
summary = fit.summary()
dir(fit)

fit.summary2()

sm.