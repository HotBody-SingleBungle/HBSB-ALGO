def solution(n):
    answer = 0
    sum_lst = []
    sqr = int(n**(0.5))
    for i in range(1, sqr + 1):
        if i not in sum_lst and n % i == 0 and i != sqr:
            sum_lst.append(i)
            sum_lst.append(n//i)
        elif i == sqr and sqr**2 == n:
            sum_lst.append(i)
    answer = sum(sum_lst)
    return answer