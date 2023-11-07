import pandas as pd
auto = pd.read_csv("Auto.csv", na_values="?")

auto.info()
auto["horsepower"] = pd.to_numeric(auto["horsepower"])

auto.iloc[:,0:-1].min()
auto.iloc[:,0:-1].max()

auto.iloc[:,0:-1].mean()
auto.iloc[:,0:-1].std()

