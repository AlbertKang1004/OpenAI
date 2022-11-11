"""Pandas Tutorial"""

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# Making Changes to the data
print(df.head(5), '\n')

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5), '\n')

df = df.drop(columns=['Total'])
print(df.head(5), '\n')

df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(5), '\n')

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5), '\n')
