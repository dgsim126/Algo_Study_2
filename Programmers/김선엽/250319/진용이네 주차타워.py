from collections import deque

def solution(n, m, R, W, cars):
    parking_fee = 0     # 총 요금 계산
    parking_spot = {}   # 주차한 자리
    is_in = [False] * n     # 현재 주차공간
    waiting = deque([])
    cars = deque(cars)

    while (cars or waiting) and m > 0:
        if False in is_in:  # 빈자리가 있을 때
            if waiting: # 웨이팅 우선
                car = waiting.popleft()
            else:
                car = cars.popleft()
                if car < 0:
                    index = parking_spot[(-1) * car]
                    is_in[index] = False
                    continue
            for i in range(n):  # 빈자리 찾고 요금 계산
                if not is_in[i]:
                    parking_fee += R[i] * W[car-1]
                    parking_spot[car] = i
                    is_in[i] = True
                    m -= 1
                    break
        else:   # 빈자리가 없을 때
            car = cars.popleft()    
            if car < 0:
                index = parking_spot[(-1) * car]
                is_in[index] = False
                continue
            else:
                waiting.append(car)

    return parking_fee

# print(solution(3, 4, [2,3,5],[2,1,3,8],[3,2,-3,1,4,-4,-2,-1]))
# print(solution(2,4,[5,2],[100,500,1000,2000],[3,1,2,4,-1,-3,-2,-4]))

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    R = []
    W = []
    cars = []
    for _ in range(n):
        R.append(int(input()))
    for _ in range(m):
        W.append(int(input()))
    for _ in range(2*m):
        cars.append(int(input()))
    
    answer = solution(n,m,R,W,cars)
    print(f"#{test_case} {answer}")
