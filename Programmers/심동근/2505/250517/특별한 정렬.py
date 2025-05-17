'''
일단 정렬은 한 후
deque으로 변경해서 pop, popleft순서대로 lst가 빌 때까지
'''
from collections import deque


def solution(N, lst):
    lst= sorted(lst)
    lst= deque(lst)
    result= []

    for i in range(5):
        result.append(lst.pop())
        result.append(lst.popleft())

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= list(map(int, input().split()))
    print(f"#{test_case}", *solution(N, lst))
# N= 10
# lst= [1,2,3,4,5,7,6,8,9,10]
# print(solution(N, lst))