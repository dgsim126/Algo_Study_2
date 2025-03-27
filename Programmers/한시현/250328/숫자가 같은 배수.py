# 1트
T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    num_list = list(map(int, str(num)))
    num_len = len(num_list)

    is_possible = False

    for i in range(2, 10):
        compare = num * i
        check = 0
        compare_list = list(map(int, str(compare)))

        if len(compare_list) > num_len:
            break

        for j in range(num_len):
            if compare_list[j] in num_list:
                check += 1

        if check == num_len:
            is_possible = True
            break

    if is_possible:
        print(f'#{test_case} possible')
    else:
        print(f'#{test_case} impossible')


# 2트
T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    num_list = list(map(int, str(num)))
    num_len = len(num_list)

    is_possible = False

    for i in range(2, 10):
        compare = num * i
        compare_list = list(map(int, str(compare)))

        if len(compare_list) > num_len:
            break

        for j in range(num_len):
            if num_list[j] in compare_list:
                compare_list.remove(num_list[j])

        if not compare_list:
            is_possible = True
            break

    if is_possible:
        print(f'#{test_case} possible')
    else:
        print(f'#{test_case} impossible')