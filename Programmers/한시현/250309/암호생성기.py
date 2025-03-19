from collections import deque

for test_case in range(10):
    nums = deque(list(map(int, input().split())))

    count = 1
    while True:
        nl = nums.popleft()
        nl -= count
        if nl <= 0:
            nl = 0
        nums.append(nl)

        if nl == 0 and nums[-1] == 0:
            break

        count += 1
        if count == 6:
            count = 1


    print(f'#{test_case+1}', *nums)