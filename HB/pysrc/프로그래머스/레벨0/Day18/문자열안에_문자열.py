def solution(str1, str2):
    answer = 2
    
    for i in range(len(str1)-len(str2)+1):
        a=len(str2)
        for j in range(len(str2)):
            if str1[i+j]==str2[j]:
                a-=1
            else:
                break
            if a==0:
                answer =1
    return answer