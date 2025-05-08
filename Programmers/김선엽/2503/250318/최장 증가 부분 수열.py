# from itertools import combinations

# def solution(n, numbers):
#     for i in range(n, 0, -1):
#         for comb in combinations(numbers, i):
#             possible = True
#             for j in range(len(comb)-1):
#                 if comb[j+1] < comb[j]:
#                     possible = False
#                     break
#             if possible:
#                 return i
#             else:
#                 continue

# T = int(input())
# for test_case in range(1, T+1):
#     n = int(input())
#     numbers = list(map(int, input().split()))
#     answer = solution(n, numbers)

#     print(f"#{test_case} {answer}")


T = int(input())

for tc in range(T):
    N = int(input())
    N_lst = list(map(int, input().split()))

    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if N_lst[i] > N_lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                print(i, j, dp)

    print(f"#{tc+1} {max(dp)}")