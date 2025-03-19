T = 10
def recursive(n, m):
    if m == 0:
        return 1
    return n * recursive(n, m - 1)

for _ in range(1, T + 1):
    test_case = int(input())
    n, m = map(int, input().split())

    print(f"#{test_case} {recursive(n, m)}")