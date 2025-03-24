from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    cards = input().split()
    cards_len = len(cards)

    half = (cards_len + 1) // 2
    first, second = deque(cards[:half]), deque(cards[half:])

    first_turn = True
    answer = []
    for i in range(cards_len):
        if first_turn:
            answer.append(first.popleft())
            first_turn = False

        elif not first_turn:
            answer.append(second.popleft())
            first_turn = True

    print(f'#{test_case} {" ".join(map(str, answer))}')
    