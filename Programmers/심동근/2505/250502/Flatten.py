'''
10개 테스트 케이스 30초(1개당 3초)
- 계속 가장 높은 곳을 찾고, 가장 낮은 곳을 찾아 하나씩 옮기는 경우를 생각하면
max값 찾기 + min값 찾기 + 이동
(O(n) + O(n)) * 1000 그냥 풀어도 되네?
'''

def solution(N, lst):
    for i in range(N):
        max_val= max(lst)
        min_val= min(lst)
        if(max_val-min_val==1):
            return 1
        if(max_val-min_val==0):
            return 0

        max_index= lst.index(max_val)
        min_index= lst.index(min_val)
        lst[max_index]-=1
        lst[min_index]+=1

    return max(lst)-min(lst)



## main ##
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, lst)}")
# N= 3
# lst= [3,4,111]
# print(solution(N, lst))
