def solution(denum1, num1, denum2, num2):
    answer = []
    ud = num1*num2
    up = denum1*num2 + denum2*num1
    ran = ud
    for i in range(0,ran+1):
        if(ud % (ran-i) ==0 and up%(ran-i)==0):
            ud = ud//(ran-i)
            up = up//(ran-i)
            break
    answer.append(up)
    answer.append(ud)
            
    return answer