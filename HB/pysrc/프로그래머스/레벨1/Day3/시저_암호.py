def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif 65 <= ord(s[i]) <= 90:
            if ord(s[i])+n > 90:
                answer += chr(ord(s[i])+n-26)
            else:
                answer += chr(ord(s[i])+n)
        elif 97 <= ord(s[i]) <= 122:
            if ord(s[i])+n > 122:
                answer += chr(ord(s[i])+n-26)
            else:
                answer += chr(ord(s[i])+n)
    print(answer)
    return answer