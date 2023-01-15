def solution(s):
    answer = ''
    lst = []
    for i in s:
        lst.append(ord(i))
    lst.sort()
    for i in range(len(s)):
        answer += chr(int(lst.pop()))
    return answer