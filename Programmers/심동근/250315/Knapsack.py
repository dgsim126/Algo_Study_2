'''
주어진 경우에서 1~N개를 뽑아 부피의 합 측정(combination 사용)
부피의 합이 K보다 작거나 같은 경우 가치의 합 측정
가장 큰 가치의 합을 구하면 된다.

-> 제한시간 초과 발생
: DP로 풀어볼 것
- dfs와 비슷하게 돌면서 최적의 루트를 찾고 값을 갱신해서 중복 계산이 없도록 구현

'''
from itertools import combinations

def solution(N, K, lst):
    max_= 0

    for i in range(1, N+1):
        for comb in combinations(lst, i):
            volumn_sum= sum(item[0] for item in comb)
            if(volumn_sum<=K):
                value_sum = sum(item[1] for item in comb)
                if(max_<value_sum):
                    max_= value_sum

    return max_

## main ##
T = int(input())
for test_case in range(1, T + 1):
    N, K= map(int, input().split())
    lst= []

    for i in range(N):
        volumn, value= map(int, input().split())
        lst.append([volumn, value])

    print(f"#{test_case} {solution(N, K, lst)}")



# N= 4
# K= 5
# lst= [[1,2],[3,2],[4,4],[2,3]]
# print(solution(N, K, lst))
