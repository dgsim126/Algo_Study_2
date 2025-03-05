T = int(input())

# N-Queen : 백 트래킹 (DFS)
def dfs(board, row, col, n):
    global possible_case

    for i in range(row):
        if board[i][col] == 1:
            return False


for test_case in range(1, T + 1):
    N = int(input())
    possible_case = 0

    chessboard = [[0] * N for i in range(N)]

    dfs(chessboard, 0, 0, N)

    print(f'#{test_case} {possible_case}')