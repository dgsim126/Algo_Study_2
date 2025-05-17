# 이건 왜 D2..?
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    print(f'#{test_case} {max(nums) - min(nums)}')