text = 'price: $3.20'
price = text[8:]            # 전체 문자열에서 가격만 별도의 문자열로 추출
print(price, type(price))   # 값 및 자료형 확인
price = float(price)        # 문자열을 실수로 형변환
print(price, type(price))   # 값 및 자료형 확인
