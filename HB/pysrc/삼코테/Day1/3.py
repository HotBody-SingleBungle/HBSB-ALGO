N = int(input())
plans = list(map(str, input().split()))
x = 0
y = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir = ['d', 'r', 'u', 'l']
for plan in plans:
    for i in range(4):
        if plan == dir[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                x = nx
                y = ny
            else:
                continue
        
print(x,y)