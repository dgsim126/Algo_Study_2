'''
bfs 기초
'''
from collections import deque


def to_find_start(lst):
    for y in range(len(lst)):
        for x in range(len(lst)):
            if(lst[y][x]==2):
                return y, x

def solution(N, lst):
    dx= [0, 1, 0, -1] # 북 동 남 서
    dy= [-1, 0, 1, 0]

    start_y, start_x= to_find_start(lst)

    queue= deque()
    queue.append((start_y, start_x, 0))

    while(queue):
        y, x, way= queue.popleft()
        # print(y, x)

        for i in range(4):
            new_y= y+dy[i]
            new_x= x+dx[i]

            if(0<=new_y<len(lst) and 0<=new_x<len(lst) and lst[new_y][new_x]!=1):
                if(lst[new_y][new_x]==3): # 탈출조건
                    return way

                lst[new_y][new_x]= 1
                queue.append((new_y, new_x, way+1))

    return 0


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= []
    for i in range(N):
        lst.append(list(map(int, input().strip())))
    print(f"#{test_case} {solution(N, lst)}")
# N= 5
# lst= [[1,3,1,0,1],
# [1,0,1,0,1],
# [1,0,1,0,1],
# [1,0,1,0,1],
# [1,0,0,2,1]]
# print(solution(N, lst))