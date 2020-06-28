from pandas import DataFrame as df

data = {'str': ['A', 'B', 'C'], 'num': [10, 20, 30], 'bool': [False, True, True]}
df_data = df(data)
df_partial = df_data.loc[:, ['str', 'bool']]  # 'str', 'bool'열의 데이터만 추출
print(df_partial)
