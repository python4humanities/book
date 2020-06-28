import pandas as pd

file_path = './sample/고객_행동.xlsx'
df_data = pd.read_excel(file_path, index_col=0)
df_data = df_data * 0.5          # DataFrame 객체의 모든 원소에 0.5 곱하기
print(df_data)
