T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 전선 수
    loc = []
    for _ in range(N):
        ab = list(map(int, input().split()))
        loc.append(ab)

    count = 0
    for i in range(len(loc)-1):
        for j in range(i+1, len(loc)):
            if loc[i][0] > loc[j][0] and loc[i][1] < loc[j][1] or loc[i][0] < loc[j][0] and loc[j][1] < loc[i][1]:
                count += 1

    print(f'#{test_case} {count}')