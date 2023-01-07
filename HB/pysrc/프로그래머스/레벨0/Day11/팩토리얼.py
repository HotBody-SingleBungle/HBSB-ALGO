def solution(n):
    answer = 1
    cnt = 1
    while 1:
        if answer *(cnt+1) > n >= answer:
            break
        else:
            answer *= (cnt+1)
            cnt += 1
            print(cnt)
    return cnt