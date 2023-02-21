def solution(babbling):
    # print(len(babbling))
    answer = 0
    for i in range(len(babbling)):
        replaced_word = babbling[i].replace('aya', '1')
        replaced_word = replaced_word.replace('ye', '2')
        replaced_word = replaced_word.replace('woo', '3')
        replaced_word = replaced_word.replace('ma', '4')
        print(replaced_word)
        if replaced_word.isdigit():
            cnt = 0
            if len(replaced_word) == 1:
                answer += 1
            else:
                for j in range(len(replaced_word)-1):
                    if replaced_word[j] == replaced_word[j+1]:
                        print(cnt)
                        break
                    else:
                        cnt += 1
                        print(cnt)
                        if cnt == len(replaced_word)-1:
                            print(replaced_word[j])
                            answer += 1
        else:
            pass
        # print(i)
    print("answer is " , answer)
    return answer
solution(["ayaye", "woo", "yeye", "yemawoo", "ayaayaa"])