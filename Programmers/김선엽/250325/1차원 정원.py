def solution(N, D):
    cover = 2 * D + 1
    if N % cover > 0:
        count = (N // cover) + 1
    else:
        count = (N // cover)

    return count

T = int(input())
for test_case in range(1, T+1):
    N, D = map(int, input().split())
    answer = solution(N, D)

    print(f"#{test_case} {answer}")