def solution(N, M):
    for i in range(N):
        if(M%2==0):
            return "OFF"
        M//=2
    return "ON"


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    print(f"#{test_case} {solution(N, M)}")
# N= 4
# M= 62
# print(solution(N, M))