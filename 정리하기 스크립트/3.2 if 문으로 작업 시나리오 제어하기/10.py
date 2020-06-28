korea = ['한국', '대한민국', '남한']
us = ['미국', '미합중국']

word = '남한'

if word in korea:        # 리스트인 korea에 word가 포함되었는지 검사
    print('한국')
elif word in us:
    print('미국')
