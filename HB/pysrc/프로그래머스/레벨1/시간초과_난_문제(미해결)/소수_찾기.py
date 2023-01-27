def solution(n):
    answer = 2
    if n == 2 or n == 3:
        answer = n  - 1
    else:
        for i in range(4,n+1):
            for j in range(2, int(i**(0.5))+1):
                if i % j == 0:
                    break
                elif j == int(i**(0.5)):
                    answer += 1
    return answer
solution(1000000)
            