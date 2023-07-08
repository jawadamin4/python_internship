import numpy as np
import pandas as pd

data = {
    "name": ['jawad', 'ahmad ', 'mahmood'],
    "age": [23, 28, 26],
    "city": ['nowshera', 'islamabad', 'mardan']
}

df = pd.DataFrame(data)

# df.to_csv('data.csv') # with indexs

df.to_csv('data.csv', index=False)  # without indexs

print(df.head(2))  # if we have a lots of data, and we want to see some of them so we can use head and tail
print(df.tail(2))
print(df.describe())  # Generate descriptive statistics

print(df['name'])  # specific column
print(df['age'])
print(df['city'])

df['age'][0] = 70
df.to_csv('data.csv')
print(df)

print(df.dtypes)  # show the datatypes of data coulmns
print(df.to_numpy())  # convert it to numpy array
print(df.T)  # transpose columns to rows
print(df.sort_index(axis=0, ascending=False))  # 0 for rows
print(df.sort_index(axis=1, ascending=False))  # 1 for columns

df.loc[0, 'name'] = 'amin khan'  # we can change value like this
print(df)
print(df.iloc[0, 2])  # if not using name of column then direct like this
print(df.drop(['age'], axis=1))  # to drop any column

print("----------------------------------------------------------------------------")
#  ----------------------------------------------------------------------------------------------
d1 = {
    'Name': ['Shark', 'Whale', 'Jellyfish', 'Starfish'],
    'ID': [1, 2, 3, 4],
    'Population': [100, 200, np.nan, pd.NaT],
    'Regions': [1, None, pd.NaT, pd.NaT]
}
df1 = pd.DataFrame(d1)
print(df1)

dfresult = df1.dropna()  # Dropping All Rows with Missing Values
print(dfresult)

dfresult = df1.dropna(axis=1)  # Dropping All Columns with Missing Values
print(dfresult)
