def solution(N):
    arr= [-1]*(N + 1)
    for i in range(1, N + 1):
        if i == 1:
            arr[i] = 1
        elif i == 2:
            arr[i] = 3
        elif i == 3:
            arr[i] = 6
        else:
            arr[i] = arr[i - 1] + 2 * arr[i - 2] + arr[i - 3]
    return arr[N]

## main ##
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = solution(N)
    print(f"#{test_case} {result}")
