'''
팀을 2개로 나누는 경우는 맨 앞에 1번 플레이어로 만들 수 있는 (전체 인원 수/2)수의 집합을 확인하면 된다.
능력치의 합은
'''
from itertools import combinations

def diff(A, is_used, lst):

    result_A= 0
    result_B= 0
    B= []

    for i in range(len(is_used)):
        if(is_used[i]==False):
            B.append(i)

    # print(f"팀 A: {A}, 팀 B: {B}")

    for comb in combinations(A, 2):
        temp_1, temp_2= comb
        result_A+= lst[temp_1][temp_2] + lst[temp_2][temp_1]


    for comb in combinations(B, 2):
        temp_1, temp_2= comb
        result_B+= lst[temp_1][temp_2] + lst[temp_2][temp_1]

    # print(result_A, result_B)
    result= max(result_A, result_B) - min(result_A, result_B)
    # print(result)
    # print()
    return result

def solution(N, lst):
    is_used= [False]*N
    is_used[0]= True
    global result
    result= 2147483647

    def dfs(is_used, depth, value, lst):
        global result

        # 탈출조건
        if(depth==N//2):
            temp= diff(value, is_used, lst)
            # print(temp)
            if(temp<result):
                result= temp
            return

        for i in range(N):
            if(is_used[i]==False):
                value.append(i)
                is_used[i]= True

                dfs(is_used, depth+1, value, lst)

                value.pop()
                is_used[i]= False

    dfs(is_used, 1, [0], lst)
    return result

## main ##
# N= 6
# lst= [[0,1,2,3,4,5],
#       [1,0,2,3,4,5],
#       [1,2,0,3,4,5],
#       [1,2,3,0,4,5],
#       [1,2,3,4,0,5],
#       [1,2,3,4,5,0]]
# print(solution(N, lst))
N= int(input())
lst= []
for i in range(N):
    lst.append(list(map(int, input().split())))
print(solution(N, lst))
