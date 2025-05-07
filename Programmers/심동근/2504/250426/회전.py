
def solution(N, M, lst):
    return lst[M%N]

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, M, lst)}")

# N= 5
# M= 5
# lst= [18140, 14618, 18641, 22536, 23097]
# print(solution(N, M, lst))