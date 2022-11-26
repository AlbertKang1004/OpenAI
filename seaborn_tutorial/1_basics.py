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
print(crash_df)

tips_df = pd.read_csv('tips.csv')
print(tips_df)

# Distribution Plot
sns.displot(crash_df['not_distracted'], kde=False, bins=25)
plt.close()
# kde: displays the trendline
# bins: number of bars

# Joint Plot
sns.jointplot(x='speeding', y='alcohol', data=crash_df, kind='hex')
plt.close()
# x: data for the x-axis
# y: data for the y-axis
# data: data being used
# kind:
#       'reg': regression
#       'kde': kernel density estimation
#       'hex': hexagon distribution

# KDE Plot
sns.kdeplot(crash_df['alcohol'])
plt.close()

# Pair Plots
sns.pairplot(tips_df, hue='sex', palette={'Male': 'Blue', 'Female': 'Red'})
plt.close()
# hue: variable in data to map plot aspects to different colors'
# palette: Set of colors for mapping the hue variable

# Rug Plot
sns.rugplot(tips_df['tip'])
plt.show()

