T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    count = 0
    for num in range(a, b+1):
        if num ** 0.5 == int(num ** 0.5):
            str_num = str(num)
            str_root_num = str(int(num ** 0.5))
            if str_num == str_num[::-1] and str_root_num == str_root_num[::-1]:
                count += 1

    print(f'#{test_case} {count}')