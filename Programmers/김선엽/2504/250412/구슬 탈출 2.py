### bfs 풀이, r, b 공 서로 간섭 구현이 빡셈

from collections import deque
import sys
input = sys.stdin.readline

def solution(N, M, board):
    r_x, r_y = 0, 0
    b_x, b_y = 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                r_x, r_y = i, j
            if board[i][j] == "B":
                b_x, b_y = i, j
    t = 0
    direction = ([1, 0], [-1, 0], [0, 1], [0, -1])
    queue = deque([[r_x, r_y, b_x, b_y, t]])

    visited = set()

    while queue:
        
        redx, redy, bluex, bluey, time = queue.popleft()
        visited.add((redx, redy, bluex, bluey))
        if time >= 10:
            continue
            
        for dx, dy in direction:
            blue_in_hole = False
            red_in_hole = False
            r_stop = True
            b_stop = True
            r_redx, r_redy = redx, redy
            r_bluex, r_bluey = bluex, bluey
            while (r_stop or b_stop) and not (red_in_hole and blue_in_hole):
                if 1 <= r_redx + dx < N-1 and 1 <= r_redy + dy < M-1 and board[r_redx + dx][r_redy + dy] != "#" and r_stop:
                    if (r_redx + dx == r_bluex and r_redy + dy == r_bluey) and board[r_redx + (2 * dx)][r_redy + (2 * dy)] == "#":
                        r_stop = False
                    else:
                        # print(r_redx, r_redy)
                        r_redx += dx
                        r_redy += dy
                        # print(r_redx, r_redy)
                        if board[r_redx][r_redy] == "O":
                            r_redx = -1
                            r_redy= -1
                            # print(r_redx, r_redy)
                            red_in_hole = True
                            r_stop = False
                else:
                    r_stop = False
                if 1 <= r_bluex + dx < N-1 and 1 <= r_bluey + dy < M-1 and board[r_bluex + dx][r_bluey + dy] != "#" and b_stop:
                    if (r_bluex + dx == r_redx and r_bluey + dy == r_redy) and board[r_bluex + (2 * dx)][r_bluey + (2 * dy)] == "#":
                        b_stop = False
                        # print(10)
                    else:
                        # print("blue", r_bluex, r_bluey)
                        r_bluex += dx
                        r_bluey += dy
                        # print("blue", r_bluex, r_bluey)
                        if board[r_bluex][r_bluey] == "O":
                            # print("here")
                            r_bluex = -1
                            r_bluey= -1
                            # print("blue", r_bluex, r_bluey)
                            blue_in_hole = True
                            b_stop = False
                else:
                    # print("there")
                    b_stop = False
                    
                # print(f"redx:{redx}, redy:{redy}, bluex:{bluex}, bluey:{bluey}, time:{time}, dx:{dx}, dy:{dy}")    
            # print(f"redx:{r_redx}, redy:{r_redy}, bluex:{r_bluex}, bluey:{r_bluey}, time:{time}, dx:{dx}, dy:{dy}")
            # print(f"redinhole:{red_in_hole}, blueinhole:{blue_in_hole}, r_stop:{r_stop}, b_stop:{b_stop}")
            if red_in_hole and not blue_in_hole:
                return time + 1
            elif not red_in_hole and not blue_in_hole and (r_redx, r_redy, r_bluex, r_bluey) not in visited:
                queue.append([r_redx, r_redy, r_bluex, r_bluey, time + 1])
    
    return -1

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
answer = solution(N, M, board)

print(answer)