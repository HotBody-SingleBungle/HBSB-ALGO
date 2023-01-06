def solution(n):
    answer = []
    sqr = int(n **(0.5))
    for i in range(1, sqr+1):
        if n % i == 0:
            answer.append(i)
            if i != n//i:
                answer.append(n//i)
    answer = sorted(answer)
    return answer