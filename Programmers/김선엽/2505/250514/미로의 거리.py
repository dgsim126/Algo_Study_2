from collections import deque

def solution(N, board):
    queue = deque([])
    for i in range(N):
        for j in range(N):
            if board[i][j] == "2":
                queue.append([i, j, 0])
                break
    direction = ([-1, 0], [1, 0], [0, -1], [0, 1])
    visited = [[False] * N for _ in range(N)]

    while queue:
        x, y, t = queue.popleft()
        if board[x][y] == "3":
            return t - 1
        else:
            for dx, dy in direction:
                rx, ry = x + dx, y + dy
                if 0 <= rx < N and 0 <= ry < N and board[rx][ry] != "1" and not visited[rx][ry]:
                    visited[rx][ry] = True
                    queue.append([rx, ry, t+1])
    return 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(input()))
    answer = solution(N, board)
    print(f"#{test_case} {answer}")