# 팔방에 지뢰 없는 위치 찾기, 구역 갱신 후 구역 수만큼 +
# 구역 갱신 후에 남은 . 수만큼 +
from collections import deque

def bfs(c_x, c_y):
    queue = deque([(c_x,c_y)])
    board[c_y][c_x] = '0'

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == '.':
                    cnt = count_mine(nx, ny)
                    board[ny][nx] = str(cnt)
                    if cnt == 0:
                        queue.append((nx,ny))

def count_mine(x, y):
    count = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[ny][nx] == '*':
                count += 1
    return count

def solution():
    click = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == '.' and count_mine(x, y) == 0:
                bfs(x,y)
                click += 1

    for line in board:
        click += line.count('.')

    return click

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(input()) for _ in range(n)]

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    print(f'#{test_case} {solution()}')