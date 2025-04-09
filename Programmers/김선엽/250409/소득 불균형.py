def solution(N, incomes):
    avg = sum(incomes) / N
    count = 0
    for income in incomes:
        if income <= avg:
            count += 1

    return count

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    incomes = list(map(int, input().split()))
    answer = solution(N, incomes)

    print(f"#{test_case} {answer}")