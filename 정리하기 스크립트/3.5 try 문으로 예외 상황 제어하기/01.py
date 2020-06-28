obj = '2'
try:
    print('try: start')
    print(obj ** 2)   # TypeError 발생 지점
    print('try: end')
except:
    print('except')
else:
    print('else')
finally:
    print('finally')
