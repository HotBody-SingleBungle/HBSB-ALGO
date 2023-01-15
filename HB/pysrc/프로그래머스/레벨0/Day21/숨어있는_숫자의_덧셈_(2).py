def solution(my_string):
    answer = 0
    a=''
    for i in range(len(my_string)):
        if ord('0') <= ord(my_string[i]) <= ord('9'):
            a += my_string[i]
            if i == len(my_string)-1:
                answer += int(a)
        elif a!='' and (ord('0') > ord(my_string[i]) or ord(my_string[i]) > ord('9')):
            answer += int(a)
            a=''
        else:
            pass
    return answer