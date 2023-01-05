def solution(n):
    answer = 0
    sqr = int(n**(0.5))
    for i in range(1,sqr+1):
        if n%i ==0:
            answer+=1
    if sqr == n**(0.5):
        answer = answer*2-1
    else:
        answer = answer*2
    return answer