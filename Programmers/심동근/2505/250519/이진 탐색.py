
def find(goal, A):
    start_index= 0
    end_index= len(A)-1
    last= 0

    while(True):
        current_index= (start_index + end_index)//2

        # 탈출조건
        if(A[current_index]==goal):
            return 1

        if(A[current_index]>goal):
            if(last==-1):
                return 0
            end_index= current_index-1
            last= -1
        elif(A[current_index]<goal):
            if(last==1):
                return 0
            start_index= current_index+1
            last= 1


def solution(N, M, A, B):
    A= sorted(A)
    result= 0

    for i in range(M):
        current= B[i]
        result+=find(current, A)

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    A= list(map(int, input().split()))
    B= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, M, A, B)}")
# N= 3
# M= 3
# A= [1,2,3]
# B= [2,3,4]
# print(solution(N, M, A, B))