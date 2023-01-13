def solution(score):
    answer = []
    answer_= []
    for i in range(len(score)):
        answer.append(score[i][0]+score[i][1])
    answer_ = answer.sort()
    print(answer_)
    return answer
solution([[80, 70], [90, 50], [40, 70], [50, 80]])