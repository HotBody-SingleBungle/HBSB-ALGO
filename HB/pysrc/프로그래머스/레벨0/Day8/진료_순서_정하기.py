def solution(emergency):
    answer = []
    emergency_ = sorted(emergency)[::-1]
    for i in emergency:
        answer.append(emergency_.index(i)+1)
    return answer