def solution(my_string):
    answer = []
    ans = ''
    for i in range(len(my_string)):
        if ord(my_string[i]) < ord("a"):
            answer.append(chr(ord(my_string[i])+32))
        else:
            answer.append(my_string[i])
    answer.sort()
    for i in answer:
        ans += i
    return ans
        