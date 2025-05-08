from itertools import combinations

def solution(N, K, list):
    answer = 0
    print(list, N, K)
    for i in range(1, len(list) + 1):
        for comb in combinations(list, i):
            print(comb, sum(comb))
            if sum(comb) == K:
                answer += 1

    return answer


# print(solution(4,3,[1, 2, 1, 2]))

N, K = map(int, input().split())
list = list(map(int, input().split()))

print(solution(N, K, list))