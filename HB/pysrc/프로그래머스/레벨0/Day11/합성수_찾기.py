def solution(n):
    answer = 0
    cnt = 0
    if n == 1 or n == 2 or n == 3:
        answer = 0
        
    else:
        for i in range(2, n+1):
            cnt = 0
            for j in range(2,i):
                if i%j == 0:
                    answer += 1
                    break
    return answer