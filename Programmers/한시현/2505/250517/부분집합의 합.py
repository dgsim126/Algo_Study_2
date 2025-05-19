from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    a = [1,2,3,4,5,6,7,8,9,10,11,12]

    count = 0
    # com_a = list(combinations(a, n))
    # for i in com_a:
    #     if sum(i) == k:
    #         count += 1

    for comb in combinations(a,n):
        if sum(comb) == k:
            count += 1

    print(f'#{test_case} {count}')