def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        quiz_num=quiz[i].split(' ')
        a=0
        if quiz_num[1] =='+':
            a=int(quiz_num[0])+int(quiz_num[2])
        else:
            a=int(quiz_num[0])-int(quiz_num[2])
        if a==int(quiz_num[4]):
            answer.append('O')
        else:
            answer.append('X')
    return answer