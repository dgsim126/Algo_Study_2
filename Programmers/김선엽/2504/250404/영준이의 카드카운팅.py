def solution(cards):
    dict = {
        "S" : set(),
        "D" : set(),
        "H" : set(),
        "C" : set()
    }

    for i in range(0, len(cards), 3):
        card_num = int(cards[i+1] + cards[i+2])
        if card_num in dict[cards[i]]:
            return False
        else:
            dict[cards[i]].add(card_num)

    require = [(13-len(dict["S"])),(13-len(dict["D"])),(13-len(dict["H"])),(13-len(dict["C"]))]

    return require


T = int(input())
for test_case in range(1, T+1):
    cards = input()
    if not solution(cards):
        print(f"#{test_case} ERROR")
    else:
        answer = solution(cards)

        print(f"#{test_case}", *answer)