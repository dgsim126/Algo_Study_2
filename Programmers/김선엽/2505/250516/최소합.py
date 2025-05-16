def solution(N, board):
    find_ = [[0] * N for _ in range(N)]
    find_[N-1][N-1] = board[N-1][N-1]
    find_[N-2][N-1] = board[N-2][N-1] + find_[N-1][N-1]
    find_[N-1][N-2] = board[N-1][N-2] + find_[N-1][N-1]

    for i in range(3, N+1): # 왼 -> 오 대각선 기준 아래 부분
        for j in range(i):
            if j == 0: # N = 5, i = 3 일 때, [4][2], [3][3], [2][4]
                find_[N-1-j][N-i+j] = board[N-1-j][N-i+j] + find_[N-1-j][N-i+j+1]
            elif j == i - 1:
                find_[N-1-j][N-i+j] = board[N-1-j][N-i+j] + find_[N-1-j+1][N-i+j]
            else:
                find_[N-1-j][N-i+j] = board[N-1-j][N-i+j] + min(find_[N-1-j+1][N-i+j], find_[N-1-j][N-i+j+1])

    for i in range(N-1, 0, -1): # 왼 -> 오 대각선 기준 아래 부분 2, 1
        for j in range(i):
            # print(board[i-1-j][0+j])
            find_[i-1-j][0+j] = board[i-1-j][0+j] + min(find_[i-1-j][0+j+1], find_[i-1-j+1][0+j])
            # N = 5, i = 4 일 때, [3][0], [2][1]. [1][2], [0][3]
            # N = 5, i = 3 일 때,
    # print(find_)
    return find_[0][0]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    answer = solution(N, board)
    print(f"#{test_case} {answer}")