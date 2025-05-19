def solution(N, M, numbers, mumbers):
    answer = 0
    numbers = set(numbers)
    for mum in mumbers:
        if mum in numbers:
            answer += 1
    return answer

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    mumbers = list(map(int, input().split()))
    answer = solution(N, M, numbers, mumbers)
    print(f"#{test_case} {answer}")
