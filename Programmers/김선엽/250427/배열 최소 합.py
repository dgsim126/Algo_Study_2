from itertools import permutations

def solution(n, board):
    index = [i for i in range(n)]

    min = 10000000000
    for comb in permutations(index, n):
        index = 0
        result = 0
        for c in comb:
            result += board[index][c]
            index += 1

        if min > result:
            min = result
    
    return min
    
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    answer = solution(n, board)

    print(f"#{test_case} {answer}")