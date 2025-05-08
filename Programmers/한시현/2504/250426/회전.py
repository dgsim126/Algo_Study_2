from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    nums = deque((map(int, input().split())))

    for _ in range(m):
        nums.append(nums.popleft())

    print(f'#{test_case} {nums[0]}')