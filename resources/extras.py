import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pylab as plt

auto = pd.read_csv("Auto.csv", na_values="?")
auto = auto.dropna()
auto = auto.rename(columns={"cylinders":"cyl", "horsepower":"hp", "displacement": "disp", "acceleration":"acc"})

fit = smf.ols("mpg ~ hp", auto).fit()
plt.clf()
plt.scatter(auto.hp, auto.mpg)
plt.plot(auto.hp, fit.params[0] + fit.params[1] * auto.hp)
plt.show()



#sns.pairplot(auto)
#plt.show()
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
auto.drop("name", axis=1).round(decimals=2).corr().round(decimals=2)


taxis = sns.load_dataset("taxis")
taxis.info()

smf.ols("fare ~ color + distance",data=taxis).fit().summary()


plt.scatter(taxis.fare, taxis.tip)
plt.show()
