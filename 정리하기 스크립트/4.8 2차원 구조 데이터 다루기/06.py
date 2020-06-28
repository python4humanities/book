from pandas import DataFrame as df

data = {'num': [10, 20, 30], 'bool': [False, True, True]}
index = ['A', 'B', 'C']
df_data = df(data, index=index)
print(df_data)
print('-' * 22)
df_data.loc[:, 'num'] = [1, 2, 3]     # 'num'열에 차례로 1, 2, 3 삽입
df_data.loc[:, 'bool'] = False        # 'bool'열에 차례로 False, False, False 삽입
df_data.loc[:, 'fruit'] = ['apple', 'banana', 'cherry']     # 새 열인 'fruit' 삽입
print(df_data)
