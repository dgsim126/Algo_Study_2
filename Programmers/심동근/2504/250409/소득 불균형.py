
def solution(N, lst):
    average= sum(lst)//N
    result= 0

    for i in range(len(lst)):
        if(lst[i]<=average):
            result+=1

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, lst)}")