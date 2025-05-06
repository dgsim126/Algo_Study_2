T = int(input())
for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    box = [0]*n

    LtoR = []
    for _ in range(q):
        save = list(map(int, input().split()))
        LtoR.append(save)

    for i in range(len(LtoR)):
        box[LtoR[i][0]-1:LtoR[i][1]] = [i+1] * (LtoR[i][1] - LtoR[i][0] + 1)

    print(f'#{test_case}', *box)