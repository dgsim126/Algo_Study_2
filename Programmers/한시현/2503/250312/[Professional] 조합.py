# 페르마 소정리?
T = int(input())
for test_case in range(1, T + 1):
    N, R = map(int, input().split())
    numerator = 1
    denominator = 1

    num = N
    for i in range(N, N-R, -1):
        numerator *= i

    for j in range(R):
        denominator *= (j+1)

    answer = numerator // denominator % 1234567891

    print(f"#{test_case} {answer}")