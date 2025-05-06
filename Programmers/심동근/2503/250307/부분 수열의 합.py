from itertools import combinations
 
def solution(n, k, lst):
    result = 0
    # 모든 부분 수열을 생성하고 합이 K가 되는지 검사
    for i in range(1, n+1):  
        for subset in combinations(lst, i):
            if sum(subset) == k:
                result += 1
 
    return result
 
 
# main ##
T = int(input())
 
for test_case in range(1, T + 1):
    n, k= input().split()
    n= int(n)
    k= int(k)
    lst= list(map(int, input().split()))
    # print(n,k,lst)
    result= solution(n, k, lst)
    print(f"#{test_case} {result}")
# n= 4
# k= 3
# lst= [1,2,1,2]
# print(solution(n,k,lst))