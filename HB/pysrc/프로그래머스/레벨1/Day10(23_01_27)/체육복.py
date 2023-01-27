def solution(n, lost, reserve):
    answer = 0
    c_list = [0] * n
    for i in range(len(lost)):
        c_list[lost[i]-1] = -1
    for i in range(len(reserve)):
        c_list[reserve[i]-1] += 1
        
    for i in range(n):
        if i <= n-2 and c_list[i] == -1 and c_list[i+1] == 1:
            c_list[i+1] = 0
            c_list[i] = 0
        elif i <= n-2 and c_list[i] == 1 and c_list[i+1] == -1:
            c_list[i] = 0
            c_list[i+1] = 0
            
    for i in c_list:
        if i >= 0:
            answer += 1
    print(answer)
    return answer
solution(5, [2,3], [1,3,4])