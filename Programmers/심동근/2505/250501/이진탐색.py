'''
누가 더 이진탐색으로 원하는 페이지에 먼저 도달하는지 확인하는 문제
'''

def toFind(goal, P):
    cnt= 1
    start= 1
    end= P

    while(True):
        mid= int((start+end)/2)
        if(mid==goal):
            return cnt

        if(mid>goal):
            end= mid
            cnt+=1
        else:
            start= mid
            cnt+=1

def solution(P, A, B):
    A_result= toFind(A, P)
    B_result= toFind(B, P)

    if(A_result>B_result):
        return "B"
    elif(A_result<B_result):
        return "A"
    else:
        return 0

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, A, B= map(int, input().split())
    print(f"#{test_case} {solution(P, A, B)}")