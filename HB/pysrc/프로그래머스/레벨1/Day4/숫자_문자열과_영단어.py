def solution(s):
    answer = 0
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(alpha)):
        if alpha[i] in s:
            print(s.find(alpha[i]))
            
        
    return answer
solution("oneoneone")