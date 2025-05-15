T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a.append(input())
    for _ in range(m):
        b.append(input())

    check = []
    for a_ in a:
        if a_ in b:
            check.append(a_)
    for b_ in b:
        if b_ in a:
            check.append(b_)

    print(f'#{test_case} {len(list(set(check)))}')