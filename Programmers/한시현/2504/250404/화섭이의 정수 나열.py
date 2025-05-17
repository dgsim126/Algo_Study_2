T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 런타임 에러
    # if N % 20 == 0:
    #     count = N//20
    # else:
    #     count = N//20+1
    #
    # nums = []
    # for _ in range(count):
    #     nums.extend(list(map(int, input().split())))
    # 한 줄에 20개가 아닌 경우가 있는 듯 하다..

    nums = []
    while len(nums) < N:
        nums.extend(map(int, input().split()))

    num_array = nums.copy() # 1개짜리 미리 저장
    for step in range(2,5):
        for start in range(0, len(nums)-step+1):
            num_str = ''.join(map(str, nums[start:start+step]))
            num_array.append(int(num_str))

    erase_duple = list(set(num_array))
    erase_duple.sort()

    for i in range(int(''.join(map(str, nums)))):
        if i not in erase_duple:
            print(f'#{test_case} {i}')
            break