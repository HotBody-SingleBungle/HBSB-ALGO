def solution(numbers):
    answer = 0
    lst = [i for i in range(0, 10)]
    for i in range(len(numbers)):
        if numbers[i] in lst:
            lst[lst.index(numbers[i])] = 0
    answer = sum(lst)
    return answer