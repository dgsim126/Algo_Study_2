T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a == b:
        print(f'#{test_case} {a}')
    else:
        print(f'#{test_case} 1')