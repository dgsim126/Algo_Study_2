n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
apples = [list(map(int, input().split())) for _ in range(k)]

l = int(input()) # 방향 변환 횟수
info = []
for _ in range(l):
    x, c = input().split()
    info.append([int(x), c]) # 게임 시작 후 x 경과, c 방향으로 회전 (L: 왼쪽, D: 오른쪽)

board = [['.']*n for _ in range(n)]
board[0][0] = 's'

for x,y in apples:
    board[x-1][y-1] = 'a'

direct = ['R', 'D', 'L', 'U']
current_l = [0,0]
current_d = 0
snake = [[0, 0]]

second = 0
while True:
    second += 1

    if info and second - 1 == info[0][0]: # 초 끝나고 방향 전환
        change = info.pop(0)
        if change[1] == 'D':
            current_d = (current_d + 1) % 4
        elif change[1] == 'L':
            current_d = (current_d - 1) % 4
    current_direct = direct[current_d]

    if current_direct == 'R':
        next = [current_l[0], current_l[1]+1]
    elif current_direct == 'L':
        next = [current_l[0], current_l[1]-1]
    elif current_direct == 'U':
        next = [current_l[0]-1, current_l[1]]
    else: # current_direct == 'D':
        next = [current_l[0]+1, current_l[1]]

    if 0 <= next[0] < n and 0 <= next[1] < n:
        if board[next[0]][next[1]] == 's':
            break

        if board[next[0]][next[1]] == 'a': # 사과일때 몸 길이 늘려서 리스트에 저장
            board[next[0]][next[1]] = 's'
            snake.append(next)
        else: # 사과 없을때 꼬리 pop
            tail = snake.pop(0)
            board[tail[0]][tail[1]] = '.'
            board[next[0]][next[1]] = 's'
            snake.append(next)
    else:
        break

    current_l = next

print(second)