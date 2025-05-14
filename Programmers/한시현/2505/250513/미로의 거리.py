from collections import deque

def bfs(start_x, start_y, c):
    queue = deque([(start_x, start_y, c)])

    while queue:
        x, y, count = queue.popleft()
        visited[y][x] = True

        for o in range(4):
            nx = x + dx[o]
            ny = y + dy[o]

            if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
                if maze[ny][nx] == 3:
                    return count

                elif maze[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((nx, ny, count+1))

    return 0

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    answer = -1
    for j in range(n):
        for i in range(n):
            if maze[j][i] == 2:
                answer = bfs(i, j, 0)
                break
        if answer != -1:
            break

    print(f'#{test_case} {answer}')