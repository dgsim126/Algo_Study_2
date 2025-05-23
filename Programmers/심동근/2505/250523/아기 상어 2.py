'''
1. 거리가 가장 가까운 물고기
2. 크기가 같은 물고기는 먹을 수 없지만, 해당 위치를 지나갈 수 있음
3. 먹을 수 있는 순위가 같은 물고기가 많다면 가장 위, 가장 왼쪽
'''
from collections import deque


def findStart(N, space):
    for y in range(N):
        for x in range(N):
            if(space[y][x]==9):
                return y, x

def solution(N, space):
    y, x= findStart(N, space)
    space[y][x]= 0
    size= 2
    temp= 0
    total_times= 0

    dy= [-1, 0, 1, 0] # 북 서 남 동
    dx= [0, -1, 0, 1]

    queue = deque([[y, x, 0]])
    is_visited= [[False] * N for _ in range(N)]
    fish_list= []

    while(queue):
        current_y, current_x, time= queue.popleft()

        for i in range(4):
            next_y = current_y + dy[i]
            next_x = current_x + dx[i]

            if(0<=next_y<N and 0<=next_x<N and is_visited[next_y][next_x]==False):
                if(0<space[next_y][next_x]<size): # 나보다 작음
                    y, x= next_y, next_x
                    total_times+=time
                    temp+=1
                    if(temp>=size):
                        size+=1
                        temp= 0
                    space[next_y][next_x]= 0
                    # queue= deque([[y,x,0]])
                    # is_visited = [[False] * N for _ in range(N)]

                    queue.append([next_y, next_x, time + 1])
                    is_visited[next_y][next_x] = True
                    fish_list.append([space[next_y][next_x], next_y, next_x, time])
                    if(len(queue)==0):
                        ## 항ㅁ고!!!

                elif(space[next_y][next_x]>size):
                    continue
                else:
                    queue.append([next_y,next_x,time+1])
                    is_visited[next_y][next_x]= True

    return size, total_times








## main ##
N= 4
space= [[4, 3, 2, 1],
        [0, 0, 0, 0],
        [0, 0, 9, 0],
        [1, 2, 3, 4]]
print(solution(N, space))