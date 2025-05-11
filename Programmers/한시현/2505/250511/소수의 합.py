def prime(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    total = 0
    for i in range(a + 1, b):
        if prime(i):
            total += i

    print(f"#{test_case} {total}")
    #