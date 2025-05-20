from collections import deque

def bfs(current_station, change):
    queue = deque([(current_station, change)])

    while queue:
        station_idx, c = queue.popleft()

        if station_idx >= n - 1: # 목적지 도달
            return c

        for i in range(1, battery[station_idx] + 1): # 충전 후 갈 수 있는 모든 정류장
            next_station = station_idx + i

            if next_station < n and not visited[next_station]:
                visited[next_station] = True
                queue.append((next_station, c + 1))

    return 0

T = int(input())
for test_case in range(1, T + 1):
    inputs = list(map(int, input().split()))
    n = inputs[0]
    battery = inputs[1:]
    visited = [False] * n
    visited[0] = True

    answer = bfs(0, -1) # 처음 충전은 횟수에서 제외
    print(f"#{test_case} {answer}")