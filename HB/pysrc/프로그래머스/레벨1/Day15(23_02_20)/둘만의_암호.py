def solution(s, skip, index):
    answer = ''
    skip_idx = [ord(skip[i]) for i in range(len(skip))]

    for j in range(len(s)):
        cnt = 0
        cnt_ = 0

        for i in range(50):

            if ord(s[j])+i+1 < 123:
                if ord(s[j])+i+1 in skip_idx:
                    cnt_ += 1
                    pass

                else:
                    cnt += 1

                    if cnt == index:
                        if ord(s[j])+i+1 <= 122:
                            answer += chr(ord(s[j])+cnt+cnt_)
                        else:
                            answer += chr(ord(s[j])+cnt+cnt_-26)
                        break

            else:
                if ord(s[j])+i-25 in skip_idx or ord(s[j])+i-25-26 in skip_idx:
                    cnt_ += 1
                    pass
                else:
                    cnt += 1

                    if cnt == index:
                        if ord(s[j])+cnt-26+cnt_ < 123:
                            answer += chr(ord(s[j])+cnt-26+cnt_)
                        else:
                            answer += chr(ord(s[j])+cnt-52+cnt_)
                        break
    print(answer)
    return answer
solution('z', 'abcdefghij', 20)
# print(ord("}"))