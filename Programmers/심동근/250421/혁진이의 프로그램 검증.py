from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def check_bomb(N, board, y, x):
    cnt = 0
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if board[ny][nx] == '*':
                cnt += 1
    return cnt

def bfs(N, board, y, x):
    queue = deque()
    queue.append((y, x))
    board[y][x] = '0'  # 방문 처리: 숫자로 바꿔줌

    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(8):
            ny, nx = cur_y + dy[i], cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == '.':
                bomb_cnt = check_bomb(N, board, ny, nx)
                board[ny][nx] = str(bomb_cnt)
                if bomb_cnt == 0:
                    queue.append((ny, nx))

def solution(N, board):
    click_count = 0

    # 1. 먼저 주변 지뢰 0인 칸부터 탐색
    for y in range(N):
        for x in range(N):
            if board[y][x] == '.':
                if check_bomb(N, board, y, x) == 0:
                    bfs(N, board, y, x)
                    click_count += 1

    # 2. 아직도 '.'인 애들은 하나씩 따로 클릭해야 함
    for y in range(N):
        for x in range(N):
            if board[y][x] == '.':
                click_count += 1
                board[y][x] = str(check_bomb(N, board, y, x))  # 굳이 안 해도 됨

    return click_count


## main ##
N= 5
board= [['.', '.', '*', '.', '.'],
        ['.', '.', '*', '.', '.'],
        ['.', '*', '.', '.', '*'],
        ['.', '*', '.', '.', '.'],
        ['.', '*', '.', '.', '.']]
print(solution(N, board))