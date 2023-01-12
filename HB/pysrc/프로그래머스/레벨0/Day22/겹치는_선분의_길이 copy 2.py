def solution(lines):
    ablist = []
    bclist = []
    calist = []
    abclist = []

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
    print(abclist)
    print(ablist)
    print(bclist)
    print(calist)
    
    print(len(ablist) + len(bclist) + len(calist) -1 - 2*len(abclist))
    return (len(ablist) + len(bclist) + len(calist) - 1 - 2*len(abclist))
solution([[0, 5], [3, 9], [1, 10]]	)