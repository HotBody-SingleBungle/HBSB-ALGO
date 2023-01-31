def solution(numbers, hand):
    answer = ''
    lefhad = 10
    righad = 12
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers.pop(i)
            numbers.insert(i, 11)
    print(numbers)
    for i in range(len(numbers)):
        r = numbers[i] // 3
        c = numbers[i] % 3
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'
            lefhad = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
            righad = numbers[i]
        elif ((numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8 or numbers[i] == 0) and ((lefhad == 1 and righad == 3) or (lefhad == 4 and righad == 6) or ((lefhad == 7 and righad == 9)))) or abs(lefhad - numbers[i]) == abs(righad - numbers[i]):
            if hand == "right":
                answer += 'R'
                righad = numbers[i]
            else:
                answer += 'L'
                lefhad = numbers[i]
        elif lefhad % 3 != 0 and righad % 3 != 0:
            if abs(r - (lefhad // 3))+abs(c - (lefhad % 3)) > abs(r - (righad // 3))+abs(c - (righad % 3)):
                answer += 'R'
                righad = numbers[i]
            elif abs(r - (lefhad // 3))+abs(c - (lefhad % 3)) < abs(r - (righad // 3))+abs(c - (righad % 3)):
                answer += 'L'
                lefhad = numbers[i]
            else:
                if hand == "right":
                    answer += 'R'
                    righad = numbers[i]
                else:
                    answer += 'L'
                    lefhad = numbers[i]
        elif lefhad % 3 == 0:
            if abs(r - (lefhad // 3 - 1))+abs(c - 3) > abs(r - (righad // 3))+abs(c - (righad % 3)):
                answer += 'R'
                righad = numbers[i]
            elif abs(r - (lefhad // 3 - 1))+abs(c - 3) < abs(r - (righad // 3))+abs(c - (righad % 3)):
                answer += 'L'
                lefhad = numbers[i]
            else:
                if hand == "right":
                    answer += 'R'
                    righad = numbers[i]
                else:
                    answer += 'L'
                    lefhad = numbers[i]
        elif righad % 3 == 0:
            if abs(r - (lefhad // 3))+abs(c - (lefhad % 3)) > abs(r - (righad // 3 - 1))+abs(c - 3):
                answer += 'R'
                righad = numbers[i]
            elif abs(r - (lefhad // 3))+abs(c - (lefhad % 3)) <  abs(r - (righad // 3 - 1))+abs(c - 3):
                answer += 'L'
                lefhad = numbers[i]
            else:
                if hand == "right":
                    answer += 'R'
                    righad = numbers[i]
                else:
                    answer += 'L'
                    lefhad = numbers[i]
    print(answer)

# 나머지와 몫으로 구하자 다시 해보자 - 17:37
    return answer
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")