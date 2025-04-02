T = int(input())
for test_case in range(1, T + 1):
    S, T = input().split()

    while len(S) < 100:
        S += S
    while len(T) < 100:
        T += T

    if S[:100] == T[:100]:
        print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no')