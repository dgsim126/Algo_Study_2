# b, finish = map(int, input().split())
# can_hold = list(map(int, input().split()))
# belt = []
# for i in range(1, b*2+1):
#     belt.append([i, i, 0, can_hold[i-1]]) # 칸 번호, 칸 위치, 로봇 있는지 여부(0,1), 내구도
#
# level = 0
# while True:
#     level += 1
#     count = 0
#     for j in range(b * 2): # 벨트 회전 (칸 위치 이동)
#         if belt[j][1] == b*2: # 칸 위치가 2N인 경우, -> 1
#             belt[j][1] = 1
#         else: # 칸 위치가 2N 아닌 경우 -> +1
#             belt[j][1] += 1
#
#     for m in range(b * 2): # 로봇 하차
#         if belt[m][1] == b and belt[m][2] == 1: # 하차
#             belt[m][2] = 0
#             break
#
#     for l in range(b): # 로봇 이동
#         if belt[l][2] == 1:
#             if 0 <= l+1 < b: # 다음 칸이 n 범위 안
#                 if belt[l+1][3] > 0 and belt[l+1][2] != 1:
#                     belt[l+1][2] = 1
#                     belt[l+1][3] -= 1
#                     if belt[l+1][1] == b:
#                         belt[l+1][2] = 0
#
#     for k in range(b * 2): # 로봇 승하차
#         if belt[k][1] == 1 and belt[k][2] == 0 and belt[k][3] > 0: # 승차
#             belt[k][2] = 1
#             belt[k][3] -= 1 # 내구도 감소
#         elif belt[k][1] == b and belt[k][2] == 1: # 하차
#             belt[k][2] = 0
#
#     for n in range(b * 2):
#         if belt[n][3] <= 0:
#             count += 1
#
#     if count >= finish:
#         break
#
# print(level)

from collections import deque

n, finish = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * n)

level = 0
while True:
    level += 1

    # 벨트 회전
    # bp = belt.pop()
    # belt.appendleft(bp)
    # rp = robot.pop()
    # robot.appendleft(rp)
    belt.rotate(1)
    robot.rotate(1)

    # 회전 후 로봇 하차
    robot[-1] = 0

    # 로봇 이동 (역순으로 해야함)
    for i in range(n-2, -1, -1): # n-1 ~ 0
        if robot[i] == 1:
            if 0 <= i+1 < n:
                if robot[i+1] == 0 and belt[i+1] > 0:
                    belt[i+1] -= 1
                    robot[i+1] = 1
                    robot[i] = 0

    # 이동 후 로봇 하차
    robot[-1] = 0

    # 로봇 승차
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    # # 이동 후 로봇 하차
    # robot[-1] = 0

    count = 0
    for b in belt:
        if b == 0:
            count += 1
    if count >= finish:
        break

print(level)

# GPT
from collections import deque

n, finish = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * n)

level = 0
while True:
    level += 1

    # 1. 벨트와 로봇 회전
    bp = belt.pop()
    belt.appendleft(bp)
    rp = robot.pop()
    robot.appendleft(rp)
    robot[-1] = 0  # 회전 후 하차

    # 2. 로봇 이동 (역순)
    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
    robot[-1] = 0  # 이동 후 하차

    # 3. 로봇 탑승
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    # 4. 내구도 0 확인
    if belt.count(0) >= finish:
        break

print(level)
