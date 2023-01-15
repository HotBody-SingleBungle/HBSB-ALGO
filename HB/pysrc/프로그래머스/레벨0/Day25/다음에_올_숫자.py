def solution(common):
    answer = 0
    if common[0] - common[1] == common[-2] - common[-1]:
        answer = -(common[0] -common[1])+ common[-1]
    elif common[0] / common[1] == common[-2] / common[-1]:
        answer = common[-1]**2 / common[-2]
    return answer