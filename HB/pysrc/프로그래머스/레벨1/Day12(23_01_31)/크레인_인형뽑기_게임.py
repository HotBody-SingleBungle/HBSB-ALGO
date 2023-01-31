def solution(board, moves):
    answer = 0
    lst=[]
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] !=0:
                if len(lst) and lst[-1] == board[j][moves[i]-1]:
                    lst.pop()
                    board[j][moves[i]-1] =0
                    answer +=2
                else:
                    lst.append(board[j][moves[i]-1])
                    board[j][moves[i]-1] =0
                
                break
    print(lst)
                
    return answer