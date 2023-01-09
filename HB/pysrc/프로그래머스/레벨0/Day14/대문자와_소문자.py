def solution(my_string):
    answer = ''
    pl = ord("A") - ord("a")
    for i in range(len(my_string)):
        if ord("a") <= ord(my_string[i]) <= ord("z"):
            answer +=chr(ord(my_string[i]) + pl)
        else:
            answer += chr(ord(my_string[i]) - pl)
    return answer