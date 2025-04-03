from itertools import combinations


def solution(N, K, lst):
    min_= 2147483647

    lst= sorted(lst)

    for i in range(N-K+1):
        # print(lst[i:i+K])
        if(lst[i+K-1]-lst[i]<min_):
            min_= lst[i+K-1]-lst[i]

    return min_


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K= map(int, input().split())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, K, lst)}")
