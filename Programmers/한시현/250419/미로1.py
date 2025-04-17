def dfs(y, x):
    global possible
    visited[y][x] = True

    if maze[y][x] == 3:
        possible = 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 16 and 0 <= ny < 16:
            if maze[ny][nx] != 1 and not visited[ny][nx]:
                dfs(ny, nx)


for _ in range(10):
    test_case = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 좌, 우, 상, 하

    possible = 0
    dfs(1, 1)

    print(f'#{test_case} {possible}')