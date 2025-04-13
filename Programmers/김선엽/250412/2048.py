# from collections import deque
# import copy

# def solution(N, board):
#     direction = ([-1, 0], [1, 0], [0, -1], [0, 1])
#     time = 5
#     queue = deque([[board, time]])
#     max = 0

#     while queue:
#         cur, t = queue.popleft()

#         if t == 0:
#             for i in range(N):
#                 for j in range(N):
#                     if cur[i][j] > max:
#                         max = cur[i][j]
#             continue
        
#         for dx, dy in direction:
#             diff = copy.deepcopy(cur)
#             if dx == -1:
#                 for i in range(N):
#                     for j in range(N):
#                         if diff[i][j] > 0:
#                             ri, rj = i, j
#                             while True:
#                                 if 0 <= ri + dx < N and 0 <= rj + dy < N:
#                                     if diff[ri + dx][rj + dy] > 0:
#                                         if diff[ri + dx][rj + dy] == diff[i][j]:
#                                             diff[ri + dx][rj + dy] *= 2
#                                             diff[i][j] = 0
#                                         else:
#                                             diff[ri][rj], diff[i][j] = diff[i][j], diff[ri][rj]
#                                             break
#                                     else:
#                                         ri += dx
#                                         rj += dy
#                                 else:
#                                     diff[ri][rj], diff[i][j] = diff[i][j], diff[ri][rj]
#                                     break
#             elif dx == 1:
#                 for i in range(N-1, -1, -1):
#                     for j in range(N):
#                         if diff[i][j] > 0:
#                             ri, rj = i, j
#                             while True:
#                                 if 0 <= ri + dx < N and 0 <= rj + dy < N:
#                                     if diff[ri + dx][rj + dy] > 0:
#                                         if diff[ri + dx][rj + dy] == diff[i][j]:
#                                             diff[ri + dx][rj + dy] *= 2
#                                             diff[i][j] = 0
#                                         else:
#                                             diff[ri][rj], diff[i][j] = diff[i][j], diff[ri][rj]
#                                             break
#                                     else:
#                                         ri += dx
#                                         rj += dy
#                                 else:
#                                     diff[ri][rj], diff[i][j] = diff[i][j], diff[ri][rj]
#                                     break
#             elif dy == -1:
#                 for i in range(N):
#                     for j in range(N):
#                         if diff[j][i] > 0:
#                             ri, rj = i, j
#                             while True:
#                                 if 0 <= rj + dx < N and 0 <= ri + dy < N:
#                                     if diff[rj + dx][ri + dy] > 0:
#                                         if diff[rj + dx][ri + dy] == diff[j][i]:
#                                             diff[rj + dx][ri + dy] *= 2
#                                             diff[j][i] = 0
#                                         else:
#                                             diff[rj][ri], diff[j][i] = diff[j][i], diff[rj][ri]
#                                             break
#                                     else:
#                                         rj += dx
#                                         ri += dy
#                                 else:
#                                     diff[rj][ri], diff[j][i] = diff[j][i], diff[rj][ri]
#                                     break
#             elif dy == 1:
#                 for i in range(N-1, -1, -1):
#                     for j in range(N):
#                         if diff[j][i] > 0:
#                             # print(j, i)
#                             ri, rj = i, j
#                             while True:
#                                 if 0 <= rj + dx < N and 0 <= ri + dy < N:
#                                     if diff[rj + dx][ri + dy] > 0:
#                                         if diff[rj + dx][ri + dy] == diff[j][i]:
#                                             diff[rj + dx][ri + dy] *= 2
#                                             diff[j][i] = 0
#                                         else:
#                                             diff[rj][ri], diff[j][i] = diff[j][i], diff[rj][ri]
#                                             break
#                                     else:
#                                         rj += dx
#                                         ri += dy
#                                 else:
#                                     diff[rj][ri], diff[j][i] = diff[j][i], diff[rj][ri]
#                                     break
#                                 # print(diff)
#             print(t, diff)
#             queue.append([diff, t - 1])

#     return max

# N = int(input())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))
# print(solution(N, board))

import sys, copy
N = int(input())
pan = []
ans = 0

for _ in range(N):
    pan.append([int(x) for x in sys.stdin.readline().rstrip().split()])

def left(board):
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if board[i][j] != 0: # 0이 아닌 값이
                tmp = board[i][j]
                board[i][j] = 0 # 일단 비워질꺼니까 0으로 바꿈

                if board[i][cursor] == 0: # 비어있으면
                    board[i][cursor] = tmp # 옮긴다

                elif board[i][cursor] == tmp: # 같으면
                    board[i][cursor] *= 2 # 합친다
                    cursor += 1
                else: # 비어있지도 않고 다른 값일때
                    cursor += 1 # pass
                    board[i][cursor] = tmp # 바로 옆에 붙임

    return board

def right(board):
    for i in range(N):
        cursor = N - 1
        for j in range(N - 1, -1, -1):

            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp

                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
    return board

def up(board):
    for j in range(N):
        cursor = 0
        for i in range(N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp

                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1

                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board

def down(board):
    for j in range(N):
        cursor = N - 1
        for i in range(N - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp

                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1

                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    return board

def dfs(n, arr):
    global ans
    if n == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return

    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(n + 1, left(copy_arr))
        elif i == 1:
            dfs(n + 1, right(copy_arr))
        elif i == 2:
            dfs(n + 1, up(copy_arr))
        else:
            dfs(n + 1, down(copy_arr))

dfs(0, pan)
print(ans)