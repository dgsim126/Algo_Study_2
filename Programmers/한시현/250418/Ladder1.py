T = int(input())

def solution(y, x, end_y):




for test_case in range(1, T + 1):
    ladder = [list(map(int, input().split())) for _ in range(100)]

    dx = [-1, 1, 0]
    dy = [0, 0, -1]
    # 좌, 우, 상

    goal_x = ladder[99].index(2)

    solution(99, goal_x)