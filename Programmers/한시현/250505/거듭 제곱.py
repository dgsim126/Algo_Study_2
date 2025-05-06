def recursive(n):
    global m
    m -= 1
    if m != 0:
        return n * recursive(n)
    else:
        return n

for test_case in range(1, 11):
    tc = int(input())
    i, m = map(int, input().split())

    print(f'#{test_case} {recursive(i)}')