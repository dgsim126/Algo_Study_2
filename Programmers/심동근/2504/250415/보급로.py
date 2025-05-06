'''
지도의 크기가 최대 100*100 이기에 모든 경우를 확인하는 방법은 아닐 듯 하다.
(모든 위치에서 2방향으로 진행한다면, 거리를 고려하지 않기에 3방향으로 진행하는 걸 고려한다면 불가능)
DP
내가 특정 위치에 도착할 때마다 거기까지 갈 수 있는 최소값을 계속 업데이트해야함
즉, 주변 4방향으로부터 값이 들어왔을 때 가중치를 저장한다는 의미
- 다시 왔던 방향으로 돌아갈 수 있기에 DP 불가능


'''
from collections import deque

def print_grid(grid):
    for row in grid:
        print(" ".join(f"{cell:3}" if cell != float('inf') else "inf" for cell in row))
    print()

def solution(N, grid):
    # 최소 복구 시간 저장 배열
    result = [[float('inf')] * N for _ in range(N)]
    result[0][0] = 0

    # 방향: 동, 남, 서, 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    q.append((0, 0))
    step= 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                cost = result[x][y] + grid[nx][ny]
                if cost < result[nx][ny]:
                    result[nx][ny] = cost
                    q.append((nx, ny))
        step += 1
        print(f"[Step {step}] 현재 위치: ({x}, {y}) 이후 결과 배열:")
        print_grid(result)

    print("[최종 결과 배열]")
    print_grid(result)
    return result[N - 1][N - 1]

    return result[N - 1][N - 1]


### main ###

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, list(input().strip()))) for _ in range(N)]
    print(f"#{test_case} {solution(N, grid)}")
