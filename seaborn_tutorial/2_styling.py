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

sns.set_style('ticks')
sns.set_context('paper')

# plt.figure(figsize=(8, 4))
sns.jointplot(x='speeding', y='alcohol', data=crash_df, kind='reg')
sns.despine(left=True, bottom=True)
plt.show()

