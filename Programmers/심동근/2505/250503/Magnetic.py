'''
각 열을 확인하면 된다.
위가 N, 아래가 S
1은 N, 2는 S

각 열을 확인할 때, 앞쪽에 2는 다 제거(2가 아닌 1이 나올때까지)
                뒤쪽의 1은 다 제거(1이 아닌 2가 나올때까지)

제거된 거에서 (1,2)의 쌍의 개수를 찾기
'''

from collections import deque

def solution(n, board):
    cnt= 0

    for i in range(n):
        lst= deque()

        for j in range(n):
            if(board[j][i]!=0):
                lst.append(board[j][i])

        while(lst):
            if(lst[0]==2):
                lst.popleft()
            else:
                break

        while(lst):
            if(lst[-1]==1):
                lst.pop()
            else:
                break

        temp= 0

        while(len(lst)>1):
            if(lst[0]==1 and lst[1]==2):
                cnt+=1
                temp+=1
                lst.popleft()
                lst.popleft()
            else:
                lst.popleft()
    return cnt


## main ##
T = 10
for test_case in range(1, T + 1):
    n= int(input())
    board= []
    for i in range(n):
        temp= list(map(int, input().split()))
        board.append(temp)
    result= solution(n, board)
    print(f"#{test_case} {result}")
