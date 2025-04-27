'''
N 사이즈의 리스트를 만들고
0부터 N-1의 값을 각 리스트에 자리에 하나씩 넣어서 합을 구한다.
- 제한시간 초과
'''
from itertools import permutations

# def getSum(lst, index_lst):
#     result= 0
#     for i in range(len(index_lst)):
#         result+=lst[i][index_lst[i]]
#
#     return result
#
# def solution(N, lst):
#     is_used= [i for i in range(N)]
#     result= 2147483647
#
#     for perm in permutations(is_used, N):
#         temp= getSum(lst, list(perm))
#         if(temp<result):
#             result= temp
#
#     return result


def solution(N, lst):
    global result
    result= 2147483647

    def dfs(is_used, sum_, depth):
        global result
        if(depth==N and sum_<result):
            result= sum_
            return
        if(sum_>result):
            return

        for i in range(N):
            if(is_used[i]==0):
                is_used[i]= 1

                dfs(is_used, sum_+lst[depth][i], depth+1)

                is_used[i]= 0


    is_used = [0] * N
    dfs(is_used, 0, 0)
    return result


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    print(f"#{test_case} {solution(N, lst)}")

# N= 3
# lst= [[2,1,2],
#       [5,8,5],
#       [7,2,2]]
# print(solution(N, lst))
