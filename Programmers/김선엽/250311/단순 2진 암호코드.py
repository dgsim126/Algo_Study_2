# 암호코드는 8개 숫자
# 조같네

from collections import deque

def solution(N, M, board):
    for i in range(N):
        for j in range(M):
            print(i, j)
            if board[i][j] == "1":
                queue = board[i][j:j+56]
                break
    while True:
        if queue[-1] == "0":
            queue = "0" + queue[0:55]
        else:
            break

    dic_ = {
        "3211": 0,
        "2221": 1,
        "2122": 2,
        "1411": 3,
        "1132": 4,
        "1231": 5,
        "1114": 6,
        "1312": 7,
        "1213": 8,
        "3112": 9
    }

    count = 1
    num = ""
    for i in range(55):
        if queue[i] != queue[i+1]:
            
        



N = 11
M = 70
board = [input() for _ in range(N)]

solution(N, M, board)