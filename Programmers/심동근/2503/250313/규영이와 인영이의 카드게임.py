'''
9!의 경우의 수를 모두 직접 만들어서 비교하지는 않을 것으로 추측
'''

from itertools import permutations

def play_game(gyuyoung_cards):
    all_cards = set(range(1, 19))
    inyoung_cards = list(all_cards - set(gyuyoung_cards))  # 인영이가 가지는 카드 리스트

    win_count = 0
    lose_count = 0

    for inyoung_perm in permutations(inyoung_cards):  # 인영이 카드의 모든 순열
        gyuyoung_score = 0
        inyoung_score = 0

        for i in range(9):  # 9라운드 진행
            if gyuyoung_cards[i] > inyoung_perm[i]:
                gyuyoung_score += gyuyoung_cards[i] + inyoung_perm[i]
            else:
                inyoung_score += gyuyoung_cards[i] + inyoung_perm[i]

        if gyuyoung_score > inyoung_score:
            win_count += 1
        elif gyuyoung_score < inyoung_score:
            lose_count += 1

    return win_count, lose_count

# 입력 처리
T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    gyuyoung_cards = list(map(int, input().split()))
    win, lose = play_game(gyuyoung_cards)
    print(f"#{t} {win} {lose}")
