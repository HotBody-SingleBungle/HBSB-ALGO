def solution(X, Y):
    answer = ''
    ans_list = []
    x_list = list(X)
    y_list = list(Y)
    for i in range(len(x_list)):
        if x_list[i] in y_list:
            ans_list.append(x_list[i])
            y_list.pop(y_list.index(x_list[i]))
        else:
            answer = "-1"
    print(ans_list)
    if len(ans_list):
        if len(ans_list) == ans_list.count('0'):
            answer="0"
        else:
            ans_list.sort(reverse=True)
            answer = ''.join(ans_list)            
    print(answer)
    return answer
solution("100", "203045")