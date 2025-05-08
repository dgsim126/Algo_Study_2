# def solution(H, W, board, num, plays):
#     for i in range(H):
#         board[i] = list(board[i])

#     print(board)
#     for i in range(H):
#         for j in range(W):
#             if board[i][j] == "<":
#                 pos = [i, j, (0, -1)]
#             elif board[i][j] == ">":
#                 pos = [i, j, (0, 1)]
#             elif board[i][j] == "v":
#                 pos = [i, j, (-1, 0)]
#             elif board[i][j] == "^":
#                 pos = [i, j, (1, 0)]
    
#     for i in range(num):
#         print(board, pos)
#         x, y, dir = pos
#         dx, dy = dir
#         if plays[i] == "U":
#             if 0 <= x - 1 < H and board[x - 1][y] == ".":
#                 board[x][y] = "."
#                 board[x-1][y] = "^"
#                 pos = [x-1, y, (-1,0)]
#             else:
#                 board[x][y] = "^"
#                 pos = [x, y, (-1,0)]
#         elif plays[i] == "D":
#             if 0 <= x + 1 < H and board[x + 1][y] == ".":
#                 board[x][y] = "."
#                 board[x+1][y] = "v"
#                 pos = [x+1, y, (1,0)]
#             else:
#                 board[x][y] = "v"
#                 pos = [x, y, (1,0)]
#         elif plays[i] == "L":
#             if 0 <= y - 1 < W and board[x][y-1] == ".":
#                 board[x][y] = "."
#                 board[x][y-1] = "<"
#                 pos = [x, y-1, (0,-1)]
#             else:
#                 board[x][y] = "<"
#                 pos = [x, y, (0,-1)]
#         elif plays[i] == "R":
#             if 0 <= y + 1 < W and board[x][y+1] == ".":
#                 board[x][y] = "."
#                 board[x][y+1] = ">"
#                 pos = [x, y+1, (0,1)]
#             else:
#                 board[x][y] = ">"
#                 pos = [x, y, (0,1)]
#         elif plays[i] == "S":
#             while True:
#                 x += dx
#                 y += dy
#                 if 0 <= x < H and 0 <= y < W:
#                     if board[x][y] == "*":
#                         board[x][y] = "."
#                     elif board[x][y] == "#":
#                         break
#                 else:
#                     break

# board = [
#     "***....",
#     "*-..#**",
#     "#<.****"
# ]
# solution(3, 7, board, 23, "SURSSSSUSLSRSSSURRDSRDS")


## 제출

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    num = int(input())
    plays = input()
    for i in range(H):
        board[i] = list(board[i])

    print(board)
    for i in range(H):
        for j in range(W):
            if board[i][j] == "<":
                pos = [i, j, (0, -1)]
            elif board[i][j] == ">":
                pos = [i, j, (0, 1)]
            elif board[i][j] == "v":
                pos = [i, j, (-1, 0)]
            elif board[i][j] == "^":
                pos = [i, j, (1, 0)]
    
    for i in range(num):
        x, y, dir = pos
        dx, dy = dir
        if plays[i] == "U":
            if 0 <= x - 1 < H and board[x - 1][y] == ".":
                board[x][y] = "."
                board[x-1][y] = "^"
                pos = [x-1, y, (-1,0)]
            else:
                board[x][y] = "^"
                pos = [x, y, (-1,0)]
        elif plays[i] == "D":
            if 0 <= x + 1 < H and board[x + 1][y] == ".":
                board[x][y] = "."
                board[x+1][y] = "v"
                pos = [x+1, y, (1,0)]
            else:
                board[x][y] = "v"
                pos = [x, y, (1,0)]
        elif plays[i] == "L":
            if 0 <= y - 1 < W and board[x][y-1] == ".":
                board[x][y] = "."
                board[x][y-1] = "<"
                pos = [x, y-1, (0,-1)]
            else:
                board[x][y] = "<"
                pos = [x, y, (0,-1)]
        elif plays[i] == "R":
            if 0 <= y + 1 < W and board[x][y+1] == ".":
                board[x][y] = "."
                board[x][y+1] = ">"
                pos = [x, y+1, (0,1)]
            else:
                board[x][y] = ">"
                pos = [x, y, (0,1)]
        elif plays[i] == "S":
            while True:
                x += dx
                y += dy
                if 0 <= x < H and 0 <= y < W:
                    if board[x][y] == "*":
                        board[x][y] = "."
                    elif board[x][y] == "#":
                        break
                else:
                    break

    
    print(f"#{test_case} "+ "".join(board[0]))
    for i in range(1, len(board)):
        print("".join(board[i]))
    
# board = [
#     "***....",
#     "*-..#**",
#     "#<.****"
# ]
# solution(3, 7, board, 23, "SURSSSSUSLSRSSSURRDSRDS")