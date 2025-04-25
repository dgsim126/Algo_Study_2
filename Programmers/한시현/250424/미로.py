from collections import deque

def bfs(i, j):
    queue = deque([(i,j)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if maze[ny][nx] != 1 and not visited[ny][nx]:
                    if maze[ny][nx] == 3:
                        return 1
                    visited[ny][nx] = True
                    queue.append((nx, ny))
    return 0

def solution():
    for j in range(n):
        for i in range(n):
            if maze[j][i] == 2:
                return bfs(i, j)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(f'#{test_case} {solution()}')