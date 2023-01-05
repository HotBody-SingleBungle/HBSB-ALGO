def solution(age):
    answer = ''
    alpha = "abcdefghij"
    while age //10 or age %10:
        answer += alpha[age%10]
        age = age //10
    return answer[::-1]