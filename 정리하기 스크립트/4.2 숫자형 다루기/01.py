import statistics

insta_visits = [10, 80, 21, 5, 100]

print(statistics.mean(insta_visits))      # 원소의 평균 출력
print(statistics.median(insta_visits))    # 원소의 중간값 출력
print(statistics.stdev(insta_visits))     # 원소의 표본 표준편차 출력
print(statistics.pstdev(insta_visits))    # 원소의 모집단 표준편차 출력
