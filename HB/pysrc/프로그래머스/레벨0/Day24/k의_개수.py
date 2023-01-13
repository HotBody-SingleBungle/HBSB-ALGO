def solution(i, j, k):
    answer = 0
    sen=''
    for a in range(i, j+1):
        sen+=str(a)
    for b in sen:
        if int(b) == k:
            answer+=1
    return answer