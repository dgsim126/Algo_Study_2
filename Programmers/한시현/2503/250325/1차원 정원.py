T = int(input())
for test_case in range(1, T + 1):
    n, d = map(int, input().split())

    ran = 2*d + 1
    if n % ran == 0:
        answer = n // ran
    else:
        answer = n // ran + 1

    print(f'#{test_case} {answer}')