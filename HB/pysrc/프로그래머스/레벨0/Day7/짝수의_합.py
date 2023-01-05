def solution(n):
    answer = 0
    if (n % 2 == 0):
        answer = (n+2) * (n)/4
    else:
        answer = (n**(2) - 1)/4
    return answer