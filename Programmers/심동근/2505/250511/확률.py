'''
N자리의 자연수를 생성(이때, 각 자릿수에 중복 사용된 숫자가 없으면 당첨)
N을 입력받아 당첨 확률을 구하라
- 맨 앞에는 0이 들어갈 수 없고 뒤에는 0이 들어갈 수 있다는 부분을 염두할 것
0부터 9까지의 숫자를 의미하는 is_used[False]*10을 생성
dfs로 문제 해결
'''

def target_count(N):
    result= 9
    if(N==1):
        return result

    added= 9
    for _ in range(N-1):
        result*=added
        added-=1

    return result

def all_count(N):
    result= 9
    if(N==1):
        return result

    for _ in range(N-1):
        result*=10

    return result



def solution(N):

    # def dfs(N, is_used, depth):
    #     global cnt
    #
    #     # 탈출조건
    #     if(depth==N):
    #         cnt+=1
    #         return
    #
    #     for i in range(10):
    #         if(depth==0 and i==0):
    #             continue
    #
    #         if(is_used[i]==False):
    #             is_used[i]= True
    #
    #             dfs(N, is_used, depth+1)
    #
    #             is_used[i]= False
    #
    #
    # global cnt
    # cnt= 0
    # is_used= [False]*10

    if(N>10):
        return "0.00000"

    # dfs(N, is_used, 0)
    target= target_count(N)
    all= all_count(N)
    result= round(target/all, 5)
    result= str(result)

    if(len(result)!=7):
        for i in range(7-len(result)):
            result+="0"

    return result



## main ##
# N= 11
# print(solution(N))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N= int(input())
    print(f"#{test_case} {solution(N)}")