import re

prices = '제품A:8,000원\n제품B:900원\n제품C:1,400원\n'   # 원본 문자열
pattern0 = re.compile('^제품([A-C]):([0-9,]{3,5})원$')
pattern1 = re.compile('^제품([A-C]):([0-9,]{3,5})원$', re.M)  # re.M을 인수로 전달
print(re.findall(pattern0, prices))
print(re.findall(pattern1, prices))
