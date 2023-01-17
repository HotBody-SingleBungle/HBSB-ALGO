def solution(d, budget):
    answer = 0
    d.sort()
    sum_=0
    for i in range(len(d)):
        sum_+=d[i]
        if sum_ <= budget:
            answer+=1
        if answer > budget:
            answer -= 1
            break
    return answer