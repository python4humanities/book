import pandas as pd

file_path = './sample/고객_행동.xlsx'
df_data = pd.read_excel(file_path, index_col=0)  # 데이터를 불러와 df_data에 저장
print(df_data)                                   # df_data의 데이터 확인
