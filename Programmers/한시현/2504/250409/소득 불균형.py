T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    earn = list(map(int, input().split()))
    ave = sum(earn)/n

    count = 0
    for i in range(n):
        if earn[i] <= ave:
            count += 1

    print(f'#{test_case} {count}')