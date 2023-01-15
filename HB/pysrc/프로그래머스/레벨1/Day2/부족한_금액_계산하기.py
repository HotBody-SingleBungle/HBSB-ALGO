def solution(price, money, count):
    answer = -1
    sum_ = 0
    for i in range(count+1):
        sum_ += i
    answer = -(money - sum_*price)
    if answer <0:
        answer = 0
    return answer