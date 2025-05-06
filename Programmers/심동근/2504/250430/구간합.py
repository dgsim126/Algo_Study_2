'''
계속 슬라이싱 후 sum하는 것보다 첫 합을 구하고 맨 앞 값 뺴고, 맨 뒤 값 더하는게 유리할 듯
'''

def solution(N, M, lst):
    current= sum(lst[0:M])
    max_result= current
    min_result= current

    for i in range(0, N-M):
        current= current-lst[i]+lst[i+M]
        max_result= max(max_result, current)
        min_result= min(min_result, current)

    return max_result-min_result


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, M, lst)}")
# N= 10
# M= 3
# lst= [1,2,3,4,5,6,7,8,9,10]
# print(solution(N, M, lst))