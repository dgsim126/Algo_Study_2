def solution(N, M, L, node_list):
    node_v = [0 for _ in range(N + 1)]
    # print(node_v)

    for node in node_list:
        node_v[node[0]] = node[1]

    def find_num(n):
        # print(1)
        if node_v[n] == 0:
            if N < 2 * n + 1:
                return find_num(2 * n)
            else:
                return find_num(2*n) + find_num(2*n+1)
        else:
            return node_v[n]

    answer = find_num(L)

    return answer

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    node_list = []
    for _ in range(M):
        node_list.append(list(map(int, input().split())))
    answer = solution(N, M, L, node_list)
    print(f"#{test_case} {answer}")