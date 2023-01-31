def solution(new_id):
    answer = (step7(step6(step345(step12(new_id)))))
    return answer
def step12(id):
    ans =""
    for i in range(len(id)):
        if ord("A") <= ord(id[i]) <= ord("Z"):
            ans += chr(ord(id[i])+32)
        elif ord("a") <= ord(id[i]) <= ord("z") or ord(id[i]) == ord(".") or ord("0") <= ord(id[i]) <= ord("9") or ord(id[i]) == ord("_") or ord(id[i]) == ord("-"):
            ans += id[i]
        else:
            pass
    return ans
def step345(id):
    ans = ''
    for i in range(len(id)-1):
        if id[i] == '.' and id[i+1] == '.':
            pass
        
        else:
            ans += id[i]
    ans += id[-1]
    if len(ans) and ans[0] == '.':
        ans = ans[1:]
    if len(ans) and ans[-1] == '.':
        ans = ans[0:len(ans)-1]
    if ans == "":
        ans += 'a'
    return ans
solution('..123....123..123....3..1..')
solution("...")
def step6(id):
    if len(id) > 15:
        id = id[:15]
    if id[-1] == '.':
        id=id[:14]
    return id
def step7(id):
    while len(id) < 3:
        id += id[-1]
    return id