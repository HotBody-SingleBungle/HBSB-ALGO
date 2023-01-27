def solution(participant, completion):
    answer = ''
    visit = [0]*len(participant)
    for i in range(len(participant)):
        if participant[i] in completion:
            visit[i] = 1
            completion.pop(completion.index(participant[i]))
    for i in range(len(visit)):
        if visit[i] == 0:
            answer = participant[i]
    return answer