for i in range(10):
    T = int(input())
    N, M = map(int, input().split())
    answer = N ** M
    print(f"#{T} {answer}")