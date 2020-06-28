import pandas as pd
from pandas import DataFrame as df

src_file_path = './sample/고객_행동.xlsx'        # 소스 파일의 경로
rst_file_path = './sample/경로_별_순위.xlsx'     # 결과를 저장할 파일의 경로
df_data = pd.read_excel(src_file_path, index_col='model')
df_data = df_data.loc[:, ['view', 'click', 'keep', 'sales', 'review_score']]
df_data = df_data.rank(ascending=False, method='min')
print(df_data)
writer = pd.ExcelWriter(rst_file_path, engine='xlsxwriter')  # 엑셀 파일 객체 생성
df_data.to_excel(writer, sheet_name='Sheet1')         # 시트에 데이터 전달
writer.save()                                         # 파일 생성 작업 마무리
