def solution(N, stages):
    answer_ = []
    answer = []
    visit = [0] * (N+2)
    for i in range(len(stages)):
        visit[stages[i]] += 1
    print(visit)
    cnt = 0
    for i in range(1, len(visit)-1):
        a = len(stages) - cnt
        b = visit[i]
        cnt += b
        answer_.append([i,b/a])
        if cnt == len(stages):
            for j in range(i+1, len(visit)-1):
                answer_.append([j, 0])
            break
    answer_.sort(key=lambda x:(-x[1], x[0]))
    for i in range(len(answer_)):
        answer.append(answer_[i][0]) 
    print(answer)
    return answer
# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])

# 와 0 으로 나누는 경우 생각도 못했다 망할 카카오
# solution(7,[1,5,5,3,3,5,5])