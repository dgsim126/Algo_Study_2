T = int(input())
for test_case in range(1, T + 1):
    l, u, x = map(int, input().split())

    if x > u:
        answer = -1
    elif x < l:
        answer = l - x
    else:
        answer = 0

    print(f'#{test_case} {answer}')