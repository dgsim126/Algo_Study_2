from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nums_l = list(map(int, input().split()))
    nums_l.sort()
    nums = deque(nums_l)
    answer = []

    biggest = True
    for i in range(10):
        if biggest:
            answer.append(nums.pop())
            biggest = False
        elif not biggest:
            answer.append(nums.popleft())
            biggest = True

    print(f'#{test_case}', *answer)