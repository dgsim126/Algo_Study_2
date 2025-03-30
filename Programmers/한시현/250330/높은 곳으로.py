T = int(input())
for test_case in range(1, T + 1):
    N, P = map(int, input().split()) # N번 선택, 폭탄 위치 P

    recent = 0
    for i in range(1, N + 1):
        if recent + i == P:
            continue
        recent += i

    if recent < 10**9:
        print(recent)
    else:
        print(10**9)

# 가장 작은 층들을 활용해 P-1 만들고 거기서부터 i층씩 추가