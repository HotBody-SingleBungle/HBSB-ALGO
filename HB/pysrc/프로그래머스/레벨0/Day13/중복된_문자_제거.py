def solution(my_string):
    answer = ''
    visit = [0]*53
    for i in range(len(my_string)):
        if 65<= ord(my_string[i]) <= 90 and not visit[ord(my_string[i]) - 65+27]:
            visit[ord(my_string[i]) - 65+26+1] = 1
            answer += my_string[i]
        elif my_string[i] == " " and not visit[0]:
            visit[0] = 1
            answer += " "
        elif 97 <= ord(my_string[i]) <= 122 and not visit[ord(my_string[i])-97+1]:
            visit[ord(my_string[i])-97+1] = 1
            answer += my_string[i]
        
        print(ord("W"))
    return answer