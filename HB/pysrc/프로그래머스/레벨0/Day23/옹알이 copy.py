def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    answer = 0
    visit = [0]*4
    for i in range(len(babbling)):
        for j in range(len(word)):
            if babbling[i][:len(word[j])] == word[j] and not visit[j]:
                babbling[i] = babbling[i][len(word[j]):]
                visit[j] = 1
                if babbling[i] == '':
                    answer += 1
                    break
            else:
                pass
    print(babbling)
solution(["aya", "yee", "u", "maa", "wyeoo", "ayayewooma"])