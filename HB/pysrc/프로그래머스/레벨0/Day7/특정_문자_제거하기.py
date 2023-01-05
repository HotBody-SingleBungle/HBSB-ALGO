def solution(my_string, letter):
    # answer_ = my_string.index(letter)
    # lth = len(letter)
    # answer = my_string[:answer_]
    # answer += my_string[answer_+lth:]
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] == letter:
            pass
        else:
            answer += my_string[i]
    return answer