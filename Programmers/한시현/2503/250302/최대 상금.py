T = int(input())

def dfs(count):
    global max_value

    if count == change:
        current_value = int(''.join(map(str, list_n)))
        max_value = max(max_value, current_value)
        return

    for i in range(len(list_n)):
        for j in range(i + 1, len(list_n)):
            list_n[i], list_n[j] = list_n[j], list_n[i]

            dfs(count + 1)

            # gpt : 백트래킹
            list_n[i], list_n[j] = list_n[j], list_n[i]

for test_case in range(1, T + 1):
    n, change = map(int, input().split())
    list_n = list(map(int, str(n)))

    max_value = 0
    dfs(0)

    print(f'#{test_case} {max_value}')
