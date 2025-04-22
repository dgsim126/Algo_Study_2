from collections import Counter

T = int(input())
for test_case in range(1, T + 1):
    tc = int(input())
    nums = list(map(int, input().split()))
    c_nums = Counter(nums).most_common()

    print(f'#{test_case} {c_nums[0][0]}')