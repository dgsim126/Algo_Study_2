T = int(input())
def check(start):
    if start == '#':
        next = '.'
    else:
        next = '#'

    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0 and board[i][j] != '?':
                if board[i][j] != start:
                    return False
            elif (i+j) % 2 == 1 and board[i][j] != '?':
                if board[i][j] != next:
                    return False
    return True

for test_case in range(1, T + 1): # # : 검은색 . : 하얀색
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(input()))

    if check('#') or check('.'):
        print(f'#{test_case} possible')
    else:
        print(f'#{test_case} impossible')