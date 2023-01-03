def solution(array):
    answer = 0
    max_ = 0
    visit = [0] * 1000
    for i in array:
        visit[i] += 1
    
    for i in range(1000):
        if visit[i] > max_:
            max_ = visit[i]
    answer = visit.index(max_)
    if visit.count(max_)>1:
        answer = -1
    
            
    return answer