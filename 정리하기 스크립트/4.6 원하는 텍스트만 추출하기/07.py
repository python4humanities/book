import re

text = '3+10은 13이야.'
pattern0 = re.compile(r'3+10')
pattern1 = re.compile(r'3\+10')     # 패턴에서 ‘+’ 대신 ‘\+’를 사용
print(re.findall(pattern0, text))
print(re.findall(pattern1, text))
