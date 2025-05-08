from collections import deque

def solution(board):
    for i in range(100):
        turn = 0
        col = i
        if board[0][col] == 1:
            x = 0

            while x != 99:
                if 0 <= col-1 < 100 and board[x][col-1] == 1:
                    index = col
                    while True:
                        if 0 <= index-1 < 100 and board[x][index-1] == 1:
                            index -= 1
                        else:
                            col = index
                            turn += 1
                            break
                if 0 <= col+1 < 100 and board[x][col+1] == 1:
                    index = col
                    while True:
                        if 0 <= index+1 < 100 and board[x][index+1] == 1:
                            index += 1
                        else:
                            col = index
                            turn += 1
                            break
                
                x += 1

                if x == 99 and board[99][col] == 2:
                    return i
                else:
                    break

T = int(input())
for test_case in range(1, T+1):
    board = []
    board.append(list(map, int(input().split())))
    answer = solution(board)

    print(f"#{test_case} {answer}")