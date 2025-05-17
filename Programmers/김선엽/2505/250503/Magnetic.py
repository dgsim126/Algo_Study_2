import sys
sys.stdin = open("data/Magnetic_data.txt", "r")

from collections import deque

def solution(board):
    answer = 0
    for i in range(100):
        queue = deque([])
        for j in range(100):
            if board[j][i] == 2:
                if not queue:
                    continue
                elif queue[-1] == 1:
                    queue.append(2)
                    answer += 1

            elif board[j][i] == 1:
                queue.append(1)
    return answer

T = 10
for test_case in range(1, T+1):
    n = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
    answer = solution(board)
    print(f"#{test_case} {answer}")