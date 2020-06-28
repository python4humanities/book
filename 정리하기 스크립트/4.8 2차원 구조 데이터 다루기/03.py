from pandas import DataFrame as df

data = {'num': [10, 20, 30], 'bool': [False, True, True]}
index = ['A', 'B', 'C']          # 행 인덱스로 사용할 리스트 생성
df_data = df(data, index=index)  # 키워드 인수인 index 전달
print(df_data)
