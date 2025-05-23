T = int(input())
for test_case in range(1, T + 1):
    a, b, n = map(int, input().split())
    count = 0
    while True:
        count += 1
        if a > b:
            b += a
        else:
            a += b
        if a > n or b > n:
            break

    print(f'{count}')