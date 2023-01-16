def solution(sizes):
    answer = 0
    l_lst = []
    s_lst = []
    for i in range(len(sizes)):
        sizes[i].sort()
        l_lst.append(sizes[i][1])
        s_lst.append(sizes[i][0])
    l_lst.sort()
    s_lst.sort()
    answer += s_lst[-1] * l_lst[-1]
    return answer