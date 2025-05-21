from collections import deque

def solution(N, A, B):
    all= set(A+B)
    result= []
    A= deque(A)
    B= deque(B)

    while(len(A)!=0 or len(B)!=0):
        flag= False
        while(len(A)!=0 and flag==False):
            A_val= A[0]
            if(A.popleft() in all):
                all.remove(A_val)
                result.append([A_val, "A"])
                flag= True

        flag= False
        while(len(B) != 0 and flag == False):
            B_val = B[0]
            if(B.popleft() in all):
                all.remove(B_val)
                result.append([B_val, "B"])
                flag = True

    result.sort(key= lambda x : x[0])

    answer= ""
    for i in range(N):
        answer+=result[i][1]

    return answer

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    A= list(map(int, input().split()))
    B= list(map(int, input().split()))
    print(solution(N, A, B))
# N= 6
# A= [6,5,4,3,2,1]
# B= [6,5,4,3,2,1]
# print(solution(N, A, B))