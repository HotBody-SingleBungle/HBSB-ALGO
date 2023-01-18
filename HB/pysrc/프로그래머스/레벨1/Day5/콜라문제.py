def solution(a, b, n):
    answer = 0
    while n != 1:
        answer += n//a *b
        if n % a:
            if n // a >= 1:
                n = (n//a)*b + (n % a)
            else:
                return answer
        else:
            n //= a
            n*=b
    return answer
solution(3,2,20)