def solution(numbers, hand):
    answer = ''
    lefhad = 0
    righad = 0
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'
            lefhad = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
            righad = numbers[i]
        else:
        # elif numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8 or numbers[i] == 0:
            if lefhad - numbers[i] == righad - numbers[i] or abs(lefhad - numbers[i]) == abs(righad - numbers[i]):
                if hand == "right":
                    answer += 'R'
                    righad = numbers[i]
                else:
                    answer += 'L'
                    lefhad = numbers[i]
    print(answer)


    return answer
solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")