

def solution(N, K, lst):
    lst= sorted(lst, reverse=True)
    result= 0
    for i in range(K):
        result+=lst[i]

    return result


## main ##
T = int(input())
for test_case in range(1, T + 1):
    N, K= map(int, input().split())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, K, lst)}")
# N= 3
# K= 2
# lst= [100, 90, 80]
# print(solution(N, K, lst))
