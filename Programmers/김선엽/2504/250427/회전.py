T = int(input())
for test_case in range(1, T+1):
    n, t = map(int, input().split())
    list_ = list(map(int, input().split()))

    i = t % n

    print(f"#{test_case} {list_[i]}")