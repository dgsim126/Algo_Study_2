from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 정수 N
    nums = list(map(int, input().split())) # N 개의 정수

    comb_list = list(combinations(nums, 2))

    danjo = 0
    for comb in comb_list:
        is_danjo = True
        check = str(comb[0] * comb[1])
        len_check = len(check)

        if len_check != 1:
            for i in range(len_check-1):
                if int(check[i]) > int(check[i+1]):
                    is_danjo = False
                    break

        if is_danjo and int(check) > danjo:
            danjo = int(check)
            #print('save')

    if danjo != 0:
        print(f'#{test_case} {danjo}')
    else:
        print(f'#{test_case} -1')