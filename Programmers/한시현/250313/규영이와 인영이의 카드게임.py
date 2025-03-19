# 이거 왜 파이썬 없음?
from itertools import permutations, combinations

T = int(input())
for test_case in range(1, T + 1):
    cards = [n+1 for n in range(18)]

    gyu0 = list(map(int, input().split()))
    in0 = [n for n in cards if n not in gyu0]

    win, lose = 0, 0
    in0_per = list(permutations(in0))

    for in0_per_case in in0_per:
        g_score, i_score = 0, 0

        for i in range(len(gyu0)):
            if gyu0[i] > in0_per_case[i]:
                g_score += gyu0[i] + in0_per_case[i]
            elif gyu0[i] < in0_per_case[i]:
                i_score += gyu0[i] + in0_per_case[i]

        if g_score > i_score:
            win += 1
        elif g_score < i_score:
            lose += 1

    print(f"#{test_case} {win} {lose}")