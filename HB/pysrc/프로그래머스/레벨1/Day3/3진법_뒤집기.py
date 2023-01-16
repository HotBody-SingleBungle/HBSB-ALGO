def solution(n):
    answer = 0
    ans = ''
    while n:
        ans+=str(n%3)
        n//=3
    ans = ans[::-1]
    for i in range(len(ans)):
        answer += int(ans[i])*3**i
    return answer