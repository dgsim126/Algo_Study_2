for case in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))
    count = 0

    for i in range(2, N-1):
        if buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2] and buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2]:
            count += (buildings[i] - max(buildings[i+1], buildings[i+2], buildings[i-1], buildings[i-2]))

    print(f'#{case+1} {count}')