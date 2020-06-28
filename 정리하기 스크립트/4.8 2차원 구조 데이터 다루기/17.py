import pandas as pd

def to_cent(x):            # 인수의 값을 100으로 나누어 반환하는 함수 정의
    return x/100

xlsx_file_path = './sample/고객_행동.xlsx'
df_data = pd.read_excel(xlsx_file_path, index_col=0)
df_data.loc[:,'sales'] = df_data.loc[:,'sales'].map(to_cent)
print(df_data)
