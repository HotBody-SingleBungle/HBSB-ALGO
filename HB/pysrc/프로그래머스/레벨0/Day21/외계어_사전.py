def solution(spell, dic):
    answer = 2
    for i in range(len(dic)):
        dic[i] =[k for k in dic[i]]
        for j in range(len(spell)):
            if spell[j] in dic[i]:
                dic[i].pop(dic[i].index(spell[j]))
            else:
                dic[i].append('x')
#dic[i] =dic[i][:j]+dic[i][j+1:]
        if dic[i] == []:
            answer = 1
    return answer