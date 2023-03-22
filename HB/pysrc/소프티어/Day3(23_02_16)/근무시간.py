lst = []
ans = 0
for i in range(5):
    lst.append(input())
for i in range(5):
    ans += (int(lst[i][6:8]) - int(lst[i][0:2]))* 60 + int(lst[i][9:11]) - int(lst[i][3:5])
print(ans)