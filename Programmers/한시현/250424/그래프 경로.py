from collections import deque

def bfs(start, goal):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == goal:
            return 1
        for i in range(v+1):
            if not visited[i] and mat[node][i] == 1:
                queue.append(i)
                visited[i] = True
    return 0

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    mat = [[0]*(v+1) for i in range(v+1)]
    for _ in range(e):
        st, en = map(int, input().split())
        mat[st][en] = 1
    s, g = map(int, input().split())
    visited = [False] * (v+1)

    print(f'#{test_case} {bfs(s, g)}')