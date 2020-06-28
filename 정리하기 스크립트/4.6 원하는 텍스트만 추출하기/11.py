import re

news_title = '서브프라임 사태의 재현? 美 파생상품 급증'
us_pattern = re.compile('美國?|USA?', re.I)
news_title_cleaned = re.sub(us_pattern, '미국', news_title)
print(news_title_cleaned)
