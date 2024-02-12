import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the book first!

# 1. Box plots are *old fashioned*, from a time without PCs.
#    (Popularized in 1970)
# 2. Box plots are used in scientific papers, so you need to understand
#    them somewhat.
# 3. Box plots are not very suitable for communication outside science,
#    use violin plots instead.

supermarket = pd.read_csv("supermarket_sales.csv")
sns.set(style="whitegrid")

sns.boxplot(x="cogs", y="City", data=supermarket)
plt.show()
plt.clf()

# Explanation of the box plot.
yangon = supermarket[supermarket.City == "Yangon"].cogs
quantiles = np.quantile(yangon, [0.25, 0.5, 0.75])
iqr = quantiles[2] - quantiles[0]  # 75th percentile - 25th percentile.
1.5 * iqr + quantiles[2]

# There are many variants of the box plot out there, and they rarely specify
# which convention they adhere to.

# You can more variables to the plot.
sns.boxplot(x="cogs", y="City", hue="Customer type", data=supermarket)
plt.show()
plt.clf()

# Superior option: Violinplots! Multple kdes.
sns.violinplot(x="cogs", y="City", data=supermarket)
plt.show()
plt.clf()

# Comparison with violin plot.
plt.figure(1)
sns.violinplot(x="cogs", y="City", data=supermarket)
plt.figure(2)
sns.boxplot(x="cogs", y="City", data=supermarket)
plt.show()

# Violin plots with more colors.
sns.violinplot(x="cogs", y="City", hue="Customer type", data=supermarket)
plt.show()
plt.clf()
