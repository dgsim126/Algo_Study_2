T = int(input())
for test_case in range(1, T + 1):
    N, P = map(int, input().split()) # N번 선택, 폭탄 위치 P

    recent = 0
    boom = False
    for i in range(1, N + 1):
        if recent + i == P:
            boom = True
        recent += i

    if boom:
        print(recent-1)
    else:
        print(recent)