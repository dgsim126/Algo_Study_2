from collections import deque

def solution(board):
    row, col = len(board), len(board[0])
    cur_board = [[[0, 0, -1]] * col for _ in range(row)]
    half = len(board) // 2

    row1, row2, row3, row4, row5, row6, row7, row8 = deque([]), deque([]), deque([]), deque([]), deque([]), deque([]), deque([]), deque([])
    row_list = [row1, row2, row3, row4, row5, row6, row7, row8]
    col1, col2, col3, col4, col5, col6, col7, col8 = deque([]), deque([]), deque([]), deque([]), deque([]), deque([]), deque([]), deque([])
    col_list = [col1, col2, col3, col4, col5, col6, col7, col8]
    dig1, dig2 = deque([]), deque([])

    dig_dot = set((1,1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8))

solution([[2,4],[3,3]])

# 구글

T = int(input())
dx = [0,0,1,1,-1,-1,1,-1]
dy = [1,-1,0,-1,0,1,1,-1] # 상하좌우대각선
def change(a, b, color, d): # 바꿔야할 좌표를 리스트에 넣는 함수 (DFS)
    global flag # d 방향에 같은 컬러가 있는지 확인하는 flag
    na = a + dx[d]
    nb = b + dy[d]
    if na < 0 or nb < 0 or na >=N or nb >= N:
        return
    if pan[na][nb] == color:
        flag = True
        return
    if pan[na][nb] != 0 and pan[na][nb] != color:
        willchange.append((na,nb))
        change(na, nb, color, d)

for test_case in range(1, T + 1):
    black, white = 0,0
    N, M = map(int, input().split())
    pan = [[0 for _ in range(N)] for i in range(N)]
    pan[N//2-1][N//2-1] = 2 # 초기값 설정
    pan[N//2][N//2-1] = 1
    pan[N//2-1][N//2] = 1
    pan[N//2][N//2] = 2
    for i in range(M):
        y, x, color = map(int, input().split()) # color == 1? black/ color == 2? white
        pan[x-1][y-1] = color # 색 입력
        for j in range(8): # 방금 놓은 돌을 기준으로 상하좌우대각선 모든 방향에 같은 색의 돌이 있는지 확인
            flag = False # 그 방향에 같은 색의 컬러가 있는지 확인하는 flag
            willchange = [] # 색깔이 바뀌어야하는 좌표들의 리스트
            change(x-1, y-1, color, j) # 바뀌어야하는 좌표들을 찾는 함수
            if flag==True: # 같은 색의 컬러가 있다면 바뀌어야하는 좌표들을 바꿔줌
                for t in willchange:
                    pan[t[0]][t[1]] = color
    for i in range(N): # count하기
        for j in range(N):
            if pan[i][j] == 1:
                black += 1
            elif pan[i][j] == 2:
                white += 1
    print(f'#{test_case} {black} {white}')