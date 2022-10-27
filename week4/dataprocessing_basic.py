import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_train = pd.read_csv("train.csv", error_bad_lines=False)

print(df_train.shape, '\n')
print(df_train.columns, '\n')
print(df_train.info, '\n')

print(df_train.head())

print(df_train.isnull().sum())
# the number of missing values in each column

# ============== HANDLE MISSING VALUES ==============

df_train[df_train['Survived'] == 1]['Age'].describe()
