def solution(dartResult):
    answer = 0
    a = [[], [], []]
    DR = list(dartResult)
    if (DR[1].isdigit()):
        a[0].append(int(DR[0]+DR[1]))
        DR.pop(0)
        DR.pop(0)
    else:
        a[0].append(int(DR[0]))
        DR.pop(0)
    if DR[0] == 'S':
        a[0][0] = a[0][0]**1
        DR.pop(0)
    elif DR[0] == 'D':
        a[0][0] = a[0][0]**2
        DR.pop(0)
    elif DR[0] == 'T':
        a[0][0] = a[0][0]**3
        DR.pop(0)
    if (DR[0] == "#" or DR[0] == "*"):
        specialchr(a, DR[0])
        DR.pop(0)
    if (DR[1].isdigit()):
        a[1].append(int(DR[0]+DR[1]))
        DR.pop(0)
        DR.pop(0)
    else:
        a[1].append(int(DR[0]))
        DR.pop(0)
    if DR[0] == 'S':
        a[1][0] = a[1][0]**1
        DR.pop(0)
    elif DR[0] == 'D':
        a[1][0] = a[1][0]**2
        DR.pop(0)
    elif DR[0] == 'T':
        a[1][0] = a[1][0]**3
        DR.pop(0)
    if (DR[0] == "#" or DR[0] == "*"):
        specialchr(a, DR[0])
        DR.pop(0)
    if (DR[1].isdigit()):
        a[2].append(int(DR[0]+DR[1]))
        DR.pop(0)
        DR.pop(0)
    else:
        a[2].append(int(DR[0]))
        DR.pop(0)
    if DR[0] == 'S':
        a[2][0] = a[2][0]**1
        DR.pop(0)
    elif DR[0] == 'D':
        a[2][0] = a[2][0]**2
        DR.pop(0)
    elif DR[0] == 'T':
        a[2][0] = a[2][0]**3
        DR.pop(0)
    if len(DR) and (DR[0] == "#" or DR[0] == "*"):
        specialchr(a, DR[0])
        DR.pop(0)
        answer += a[0][0] + a[1][0] + a[2][0]    
    
    else:
        answer += a[0][0] + a[1][0] + a[2][0]    
    

    return answer
    
def specialchr(a, special):
    
    if special == "*":
        if len(a[2]):
            a[2][0] *= 2
            a[1][0] *= 2
        elif len(a[1]):
            a[1][0] *= 2
            a[0][0] *= 2
        else:
            a[0][0] *= 2   
    elif special == "#":
        if len(a[2]):
            a[2][0] *= -1
        elif len(a[1]):
            a[1][0] *= -1
        else:
            a[0][0] *= -1   

solution("1T2D3D#")