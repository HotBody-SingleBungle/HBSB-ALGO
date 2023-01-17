def solution(d, budget):
    answer = 0
    d.sort()
    sum_=0
    cnt=0
    
    for i in range(len(d)):
        sum_+=d[i]
        cnt+=1

        if sum_ == budget:
            answer=cnt
            return answer
        
        if sum_>budget:
            cnt-=1
            break
    
            
    return answer