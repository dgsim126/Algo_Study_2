T = int(input())
for test_case in range(1, T + 1):
    x_start, x_end, y_start, y_end = map(int, input().split())
    start = max(x_start, y_start)
    end = min(x_end, y_end)

    if start >= end:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {end-start}')