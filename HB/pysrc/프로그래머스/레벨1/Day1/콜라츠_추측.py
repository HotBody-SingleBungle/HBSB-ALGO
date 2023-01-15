def solution(num):
    answer = -1
    cnt = 0
    while cnt < 500:
        if num == 1:
            answer = cnt
            break
        if num %2 == 0:
            num //= 2
        else:
            num *= 3
            num += 1
        cnt += 1
    return answer