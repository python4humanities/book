a = ('Seoul', 'Paris', 'Paris', 'US')   # 튜플 생성
a = list(a)      # 튜플을 리스트로 형변환
a[3: 4] = []     # [3]을 제거
a = tuple(a)     # 리스트를 다시 튜플로 형변환
print(a)
