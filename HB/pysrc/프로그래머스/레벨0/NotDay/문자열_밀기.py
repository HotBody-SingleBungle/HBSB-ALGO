def solution(A, B):
    answer = -1
    if A == B:
        answer = 0
    else:
        for i in range(1, len(A)):
            if A[-i:] + A[:len(A)-i] == B:
                answer = i
                break
    print(answer)
    return answer
solution("tattta","tatatt")