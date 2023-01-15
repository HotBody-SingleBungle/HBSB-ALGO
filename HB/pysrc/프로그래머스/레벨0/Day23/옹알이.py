def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in range(len(babbling)):    
        word_erase = ["aya", "ye", "woo", "ma"]
        visit = [0]*4
        for j in range(4):
            if babbling[i] == '':
                answer += 1
                break
            if babbling[i].strip()[:3] in word and not visit[word.index(babbling[i][:3])]:
                visit[word.index(babbling[i][:3])] = 1
                #word_erase[word.index(babbling[i][:3])]=0
                babbling[i] = babbling[i][3:]
                if j == 3:
                    answer += 1
            elif babbling[i][:2] in word and not visit[word.index(babbling[i][:2])]:
                visit[word.index(babbling[i][:2])] = 1
                #word_erase[word.index(babbling[i][:2])]=0
                babbling[i] = babbling[i][2:]
                if j == 3:
                    answer += 1
            else:
                break
    print(answer)
solution(["aya", "ayayewooma", "yee", "u", "maa", "wyeoo"])