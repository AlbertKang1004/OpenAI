"""Pandas Tutoriall"""

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# df.to_csv('modified.csv', index=False)
# df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')

