from collections import deque

def dice_roll(i, dice):
    if i == 1: # 우
        return [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif i == 2: # 좌
        return [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif i == 3: # 상
        return [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    elif i == 4: # 하
        return [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
order = deque(map(int, input().split())) # 1: 우, 2: 좌, 3: 상, 4: 하

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0]*7 # 인덱스 1~6 사용 위해

while order:
    current_order = order.popleft()

    nx = x + dx[current_order-1]
    ny = y + dy[current_order-1]

    if 0 <= nx < n and 0 <= ny < m:
        dice = dice_roll(current_order, dice) # 위치 주의

        if board[nx][ny] == 0:
            board[nx][ny] = dice[6]
        else: # board[nx][ny] != 0
            dice[6] = board[nx][ny]
            board[nx][ny] = 0

        x, y = nx, ny

        print(dice[1])