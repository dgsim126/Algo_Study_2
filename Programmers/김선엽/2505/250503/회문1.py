def solution(n, board):
    answer = 0
    for i in range(8):
        for j in range(8 - n + 1):
            string = board[i][j:j+n]
            if string == string[::-1]:
                answer += 1

    for i in range(8):
        for j in range(8 - n + 1):
            string = [board[k][i] for k in range(j, j+n)]
            if string == string[::-1]:
                answer += 1

    return answer

T = 10
for test_case in range(1, T + 1):
    n = int(input())
    board = []
    for _ in range(8):
        board.append(list(input()))
    answer = solution(n, board)
    print(f"#{test_case} {answer}")