T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
