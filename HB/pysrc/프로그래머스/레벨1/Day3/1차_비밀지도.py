def solution(n, arr1, arr2):
    answer = []
    line = [[0] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        n = arr1[i]
        m = arr2[i]
        for j in range(len(arr1)):
            line[i][4-j] += n % 2 + m % 2
            n //= 2
            m //= 2 
    for i in range(len(arr1)):
        ans = ''       
        for j in range(len(arr1)):
            if line[i][j] > 0:
                ans += "#"
            else:
                ans+= ' '
        answer.append(ans)
    print(answer)
    return answer
