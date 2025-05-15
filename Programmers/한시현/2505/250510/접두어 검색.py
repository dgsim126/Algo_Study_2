T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    words = []
    prefix = []
    for _ in range(n):
        words.append(input())
    for _ in range(m):
        prefix.append(input())

    count = 0
    for pf in prefix:
        pf_len = len(pf)
        for word in words:
            if word[:pf_len] == pf:
                count += 1
                break

    print(f'#{test_case} {count}')