'''
A= set(1~12)
N개의 원소를 가지고 있고, 부분집합의 합이 K인 것
dfs로 내려가면서 초과되면 더 이상 내려가지 않는 구조
'''

def solution(N, K):

    def dfs(current, is_used, depth, last_value):
        global result

        if(depth==N and current==K): # 탈출조건(성공)
            result+=1
            # print(temp)
            return
        if(depth>=N or current>K): # 탈출조건(실패)
            return
        if(last_value==12):
            return

        for i in range(last_value+1, 13):
            if(is_used[i]==False):
                is_used[i]= True
                temp[depth]= i

                # print(f"dfs({current+i}, {is_used}, {depth})")
                dfs(current+i, is_used, depth+1, i)

                is_used[i]= False
                temp[depth]= -1

    global result
    result= 0
    is_used= [False]*13 # index=0은 사용하지 않음
    temp= [-1]*N

    dfs(0, is_used, 0, 0)

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K= map(int, input().split())
    print(f"#{test_case} {solution(N, K)}")
# N= 5a
# K= 10
# print(solution(N, K))
