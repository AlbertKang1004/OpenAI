"""Pandas Tutorial"""

import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')

print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)], '\n')

cols = list(df.columns.values)
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.reset_index(drop=True, inplace=True)
new_df.drop(cols[4:11], axis=1, inplace=True)
print(new_df, '\n')

# exclude names that include "Mega"
# print(df.loc[df['Name'].str.contains('Mega')], '\n')
print(df.loc[~ df['Name'].str.contains('Mega')], '\n')

# Regular Expression
print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)], '\n')
