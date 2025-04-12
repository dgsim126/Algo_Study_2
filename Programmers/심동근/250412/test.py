def left(board):
    for i in range(len(board)):
        temp = []
        for j in range(len(board[i])):
            if (board[i][j] != 0):
                temp.append(board[i][j])
        print(temp)



## main ##
N= 3
board= [[2,0,2],[4,4,8],[16,8,8]]
print(left(board))