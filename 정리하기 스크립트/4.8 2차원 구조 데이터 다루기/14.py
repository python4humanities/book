import pandas as pd

xlsx_file_path = './sample/고객_행동.xlsx'
df_data = pd.read_excel(xlsx_file_path, index_col=0)
df_data = df_data.sort_values(by='sales', ascending=False)
print(df_data)
