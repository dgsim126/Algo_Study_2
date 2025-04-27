T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]

    answer = ''

    # 가로
    for i in range(n):
        for j in range(n - m + 1):
            slice_row = board[i][j:j+m]
            if slice_row == slice_row[::-1]:
                answer = ''.join(slice_row)
                break
        if answer:
            break

    # 세로
    if not answer:
        for j in range(n):
            for i in range(n - m + 1):
                slice_col = [board[x][j] for x in range(i, i+m)]
                if slice_col == slice_col[::-1]:
                    answer = ''.join(slice_col)
                    break
            if answer:
                break

    print(f'#{test_case} {answer}')