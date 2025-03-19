T = int(input())
for test_case in range(1, T + 1):
    nums_len = int(input()) # 수열의 길이
    nums = list(map(int, input().split())) # 수열의 원소들

    lis_len = 0
    max_len = 0
    for i in range(nums_len-1):
        lis = [nums[i]]
        for j in range(i+1, nums_len):
            if lis[-1] <= nums[j]:
                lis.append(nums[j])
            elif lis[-1] > nums[j]:
                lis.pop()
                lis.append(nums[j])
        lis_len = len(lis)
        if max_len < lis_len:
            max_len = lis_len

    print(f'#{test_case} {max_len}')