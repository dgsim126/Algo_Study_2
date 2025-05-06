for test_case in range(1, 11):
    tc = int(input())
    nums = [list(map(int, input().split())) for _ in range(100)]
    sums = []

    # 가로
    for i in range(100):
        sums.append(sum(nums[i]))

    # 세로
    for col in range(100):
        add = 0
        for row in range(100):
            add += nums[row][col]
        sums.append(add)

    # 대각선 \
    x = 0
    y = 0
    add2 = 0
    while x <= 99:
        add2 += nums[x][y]
        x += 1
        y += 1
    sums.append(add2)

    # 대각선 /
    xx = 0
    yy = 99
    add3 = 0
    while x <= 99:
        add3 += nums[x][y]
        x += 1
        y -= 1
    sums.append(add3)

    print(f'#{tc} {max(sums)}')