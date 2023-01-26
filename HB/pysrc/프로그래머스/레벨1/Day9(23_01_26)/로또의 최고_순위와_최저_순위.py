def solution(lottos, win_nums):
    answer = []
    cnt = 0
    ans = 6
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
    cnt+=lottos.count(0)
    if cnt == 6:
        ans=1
    elif cnt == 5:
        ans=2
    elif cnt == 4:
        ans=3
    elif cnt == 3:
        ans=4
    elif cnt == 2:
        ans=5
    else:
        pass
    answer.append(ans)
    cnt-=lottos.count(0)
    if cnt == 6:
        ans=1
    elif cnt == 5:
        ans=2
    elif cnt == 4:
        ans=3
    elif cnt == 3:
        ans=4
    elif cnt == 2:
        ans=5
    else:
        ans=6
    answer.append(ans)
    return answer