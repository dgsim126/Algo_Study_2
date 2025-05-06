def solution(N, board):
    row, col = len(board), len(board[0])

    def bfs():
        direction = [(1, 0), (0, 1), (1, -1), (1, 1)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "o":
                    x, y = i, j
                    for dx, dy in direction:
                        count = 1
                        while True:
                            if 0 <= x + dx < row and 0 <= y + dy < col and board[x + dx][y + dy] == "o":
                                x += dx
                                y += dy
                                count += 1
                                if count >= 5:
                                    return True
                            else:
                                break

        return False

    return bfs()


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    if solution(N, board):
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
