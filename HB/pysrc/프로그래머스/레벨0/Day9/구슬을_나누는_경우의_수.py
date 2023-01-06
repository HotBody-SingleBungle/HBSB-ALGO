def solution(balls, share):
    answer = 1
    n=balls
    m=share
    for i in range(n-m+1, n+1):
        answer*=i
    for i in range(1,m+1):
        answer//=i
    return answer
