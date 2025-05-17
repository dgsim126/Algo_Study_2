'''
0~N까지 이동, 이때 한번 충전으로 K만큼 이동 가능

현 위치에서 K만큼 임의로 이동시킨다.
이때, 이동된 위치에서 내 뒤를 기준으로 가장 가까운 충전소의 인덱스로 이동
'''
from collections import deque


def solution(K, N, M, lst):
    current_index= 0
    lst= deque(lst)
    cnt= 0 # 충전 횟수

    while(current_index<N):
        max_index= current_index+K # 가장 멀리갈 수 있는 경우

        if(max_index>=N): # 탈출 조건
            return cnt

        if(len(lst)==0):
            return 0

        # print("여기까지 갈 수 있음", max_index)

        if(max_index<lst[0]): # 놓칠뻔
            return 0

        # 가장 멀리갈 수 있는 범위에서 가장 인접한 충전소 찾기
        while(len(lst)!=0 and max_index>=lst[0]):
            current_index= lst.popleft()

        cnt+=1 # 충전소를 찾았기에 +1

        # print("하지만 여기까지(가장 인접한 충전소)", current_index)
        # print("남은 충전소", lst)
        # print()
        # input()

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M= map(int, input().split())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(K, N, M, lst)}")
# K= 3
# N= 10
# M= 5
# lst= [1,3,7,8,9]
# print(solution(K, N, M, lst))