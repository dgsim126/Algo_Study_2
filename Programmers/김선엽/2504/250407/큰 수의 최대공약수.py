T = int(input())
for test_case in range(1, T+1):
    A, B = map(int, input().split())
    if A == B:
        print(f"#{test_case}", A)
        continue
    else:
        print(f"#{test_case} 1")