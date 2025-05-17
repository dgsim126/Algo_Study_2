def solution(N, M, L, numbers, orders):
    for order in orders:
        if order[0] < len(numbers):
            numbers = numbers[:order[0]] + [order[1]] + numbers[order[0]:]
        else:
            numbers = numbers + [order[1]]

    return numbers[L]

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    orders = []
    for _ in range(M):
        orders.append(list(map(int, input().split())))
    answer = solution(N, M, L, numbers, orders)
    print(f"#{test_case} {answer}")