from heapq import heappush, heappop
from collections import deque

def solution(n, m, rate, weight, movement):
    # 주차 공간을 관리할 최소 힙 (번호가 작은 자리부터 채움)
    empty_spaces = []
    for i in range(n):
        heappush(empty_spaces, i)  # 0-based index 사용

    # 현재 주차장 상태 (주차 공간 별 차량 번호 저장)
    parking_lot = [None] * n  # None이면 비어 있는 공간

    # 차량이 기다리는 대기 리스트
    waiting_queue = deque()

    # 차량 별 주차 공간을 저장 (차량이 어느 공간에 주차되었는지)
    parked_car_position = {}

    # 최종 요금 합산 결과
    total_fee = 0

    # 차량 이동 처리
    for car_num in movement:
        if car_num > 0:  # 차량 입차
            if empty_spaces:  # 빈 공간이 있다면 바로 주차
                spot = heappop(empty_spaces)  # 가장 작은 번호의 공간 가져오기
                parking_lot[spot] = car_num  # 주차장에 차량 저장
                parked_car_position[car_num] = spot  # 차량 위치 저장

                # 요금 계산
                total_fee += rate[spot] * weight[car_num - 1]
            else:  # 빈 공간이 없으면 대기
                waiting_queue.append(car_num)

        else:  # 차량 출차
            car_num = -car_num
            spot = parked_car_position.pop(car_num)  # 주차 공간 위치 찾기
            parking_lot[spot] = None  # 해당 공간 비우기
            heappush(empty_spaces, spot)  # 다시 사용 가능하도록 빈 공간에 추가

            # 대기 차량이 있으면 바로 주차
            if waiting_queue:
                next_car = waiting_queue.popleft()
                parking_lot[spot] = next_car  # 주차장에 차량 저장
                parked_car_position[next_car] = spot  # 차량 위치 저장

                # 요금 계산
                total_fee += rate[spot] * weight[next_car - 1]

    return total_fee

# 예제 입력
n = 2  # 주차 공간(1~n)
m = 4  # 차량의 수
rate = [5, 2]  # 주차장 자리 별 단위 무게당 요금
weight = [100, 500, 1000, 2000]  # 차량 별 무게
movement = [3, 1, 2, 4, -1, -3, -2, -4]  # 차량 이동 순서

print(solution(n, m, rate, weight, movement))  # 결과 출력
