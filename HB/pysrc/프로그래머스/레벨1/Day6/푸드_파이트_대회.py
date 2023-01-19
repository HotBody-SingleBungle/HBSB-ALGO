def solution(food):
    another = ''
    answer = ''
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
    another += answer[::-1]
    answer += '0'
    answer += another
    return answer