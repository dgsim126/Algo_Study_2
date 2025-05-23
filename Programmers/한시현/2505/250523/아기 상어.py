from collections import deque

def bfs(xx, yy, s, m, e, sp):
    queue = deque([(xx, yy, s, m, e, sp)])

    while queue:
        x, y, size, move, eat, ocean = queue.popleft()
        #print('loop check')

        esc = True
        for j in range(n):
            for i in range(n):
                if ocean[j][i] != 0 and ocean[j][i] != 9:
                    esc = False
                    break
            if not esc:
                break
        if esc:
            return move

        for o in range(4):
            nx = x + dx[o]
            ny = y + dy[o]
            if 0 <= nx < n and 0 <= ny < n:
                if ocean[ny][nx] != 0 and ocean[ny][nx] < size: # 크기가 작은 물고기일 경우
                    #print(f'eat {nx} {ny} {ocean[ny][nx]}')
                    eat += 1
                    if ocean[y][x] < size:
                        ocean[y][x] = 0
                    ocean[ny][nx] = 9
                    if eat == size:
                        queue.append((nx, ny, size+1, move+1, 0, ocean))
                    else:
                        queue.append((nx, ny, size, move+1, eat, ocean))
                    #print(f'{move + 1}')

                elif ocean[ny][nx] == 0: # 0 일 경우
                    if ocean[y][x] < size:
                        ocean[y][x] = 0
                    ocean[ny][nx] = 9
                    queue.append((nx, ny, size, move+1, eat, ocean))
                    #print(f'{move + 1}')

                # elif ocean[ny][nx] != 0 and ocean[ny][nx] >= size: # 크기가 큰 물고기일 경우
                #     if ocean[y][x] < size:
                #         ocean[y][x] = 0
                #     queue.append((nx, ny, size, move+1, ocean))
                #     #print(f'{move + 1}')

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0
for col in range(n):
    for row in range(n):
        if space[col][row] == 9:
            answer = bfs(row, col, 2, 0, 0, space)
            break
    if answer != 0:
        break

print(answer)