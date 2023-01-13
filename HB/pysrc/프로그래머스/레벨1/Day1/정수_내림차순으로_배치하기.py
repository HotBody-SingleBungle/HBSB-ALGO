def solution(n):
    answer = ''
    lst = []
    for i in str(n):
        lst.append(i)
    lst = sorted(lst)[::-1]
    for i in range(len(lst)):
        answer += lst[i]
    return int(answer)