from collections import deque
from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    cards = deque(map(int, input().split()))
    card_len = len(cards)
    p1 = []
    p2 = []

    winner = 0
    turn = 0
    for i in range(card_len):
        if turn % 2 == 0:
            p1.append(cards.popleft())
            if len(p1) >= 3:
                for p1_last3 in combinations(p1, 3):
                    p1_last3 = sorted(p1_last3)
                    if (p1_last3[-1] == p1_last3[-2] == p1_last3[-3]) or (p1_last3[-1] == p1_last3[-2]+1 and p1_last3[-2] == p1_last3[-3]+1):
                        winner = 1
                        break
                if winner != 0:
                    break

        elif turn % 2 == 1:
            p2.append(cards.popleft())
            if len(p2) >= 3:
                for p2_last3 in combinations(p2, 3):
                    p2_last3 = sorted(p2_last3)
                    if (p2_last3[-1] == p2_last3[-2] == p2_last3[-3]) or (p2_last3[-1] == p2_last3[-2]+1 and p2_last3[-2] == p2_last3[-3]+1):
                        winner = 2
                        break
                if winner != 0:
                    break
        turn += 1

    print(f'#{test_case} {winner}')