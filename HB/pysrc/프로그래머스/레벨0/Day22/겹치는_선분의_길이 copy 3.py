def solution(lines):
    ablist = []
    bclist = []
    calist = []
    abclist = []
    ab = 0
    bc = 0
    ca = 0
    abc = 0

    for i in range(lines[0][0], lines[0][1]+1):
        if i in [j for j in range(lines[1][0], lines[1][1]+1)]:
            ablist.append(i)
    for i in range(lines[1][0], lines[1][1]+1):
        if i in [j for j in range(lines[2][0], lines[2][1]+1)]:
            bclist.append(i)
    for i in range(lines[0][0], lines[0][1]+1):
        if i in [j for j in range(lines[2][0], lines[2][1]+1)]:
            calist.append(i)
    for i in range(lines[1][0], lines[1][1]+1):
        if i in calist:
            abclist.append(i)
    if ablist != []:
        ab = ablist[-1] - ablist[0]
    if bclist != []:
        bc = bclist[-1] - bclist[0]
    if calist != []:
        ca = calist[-1] - calist[0]
    if abclist != []:
        abc = abclist[-1] - abclist[0]
    
    print(ab + bc + ca - 2* abc)
    return ab + bc + ca - 2* abc
solution([[-1, 1], [1, 3], [3, 9]]	)