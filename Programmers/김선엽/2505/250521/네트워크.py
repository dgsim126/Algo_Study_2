from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    # print(visited)
    graph = [i for i in range(n)]
    set_graph = set(graph)

    while set_graph:
        plus = list(set_graph)[0]
        queue = deque([plus])
        set_graph.remove(plus)
        visited[plus] = True
        while queue:
            cur = queue.popleft()
            # print(cur)
            for i in range(len(computers[cur])):
                if i != cur and computers[cur][i] == 1 and not visited[i]:
                    queue.append(i)
                    set_graph.remove(i)
                    visited[i] = True
        answer += 1
        # print(answer)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))