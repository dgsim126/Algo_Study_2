from collections import deque

def bfs(com, computers, visited):
    queue = deque([com])
    visited[com] = True

    while queue:
        node = queue.popleft()

        for i in range(len(computers)):
            if computers[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1

    return answer