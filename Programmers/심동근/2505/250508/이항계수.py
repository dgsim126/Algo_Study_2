import math


def binomial_coeff(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


T = int(input())
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())

    # a + b == n 이므로, a 또는 b를 사용해도 무방
    coeff = binomial_coeff(n, a)

    print(f"#{test_case} {coeff}")
