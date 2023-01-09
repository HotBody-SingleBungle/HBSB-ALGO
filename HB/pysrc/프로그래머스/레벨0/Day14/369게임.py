def solution(order):
    answer = str(order)
    cnt = 0
    for i in answer:
        if i == "3" or i == "6" or i == "9":
            cnt += 1
    return cnt