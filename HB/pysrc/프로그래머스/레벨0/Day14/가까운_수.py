def solution(array, n):
    answer = 0
    lst=[]
    array.sort()
    for i in array:
        if i>=n:
            lst.append(i-n)
        else:
            lst.append(n-i)
    answer=array[lst.index(min(lst))]
    return answer