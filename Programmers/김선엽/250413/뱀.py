from collections import deque

def solution(N, K, appels, L, turns):
    board = [[0] * N for _ in range(N)]
    direction = [0, 1]
    time = 0
    for apple in apples:
        board[apple[0]][apple[1]] = "A"
    turns = deque(turns)

    snakes = deque([0, 0])

    while True:
        x, y = snakes.popleft()
        rx, ry = x + direction[0], y + direction[1]

N = int(input())
K = int(input())
apples = []
for _ in range(K):
    apples.append(list(map(int,input().split())))
L = int(input())
turns = []
for _ in range(L):
    turns.append(list(map(str, input().split())))

print(solution(N, K, apples, L, turns))