import pandas as pd

file_path = './sample/고객_행동.xlsx'
df_data = pd.read_excel(file_path, index_col=0)
df_data.loc[:, 'sales_rank'] = df_data.loc[:, 'sales'].rank(ascending=False)
df_data.loc[:, 'sales_rank'] = pd.to_numeric(df_data.loc[:, 'sales_rank'], downcast='integer')
print(df_data)
