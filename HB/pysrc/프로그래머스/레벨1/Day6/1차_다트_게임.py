def solution(dartResult):
    dgt = []
    answer = 0
    a = dartResult.split()
    for i in range(len(a)-1):
        if a[i].isdigit():
            if a[i+1].isdigit():
                dgt.append(a[i:i+2])
    print(dgt)
    return answer
solution("1S3D#5T*")