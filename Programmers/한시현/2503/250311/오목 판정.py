T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for i in range(N):
        line = input()
        board.append(line)

    five = 'NO'
    count = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] == 'o':
                # case ㅡ
                if col+4 < N and board[row][col:col+5] == 'ooooo':
                    five = 'YES'
                    print('case ㅡ')
                    break
                # case |
                if row+4 < N:
                    if board[row][col] == 'o' and board[row+1][col] == 'o' and board[row+2][col] == 'o' and board[row+3][col] == 'o' and board[row+4][col] == 'o':
                        five = 'YES'
                        print('case |')
                        break
                # case \
                if col+4 < N and row+4 < N:
                    if board[row][col] == 'o' and board[row+1][col+1] == 'o' and board[row+2][col+2] == 'o' and board[row+3][col+3] == 'o' and board[row+4][col+4] == 'o':
                        five = 'YES'
                        print('case \\')
                        break
                # case /
                if col-4 >= 0 and row+4 < N:
                    if board[row][col] == 'o' and board[row+1][col-1] == 'o' and board[row+2][col-2] == 'o' and board[row+3][col-3] == 'o' and board[row+4][col-4] == 'o':
                        five = 'YES'
                        print('case /')
                        break

    print(f'#{test_case} {five}')