def solution(array):
    answer = 0
    for i in array:
        while i //10 or i%10:
            if i%10 ==7:
                answer+=1
            i = i // 10
    return answer