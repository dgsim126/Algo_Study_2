def solution(a, b):
    count = 0
    nums = [1, 4, 9, 121, 484]
    for num in nums:
        if a <= num <= b:
            count += 1

    return count
 
T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    answer = solution(a, b)

    print(f"#{test_case} {answer}")