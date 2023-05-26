def solution(num_list):
    answer = 0
    mul = 1

    for i in num_list:
        mul *= i
    sum_2 = (sum(num_list))**2
    if mul > sum_2:
        return 0
    else:
        return 1