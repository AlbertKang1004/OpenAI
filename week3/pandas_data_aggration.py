"""Pandas Data Aggragation"""

import pandas as pd
from numpy import nan as NA
from pandas_basic import wildlife_df
import missingno as msno
import matplotlib.pyplot as plt

# ========================COUNT========================

print(wildlife_df.count(), '\n')
# count the number of rows for each column

print(wildlife_df['animal'].count(), '\n')
# count the number of rows for column 'animal'

# =========================SUM=========================

print(wildlife_df['water_need'].sum(), '\n')

print(wildlife_df['animal'].sum(), '\n')
# this adds up every string found in column 'animal'.

# =======================MIN/MAX=======================

print(wildlife_df['water_need'].min(), '\n')
print(wildlife_df['water_need'].max(), '\n')

# ======================GROUPING=======================

print(wildlife_df.groupby('animal')[['water_need']].mean(), '\n')

# Create a groupby object
animal_groups = wildlife_df.groupby('animal')

# Iterate over it, where name is the name of the group and
# group is the group itself
for name, group in animal_groups:
    print(f"First 2 entries for {name}")
    print("------------------------")
    print(group.head(2), end="\n\n")

print(animal_groups.get_group('elephant'), '\n')

# ====================DATA CLEANING=====================

data_frame = pd.DataFrame([[1, 2, 4, NA],
                           [8, NA, NA, NA],
                           [NA, NA, NA, NA],
                           [NA, NA, 16, NA],
                           [32, NA, 64, NA]],
                          columns=['A', 'B', 'C', 'D'])

print(data_frame, '\n')

print(data_frame.dropna(), '\n')
# removes all the rows where one element is missing

print(data_frame.dropna(how='all'), '\n')
# removes rows only with all values missing

print(data_frame.dropna(how='all', axis=1), '\n')
# removes columns only with all values missing

print(data_frame.fillna(0), '\n')
# fills empty space with 0

print(data_frame.fillna(data_frame.mean()), '\n')
# filling with the mean

print(data_frame.fillna({'A': -1, 'D': 0}), '\n')
# filling the values by column with a dictionary

# =======================REPLACE=======================

print(data_frame.replace(NA, 'NA', inplace=False), '\n')
# replace NA with 'NA'.

# ======================ANALIZING======================

print(data_frame.isnull().sum(), '\n')
# return how many missing values are in the dataframe

print(data_frame.info(), '\n')

fig, ax = plt.subplots(figsize=[5, 5])
msno.matrix(data_frame, ax=ax)
plt.show()

