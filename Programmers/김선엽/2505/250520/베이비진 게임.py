from collections import deque

def solution(cards):
    cards = deque(cards)
    p1 = []
    p2 = []
    for i in range(len(cards)):
        if i % 2 == 0:
            p1.append(cards[i])
            set_1 = set(p1)
            p1_win = (p1.count(cards[i]) == 3) or ((cards[i] - 1) in set_1 and (cards[i] + 1) in set_1) or (
                        (cards[i] + 1) in set_1 and (cards[i] + 2) in set_1) or (
                                 (cards[i] - 2) in set_1 and (cards[i] - 1) in set_1)
            p2_win = False
        else:
            p2.append(cards[i])
            set_2 = set(p2)
            p2_win = (p2.count(cards[i]) == 3) or ((cards[i] - 1) in set_2 and (cards[i] + 1) in set_2) or (
                        (cards[i] + 1) in set_2 and (cards[i] + 2) in set_2) or (
                                 (cards[i] - 2) in set_2 and (cards[i] - 1) in set_2)
            p1_win = False
        # print(p1, p2, p1_win, p2_win)
        if p1_win and not p2_win:
            return 1
        elif not p1_win and p2_win:
            return 2

    return 0

T = int(input())
for test_case in range(1, T+1):
    cards = list(map(int, input().split()))
    print(f"#{test_case} {solution(cards)}")