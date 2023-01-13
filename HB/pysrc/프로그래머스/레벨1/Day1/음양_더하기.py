def solution(absolutes, signs):
    answer = 123456789
    for i in range(len(signs)):
        if signs[i]:
            absolutes[i] = -(absolutes[i])
    answer = -sum(absolutes)
    return answer