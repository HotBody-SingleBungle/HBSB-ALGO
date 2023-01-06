def solution(num_list, n):
    answer = [[] for _ in range(len(num_list) // n)]
    for i in range(len(num_list)//n):
        for j in range(n):
            answer[i].append(num_list[n*i+j])
    return answer