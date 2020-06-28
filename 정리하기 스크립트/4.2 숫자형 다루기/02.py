numbers = []
num = -3

while num < 5:
    numbers += [num]
    num += 1

print(numbers)
print(sum(numbers), max(numbers), min(numbers))    # 합, 최댓값, 최솟값 출력
