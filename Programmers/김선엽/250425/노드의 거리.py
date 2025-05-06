from collections import deque

def solution(V, graph, s, e):
    bridge = {}
    for start, end in graph:
        if start not in bridge:
            bridge[start] = deque([end])
        else:
            bridge[start].append(end)

        if end not in bridge:
            bridge[end] = deque([start])
        else:
            bridge[end].append(start)
    
    queue = deque([[s, 0]])
    visited = [False] * V

    # print(visited)

    while queue:
        cur, time = queue.popleft()
        visited[cur-1] = True

        if cur == e:
            return time

        if bridge[cur]:
            for next in bridge[cur]:
                if not visited[next-1]:
                    queue.append([next, time+1])
        else:
            continue
    return 0
            
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        graph.append(list(map(int, input().split())))

    s, e = map(int, input().split())

    answer = solution(V, graph, s, e)

    print(f"#{test_case} {answer}")