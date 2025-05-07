'''
회문 찾는 문제
모든 경우의 수를 확인해야 할 듯
'''
from collections import deque


def isSame(lst):
    lst= deque(lst)

    while(len(lst)>1):
        if(lst.pop()!=lst.popleft()):
            return 0

    return 1

def toFindRow(N, board):
    cnt= 0
    for i in range(8):
        for j in range(0, 8-N+1):
            # print(board[i][j:j+N], isSame(board[i][j:j+N]))
            cnt+=isSame(board[i][j:j+N])
        # print()

    return cnt

def toFindColumn(N, board):
    lst= []
    for i in range(8):
        temp= []
        for j in range(8):
            temp.append(board[j][i])
        lst.append(temp)

    return toFindRow(N, lst)

def solution(N, board):
    if(N==1):
        return 64

    return toFindRow(N, board) + toFindColumn(N, board)

## main ##
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    board= []
    for i in range(8):
        board.append(list(input().strip()))
    print(f"#{test_case} {solution(N, board)}")