T = int(input())
for test_case in range(1, T + 1):
    n, m, target = map(int, input().split())
    num_lst = list(map(int, input().split()))
    for _ in range(m):
        idx, num = map(int, input().split())
        num_lst[idx:idx] = [num]

    print(f'#{test_case} {num_lst[target]}')