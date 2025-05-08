# 슬라이딩 윈도우

from itertools import combinations

def solution(N, K, candies):
    candies = sorted(candies, reverse=True)
    min = 1000000000
    for comb in combinations(candies, K):
        cur = max(comb) - min(comb)
        if cur < min:
            min = cur
    
    return min
        
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    answer = solution(N, K, candies)

    print(f"#{test_case} {answer}")