import pandas as pd

src_file_path = './sample/고객_행동.xlsx'      # 원본 파일 경로
df_data = pd.read_excel(src_file_path, sheet_name='Sheet1', index_col='model')
df_cdj = df_data.loc[:, ['view', 'click', 'keep', 'sales', 'review_score']]
df_price = df_data.loc[:, ['price']]
df_price = df_price.sort_values(by='price', ascending=False)

for element in df_cdj.columns:
    df_cdj[f'rank_{element}'] = df_cdj[element].rank(ascending=False, method='min')
    df_cdj[f'rank_{element}'] = pd.to_numeric(df_cdj[f'rank_{element}'], downcast='integer')

rst_file_path = './sample/고객_행동_분석.xlsx'      # 분석 결과를 저장할 파일 경로
writer = pd.ExcelWriter(rst_file_path, engine='xlsxwriter')  # 엑셀 파일 객체 생성
df_cdj.to_excel(writer, sheet_name='cdj')                 # cdj 시트에 df_cdj 전달
df_price.to_excel(writer, sheet_name='price')         # price 시트에 df_price 전달

cdj_chart = writer.book.add_chart({'type': 'line'})     # cdj 선형 차트 생성
cdj_cat = ['cdj', 0, 6, 0, 10]
cdj_val_a = ['cdj', 1, 6, 1, 10]
cdj_val_b = ['cdj', 2, 6, 2, 10]
cdj_chart.add_series({'name': 'A', 'categories': cdj_cat, 'values': cdj_val_a})
cdj_chart.add_series({'name': 'B', 'categories': cdj_cat, 'values': cdj_val_b})
cdj_chart.set_y_axis({'major_unit': 1, 'minor_unit': None, 'reverse': True})
cdj_chart.set_title({'name': '제품 A, B의 고객 구매 경로'})
writer.sheets['cdj'].insert_chart(11, 0, cdj_chart)

price_chart = writer.book.add_chart({'type': 'column'})    # price 세로막대형 차트 생성
price_cat = ['price', 1, 0, 10, 0]
price_val = ['price', 1, 1, 10, 1]
price_chart.add_series({'name': 'Price', 'categories': price_cat, 'values': price_val})
price_chart.set_title({'name': '제품 별 가격 포지션'})
writer.sheets['price'].insert_chart(0, 2, price_chart)

writer.save()