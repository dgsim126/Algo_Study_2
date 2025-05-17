def solution(N, M, board):
    for i in range(N):
        for j in range(N + 1 - M):
            if board[i][j:j+M] == board[i][j:j+M][::-1]:
                return "".join(board[i][j:j+M])
            
    for j in range(N):
        for i in range(N - M + 1):
            cur = ''.join(board[x][j] for x in range(i, i+M))
            if cur == cur[::-1]:
                return "".join(cur)

T = int(input())
for test_case in range(1, T+1):
    N, M, = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(input()))
    
    answer = solution(N, M, board)

    print(f"#{test_case} {answer}")