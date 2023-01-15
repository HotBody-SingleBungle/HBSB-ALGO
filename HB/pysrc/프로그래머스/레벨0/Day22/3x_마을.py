def solution(n):
    answer = 0
    tic = 0
    while tic != n:
        answer += 1
        while 1:
            if answer % 3 == 0 or '3' in str(answer):
                answer += 1
            else:
                break
        tic += 1
    return answer