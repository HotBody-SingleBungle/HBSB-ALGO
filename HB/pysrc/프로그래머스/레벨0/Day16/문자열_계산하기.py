def solution(my_string):
    answer = 0
    a= my_string.split(' ')
    while len(a)!=1:
        if a[1]=='+':
            answer= int(a[0])+int(a[2])
            a.pop(0)
            a.pop(0)
            a.pop(0)
            a.insert(0,answer)
        else:
            answer= int(a[0])-int(a[2])
            a.pop(0)
            a.pop(0)
            a.pop(0)
            a.insert(0,answer)
    return answer