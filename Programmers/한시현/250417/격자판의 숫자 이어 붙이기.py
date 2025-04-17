# dfs
T = int(input())

def dfs(x, y, depth):
    if depth == 7:
        answer.append(''.join(map(str, save)))
        return

    save.append(board[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<4 and 0<=ny<4:
            dfs(nx, ny, depth + 1)

    save.pop()

    return

for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    answer = []
    for i in range(4):
        for j in range(4):
            save = []
            dfs(i, j, 0)

    print(f'#{test_case} {len(set(answer))}')