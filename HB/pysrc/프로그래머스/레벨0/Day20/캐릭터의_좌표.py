def solution(keyinput, board):
    answer = []
    r = 0
    c = 0
    for i in range(len(keyinput)):
        if keyinput[i] == 'left':
            if r - 1 >= -(board[0]//2):
                r -= 1
        elif keyinput[i] == 'right':
            if r + 1 <= (board[0]//2):
                r += 1
        elif keyinput[i] == 'up':
            if c + 1 <= (board[1]//2):
                c += 1
        elif keyinput[i] == 'down':
            if c - 1 >= -(board[1]//2):
                c -= 1
    return answer