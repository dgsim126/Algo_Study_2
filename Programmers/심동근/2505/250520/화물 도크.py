"""
N이 100이기에 dfs로 내려가면 시간초과(게다가 최대 갯수를 찾는 문제, 즉 가지치기 불가)

시간이 짧은 순서로 정렬?
그렇게 해도 예외 발생

gpt's solution
종료 시간이 빠른 것부터 그리디 방식으로
"""
from collections import deque


def solution(N, lst):
    last= 0
    result= 0
    lst.sort(key=lambda x : x[1])
    # print(lst)

    lst= deque(lst)

    while(lst):
        start, end= lst.popleft()
        if(last<=start):
            result+=1
            last= end

    return result


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    print(f"#{test_case} {solution(N, lst)}")
# N= 5
# lst= [[20,23],[17,20],[23,24],[4,14],[8,18]]
# print(solution(N, lst))