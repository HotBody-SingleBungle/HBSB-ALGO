def solution(polynomial):
    answer = ''
    lst = polynomial.split(" ")
    x_cnt = 0
    cnt = 0
    for i in range(len(lst)):
        if "x" in lst[i]:
            if lst[i] == "x":
                x_cnt += 1
            else:
                x_cnt += int(lst[i][0:-2])
        elif lst[i] != '+':
            cnt += int(lst[i])
    if x_cnt > 0:
        if x_cnt == 1:
            answer += 'x'
        else:
            answer += str(x_cnt)+'x'
    if cnt >= 0 and x_cnt > 0:
        answer += ' + '+str(cnt)
    elif cnt >= 0 and x_cnt == 0:
        answer = str(cnt)
    print(answer)
    return answer
solution("3 + x")