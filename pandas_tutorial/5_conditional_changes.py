"""Pandas Tutorial"""

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
print(df, '\n')

df = pd.read_csv('pokemon_data.csv')
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST1', 'TEST2']
print(df, '\n')

df.to_csv('modified.csv')
