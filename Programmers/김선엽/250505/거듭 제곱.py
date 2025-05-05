def power(N, M):
    if M == 1:
        return N
    else:
        return N * power(N, M-1)

for test_case in range(10):
    T = int(input())
    N, M = map(int, input().split())
    answer = power(N, M)

    print(f"#{T} {answer}")