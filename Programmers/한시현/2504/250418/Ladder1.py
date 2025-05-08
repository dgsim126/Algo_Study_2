#T = int(input())
# input 양식 통일 안해?

def solution(y, x):
    visited[y][x] = True

    if y == 0:
        return x

    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100:
            if ladder[ny][nx] == 1 and not visited[ny][nx]:
                return solution(ny, nx)

for _ in range(10):
    test_case = int(input()) # ㅅㅂ..
    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False]*100 for _ in range(100)]

    dx = [-1, 1, 0]
    dy = [0, 0, -1]
    # 좌, 우, 상

    goal_x = ladder[99].index(2)

    answer = solution(99, goal_x)
    print(f'#{test_case} {answer}')