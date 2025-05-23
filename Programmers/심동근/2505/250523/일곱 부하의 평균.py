'''
- lst 내 값들보다 크다
- 모두 양의 정수
- 모든 부하의 키의 평균 역시 양의 정수
- 가장 작은 것을 출력
'''
def solution(lst):
    others= sum(lst)
    max_height= max(lst)
    current= 7

    while(True):
        # print(current)
        if(current>others+max_height):
            return current-others
        else:
            current+=7

## main ##
T= int(input())
for test_case in range(T):
    lst= list(map(int, input().split()))
    print(solution(lst))



# lst= [1, 2, 3, 4, 5, 7]
# print(solution(lst))