def solution(lines):
    answer = 0
    anslist = []
    visit = [0]*201
    
    for i in range(len(lines)):
        for j in range(lines[i][0],lines[i][1]+1):
            visit[j+100] += 1
    for i in range(201):
        if visit[i]>1:
            anslist.append(i-100)
    for i in range(len(anslist)-1):
        if anslist[i+1] - anslist[i] == 1:
            answer +=1
    print(anslist)
    print(answer)
    return answer
solution([[0, 2], [-3, -1], [-2, 1]])
