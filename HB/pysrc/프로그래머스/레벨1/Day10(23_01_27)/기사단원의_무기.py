def solution(number, limit, power):
    answer = 0
    anslist = []

    for i in range(1, number + 1):
        n = divnum(i)
        if n > limit:
            anslist.append(power)
        else:
            anslist.append(n)
    answer = sum(anslist)
    return answer
def divnum(num):
    cnt = 0
    sqr = int(num **(0.5))
    if num == 1:
        cnt = 1
    else:
        if num ** (0.5) == sqr:
            cnt += 1
            for i in range(1, sqr):
                if num % i == 0:
                    cnt += 2
        else:
            for i in range(1, sqr+1):
                if num % i == 0:
                    cnt += 2
    return cnt
solution(10,5,2)