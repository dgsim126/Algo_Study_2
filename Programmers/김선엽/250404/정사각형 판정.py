def solution(N, board):
    count = 0
    start = False
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == "#" and start:
                count += 1
            elif board[i][j] == "#" and not start:
                count += 1
                start = True
                x, y = i, j

    dist = count**(1/2)

    if dist != int(dist):
        return False
    
    dist = int(dist)
    string = "#" * dist
    
    for i in range(dist):
        if board[x+i][y:y+dist] != string:
            return False
    
    return True

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for i in range(N):
        board.append(input())
    
    if solution(N, board):
        print(f"#{test_case} yes")
    else:
        print(f"#{test_case} no")