# 20의 경우, 경우의 수 3개 (1010가로, 1010세로, 20)
# 1. 10으로 시작하는 경우
# 2. 20으로 시작하는 경우
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    case1 = n - 10 # 10으로 시작하는 경우
    case1_size20 = case1 // 20
    case1_size10 = case1 % 20

    case2 = n - 20  # 20으로 시작하는 경우
    case2_size20 = case2 // 20
    case2_size10 = case2 % 20
