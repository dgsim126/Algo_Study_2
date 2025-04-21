from collections import deque

def solution(board):
    queue = deque([])
    for i in range(16):
        for j in range(16):
            if board[i][j] == "2":
                queue.append([i, j])
        
    direction = ([-1, 0], [1, 0], [0, -1], [0, 1])
    visited = [[False] * 16 for _ in range(16)]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        if board[x][y] == "3":
            return 1
        
        for dx, dy in direction:
            rx, ry = x + dx, y + dy
            if 0 <= rx < 16 and 0 <= ry < 16 and not visited[rx][ry] and board[rx][ry] != "0":
                queue.append([rx, ry])
                visited[rx][ry] = True
    
    return 0

T = int(input())
for test_case in range(1, T+1):
    board = []
    for _ in range(16):
        board.append(list(input()))

    if solution(board):
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")