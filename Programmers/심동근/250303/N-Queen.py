'''
dfs문제로 추측된다.
즉 한 줄씩 이동하며 모든 위치에 체스말을 놓는 방식으로 dfs를 진행
여기서 문제는 가로, 세로는 is_used 리스트를 생성하여 쉽게 해결이 가능한데 대각선 방향은 어떻게 할까?
- N*N 사이즈로 is_used를 만들어서 dfs로 계속 넘겨? 너무 많은 공간을 할당하게 될텐데 괜찮나??? = 일단 진행
- 좀 더 생각해보니 is_possible에 [1,3,5..] 이런식으로 저장해놓고, 각 값이 들어갈때마다 앞의 값들을 확인하여 대각선에 겹치는지
-- 확인하는게 훨씬 빠른 거 같음
'''

def solution(N):

    def dfs(depth, N, lst):
        global cnt
        # 탈출조건
        if(depth==N):
            # print(lst)
            cnt+=1
            return

        for i in range(N):
            # 일단 값을 넣기
            lst[depth]= i

            flag= True
            # 내 앞의 값들 중 나와 같은 값이 있는지 확인(있다면 return)
            for j in range(depth):
                if(lst[j]==lst[depth]):
                    flag= False
                    break
            if(flag==False):
                continue

            # 내 앞의 값들 중 대각선 확인(있다면 return)
            for j in range(depth):
                if(lst[j]+(depth-j)==lst[depth] or lst[j]-(depth-j)==lst[depth]):
                    flag = False
                    break
            if(flag==False):
                continue

            dfs(depth+1, N, lst)

            # 백트래킹
            lst[depth]= -1


    lst= [-1 for _ in range(N)]
    global cnt
    cnt= 0
    dfs(0, N, lst)

    return cnt

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N= int(input())
    result= solution(N)
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////