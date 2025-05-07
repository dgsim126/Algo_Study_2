def left(board):
    for i in range(len(board)):
        row = [num for num in board[i] if num != 0]  # 0 제거
        new_row = []
        skip = False
        for j in range(len(row)):
            if skip:
                skip = False
                continue
            if j + 1 < len(row) and row[j] == row[j + 1]:
                new_row.append(row[j] * 2)
                skip = True
            else:
                new_row.append(row[j])
        new_row += [0] * (len(board[i]) - len(new_row))  # 남은 부분 0으로 채우기
        board[i] = new_row
        print(new_row[:1])  # [4], [8], [16] 이거 보려고

    return board




## main ##
N= 3
board= [[2,0,2],[4,4,8],[16,8,8]]
print(left(board))