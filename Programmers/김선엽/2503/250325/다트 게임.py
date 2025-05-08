def soltuon(arrows):
    score = 0
    for arrow in arrows:
        x, y = arrow
        dist = (x**2 + y**2) ** (1/2)
        if dist == 0:
            score += 10
            continue
        if dist % 20 == 0:
            spot = dist // 20
        else:
            spot = dist // 20 + 1
        
        result = 11 - spot
        if result >= 1:
            score += result

    return score

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arrows = []
    for _ in range(N):
        arrows.append(list(map(int, input().split())))
    answer = int(soltuon(arrows))

    print(f"#{test_case} {answer}")