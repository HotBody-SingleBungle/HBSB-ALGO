def solution(a, b):
    answer = ''
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    date = 0
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a):
        date += month[i]
    date += b-1
    answer = day[date%7]
    return answer