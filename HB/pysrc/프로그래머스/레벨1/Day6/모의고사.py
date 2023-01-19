def solution(answers):
    n = len(answers)
    answer_ = []
    cnt1=0
    cnt2=0
    cnt3=0
    answer = []
    one=[1,2,3,4,5]*2000
    two=[2,1,2,3,2,4,2,5]*1250
    three=[3,3,1,1,2,2,4,4,5,5]*1000
    for i in range(n):
        if answers[i]==one[i]:
            cnt1+=1
        if answers[i]==two[i]:
            cnt2+=1
        if answers[i]==three[i]:
            cnt3+=1
    print(cnt1,cnt2,cnt3)
    answer_.append(cnt1)
    answer_.append(cnt2)
    answer_.append(cnt3)
    answer_.sort()
    if answer_[2] == cnt1:
        answer.append(1)
    if answer_[2] == cnt2:
        answer.append(2)
    if answer_[2] == cnt3:
        answer.append(3)

    return answer