numbers = []
num = 0

while num > -5:
    numbers += [abs(num)]   # num을 절댓값 변환 후 numbers 원소로 저장
    num -= 1

print(numbers)
