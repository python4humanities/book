from pandas import DataFrame as df

data = {'num': [10, 20, 30], 'bool': [False, True, True]}
index = ['A', 'B', 'C']
df_data = df(data, index=index)
df_data.index.name = 'str'              # 행 인덱스명 부여
df_data.columns.name = 'feature'        # 열 인덱스명 부여
print(df_data)
