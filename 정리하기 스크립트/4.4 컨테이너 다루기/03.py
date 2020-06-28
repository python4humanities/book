obj0 = [0, 1, 2, 3, 4]
obj1 = ['a', 'b', 'c', 'd', 'e']

zip_result = zip(obj0, obj1)       # 이터레이터인 zip객체 생성
list_result = list(zip_result)     # 이터레이터를 리스트로 형변환

print(zip_result)
print(list_result)
