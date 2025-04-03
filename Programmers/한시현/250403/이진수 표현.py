T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    bin_m = str(bin(m)[2:])
    check = '1'*n

    if bin_m[len(bin_m)-n:] == check:
        print(f'#{test_case} ON')
    else:
        print(f'#{test_case} OFF')