'''
새로운 위치에 값을 놓을 때, 그 값은 규칙에 의거해 허락되었기에
내가 돌을 놓은 위치를 기준으로 모든 방향(7개)를 탐색하여 색이 다른 경우를 찾고, 해당 방향의 그 다음 위치의 값이
내가 놓은 돌과 같은지를 확인 -> 해당 조건을 만족할 경우 사이의 돌의 색상을 나와 같은 색상으로 변경
'''

# 흑백흑 만 확인하는게 아니라 흑백백백백백흑 인 경우도 확인해야 함.

from collections import deque

def check(x, y, color, board, N):
    anothers= [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]] # 가장 위 북쪽 방향부터 오른쪽으로
    others= [[0,-2],[2,-2],[2,0],[2,2],[0,2],[-2,2],[-2,0],[-2,-2]]
    print(f"(x={x}, y={y})에 {color} 색상의 돌 넣기")

    for i in range(8):
        # 배열 내 값인지부터 확인
        if(0>others[i][0]+x or others[i][0]+x>=N):
            continue
        if(0>anothers[i][0]+x or anothers[i][0]+x>=N):
            continue
        if(0>others[i][1]+y or others[i][1]+y>=N):
            continue
        if (0>anothers[i][1]+y or anothers[i][1]+y>=N):
            continue

        # 색상 확인
        if(board[anothers[i][0]+x][anothers[i][1]+y]!=color
                and board[others[i][0]+x][others[i][1]+y]==color):
            board[anothers[i][0]+x][anothers[i][1]+y]= color
            board[y][x]= color
    return board




def solution(N, trial): # 0==공백, 1==흑, 2==백

    ### board 초기화
    board= []
    for i in range(N):
        board.append([0 for _ in range(N)])

    half= (N//2)-1
    for i in range(4):
        board[half][half]= 2
        board[half+1][half]= 1
        board[half][half+1]= 1
        board[half+1][half+1]= 2

    ### trial에서 하나씩 빼서 check()에 넘기고 board 리턴받기
    trial= deque(trial)
    while(trial):
        x, y, color= trial.popleft()
        board= check(x-1, y-1, color, board, N)
        for i in range(4):
            print(board[i])
        print()


    return board

## main ##
N= 4
M= 12
trial= [[1, 2, 1], [1, 1, 2], [4, 3, 1], [4, 4, 2],
        [2, 1, 1], [4, 2, 2], [3, 4, 1], [1, 3, 2],
        [2, 4, 1], [1, 4, 2], [4, 1, 2], [3, 1, 2]]
print(solution(N, trial))

'''
## 디버깅
(x=0, y=1)에 1 색상의 돌 넣기
[0, 0, 0, 0]
[1, 1, 1, 0]
[0, 1, 2, 0]
[0, 0, 0, 0]

(x=0, y=0)에 2 색상의 돌 넣기
[2, 0, 0, 0]
[1, 2, 1, 0]
[0, 1, 2, 0]
[0, 0, 0, 0]

(x=3, y=2)에 1 색상의 돌 넣기
[2, 0, 0, 0]
[1, 2, 1, 0]
[0, 1, 1, 1]
[0, 0, 0, 0]

(x=3, y=3)에 2 색상의 돌 넣기
[2, 0, 0, 0]
[1, 2, 1, 0]
[0, 1, 2, 1]
[0, 0, 0, 2]

(x=1, y=0)에 1 색상의 돌 넣기
[2, 1, 0, 0]
[1, 1, 1, 0]
[0, 1, 2, 1]
[0, 0, 0, 2]

(x=3, y=1)에 2 색상의 돌 넣기
[2, 1, 0, 0]
[1, 1, 1, 2]
[0, 1, 2, 1]
[0, 0, 2, 2]

(x=2, y=3)에 1 색상의 돌 넣기
[2, 1, 0, 0]
[1, 1, 1, 2]
[0, 1, 1, 1]
[0, 0, 1, 2]

(x=0, y=2)에 2 색상의 돌 넣기
[2, 2, 0, 0]
[1, 2, 1, 2]
[2, 1, 1, 1]
[0, 0, 1, 2]

(x=1, y=3)에 1 색상의 돌 넣기
[2, 2, 0, 0]
[1, 2, 1, 2]
[2, 1, 1, 1]
[0, 0, 1, 2]

(x=0, y=3)에 2 색상의 돌 넣기
[2, 2, 2, 0]
[1, 2, 1, 2]
[2, 1, 1, 1]
[2, 0, 1, 2]

(x=3, y=0)에 2 색상의 돌 넣기
[2, 2, 2, 0]
[1, 2, 1, 2]
[2, 1, 1, 1]
[2, 0, 1, 2]

(x=2, y=0)에 2 색상의 돌 넣기
[2, 2, 2, 0]
[2, 2, 1, 2]
[2, 1, 1, 1]
[2, 0, 1, 2]

[[2, 2, 2, 0], [2, 2, 1, 2], [2, 1, 1, 1], [2, 0, 1, 2]]

Process finished with exit code 0
'''
