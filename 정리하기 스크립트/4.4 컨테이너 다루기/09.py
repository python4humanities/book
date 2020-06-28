letters = ['a', 'b', 'c']

while True:
    print(letters.pop(0))    # 리스트의 0번째 원소를 추출하기
    if not letters:          # 리스트가 []이면:
        break                # 리스트에서 빠져나올 것
