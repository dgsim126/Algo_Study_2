from collections import Counter

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input().strip()))
    check_list = Counter(cards).most_common()
    max_num = check_list[0][0]
    max_quan = check_list[0][1]

    for num, quan in check_list:
        if quan < max_quan:
            break
        if num > max_num:
            max_num = num

    print(f'#{test_case} {max_num} {max_quan}')