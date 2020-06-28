from pandas import DataFrame as df

data = {'str': ['A', 'B', 'C'], 'num': [10, 20, 30], 'bool': [False, True, True]}
df_data = df(data)
print(df_data)
print('-' * 17)
df_filtered = df_data[(df_data['num'] > 15) & (df_data['num'] < 25)]
print(df_filtered)
