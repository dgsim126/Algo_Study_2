from itertools import combinations

def solution(N, K):
    if K > 78:
        return 0
    elif K == 78:
        return 1

    result = 0
    numbers = [i for i in range(1, 13)]

    for comb in combinations(numbers, N):
        # print(comb)
        if sum(comb) == K:
            result += 1
        # elif sum(comb) > K:
        #     break

    return result

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    answer = solution(N, K)
    print(f"#{test_case} {answer}")