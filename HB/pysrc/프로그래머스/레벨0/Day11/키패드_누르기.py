def solution(numbers, hand):
    answer = ''
    right_finger = '#'
    left_finger = '*'
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
    return answer