obj0 = {'a': 0, 'b': 1}
obj1 = {'c': 2, 'd': 3}

obj0.update(obj1)             # update() 메소드를 호출해 딕셔너리 전달
print(obj0)

obj0.update(e=4, f=5)         # update() 메소드를 호출해 키워드 인수 전달
print(obj0)
