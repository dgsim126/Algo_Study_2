# bfs 문제
from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for i in range(N): # 초기 위치
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[rx][ry][bx][by] = True

queue = deque()
queue.append((rx, ry, bx, by, 0))

...