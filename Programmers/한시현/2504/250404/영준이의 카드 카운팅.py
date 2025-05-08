T = int(input())
for test_case in range(1, T + 1):
    card_str = input()
    card_list = []
    for i in range(len(card_str)//3):
        card_list.append(card_str[i*3:i*3+3])

    is_error = False
    for i in range(len(card_list)):
        if card_list.count(card_list[i]) != 1:
            is_error = True

    if is_error:
        print(f'#{test_case} ERROR')
    else:
        count_s = card_str.count('S')
        count_d = card_str.count('D')
        count_h = card_str.count('H')
        count_c = card_str.count('C')

        print(f'#{test_case} {13-count_s} {13-count_d} {13-count_h} {13-count_c}')