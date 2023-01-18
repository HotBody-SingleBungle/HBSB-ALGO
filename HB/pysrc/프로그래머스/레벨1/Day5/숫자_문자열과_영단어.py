from curses.ascii import isdigit


def solution(s):
    answer = ''
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    idx = 0
    while True:
        if idx == len(s):
            print(answer)
            return int(answer)
        if isdigit(s[idx]):
            answer += s[idx]
            idx += 1
        for i in range(len(alpha)):
            if s[idx:idx+2] == alpha[i][0:2]:
                answer += str(i)
                idx += len(alpha[i])

solution("zero12one1")