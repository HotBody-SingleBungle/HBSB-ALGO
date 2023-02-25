def solution(cards1, cards2, goal):
    answer = ''
    num_1 = 0
    num_2 = 0
    for i in range(len(goal)):
        print(i)
        if num_1 < len(cards1) and goal[i] == cards1[num_1]:
            num_1 += 1
            if num_1 + num_2 == len(goal):
                answer = "Yes"
                break
            pass
        elif num_2 < len(cards2) and goal[i] == cards2[num_2]:
            num_2 += 1
            if num_1 + num_2 == len(goal):
                answer = "Yes"
                break
            pass
        else:
            answer = "No"
            break
    print(answer)
    return answer
solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"])