def solution(N, K, scores):
    scores = sorted(scores, reverse=True)
    scores = scores[:K]

    return sum(scores)

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    answer = solution(N, K, scores)

    print(f"#{test_case} {answer}")