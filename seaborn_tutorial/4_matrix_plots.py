"""Seaborn Tutorial"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.expand_frame_repr', False)

# %matplotlib inline
# %reload_ext autoreload
# %autoreload 2

crash_df = pd.read_csv('car_crashes.csv')

tips_df = pd.read_csv('tips.csv')

flights_df = pd.read_csv('flights.csv')

iris_df = pd.read_csv('iris.csv')

att_df = pd.read_csv('attention.csv')

plt.figure(figsize=(8, 6))
sns.set_context('paper', font_scale=1.0)

crash_mx = crash_df.corr()
print(crash_mx, '\n')
sns.heatmap(crash_mx, annot=True, cmap='Reds')
plt.close()

# Using a pivot table
flights = flights_df.pivot_table(index='month', columns='year', values='passengers', sort=False)
print(flights, '\n')
sns.heatmap(data=flights, cmap='Blues', linecolor='white', linewidths=2)
plt.close()

# Cluster Map
# species = iris_df.pop('species')
# sns.clustermap(iris_df)
# plt.show()

sns.clustermap(flights, cmap='Blues', standard_scale=1)
plt.close()

# Pair Grid
# iris_g = sns.PairGrid(iris_df, hue='species')
# iris_g.map_diag(plt.hist)
# iris_g.map_offdiag(plt.scatter)
# iris_g.map_upper(plt.scatter)
# iris_g.map_lower(sns.kdeplot)
iris_g = sns.PairGrid(iris_df, hue="species",
                      x_vars=["sepal_length", "sepal_width"],
                      y_vars=["petal_length", "petal_width"])
iris_g.map(plt.scatter)
iris_g.add_legend()
plt.close()

# Facet Grid
# tips_fg = sns.FacetGrid(tips_df, col='time', hue='smoker', height=4, aspect=1.3,
#                         col_order=['Dinner', 'Lunch'], palette='Set1')
# tips_fg.map(plt.scatter, 'total_bill', 'tip', edgecolor='w')
# tips_fg.add_legend()

# kws = dict(s=50, linewidth=.5, edgecolor='w')
# tips_fg = sns.FacetGrid(tips_df, col='sex', hue='smoker', height=4, aspect=1.3,
#                         hue_order=['Yes', 'No'], hue_kws=dict(marker=['^', 'v']))
# tips_fg.map(plt.scatter, 'total_bill', 'tip', **kws)

att_fg = sns.FacetGrid(att_df, col='subject', col_wrap=5, height=1.5)
att_fg.map(plt.plot, 'solutions', 'score', marker='.')
plt.show()
