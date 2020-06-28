from collections import Counter

letters0 = ['a', 'a', 'c', 'd', 'a']
letters1 = ['b', 'a', 'e', 'd']
letters2 = ['e', 'c', 'e']

letters_sum = letters0 + letters1 + letters2
letters_count = Counter(letters_sum)
print(letters_count)             # Counter 객체 출력
print(dict(letters_count))       # Counter 객체를 딕셔너리로 형변환하여 출력
