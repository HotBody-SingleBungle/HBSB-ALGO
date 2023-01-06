answer = 0
visited = [0]*balls
def solution(balls, share):
    for i in range(balls):
        if not visited[i]:
            visited[i] = 1
            if visited.count(1) == share:
                answer += 1
            
    return answer