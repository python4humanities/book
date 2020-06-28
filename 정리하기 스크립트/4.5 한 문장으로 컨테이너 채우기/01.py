numbers = [0, 1, 2, 3, 4, 5]

result = []                    # 빈 리스트인 result 생성
for element in numbers:        # 리스트인 numbers의 원소를 차례로 추출
    result += [element * 2]    # 원소에 2를 곱한 후 result에 차례로 저장

print(result)
