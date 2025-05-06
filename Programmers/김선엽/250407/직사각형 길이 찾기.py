T = int(input())
for test_case in range(1, T+1):
    a, b, c = map(int, input().split())
    if a == b:
        print(f"#{test_case}", c)
        continue
    elif a == c:
        print(f"#{test_case}", b)
        continue
    else:
        print(f"#{test_case}", a)
        continue