def solution(num, k):
    answer = str(num)
    k_ = str(k)
    if answer.find(k_)!=-1:
        answer = answer.find(k_)+1
    else:
        answer = -1
    return answer