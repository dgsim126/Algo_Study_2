from itertools import combinations

def solution(N, numbers):
    score = set()
    score.add(0)
    zero = [0] * N

    numbers.extend(zero)

    for comb in combinations(numbers, N):
        score.add(sum(comb))
    
    return len(score)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    answer = solution(N, numbers)

    print(f"#{test_case} {answer}")