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

# Bar Plot
sns.barplot(x='sex', y='total_bill', data=tips_df, estimator=np.median)
plt.close()

# Count Plot
sns.countplot(x='sex', data=tips_df)
plt.close()

# Box Plot
sns.boxplot(x='day', y='total_bill', data=tips_df, hue='sex')
plt.legend(loc=0)
plt.close()

# Violin Plot
sns.violinplot(x='day', y='total_bill', data=tips_df, hue='sex', split=True)
plt.close()

# Strip Plot
plt.figure(figsize=(8, 5))
sns.stripplot(x='day', y='total_bill', data=tips_df, hue='sex', jitter=True, dodge=True)
plt.close()

# Swarm Plot
# sns.violinplot(x='day', y='total_bill', data=tips_df, hue='sex', split=True)
sns.swarmplot(x='day', y='total_bill', data=tips_df)
plt.close()

# Palettes
plt.figure(figsize=(8, 5))
sns.set_style('dark')
sns.set_context('talk')
sns.stripplot(x='day', y='total_bill', data=tips_df, hue='sex', palette='cool')
plt.legend(loc=1)
plt.show()
