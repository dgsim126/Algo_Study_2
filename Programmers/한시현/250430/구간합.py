T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    check = []
    for i in range(len(nums)-m+1):
        check.append(sum(nums[i:i+m]))

    print(f'#{test_case} {max(check) - min(check)}')