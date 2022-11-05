"""Data Processing: Basic"""
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

# ================= DISPLAYING DATA =================

print(df_train[df_train['Survived'] == 1]['Age'].describe(), '\n')

# display the data of people who survived

print(df_train[df_train['Survived'] == 0]['Age'].describe(), '\n')

# display the data of people who died

sns.boxplot(x='Survived', y='Age', data=df_train)

sns.displot(df_train[df_train['Survived'] == 1]['Age'].dropna(), bins=15, kde=True, color='green')
plt.title('Age distribution of Survived Titanic passengers')
sns.displot(df_train[df_train['Survived'] == 0]['Age'].dropna(), bins=15, kde=True, color='red')
plt.ylabel('Count')
plt.title('Age distribution of Deceased Titanic passengers')
# plt.show()

# ================ MISSING VALUES =================

df_train.Age = df_train.Age.fillna(df_train.Age.mean())
# fill the missing value in 'Age' column with its mean value

print(df_train['Age'].value_counts())

print(df_train['Cabin'], '\n')
df_train['Cabin_init'] = df_train['Cabin'].apply(lambda x: str(x)[0])
sns.barplot(x='Cabin_init', y='Survived', data=df_train)


# extracted the initial of the cabin and put them in 'Cabin_init'

df_train.loc[df_train.Cabin.notnull(), 'Cabin'] = 'available'
df_train.loc[df_train.Cabin.isnull(), 'Cabin'] = 'not available'
# fill the columns null with information as 'Not available' and rest as 'available'

sns.barplot(x='Cabin', y='Survived', data=df_train)
# plt.show()

print(df_train['Embarked'].value_counts(), '\n')
df_train['Embarked'] = df_train['Embarked'].fillna('S')
print(df_train['Embarked'].value_counts(), '\n')
# we can simply impute the missing values
# with most commonly occurred value,
# which is ‘S’ in this case.

