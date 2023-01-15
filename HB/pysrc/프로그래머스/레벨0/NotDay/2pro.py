n = int(input())
for i in range(n):
    answer = 0
    str_ans = ''
    lst = list(map(int,input().split()))
    lst_ = sorted(lst)
    if lst[0] == min(lst) or (lst[0] == lst_[1] and lst_[0] == 0):
        answer = -1
def sol(str_ans):
    for i in range(len(str(lst[0]))):# 654 5 4 -> 555
        if lst_[2] == lst[0] and int(str(lst[0])[i]) > lst_[1]:
            str_ans += str(lst_[1]) * (len(str(lst[0])-i))
            break
        elif int(str(lst[0])[i]) == lst_[1]:# 673 6 5 -> 666
            if int(str(lst[0])[i+1]) >= lst_[1]:
                str_ans+=str(lst_[1])
            elif lst_[0] <= int(str(lst[0])[i+1]) < lst_[1]:# 656 6 4 -> 646
                str_ans+=str(lst_[1])
            str_ans += str(lst_[0])# 615 6 3 -> 366
        elif lst_[2] > int(str(lst[0])[i]) > lst_[0]:# 555 6 4 -> 466
            str_ans += str(lst_[0])
        elif int(str(lst[0])[i])== lst_[0]:#455 6 4 -> 
            if int(str(lst[0])[i+1]) >= lst_[1]:
                str_ans+=str(lst_[0])
            elif lst_[0] <= int(str(lst[0])[i+1]) < lst_[1]:# 656 6 4 -> 646
                str_ans+=str(lst_[1#])
            str_ans += str(lst_[0])
        elif lst_[0] == lst[0]:



    print(f'#{i+1} {answer}')

# 첫 숫자를 a 와 b 중 큰 값으로// 하면 몫이 1보다 크거나 같고
# % 는 0보다 클 때 a 를 출력하고
# 몫이 1이고 % 는 0일때 다음 숫자를 보고 그 값이 // 한것보다 크면 
# a출력한다.
# 몫이 1이고 % 는 0일때 다음 숫자의 // 한것이  
# % 값이 0이면 다음 값을 확인해서 % 값이 크면 a 출력하고
# % 값이 