T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    num_lsts = [list(map(int, input().split())) for _ in range(m)]
    current = num_lsts[0].copy()

    for num_lst in num_lsts:
        find = False
        if num_lst == current:
            continue
        for i in range(len(current)):
            if current[i] > num_lst[0]:
                current[i:i] = num_lst
                find = True
                break
        if not find:
            current.extend(num_lst)

    current = current[::-1]
    print(f'#{test_case}', *current[:10])