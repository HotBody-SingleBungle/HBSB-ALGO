def solution(s):
    answer = True
    pcnt = 0
    ycnt = 0
    for i in s:
        if ord(i) == 112 or ord(i) == 80:
            pcnt += 1
        elif ord(i) == ord("y") or ord(i) == ord("Y"):
            ycnt += 1
    if pcnt == ycnt:
        answer = True
    else:
        answer = False
    return answer