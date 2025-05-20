def max_trucks_scheduled(trucks):
    trucks.sort(key=lambda x: (x[1], x[0]))
    count = 0
    current_end = 0
    for start, end in trucks:
        if start >= current_end:
            count += 1
            current_end = end

    return count

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    trucks = []
    for _ in range(N):
        s, e = map(int, input().split())
        trucks.append((s, e))
    answer = max_trucks_scheduled(trucks)
    print(f"#{test_case} {answer}")