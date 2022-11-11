"""Pandas Tutorial"""

import pandas as pd

pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('pokemon_data.csv')

print(df.groupby(['Type 1']).mean().sort_values('HP', ascending=False), '\n')

print(df.groupby(['Type 1']).sum(), '\n')
print(df.groupby(['Type 1']).count(), '\n')

df['count'] = 1
print(df.groupby(['Type 1', 'Type 2']).count()['count'], '\n')

