def solution(n, arr1, arr2):
    answer = []
    line = [[0] * n for _ in range(n)]
    for i in range(n):
        k = arr1[i]
        l = arr2[i]
        for j in range(n):
            line[i][n-1-j] += k % 2 + l % 2
            k //= 2
            l //= 2 
    for i in range(n):
        ans = ''       
        for j in range(n):
            if line[i][j] > 0:
                ans += "#"
            else:
                ans+= ' '
        answer.append(ans)
    print(line)
    return answer
