from itertools import permutations


def solution(N, board):
    office = [i for i in range(2, N+1)]
    # print(office)
    e = []
    for comb in permutations(office, N-1):
        amount = 0
        # print(comb)
        for i in range(1, len(comb)):
            # print(comb[i-1], comb[i], board[comb[i-1]-1][comb[i]-1])
            amount += board[comb[i-1]-1][comb[i]-1]
        amount += board[0][comb[0]-1]
        amount += board[comb[-1]-1][0]
        e.append(amount)
    # print(e)
    return min(e)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    answer = solution(N, board)
    print(f"#{test_case} {answer}")