def bs(total_page, target):
    left = 1
    right = total_page
    count = 0

    while True:
        mid = int((left + right) / 2)

        if mid == target:
            return count
        elif mid > target:
            right = mid
        elif mid < target:
            left = mid

        count += 1

T = int(input())
for test_case in range(1, T + 1):
    p, pa, pb = map(int, input().split())

    user_a = bs(p, pa)
    user_b = bs(p, pb)

    if user_a < user_b:
        winner = 'A'
    elif user_a > user_b:
        winner = 'B'
    else:
        winner = '0'

    print(f'#{test_case} {winner}')