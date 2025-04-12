'''
dfs로 풀어야 하는 문제
dfs로 내려가면서 만약 만들 수 있는 최대값을 만나면 바로 리턴하는 방식
'''
from collections import deque
def up(board):
    return
def right(board):
    return
def down(board):
    return
def left(board):
    for i in range(board):
        temp= []
        for j in range(len(board[i])):
            if(board[i][j]!=0):
                temp.append(board[i][j])

        while(len(temp)>=2):
            if(temp[-1]==temp[-2]):
                temp[-2]+=temp[-1]
                temp.pop()



def dfs(real_board, depth):
    board= real_board[:]
    if(depth==5):
        return

    dfs(up(board), depth+1)
    dfs(right(board), depth+1)
    dfs(down(board), depth+1)
    dfs(left(board), depth+1)

def solution(N, board):
    global max_val
    dfs(board, 0)


## main ##
N= 3
board= [[2,2,2],[4,4,4],[8,8,8]]
print(solution(N, board))

