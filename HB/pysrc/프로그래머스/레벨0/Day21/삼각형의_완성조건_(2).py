def solution(sides):
    answer = 0
    sides.sort()
    answer = 2*sides[0] - 1
    return answer