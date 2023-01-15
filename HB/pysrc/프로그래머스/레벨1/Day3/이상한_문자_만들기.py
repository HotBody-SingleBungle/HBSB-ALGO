def solution(s):
    answer = ''
    lst = s.split(' ')
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j % 2:
                if ord(lst[i][j]) >=97:
                    answer+=lst[i][j]
                else:
                    answer+=chr(ord(lst[i][j])+32)
            else:
                if ord(lst[i][j]) >=97:
                    answer+=chr(ord(lst[i][j])-32)
                else:
                    answer +=lst[i][j]
        if i != len(lst)-1:
            answer+=' '
    return answer