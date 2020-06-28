import pandas as pd

def to_cent(x):            # 인수의 값을 100으로 나누어 반환하는 함수 정의
    return x/100

xlsx_file_path = './sample/고객_행동.xlsx'
df_data = pd.read_excel(xlsx_file_path, index_col=0)
df_data = df_data.applymap(to_cent)     # DataFrame의 모든 원소에 to_cent() 함수 일괄 적용
print(df_data)
