def solution(sides):
    answer = 0
    a = max(sides)
    if sum(sides) - a > a:
        answer = 1
    else:
        answer = 2
    return answer