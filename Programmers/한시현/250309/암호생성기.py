from collections import deque

for _ in range(10):
    test_case = int(input())
    nums = deque(map(int, input().split()))

    count = 1
    while True:
        nl = nums.popleft()
        nl -= count
        if nl <= 0:
            nl = 0
        nums.append(nl)

        if nl == 0:
            break

        count += 1
        if count == 6:
            count = 1

    print(f'#{test_case}', *nums)