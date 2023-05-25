def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        ans = 0
        for j in photo[i]:
            if j in name:
                ans += yearning[name.index(j)]    
        answer.append(ans)
    return answer