T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 품목 수
    Pi = list(map(int, input().split())) # 정상가 & 할인가 2N개 (오름차순)

    discount = []
    used = []
    for P in Pi:
        if P != 0:
            if int(P*(4/3)) in Pi:
                discount.append(P)
            Pi[Pi.index(int(P*(4/3)))] = 0

    print(f'#{test_case}', *discount)