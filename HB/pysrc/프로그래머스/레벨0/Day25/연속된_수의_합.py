def solution(num, total):
    answer = []
    if total % num ==0:
        for i in range(- num//2 +1, num//2+1):
            answer.append(total // num+i)
    else:
        for i in range(-num//2+1, num//2+1):
            answer.append(total // num +i)
    return answer