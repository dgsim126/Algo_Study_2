'''
숫자 1은 아래로
숫자 2는 위로
새로줄 하나씩 확인하면서 cnt를 해야할 것 같음
하나의 세로에 들어온 후 해당 위치를 순회하며 1이 등장하는 순간부터 lst에 삽입
그리고 나서 [1,2] 묶음 덩어리를 카운트하면 된다!
[1,1,2]인 경우 [1,2] 묶음이 하나이므로 1을 cnt하고
[1,2,1,2]인 경우 [1,2] 묶음이 2개 이므로 cnt를 2개
- 묶음은 어떻게 구할까?
- while문 돌며 앞에 두개 확인하고 묶음이 맞으면 popleft() 두 번 진행
- 앞에 두개가 다르다면 popleft() 한 번 진행
-- 두 개 확인하니 예외조건 처리 잊지 말 것

예외 조건이 있나?
없는 것 같다! 일단 개발 시작
'''
from collections import deque
def solution(n, board):
    result= 0
    for i in range(n):
        lst= deque()
        for j in range(n):
            if(board[j][i]==1 or board[j][i]==2):
                lst.append(board[j][i])

        while(len(lst)>1):
            if(lst[0]==1 and lst[1]==2):
                lst.popleft()
                lst.popleft()
                result+=1
            else:
                lst.popleft()

    return result

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
