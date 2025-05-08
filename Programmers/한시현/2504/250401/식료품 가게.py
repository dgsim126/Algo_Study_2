T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Pi = list(map(int, input().split()))

    discount = []
    used = []
    for P in Pi:
        if P != 0 and int(P*(4/3)) in Pi:
            discount.append(P)
            Pi[Pi.index(int(P*(4/3)))] = 0

    print(f'#{test_case}', *discount)