"""Pandas Tutorial"""

import pandas as pd

df = pd.read_csv('pokemon_data.csv')
df_xlsx = pd.read_excel('pokemon_data.xlsx')
df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

# Display first 5 rows
print(df.head(), '\n')
print(df_xlsx.head(), '\n')
print(df_txt.head(), '\n')

# Display last 5 rows
print(df.tail(), '\n')
print(df_xlsx.tail(), '\n')
print(df_txt.tail(), '\n')

# Read Headers
print(df.columns, '\n')

# Read each column
print(df[['Name', 'Type 1', 'HP']].head(), '\n')

# Read each row
# print(df.iloc[0:4], '\n')

# for index, row in df.iterrows():
#     print(index, row['Name'])

print(df.loc[df['Type 1'] == "Fire"].sort_values('Speed'), '\n')

# Read a specific location
print(df.iloc[2, 1], '\n')

# Sorting/Describing Data
print(df.describe(), '\n')

print(df.sort_values('Name', ascending=False), '\n')

print(df.sort_values(['Type 1', 'Generation'], ascending=[1, 0]))

