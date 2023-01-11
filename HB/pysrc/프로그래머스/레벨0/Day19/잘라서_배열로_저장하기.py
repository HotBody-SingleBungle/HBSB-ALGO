def solution(my_str, n):
    answer = []
    lgt=len(my_str)//n
    last=len(my_str)%n
    for i in range(lgt):
        a=''
        for j in range(n):
            a+=my_str[i*n+j]
        answer.append(a)
    if last>0:
        answer.append(my_str[len(my_str)-last:len(my_str)])
    return answer