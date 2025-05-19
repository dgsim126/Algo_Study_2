from collections import deque

def solution(station):
    station = deque(station)
    N = station.popleft()
    queue = deque([[1, station[0], 0]])

    while queue:
        cur, dist, t = queue.popleft()

        for i in range(dist, 0, -1):
            if cur + dist >= N:
                return t
            else:
                queue.append([cur+i, station[cur+i-1], t + 1])

T = int(input())
for test_case in range(1, T+1):
    station = list(map(int, input().split()))
    answer = solution(station)
    print(f"#{test_case} {answer}")