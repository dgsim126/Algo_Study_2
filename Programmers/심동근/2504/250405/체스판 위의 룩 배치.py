'''
각 행에 O의 위치를 구한다. 이때, 각 행에 O은 오직 1개여야 한다.
모든 행의 위치를 구했으면 set으로 변경하여 수가 줄어드는지 확인한다.

조건 무조건 8개 있어야 한다를 뺴먹어서 틀림
'''

def solution(board):
    index_of= []

    for i in range(8):
        cnt= 0
        for j in range(8):
            if(board[i][j]=="O"):
                index_of.append(j)
                cnt+=1
        if(cnt>1 or cnt==0): # cnt==0 안 붙여서 틀림
            return "no"


    if(len(index_of)!=len(set(index_of))):
        return "no"

    return "yes"


## main ##
T = int(input())
for test_case in range(1, T + 1):
    board= []
    for i in range(8):
        board.append(input())
    print(f"#{test_case} {solution(board)}")