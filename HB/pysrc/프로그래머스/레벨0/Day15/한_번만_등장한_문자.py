def solution(s):
    answer = ''
    alp =[0]*26
    for i in s:
        alp[ord(i)-97] += 1
    for i in range(26):
        if alp[i]==1:
            answer+=chr(97+i)
    return answer