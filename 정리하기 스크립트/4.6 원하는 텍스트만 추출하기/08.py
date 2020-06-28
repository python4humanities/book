import re

fruits = 'Apple, Banana, Cherry, Date'          # 원본 문자열
pattern0 = re.compile('apple|cherry')
pattern1 = re.compile('apple|cherry', re.I)     # re.I를 인수로 전달
print(re.findall(pattern0, fruits))
print(re.findall(pattern1, fruits))
