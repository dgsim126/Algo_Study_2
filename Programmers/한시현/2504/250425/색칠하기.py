def solution():
    count = 0
    for start_x, start_y, end_x, end_y, color in info:
        for y in range(start_y, end_y+1):
            for x in range(start_x, end_x+1):
                if board[y][x] != color:
                    board[y][x] += color
                    if board[y][x] >= 3:
                        count += 1
    return count

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    board = [[0]*10 for _ in range(10)]

    print(f'#{test_case} {solution()}')