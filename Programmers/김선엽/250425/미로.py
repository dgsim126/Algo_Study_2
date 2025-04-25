from collections import deque

def soltuon(N, board):

    for i in range(N):
        for j in range(N):
            if board[i][j] == "2":
                queue = deque([[i, j]])

    direction = ([-1, 0], [1, 0], [0, -1], [0, 1])
    visited = [[False] * N for _ in range(N)]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        if board[x][y] == "3":
            return 1

        for dx, dy in direction:
            rx, ry = x + dx, y + dy
            if 0 <= rx < N and 0 <= ry < N and not visited[rx][ry] and board[rx][ry] != "1":
                queue.append([rx, ry])
                visited[rx][ry] = True

    return 0


T = int(input())
for test_case in range(1, T+1):
    board = []
    N = int(input())
    for _ in range(N):
        board.append(list(input()))

    answer = soltuon(N, board)

    print(f"#{test_case} {answer}")