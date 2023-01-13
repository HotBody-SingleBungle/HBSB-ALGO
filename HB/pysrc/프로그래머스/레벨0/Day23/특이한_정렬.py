def solution(numlist, n):
    answer = []
    sublist = []
    for i in range(len(numlist)):
        sublist.append(abs(numlist[i]-n))
    sublist.sort()
    for i in range(len(sublist)):
        if n + sublist[i] in numlist:
            answer.append(n + sublist[i])
            numlist.pop(numlist.index(n + sublist[i]))
        elif n - sublist[i] in numlist:
            answer.append(n - sublist[i])
    return answer