'''
주어진 경우에서 1~N개를 뽑아 부피의 합 측정(combination 사용)
부피의 합이 K보다 작거나 같은 경우 가치의 합 측정
가장 큰 가치의 합을 구하면 된다.

-> 제한시간 초과 발생
: DP로 풀어볼 것
- dfs와 비슷하게 돌면서 최적의 루트를 찾고 값을 갱신해서 중복 계산이 없도록 구현

'''
# ======================================================================================
# from itertools import combinations
#
# def solution(N, K, lst):
#     max_= 0
#
#     for i in range(1, N+1):
#         for comb in combinations(lst, i):
#             volumn_sum= sum(item[0] for item in comb)
#             if(volumn_sum<=K):
#                 value_sum = sum(item[1] for item in comb)
#                 if(max_<value_sum):
#                     max_= value_sum
#
#     return max_
# ======================================================================================

# ======================================================================================
# def solution(N, K, lst):
#
#     def dfs(depth, N, K, lst, volumn_sum, value_sum):
#         global max_value_sum
#
#         if(volumn_sum>K):
#             return
#
#         max_value_sum = max(max_value_sum, value_sum)  # 최대 가치 갱신
#
#         for i in range(N):  # 현재 물건 이후의 물건만 선택
#             if(is_used[i]==False):
#                 is_used[i]= True
#                 dfs(depth + 1, N, K, lst, volumn_sum + lst[i][0], value_sum + lst[i][1])
#
#                 is_used[i]= False
#
#         return max_value_sum
#
#     global max_value_sum
#     max_value_sum = 0
#     is_used = [False for _ in range(N)]
#
#     return dfs(0, N, K, lst, 0, 0)
# ======================================================================================


def solution(N, K, lst): # gpt
    dp = [0] * (K + 1)  # dp[i] = 부피 i일 때 최대 가치

    for volume, value in lst:
        for j in range(K, volume - 1, -1):  # 역순 탐색
            dp[j] = max(dp[j], dp[j - volume] + value)

    return dp[K]
# 인터넷 개념은 이해가 되는데 그걸 구현한 코드는 이해가 안 됨.


## main ##
N= 4 # 물건의 개수
K= 5 # 가방의 부피
lst= [[1,2],[3,2],[4,4],[2,3]]
print(solution(N, K, lst))

## main ##
# T = int(input())
# for test_case in range(1, T + 1):
#     N, K= map(int, input().split())
#     lst= []
#
#     for i in range(N):
#         volumn, value= map(int, input().split())
#         lst.append([volumn, value])
#
#     print(f"#{test_case} {solution(N, K, lst)}")




