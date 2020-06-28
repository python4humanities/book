import pandas as pd
from wordcloud import WordCloud

font = './font/SeoulNamsanM.ttf'
source = './sample/키워드_별_빈도.xlsx'
result = './sample/wordcloud.png'

df_data = pd.read_excel(source)
dict_data = {x: y for x, y in zip(df_data['keywords'], df_data['count'])}

wc = WordCloud(max_words=40, font_path=font, background_color='white')
wc.generate_from_frequencies(dict_data)
wc.to_file(result)
