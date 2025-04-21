from collections import deque

def solution(N, board):
    queue = deque([])
    for i in range(N):
        for j in range(N):
            if board[i][j] == ".":
                queue.append([i, j, 0])
    
    direction = ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1])

    while queue:
        x, y, t = queue.popleft()

        