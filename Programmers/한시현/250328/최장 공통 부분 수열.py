# 런타임 에러
# from itertools import combinations
#
# T = int(input())
# for test_case in range(1, T + 1):
#     word1, word2 = input().split()
#
#     lcs = []
#     for i in range(1, len(word1)):
#         word1_comb = list(combinations(word1, i))
#         word2_comb = list(combinations(word2, i))
#         for j in word1_comb:
#             if j in word2_comb:
#                 lcs.append(i)
#                 break
#
#     print(f'#{test_case} {max(lcs)}')

# 런타임 에러 2
# from itertools import combinations
#
# T = int(input())
# for test_case in range(1, T + 1):
#     word1, word2 = input().split()
#
#     lcs = 0
#     for i in range(1, len(word1)):
#         word1_comb = list(combinations(word1, i))
#         word2_comb = list(combinations(word2, i))
#         for j in word1_comb:
#             if j in word2_comb:
#                 if lcs < i:
#                     lcs = i
#                 break
#
#     print(f'#{test_case} {lcs}')

# index는? 첫번째 등장 위치만 반환
T = int(input())
for test_case in range(1, T + 1):
    word1, word2 = input().split()

    count1 = 0
    count2 = 0
    lcs1 = []
    lcs2 = []
    former_idx = -1
    current_idx = -1
    for i in word1:
        if i in word2:
            current_idx = word2.index(i)
            if former_idx < current_idx:
                lcs1.append(i)
                count1 += 1
                former_idx = current_idx

    former_idx = -1
    current_idx = -1
    for j in word2:
        if j in word1:
            current_idx = word2.index(j)
            if former_idx < current_idx:
                lcs2.append(j)
                count2 += 1
                former_idx = current_idx

    print(lcs1, lcs2)
    print(f'#{test_case} {max(count1, count2)}')

    # dp 문제였음..