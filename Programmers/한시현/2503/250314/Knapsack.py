# 시간 초과...
# DP로 해결해야 할 듯.

def dfs(index, current_weight, current_value):
    global max_value

    max_value = max(max_value, current_value)

    if index >= N:
        return

    dfs(index + 1, current_weight, current_value)

    if current_weight + items[index][0] <= K:
        dfs(index + 1, current_weight + items[index][0], current_value + items[index][1])

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # N: 물건 수, K: 가방 용량

    items = []
    for _ in range(N):
        Vi, Ci = map(int, input().split())  # 물건의 Vi: 부피, Ci: 가치
        items.append((Vi, Ci))

    max_value = 0
    dfs(0, 0, 0)  # (index, 현재 부피, 현재 가치)

    print(f"#{test_case} {max_value}")
