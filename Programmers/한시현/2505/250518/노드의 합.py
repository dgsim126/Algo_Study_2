from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, m, find = map(int, input().split())
    nodes = deque(tuple(map(int, input().split())) for _ in range(m)) # (리프노드 번호, 자연수)

    answer = 0
    while True:
        node_i, num = nodes.popleft()

        if node_i == find:
            answer = num
            break
        elif node_i % 2 == 0:
            if node_i == n:
                nodes.append((node_i // 2, num))
                nodes.append((node_i, num))
            else:
                for node in nodes:
                    if node[0] == node_i+1:
                        nodes.append((node_i // 2, num + node[1]))
                        nodes.append((node_i, num))
                        break
        elif node_i % 2 == 1:
            for node in nodes:
                if node[0] == node_i - 1:
                    nodes.append((node[0] // 2, num + node[1]))
                    nodes.append((node_i, num))
                    break

    print(f'#{test_case} {answer}')