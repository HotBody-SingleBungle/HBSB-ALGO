def solution(x):
    answer = False
    h_num = 0
    for i in str(x):
        h_num += int(i)
    if x % h_num == 0:
        answer = True
    return answer