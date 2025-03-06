# 풀이

def solution(board):
    length = len(board)
    row = 0
    col = 0
    left_dia = 0
    right_dia = 0
    
    for i in range(length):
        if sum(board[i]) > row:     # 행 계산
            row = sum(board[i])
        
        col_sum = 0
        for j in range(length):     # 열 계산
            col_sum += board[j][i]
        
        if col_sum > col:
            col = col_sum

        left_dia += board[i][i]     # 좌상 => 우하 대각선
        right_dia += board[i][length-1-i]   # 우상 => 좌하 대각선

    answer = max(row, col, left_dia, right_dia)


## 제출

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    length = len(board)
    row = 0
    col = 0
    left_dia = 0
    right_dia = 0
     
    for i in range(length):
        if sum(board[i]) > row:     # 행 계산
            row = sum(board[i])
         
        col_sum = 0
        for j in range(length):     # 열 계산
            col_sum += board[j][i]
         
        if col_sum > col:
            col = col_sum
 
        left_dia += board[i][i]
        right_dia += board[i][length-1-i]
 
    answer = max([row, col, left_dia, right_dia])
    print(f"#{test_case} {answer}")