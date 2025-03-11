# ### 2초? 완전 탐색은 아닐듯, N이 몇이던 무조건 5개 이상
# ### bfs다
# from collections import deque

# def solution(N, board):
#     row, col = len(board), len(board[0])

#     def bfs():
#         direction = [(1, 0), (0, 1), (1, -1), (1, 1)]
#         for i in range(len(board)):
#             for j in range(len(board)):
#                 if board[i][j] == "o":
#                     queue = deque([[i, j, 1]])
#                     visited = [[False] * row for _ in range(col)]
#                     print(queue)

#                     while queue:
#                         x, y, count = queue.popleft()
#                         visited[x][y] = True
                        
#                         for dx, dy in direction:
#                             count = 1
#                             while True:
#                                 if 0 <= x + dx < row and 0 <= y + dy < col and board[x + dx][y + dy] == "o":
#                                     x += dx
#                                     y += dy
#                                     count += 1
#                                     if count >= 5:
#                                         return True
#                                 else:
#                                     break
        
#         return False
    
#     return bfs()


# # N = int(input())

# # # board = ["....o", "...o.", "..o..", ".o...", "o...."]
# # N = 5
# # board = ["...o.", "ooooo", "...o.", "...o.", "....."]
# # # board = [".o.o.", "o.o.o", ".o.o.", "o.o.o", ".o.o."]

# # print(solution(N, board))
# N = 5
# board = [input() for _ in range(N)]
# print(board)

def solution(N, board):
    row, col = len(board), len(board[0])

    def bfs():
        direction = [(1, 0), (0, 1), (1, -1), (1, 1)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "o":
                    for dx, dy in direction:
                        x, y = i, j
                        count = 1
                        while True:
                            if 0 <= x + dx < row and 0 <= y + dy < col and board[x + dx][y + dy] == "o":
                                x += dx
                                y += dy
                                count += 1
                                if count >= 5:
                                    return True
                            else:
                                break
        
        return False
    
    return bfs()

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    if solution(N, board):
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")