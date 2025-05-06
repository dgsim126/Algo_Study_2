from collections import deque

def bfs(start, goal):
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        node, depth = queue.popleft()
        if node == goal:
            return depth
        for i in range(1, v+1):
            if not visited[i] and matrix[node][i] == 1:
                visited[i] = True
                queue.append((i, depth+1))
    return 0

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    matrix = [[0]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        n1, n2 = map(int, input().split())
        matrix[n1][n2] = 1
        matrix[n2][n1] = 1 # '방향성이 없는' 주의
    s, g = map(int, input().split())
    visited = [False] * (v+1)

    print(f'#{test_case} {bfs(s, g)}')