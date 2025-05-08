from collections import deque

def solution(N, M, board):
    if M == 1 and N == 1:
        return 1
    
    visited = [[False] * M for _ in range(N)]
    queue = deque([])
    for i in range(N):
        for j in range(M):
            if board[i][j] == "#" or board[i][j] == ".":    ## 요 조건을 빼고 넣어버림
                queue.append([i, j])
                break
    if not queue:
        return 1
    direction = ([1, 0], [-1, 0], [0, 1], [0, -1])
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for dx, dy in direction:
            rx, ry = x + dx, y + dy
            if 0 <= rx < N and 0 <= ry < M and board[rx][ry] and not visited[rx][ry]:
                if board[rx][ry] == "?":
                    if board[x][y] == "#":
                        board[rx][ry] = "."
                    else:
                        board[rx][ry] = "#"
                visited[rx][ry] = True
                queue.append([rx, ry])

    if M > 1:   # 오른쪽 비교
        for i in range(N):
            for j in range(M-1):
                if board[i][j] == board[i][j+1]:
                    return 0
    
    if N > 1:
        for i in range(N-1):
            for j in range(M):
                if board[i][j] == board[i+1][j]:
                    return 0

    return 1

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(input())[0:M])
    
    if solution(N, M, board):
        print(f"#{test_case} possible")
    else:
        print(f"#{test_case} impossible")