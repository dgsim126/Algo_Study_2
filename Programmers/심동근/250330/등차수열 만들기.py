def solution(a, b, c):
    # 이미 등차수열이면 x = 0
    if 2 * b == a + c:
        return 0.0

    x1 = abs(a - (2 * b - c))  # a를 조정
    x2 = abs(b - ((a + c) / 2))  # b를 조정
    x3 = abs(c - (2 * b - a))  # c를 조정

    return min(x1, x2, x3)

## main ##
T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    result = solution(a, b, c)
    print(f"#{test_case} {result:.1f}")
