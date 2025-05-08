from collections import deque

def toFindStartPoint(board):
    for y in range(16):
        for x in range(16):
            if(board[y][x]==2):
                return y, x

def solution(board):
    dx= [0, 1, 0, -1] # 북 동 남 서
    dy= [-1, 0, 1, 0]

    x, y= toFindStartPoint(board)

    queue= deque()
    queue.append((x, y))

    while(queue):
        current_x, current_y= queue.popleft()
        for i in range(4):
            temp_x= current_x+dx[i]
            temp_y= current_y+dy[i]
            if(0<=temp_x and temp_x<16 and 0<=temp_y and temp_y<16):
                if(board[temp_y][temp_x]==3):
                    return 1
                if(board[temp_y][temp_x]==0):
                    board[temp_y][temp_x]=1
                    queue.append((temp_x, temp_y))

    return 0



## main ##
# board= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#         [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
#         [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#         [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
#         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
#         [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
#         [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
#         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
#         [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#         [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
#         [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# print(solution(board))
T = 10
for test_case in range(1, T + 1):
    input()
    board= []
    for i in range(16):
        temp= list(map(int, input().strip()))
        board.append(temp)
    # print(board)
    print(f"#{test_case} {solution(board)}")