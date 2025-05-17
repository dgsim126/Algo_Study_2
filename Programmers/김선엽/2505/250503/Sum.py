import sys
sys.stdin = open("data/회문1_data.txt", "r")

def LToR(board):
    result = 0
    for i in range(100):
        result += board[i][i]
    return result

def RToL(board):
    result = 0
    for i in range(100):
        result += board[i][99-i]
    return result

def solution(sum_row, board):
    sum_set = set([sum_row, RToL(board), LToR(board)])
    sum_col = 0
    for i in range(100):
        col_ = []
        for j in range(100):
            col_.append(board[j][i])
        if sum(col_) > sum_col:
            sum_col = sum(col_)

    sum_set.add(sum_col)

    return max(sum_set)

T = 10
for test_case in range(1, T+1):
    n = int(input())
    board = []
    sum_row = 0
    for i in range(100):
        row = list(map(int, input().split()))
        if sum(row) > sum_row:
            sum_row = sum(row)
        board.append(row)
    answer = solution(sum_row, board)
    print(f"#{n} {answer}")