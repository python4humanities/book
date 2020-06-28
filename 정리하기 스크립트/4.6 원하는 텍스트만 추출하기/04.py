import re

voc = '선물로 Uphone 11 받았어요 ㅎㅎ'            # 원본 문자열

en_pattern = re.compile('[A-Za-z]+')             # 연속된 알파벳만 일치
ko_pattern0 = re.compile('[가-힣]+')             # 연속된 한글 음절만 일치
ko_pattern1 = re.compile('[ㄱ-ㅣ가-힣]+')        # 연속된 한글 음절, 음소만 일치
num_pattern = re.compile('[0-9]+')               # 연속된 숫자만 일치
whitespace_pattern = re.compile(r'[\s]+')        # 연속된 공란만 일치

print(re.findall(en_pattern, voc))
print(re.findall(ko_pattern0, voc))
print(re.findall(ko_pattern1, voc))
print(re.findall(num_pattern, voc))
print(re.findall(whitespace_pattern, voc))
