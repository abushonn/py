# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#object-creation
# Object creation
# Viewing data
# Selection ()
# Missing data¶
# Operations
# Merge (Concat, Join)
# Grouping
# Reshaping
# Time series
# Categoricals
# Plotting
# Getting data in/out (CSV, Excel)

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20130101', periods=10)


df = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list('ABCD'))
print(df)

df.head(3)
df.tail(4)
df.indexes


df.loc['20130102':'20130104', 'A':'C']

df.iloc[3] #row index=3
df.iloc[3:5, 0:2] #select row 3,4 ^ column 0,1
df.iloc[[1, 2, 4], [0, 2]]
df.iloc[1:3, :] #rows 1,2
df.iloc[:, 1:3] #columns 1,2
df.iloc[1, 1] #scalar element df[1,1]
df.iat[1, 1] # similar to df.iloc[1, 1]

df[(df['A'] > 0) & (df['B'] > 0)]



df2 = pd.DataFrame({'A': 1.,
'B': pd.Timestamp('20130102'),
'C': pd.Series(1, index=list(range(4)), dtype='float32'),
'D': np.array([3] * 4, dtype='int32'),
'E': pd.Categorical(["test", "train", "test", "train"]),
'F': 'foo'})

print(df2)

