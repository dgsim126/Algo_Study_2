T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    work = [list(map(int, input().split())) for _ in range(n)]
    work.sort(key=lambda x: (x[1], x[0])) # 잘 활용하자

    end_time = 0
    count = 0
    for start, end in work:
        if start >= end_time:
            count += 1
            end_time = end

    print(f'#{test_case} {count}')