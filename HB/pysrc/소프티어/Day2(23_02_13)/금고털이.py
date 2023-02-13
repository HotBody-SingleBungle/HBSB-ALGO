W ,N = map(int, input().split())
lst = []
answer = 0
for i in range(N):
    lst.append(list(map(int,input().split())))
lst.sort(key = lambda x: (-x[1]))
for i in range(len(lst)):
    if W >= lst[i][0]:
        W -= lst[i][0]
        answer += lst[i][0] * lst[i][1]
    elif 0 < W <  lst[i][0]:
        answer += W * lst[i][1]
        break
    else:
        break
print(answer)

