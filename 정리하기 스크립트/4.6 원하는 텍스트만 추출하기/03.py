import re

text = '가나ABabカタ天地'         # 한글 / 알파벳 / 일본어 / 한자

pattern0 = re.compile(r'\w')       # 문자 일치로 패턴 객체 구성
pattern1 = re.compile('[ABC]')    # 문자 클래스로 패턴 객체 구성

print(re.findall(pattern0, text))
print(re.findall(pattern1, text))
