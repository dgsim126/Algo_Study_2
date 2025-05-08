T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 수행해야 하는 연산 수
    cal = []
    for _ in range(N):
        cal.append(list(map(int, input().split())))

    print(f'#{test_case} {cal}')