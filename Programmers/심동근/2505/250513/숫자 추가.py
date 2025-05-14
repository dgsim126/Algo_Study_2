
def solution(N, M, L, lst, order):

    for i in range(M):
        index= order[i][0]
        value= order[i][1]

        lst[index:index]= [value]

    # print(lst)
    return lst[L]



## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L= map(int, input().split())
    lst= list(map(int, input().split()))
    order= []

    for i in range(M):
        order.append(list(map(int, input().split())))

    print(f"#{test_case} {solution(N, M, L, lst, order)}")