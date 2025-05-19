# from itertools import permutations
#
# def solution(N, products):
#     numbers = [i for i in range(N)]
#     # print(numbers)
#     min = 0
#     for comb in permutations(numbers, N):
#         print(comb)
#
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     products = []
#     for _ in range(N):
#         products.append(list(map(int, input().split())))
#     answer = solution(N, products)
#     print(f"#{test_case} {answer}")
#
#
def dfs(i, tmp):  # 행, 현재 타임 합
    global res
    if tmp >= res:
        return
    if i == N:
        res = min(tmp, res)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(i+1, tmp+a[i][j])
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    res = 987654321
    visited = [0]*N  # 열 체크
    dfs(0, 0)
    print("#{} {}".format(tc, res))