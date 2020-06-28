from pandas import DataFrame as df

data = {'str': ['A', 'B', 'C'], 'num': [10, 20, 30], 'bool': [False, True, True]}
df_data = df(data)
print(df_data.loc[1, 'num'])   # 명시적 인덱싱
print(df_data.iloc[1, 1])      # 암묵적 인덱싱(시퀀스)
