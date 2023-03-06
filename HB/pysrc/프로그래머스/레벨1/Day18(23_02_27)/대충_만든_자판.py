def solution(keymap, targets):
    answer = []
    target = []
    for i in targets:
        target += i
    target = set(target)
    print(target)
    return answer
solution([['a','s','v'],['c','d','e']], [['a','c','e','f'], ['g','y','e']])
print('asdf'.index('a'))