def tester():
    global obj         # tester() 본문의 obj변수를 함수 외부의 obj변수와 연동
    obj = 10           # obj에 10 저장

obj = 20               # obj에 20 저장
tester()
print(obj)
