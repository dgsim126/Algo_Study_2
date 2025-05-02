# dfs? 어렵다..

def dfs(card_list, c_num):

T = int(input())
for test_case in range(1, T + 1):
    a, change = map(int, input().split())
    cards = list(map(int, str(a)))

    dfs(cards, change)

    print(f'#{test_case} {cards}')