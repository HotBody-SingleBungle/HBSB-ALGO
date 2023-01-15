def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if yak(i) % 2:
            answer -= i
        else:
            answer += i
    return answer

def yak(n):
    sqr = int(n**(0.5))
    cnt = 0
    for i in range(1, sqr):
        if n % i == 0:
            cnt += 2
    if sqr == n **(0.5):
        cnt += 1
    return cnt