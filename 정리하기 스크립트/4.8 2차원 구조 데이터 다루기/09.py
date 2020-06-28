from pandas import DataFrame as df

data = {'str': ['A', 'B', 'C'], 'num': [10, 20, 30], 'bool': [False, True, True]}
df_data = df(data)
print(df_data)
print('-' * 17)
df_filtered = df_data.loc[df_data.loc[:, 'num'] > 15, :]    # 데이터 필터링
print(df_filtered)
