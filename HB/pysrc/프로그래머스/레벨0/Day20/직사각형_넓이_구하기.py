def solution(dots):
    answer = 0
    for i in range(3):
        if dots[3][0] == dots[i][0] and dots[3][1] != dots[i][1]:
            a = dots[3][1] - dots[i][1]
        elif dots[3][1] == dots[i][1] and dots[3][0] != dots[i][0]:
            b = dots[3][0] - dots[i][0]
    answer = a * b
    if answer < 0:
        answer *= -1
    return answer