T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = (list(map(int, input().split())))
    b = (list(map(int, input().split())))
    total = a + b
    set_total = list(set(total))

    print(f'#{test_case} {len(total) - len(set_total)}')