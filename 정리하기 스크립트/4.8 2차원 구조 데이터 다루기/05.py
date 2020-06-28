from pandas import DataFrame as df

data = {'num': [10, 20, 30], 'bool': [False, True, True]}
index = ['A', 'B', 'C']
df_data = df(data, index=index)

print(df_data.loc['A', 'num'])    # 'A'행 'num' 열의 원소값 출력
df_data.loc['A', 'num'] = 99      # 'A'행 'num' 열에 99를 저장해 갱신
print(df_data.loc['A', 'num'])    # 'A'행 'num' 열의 새 원소값 출력
