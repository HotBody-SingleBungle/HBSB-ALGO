def solution(s):
    answer = 0
    x = s[0]
    lst = []
    ans = ''
    cnt_1 = 0
    cnt_2 = 0
    for i in range(len(s)):
        if x == s[i]:
            cnt_1 += 1
            ans += s[i]
            if len(ans) and i == len(s)-1:
                lst.append(ans)
        
        else:
            cnt_2 += 1
            ans += s[i]
            if cnt_1 == cnt_2:
                lst.append(ans)
                ans = ''
                cnt_1 = 0
                cnt_2 = 0
                if i != len(s)-1:
                    x = s[i+1]
            if len(ans) and i == len(s)-1:
                lst.append(ans)
    answer += len(lst)
    print(lst)
    print(answer)           
    return answer

solution('ab')
solution('abracadabra')