from itertools import combinations
lst = []
lst2 = []
N, K = map(int,input().split())
for i in range(N):
    lst.append(list(map(int, input().split())))
perm = combinations([i for i in range(N)], N//2)
for i in perm:
    lst2.append(i)
answer = []

for i in range(len(lst2)//2):
    temp = 0
    for j in range(N//2):
        a = 0
        for k in range(K):
            a += lst[lst2[i][k]][j] - lst[lst2[len(lst2)-1-i][k]][j]
        answer.append(abs(a))
    temp += answer.pop()
    temp += answer.pop()
    temp += answer.pop()
    answer.append(temp)

print(min(answer))
