from itertools import combinations

def solution(n, board):
    answer = 0
    for i in range(n, 0, -1):
        stop = False
        for comb in combinations(board, i):
            word = set("".join(comb))
            if len(word) == 26:
                stop = True
                answer += 1
        if not stop:
            break

    return answer

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(input())
    answer = solution(n, board)

    print(f"#{test_case} {answer}")