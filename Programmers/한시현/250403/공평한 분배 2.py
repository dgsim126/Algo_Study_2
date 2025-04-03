# 런타임 에러
# from itertools import permutations
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N, K = map(int, input().split()) # N 전체 주머니 수, K 나눠 줄 주머니 수
#     candies = list(map(int, input().split()))
#
#     minimum = max(candies) - min(candies)
#     candy_perm = list(permutations(candies, K))
#
#     for i in range(len(candy_perm)):
#         ab = max(candy_perm[i]) - min(candy_perm[i])
#         if ab < minimum:
#             minimum = ab
#
#     print(f'#{test_case} {minimum}')

# 웬만하면 조합 순열 쓰면 안되겠다.

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # N 전체 주머니 수, K 나눠 줄 주머니 수
    candies = list(map(int, input().split()))
    sorted_candies = sorted(candies)

    minimum = sorted_candies[-1] - sorted_candies[0]

    for i in range(0, len(sorted_candies)-K+1):
        ab = sorted_candies[i+K-1] - sorted_candies[i]
        if ab < minimum:
            minimum = ab

    print(f'#{test_case} {minimum}')