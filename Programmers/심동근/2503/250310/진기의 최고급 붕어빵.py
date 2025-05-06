'''
while문으로 1초 단위로 계속 계산
1초 단위로 계산하며 생산된 붕어빵을 계속 추가하고,
정렬된 arrived에서 해당되는 손님이 왔을 때, 줄 수 있는지 여부 확인
'''
from collections import deque

def solution(N,M,K,arrived): # 시간초과 실패
    arrived= deque(sorted(arrived))

    time= 0
    cook_time= 0
    food= 0
    customer_arrived_at= arrived.popleft()

    while(True):
        # 1초 증가(0초 -> 1초)
        time+=1
        cook_time+=1

        if(cook_time==M): # 붕어빵이 생성되는 경우
            food+=K
            cook_time= 0

        if(customer_arrived_at==time):
            if(food<=0):
                return "Impossible"
            else:
                food-=1
                if(len(arrived)!=0):
                    customer_arrived_at= arrived.popleft()
                else:
                    return "Possible"

## main ##
T = int(input())
for test_case in range(1, T + 1):
    N, M, K= map(int, input().split())
    arrived= list(map(int, input().split()))
    result= solution(N, M, K, arrived)
    print(f"#{test_case} {result}")


# ==============================================================================================
from collections import deque


def solution(N, M, K, arrived):
    arrived.sort()  # 손님 도착 시간을 오름차순 정렬
    for i, time in enumerate(arrived):
        # time 초까지 만들어진 붕어빵 개수 계산
        food_available = (time // M) * K

        # i+1명이 붕어빵을 받아야 함
        if food_available < i + 1:
            return "Impossible"

    return "Possible"


## main ##
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrived = list(map(int, input().split()))
    result = solution(N, M, K, arrived)
    print(f"#{test_case} {result}")
