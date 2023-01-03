def solution(numbers):
    answer = []
    for _ in range(len(numbers)):
        answer.append(2*(numbers.pop(0)))
    print(answer)
    return answer