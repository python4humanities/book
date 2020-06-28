from pandas import DataFrame as df

data = {'str': ['A', 'B', 'C'], 'num': [10, 20, 30], 'bool': [False, True, True]}
df_data = df(data)
print(df_data)
