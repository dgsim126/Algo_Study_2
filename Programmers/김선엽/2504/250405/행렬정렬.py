def solution(n, board):
    is_trans = []
    for i in range(n-1, 0, -1):
        if board[i][0] == i + 1:
            is_trans.append(-1)
        else:
            is_trans.append(1)

    trans = 0
    for i in range(len(is_trans)):
        is_trans[i] = is_trans[i] * ((-1) ** trans)
        if is_trans[i] == (-1):
            trans += 1
    
    return trans

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    print(solution(n, board))