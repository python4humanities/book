file_path = 'c:/pystudy/sample.txt'           # 파일 경로

f = open(file_path, 'rt', encoding='utf-8')   # 파일 객체 생성
text = f.read()                               # 파일의 데이터를 text에 저장
f.close()                                     # 파일 객체 제거

print(text)                                   # 문자열 출력
