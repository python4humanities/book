import re

text = 'An apple is my favorite thing'
pattern0 = re.compile('^apple')          # 문자열 왼쪽 끝의 'apple'과 일치
pattern1 = re.compile('thing$')          # 문자열 오른쪽 끝의 'thing'과 일치
pattern2 = re.compile('apple|banana')    # 문자열의 'apple'이나 'banana'와 일치
print(re.findall(pattern0, text))
print(re.findall(pattern1, text))
print(re.findall(pattern2, text))
