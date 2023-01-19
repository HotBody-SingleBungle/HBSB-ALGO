def solution(t, p):
    answer = 0
    pl = len(p)
    tl = len(t)
    for i in range(tl-pl+1):
        if int(t[i:i+pl]) <= int(p):
            answer += 1
    return answer