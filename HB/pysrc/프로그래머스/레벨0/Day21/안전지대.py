def solution(board):
    answer = 0
    R = len(board)
    C = len(board[0])
    board.insert(0,[0]*C)
    board.append([0]*C)
    for i in range(R+2):
        board[i].insert(0, 0)
        board[i].append(0)
    visit = [[0] * (C+2) for _ in range(R+2)]
    for r in range(1, R+1):
        for c in range(1, C+1):
            if board[r][c] == 1:
                for i in range(r-1, r +2):
                    for j in range(c-1, c+2):
                        visit[i][j] = 1
    for i in range(1, R+1):
        for j in range(1, C+1):
            if visit[i][j] == 1:
                answer +=1
    return R*C-answer
