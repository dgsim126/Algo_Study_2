def solution(N, c_print):
    board = [[0] * 10 for _ in range(10)]
    result = 0
    for c in c_print:
        sx, sy, ex, ey, color = c
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                if not board[i][j]:
                    board[i][j] = color
                else:
                    if board[i][j] != color:
                        result += 1
    return result


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    c_print = []
    for _ in range(N):
        c_print.append(list(map(int, input().split())))
    
    answer = solution(N, c_print)

    print(f"#{test_case} {answer}")