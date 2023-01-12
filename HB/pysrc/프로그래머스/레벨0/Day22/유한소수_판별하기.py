def solution(a, b):
    while 1:
        if b % 5 and b % 2:
            break
        if b % 2 == 0:
            b = b // 2
        if b % 5 == 0:
            b = b // 5
    if a % b == 0:
        answer = 1
    else:
        answer = 2
    return answer