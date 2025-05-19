from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    size, pizza_count = map(int, input().split())
    cheese_list = list(map(int, input().split()))

    pizzas = deque()
    for i in range(pizza_count):
        pizzas.append((i + 1, cheese_list[i]))

    oven = deque()

    for _ in range(size):
        oven.append(pizzas.popleft())

    while len(oven) > 1:
        num, cheese = oven.popleft()
        cheese //= 2

        if cheese > 0:
            oven.append((num, cheese))
        else:
            if pizzas:
                oven.append(pizzas.popleft())

    print(f"#{test_case} {oven[0][0]}")