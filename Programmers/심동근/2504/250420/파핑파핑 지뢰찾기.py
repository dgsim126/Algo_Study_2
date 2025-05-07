'''
선택한 지점이 0이 나온다면 그 주변 전체를 탐색해야 함
그 주변 전체 중 0이 또 나온다면 그 주변 전체를 다시 한 번 탐색
이렇게 헀을 때, 총 몇 번 선택해야 맵 전체를 탐색할 수 있는지 알아내야 한다.

일단 for 문을 돌면서 주변 선택한 지점의 결과가 0이 나오는 경우가 있으면 탐색한다.
탐색이 전부 끝난 후, 계속 이동하면서 다시 0인 지점이 있는지 탐색한다.

해당 탐색이 끝난 후, 아직 . 인 지점들의 개수를 구하면 된다.
'''
from collections import deque


def check_bomb(N, board, y, x):
    dx= [0, 1, 1, 1, 0, -1, -1, -1] # 북 동 남 서
    dy= [-1, -1, 0, 1, 1, 1, 0, -1]
    cnt= 0

    for i in range(8):
        new_y= dy[i]+y
        new_x= dx[i]+x
        if(0<=new_y and new_y<N and 0<=new_x and new_x<N):
            if(board[new_y][new_x]=="*"):
                cnt+=1
    return cnt

def bfs(N, board, y, x):
    dx= [0, 1, 1, 1, 0, -1, -1, -1] # 북 동 남 서
    dy= [-1, -1, 0, 1, 1, 1, 0, -1]
    queue= deque()
    queue.append((y, x))
    board[y][x]= "0"

    while(queue):
        current_y, current_x = queue.popleft()
        for i in range(8):
            new_y = dy[i] + current_y
            new_x = dx[i] + current_x
            if (0 <= new_y and new_y < N and 0 <= new_x and new_x < N and board[new_y][new_x]=="."):
                bomb_cnt = check_bomb(N, board, new_y, new_x)
                board[new_y][new_x]= str(bomb_cnt)
                if (bomb_cnt == 0):
                    queue.append((new_y, new_x))

def solution(N, board):
    result= 0

    for y in range(N):
        for x in range(N):
            if(board[y][x]=="." and check_bomb(N, board, y, x)==0):
                bfs(N, board, y, x)
                result+=1

    for y in range(N):
        for x in range(N):
            if board[y][x] == '.':
                result += 1

    return result



## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    board= []
    for i in range(N):
        temp= list(input().strip())
        board.append(temp)
    print(f"#{test_case} {solution(N, board)}")



# N= 5
# board= [['.', '.', '*', '.', '.'],
#         ['.', '.', '*', '.', '.'],
#         ['.', '*', '.', '.', '*'],
#         ['.', '*', '.', '.', '.'],
#         ['.', '*', '.', '.', '.']]
# print(solution(N, board))