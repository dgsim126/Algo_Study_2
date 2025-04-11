def solution(n, board):
    result = ""
    for i in range(n):
        for j in range(5):
            if i <= len(board[j]) - 1:
                result += board[j][i]

    return result

T = int(input())
for test_case in range(1, T+1):
    board = []
    n = 0
    for _ in range(5):
        row = input()
        if n < len(row):
            n = len(row)
        board.append(row)

    answer = solution(n, board)
    print(f"#{test_case} {answer}")