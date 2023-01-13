def solution(before, after):
    answer = 1
    b_=[]
    a_ =[]
    for i in before:
        b_.append(i)
    for i in after:
        a_.append(i)
    #if a_.sort() == b_.sort():
        #answer=1
    for i in range(len(a_)):
        if a_[i] != b_[i]:
            answer*=0
    return answer