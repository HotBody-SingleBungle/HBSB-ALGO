def solution(strings, n):
    answer = []
    temp = [[] for _ in range(len(strings))]
    temp_ = [[] for _ in range(len(strings))]
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            temp[i].append(strings[i][j])
    for i in range(len(strings)):
        temp[i].insert(0,temp[i].pop(n))
        temp[i] = ''.join(temp[i])
    temp.sort()
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp_[i].append(temp[i][j])
    for i in range(len(temp)):
        temp_[i].insert(n,temp_[i].pop(0))
        temp_[i] = ''.join(temp_[i])
    
    print(temp_)
    return temp_