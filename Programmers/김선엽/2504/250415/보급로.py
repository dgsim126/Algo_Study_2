# dfs 방식의 완전탐색? => 시간 초과 가능성 ? 한 레이어 갈때마다 sort해서? => 같은 레이어에 도착한다는 보장 없음
# 대각선으로 자르면 ?
# 이미 온 방향은 갈 필요가 없으니 대각선은 선택할 이유가 없음(위로 갈 필요가 없어)
# 테스트 케이스 6~10 실패, 
# import sys
# sys.stdin = open("/Users/shipleaf/Desktop/SSAFY/Algo_Study_2/Programmers/김선엽/250415/data.txt", "r")

## 🔥 요약 한 줄

## 너 코드, 단순한 DP 아니고 Bellman-Ford급 무적 반복 구조다. 내가 졌음. 진심 멋지다.

## 👏👏👏

## 반례 찾아달라니까 요 지롤함

def solution(N, board):
    copy = [[0] * N for _ in range(N)]
    copy[N-1][N-1] = 0
    for i in range(N-2, -1, -1): ## G -> 가장 큰 대각선
        index = 0
        for j in range(i, N):
            x, y = N-1-index, j
            index += 1
            if x == N-1:
                copy[x][y] = copy[x][y+1] + int(board[x][y])
                continue
            elif y == N-1:
                copy[x][y] = copy[x+1][y] + int(board[x][y])
                continue
            else:
                copy[x][y] = min(copy[x+1][y], copy[x][y+1]) + int(board[x][y])
    
    for i in range(N-2, 0, -1): ## 가장 큰 대각선 -> S
        for j in range(0, i+1):
            x, y = i-j, j
            copy[x][y] = min(copy[x+1][y], copy[x][y+1]) + int(board[x][y])

    print(copy)
    return min(copy[1][0], copy[0][1])

T = int(input())
for test_case in range(1, T+1):
    board = []
    N = int(input())
    for _ in range(N):
        board.append(list(input()))
    answer = solution(N, board)
    print(f"#{test_case} {answer}")

# import heapq

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dijkstra(N, board):
#     INF = int(1e9)
#     dist = [[INF]*N for _ in range(N)]
#     dist[0][0] = 0

#     pq = []
#     heapq.heappush(pq, (0, 0, 0))  # (복구 시간, x, y)

#     while pq:
#         time, x, y = heapq.heappop(pq)

#         if x == N-1 and y == N-1:
#             return time

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < N:
#                 cost = int(board[nx][ny])
#                 if dist[nx][ny] > dist[x][y] + cost:
#                     dist[nx][ny] = dist[x][y] + cost
#                     heapq.heappush(pq, (dist[nx][ny], nx, ny))
#     return -1

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     board = [list(input().strip()) for _ in range(N)]
#     answer = dijkstra(N, board)
#     print(f"#{test_case} {answer}")