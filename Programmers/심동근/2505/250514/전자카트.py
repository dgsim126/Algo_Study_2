# '''
# 다익스트라 문제인 줄 알았는데 자세히 보니 n-queen 문제
# '''
#
# def solution(N, board):
#     global result
#     result= 2147483647
#
#     def dfs(current, is_used, depth):
#         global result
#
#         if(depth==N):
#             if(result>current):
#                 result= current
#             return
#
#         for i in range(N):
#             if(board[depth][i]!=0 and is_used[i]==False):
#                 is_used[i]= True
#
#                 dfs(current+board[depth][i], is_used, depth+1)
#
#                 is_used[i]= False
#
#
#     is_used= [False]*N
#     dfs(0, is_used, 0)
#
#     return result
#
#
#
#
#
# ## main ##
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N= int(input())
#     board= []
#     for i in range(N):
#         board.append(list(map(int, input().split())))
#     print(f"#{test_case} {solution(N, board)}")
# # N= 3
# # board= [
# #     [0, 18, 34],
# #     [48, 0, 55],
# #     [18, 7, 0]
# # ]
# # print(solution(N, board))

from itertools import permutations


def solve(N, e):
    min_cost = float('inf')
    for perm in permutations(range(1, N)):  # 사무실 제외한 순열
        cost = 0
        current = 0  # 시작점: 사무실

        for next in perm:
            cost += e[current][next]
            current = next

        cost += e[current][0]  # 마지막 지점에서 사무실로 복귀
        min_cost = min(min_cost, cost)

    return min_cost


# main
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    answer = solve(N, e)
    print(f"#{test_case} {answer}")
