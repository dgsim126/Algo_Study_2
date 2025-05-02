# 테이블 위 N극, 아래 S극
# 1: N극, 2: S극
for test_case in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    for y in range(n):
        N = False
        for x in range(n):
            if board[x][y] == 1:
                N = True
            elif board[x][y] == 2 and N:
                count += 1
                N = False

    print(f'#{test_case} {count}')