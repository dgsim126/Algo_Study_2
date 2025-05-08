def solution(x, y, z):
    if 2 * y == x + z:
        return 0.0  # tq
    else:
        return abs((2 * y) - (x + z)) / 2
    
T = int(input())
for test_case in range(1, T+1):
    x, y, z = map(int, input().split())
    answer = solution(x, y, z)

    print(f"#{test_case} {answer}")