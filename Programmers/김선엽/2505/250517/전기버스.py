def solution(K, N, M, charge):
    charge_set = set(charge)
    current = 0
    count = 0

    while current + K < N:  ## 가장 먼 거리를 우선선택
        for step in range(K, 0, -1):
            if (current + step) in charge_set:
                current += step
                count += 1
                break
        else:
            return 0

    return count


T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    answer = solution(K, N, M, charge)
    print(f"#{test_case} {answer}")