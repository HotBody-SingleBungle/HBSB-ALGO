def solution(n):
    answer = 0
    while n // 10:
        rest = n%10
        n = (n // 10) 
        answer += n
        n += rest
    print(answer)
    return answer
solution(1081)