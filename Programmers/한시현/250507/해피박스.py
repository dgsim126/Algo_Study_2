# 느낌이 dp인데..

T = int(input())
for test_case in range(1, T + 1):
    box, m = map(int, input().split())
    gift = [list(map(int, input().split())) for _ in range(m)]

    print(gift)