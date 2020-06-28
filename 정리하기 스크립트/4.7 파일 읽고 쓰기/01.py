text = 'I love Python.\n'                     # 파일에 기록할 문자열
file_path = 'c:/pystudy/sample.txt'           # 파일 경로

f = open(file_path, 'wt', encoding='utf-8')   # 파일 객체 생성
f.write(text)                                 # 파일에 문자열 기록
f.close()                                     # 파일 객체 제거
