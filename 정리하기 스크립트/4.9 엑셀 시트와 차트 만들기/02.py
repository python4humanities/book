import pandas as pd

src_file_path = './sample/경로_별_순위.xlsx'
rst_file_path = './sample/경로_별_순위_차트.xlsx'
df_data = pd.read_excel(src_file_path, index_col='model')
writer = pd.ExcelWriter(rst_file_path, engine='xlsxwriter')
df_data.to_excel(writer, sheet_name='Sheet1')

# 차트 작업
chart = writer.book.add_chart({'type': 'line'})     # 꺾은선형 차트 객체 생성

name_a = ['Sheet1', 1, 0]             # (1, 0)
name_b = ['Sheet1', 2, 0]             # (2, 0)
categories = ['Sheet1', 0, 1, 0, 5]   # (0, 1) 에서 (0, 5) 까지
values_a = ['Sheet1', 1, 1, 1, 5]     # (1, 1) 에서 (1, 5) 까지
values_b = ['Sheet1', 2, 1, 2, 5]     # (2, 1) 에서 (2, 5) 까지
chart.add_series({'name': name_a, 'categories': categories, 'values': values_a})
chart.add_series({'name': name_b, 'categories': categories, 'values': values_b})
chart.set_y_axis({'min': 0, 'max': 5, 'major_unit': 1, 'reverse': True})
chart.set_title({'name': 'A, B의 고객 구매 경로'})

writer.sheets['Sheet1'].insert_chart(0, 6, chart)   # 차트를 엑셀 시트에 전달
writer.save()
