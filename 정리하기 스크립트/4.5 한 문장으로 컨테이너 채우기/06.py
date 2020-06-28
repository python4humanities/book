numbers = [0, 1, 2, 3, 4, 5]

result = []
for element in numbers:
    if element < 3:
        result += [element * 2]
    else:
        result += [element * 3]

print(result)
