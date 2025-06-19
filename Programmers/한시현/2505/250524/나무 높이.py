# 첫 날은 1
T = int(input())
for test_case in range(1, T + 1):
    tree_num = int(input())
    trees = list(map(int, input().split()))
    goal = max(trees)

    day1 = 0
    day2 = 0
    for tree in trees:
        current = goal - tree
        if current % 2 == 1:
            day2 += (current // 2)
            day1 += 1
        else:
            day2 += (current // 2)

    total_day = day1 + day2 + max(0, day1 - day2) * 2
    while day2 > 0:
        day2 -= 1
        day1 += 2
        change = day1 + day2 + max(0, day1 - day2) * 2
        if total_day > change:
            total_day = change
        else:
            break

    print(f'#{test_case} {total_day}')