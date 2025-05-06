from collections import deque

def solution(V, graph, s, e):
    bridge = {}
    for start, end in graph:
        if start not in bridge:
            bridge[start] = [end]
        else:
            bridge[start].append(end)
        
    queue = deque([s])
    visited = [False] * V

    # print(visited)

    while queue:
        cur = queue.popleft()
        # print(cur)
        visited[cur-1] = True

        if cur == e:
            return 1

        if bridge[cur]:
            for next in bridge[cur]:
                if not visited[next-1]:
                    queue.append(next)
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