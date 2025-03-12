'''
하나씩 확인하면서 o를 마주친 경우 모든 방향으로 이동하며 확인(N이 작으니 가능)
'''

def check(i, j, board, n): # y축, x축, 오목판, 길이
    # 오른쪽 방향
    if(j+4<n):
        flag= True
        for k in range(1, 5):
            if(board[i][j+k]=="."):
                flag= False
                break
        if(flag==True):
            return True

    # 사이
    if(j+4<n and i+4<n):
        flag= True
        for k in range(1, 5):
            if(board[i+k][j+k]=="."):
                flag= False
                break
        if(flag==True):
            return True

    # 아래 방향
    if(i+4<n):
        flag= True
        for k in range(1, 5):
            if(board[i+k][j]=="."):
                flag= False
                break
        if(flag==True):
            return True


    # 사이
    if (i + 4 < n and j -4 >= 0):
        flag = True
        for k in range(1, 5):
            if (board[i+k][j - k] == "."):
                flag = False
                break
        if (flag == True):
            return True

    return False

def solution(n, board):
    for i in range(n):
        for j in range(n):
            if(board[i][j]=="o"):
                result= check(i, j, board, n)
                if(result==True):
                    return "YES"

    return "NO"


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n= int(input())
    board= []
    for i in range(n):
        temp= input()
        board.append(temp)

    result= solution(n, board)
    print(f"#{test_case} {result}")

