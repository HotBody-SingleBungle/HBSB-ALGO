def solution(arr):
    answer = []
    if len(arr) != 1:
        arr.pop(arr.index(min(arr)))
        answer = arr
    else:
        answer = [-1]
    return answer