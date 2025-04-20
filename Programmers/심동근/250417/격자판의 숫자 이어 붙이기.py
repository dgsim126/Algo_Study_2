'''
만들 수 있는 최대 개수는 10**7 10000000
'''
from collections import deque


def bfs(y, x, board):
    dx= [0,1,0,-1] # 북 동 남 서
    dy= [-1,0,1,0]

    lst= deque()
    first_value= str(board[y][x])
    lst.append((y,x,1,first_value))

    result= set()

    while(lst):
        static_current_y, static_current_x, depth, current_word= lst.popleft()
        if(depth>6
        ):
            result.add(current_word)
            continue

        for i in range(4):
            current_y= static_current_y+dy[i]
            current_x= static_current_x+dx[i]
            if(0<=current_x and current_x<4 and 0<=current_y and current_y<4):
                temp= str(board[current_y][current_x])
                lst.append((current_y, current_x, depth+1, current_word+temp))

    return result



def solution(board):
    result= set()
    # [y][x]
    for y in range(4):
        for x in range(4):
            result.update(bfs(y, x, board))

    # print(result)
    # print(len(result))
    return len(result)



## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    board= []
    for i in range(4):
        temp= list(map(int, input().split()))
        board.append(temp)
    print(f"#{test_case} {solution(board)}")
# board= [[1,1,1,1],
#         [1,1,1,2],
#         [1,1,2,1],
#         [1,1,1,1]]
# print(solution(board))