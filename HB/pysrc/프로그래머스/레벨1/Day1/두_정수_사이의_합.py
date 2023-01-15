def solution(a, b):
    answer = 0
    lst = [a, b]
    lst.sort()
    for i in range(lst[0], lst[1]+1):
        answer += i
    return answer