import pandas as pd
from statistics import mean

xlsx_file_path = './sample/구매_후기_별_점수.xlsx'
df_data = pd.read_excel(xlsx_file_path)

df_pivot = df_data.pivot_table(values='score', index='model', columns='topic', aggfunc=mean)
print(df_pivot)
