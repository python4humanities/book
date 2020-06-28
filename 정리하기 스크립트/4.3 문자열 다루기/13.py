headers = ['韓 美 간 경제 협력 강화', '美 정상 中 방문']
for header in headers:
    header = header.replace('韓', '한국')
    header = header.replace('美', '미국')
    header = header.replace('中', '중국')
    print(header)
