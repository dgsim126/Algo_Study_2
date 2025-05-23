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
    total_times= 0
    print(y,x)

    dy= [-1, 0, 1, 0] # 북 서 남 동
    dx= [0, -1, 0, 1]

    while(True):
        print("!!!!!!!!!!!!!!!!!!!!!!!")
        print("현재 내 크기", size)
        print("현재 총 시간", total_times)
        queue = deque()
        queue.append([y, x, 0])
        flag= False




        while(queue and flag==False):
            is_visited = [[False] * N for _ in range(N)]
            input()
            ## print ##
            for i in range(N):
                print(space[i])
            print("현재 큐", queue)

            flag= False
            current_y, current_x, time= queue.popleft() # 현재 위치와 시간 뽑기
            for i in range(4):
                next_y= current_y+dy[i]
                next_x= current_x+dx[i]
                print("next", next_y, next_x)
                if(0<=next_y<N and 0<=next_x<N and is_visited[next_y][next_x]==False): # 다음 위치가 공간 내 있는 경우만 확인
                    if(0<space[next_y][next_x]<size): # 내가 더 큰 경우(물고기 섭취)
                        print("내가 더 큼")
                        y, x= next_y, next_x
                        total_times+=time
                        size+= space[next_y][next_x]
                        space[next_y][next_x]= 0
                        flag=True
                        break
                    elif(space[next_y][next_x]>size): # 내가 더 작은 경우(갈 수 없음)
                        print("내가 더 작음(못 감)", space[next_y][next_x], size)
                        # break
                    elif(space[next_y][next_x]==size): # 크기가 같은 경우(갈 수 있음)
                        print("크기가 같음")
                        queue.append([next_y, next_x, time+1])
                        is_visited[next_y][next_x]= True
                    else:
                        print("아무것도 없어서 갈 수 있음")
                        queue.append([next_y, next_x, time+1])
                        is_visited[next_y][next_x] = True

        if(flag==False):
            return total_times




## main ##
N= 4
space= [[4, 3, 2, 1],
        [0, 0, 0, 0],
        [0, 0, 9, 0],
        [1, 2, 3, 4]]
print(solution(N, space))