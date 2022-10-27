"""Pandas Basic"""
import pandas as pd

wildlife_df = pd.read_csv('wildlife.csv',
                          delimiter=',', index_col="uniq_id")
print(wildlife_df, '\n')  # view the entire dataframe

print(wildlife_df.head(5), '\n')  # view the first 5 rows
print(wildlife_df.tail(5), '\n')  # view the last 5 rows

print(wildlife_df.sample(5), '\n')  # view the random 5 rows

print(wildlife_df.info(), '\n')  # shows the information

print(wildlife_df.shape[0])  # returns the number of rows
print(wildlife_df.shape[1], '\n')  # returns the number of columns

print(wildlife_df.describe(), '\n')  # returns a full statistical summary
print(wildlife_df.describe(include="all"), '\n')

print(wildlife_df['water_need'].values, '\n')  # can use method in numpy
print(type(wildlife_df['water_need'].values), '\n')

# ==========================CLEANING==========================

wildlife_df.columns = ['AniMaL*&', 'WATerNeEd']
print(wildlife_df.columns)

wildlife_df.rename(columns={'AniMaL*&': 'animal', 'WATerNeEd': 'water_need'}, inplace=True)
# rename the columns by its value in the dictionary
print(wildlife_df, '\n')

# =========================EXTRACTING=========================

print(wildlife_df.iloc[4], '\n')
# extracting row 4

print(wildlife_df['animal'], '\n')
# extracting column 'animal'

print(wildlife_df[['animal', 'water_need']], '\n')
# extracting columns 'animal' and 'water_need'

wildlife_2 = wildlife_df.reset_index(inplace=False)
print(wildlife_2['uniq_id'])
# extracting the index as a column

print(wildlife_df[(wildlife_df['water_need'] > 200) & (wildlife_df['water_need'] < 300)], '\n')
# extracting the rows which need water more than 200 and less than 300

print(wildlife_df[wildlife_df['water_need'] > 300], '\n')

# ===========================APPLY===========================


def water_need_to_category(water_need):
    """
    :param water_need:
    :return:
    """
    if water_need < 200:
        return "low"
    elif 200 <= water_need < 400:
        return "mid"
    else:
        return "high"


wildlife_df['water_need_category'] = wildlife_df['water_need'].apply(water_need_to_category)
print(wildlife_df.head(), '\n')

# or, we can use a lambda
average_water_need = wildlife_df['water_need'].mean()
wildlife_df['average_diff'] = wildlife_df['water_need'].apply(lambda x: x - average_water_need)
print(wildlife_df.head(), '\n')

# ========================MAPPING VALUES========================

print(wildlife_df.tail(), '\n')
wildlife_df['animal'] = wildlife_df['animal'].map({'lion': 'tiger'}).fillna(wildlife_df['animal'])
# change every 'lion' to 'tiger'
print(wildlife_df.tail(), '\n')

# ========================CONCATENATING=========================

# dataframe 1
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
# dataframe 2
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])
# dataframe 3
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

print(pd.concat([df1, df2, df3]), '\n')
# concatenate on the row axis

print(pd.concat([df1, df2, df3], axis=1), '\n')
# concatenate on the column axis

# ===========================MERGING===========================

# sample dataframe 1
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

# sample dataframe 2
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left, right, on=['key1', 'key2']), '\n')
# how='inner' by default
# INNER JOIN (Intersection)

print(pd.merge(left, right, how='outer', on=['key1', 'key2']), '\n')
# OUTER JOIN (Union)

print(pd.merge(left, right, how='left', on=['key1', 'key2']), '\n')
# LEFT JOIN (keep key1 and key2 in left)

print(pd.merge(left, right, how='right', on=['key1', 'key2']), '\n')
# RIGHT JOIN (keep key1 and key2 in right

# ===========================JOINING===========================

left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']},
                    index=[1, 2, 3, 4])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                     index=[5, 4, 7, 1])

print(left.join(right), '\n')  # based on left
print(right.join(left), '\n')  # based on right
print(left.join(right, how='outer'), '\n')
print(right.join(left, how='outer'), '\n')
# how='outer' means union of two dataframes

