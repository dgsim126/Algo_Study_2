# 그냥 bfs로는 안됨
# 다익스트라 알고리즘이 정석 풀이
from collections import deque

T = int(input())

def bfs(start_x, start_y, end_x, end_y, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start_x, start_y)])
    # visited = [[False] * len(board) for _ in range(len(board))] # 이거 쓰면 나중에 더 적은 비용 경로 있어도 갱신이 안됨
    min_arrive_time = [[float('inf')] * len(board) for _ in range(len(board))] # 최대 깊이 무한대(float('inf'))
    min_arrive_time[start_x][start_y] = 0 # 시작 위치 초기화 (0)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <len(board) and 0 <= ny < len(board):
                # if not visited[nx][ny]:
                #     visited[nx][ny] = True
                    cost = min_arrive_time[x][y] + board[nx][ny]
                    if cost < min_arrive_time[nx][ny]:
                        min_arrive_time[nx][ny] = cost
                        queue.append((nx, ny))

    return min_arrive_time[end_x][end_y]

for test_case in range(1, T + 1):
    n = int(input())
    board = []
    for _ in range(n):
        nums = list(input())
        board.append(list(map(int, nums)))

    print(f'#{test_case} {bfs(0, 0, n-1, n-1, board)}')