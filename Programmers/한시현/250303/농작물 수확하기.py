T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = []

    for _ in range(N):
        square = [int(n) for n in str(input())]
        farm.append(square)

    mid = N//2

    total_revenue = 0
    need_add = [mid]

    start = mid
    end = mid
    for i in range(N):

        for na in need_add:
            total_revenue += farm[i][na]

        if i < mid:
            start -= 1
            end += 1
            need_add.append(start)
            need_add.append(end)
        elif i >= mid and len(need_add) > 1:
            need_add.pop()
            need_add.pop()

    print(f'#{test_case} {total_revenue}')