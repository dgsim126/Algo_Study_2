def solution(board):
    num = set()
    for i in range(8):
        for j in range(8):
            if board[i][j] == "O":
                if j in num:
                    return False
                else:
                    num.add(j)
    return True

T = int(input())
for test_case in range(1, T+1):
    board = []
    total = 0
    possible = True
    for _ in range(8):
        row = list(input())
        n = row.count("O")
        if n != 1:
            possible = False
        board.append(row)
    
    if solution(board) and possible:
        print(f"#{test_case} yes")
    else:
        print(f"#{test_case} no")