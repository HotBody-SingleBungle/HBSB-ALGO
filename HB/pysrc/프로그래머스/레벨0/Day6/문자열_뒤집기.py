def solution(my_string):
    answer = ''
    lth=len(my_string)
    for i in range(lth):
        answer += my_string[lth-i-1]
    return answer