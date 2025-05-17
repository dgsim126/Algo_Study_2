def solution(N, M, lst_N, lst_M):
    lst_N= set(lst_N)
    result= 0
    for i in range(M):
        if(lst_M[i] in lst_N):
            result+=1

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    lst_N= []
    lst_M= []
    for i in range(N):
        lst_N.append(input())
    for i in range(M):
        lst_M.append(input())
    print(f"#{test_case} {solution(N, M, lst_N, lst_M)}")