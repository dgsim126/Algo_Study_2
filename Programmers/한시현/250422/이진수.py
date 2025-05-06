T = int(input())
for test_case in range(1, T + 1):
    hex_num = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    n, hex_str = input().split()
    hex_list = [h for h in hex_str]

    binlist = []
    for i in hex_list:
        bin_num = bin(hex_num[i])[2:]
        if len(bin_num) != 4:
            bin_num = '0'*(4-len(bin_num)) + bin_num
        binlist.append(bin_num)

    print(f"#{test_case} {''.join(binlist)}")