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

    # 1 0
    # 2 6 2 2 9 4 1 3 0
    # 3 0
    # 4 9 7 9 5 4 3 8 0
    # 5 0
    # 6 8 7 1 6 4 3 5 0
    # 7 0
    # 8 7 5 8 4 8 1 3 0
    # 9 0
    # 10 3 8 7 4 4 7 4 0
    # 뭐지..?