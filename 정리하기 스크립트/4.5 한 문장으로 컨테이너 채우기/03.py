numbers = [0, 1, 2, 3, 4, 5]

# 리스트인 result에 numbers원소에 대한 연산 수행 후 차례로 저장하기
result = []
for element in numbers:
    if element < 3:                # element < 3 일 때만 본문의 연산 수행
        result += [element * 2]

print(result)
