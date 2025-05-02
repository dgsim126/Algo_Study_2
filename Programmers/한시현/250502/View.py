for test_case in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    clear = 0
    for i in range(2, n-2):
        check = [building[i] - building[i-2], building[i] - building[i-1], building[i] - building[i+1], building[i] - building[i+2]]
        if min(check) > 0:
            clear += min(check)

    print(f'#{test_case} {clear}')