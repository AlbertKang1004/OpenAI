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
plt.close()
sns.set_context('paper')
sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips_df, markers=['o', '^'],
           scatter_kws={'s': 100, 'linewidth': 0.5, 'edgecolor': 'w'})
plt.close()

sns.lmplot(x='total_bill', y='tip', col='sex', row='time', data=tips_df, aspect=2)
plt.show()
