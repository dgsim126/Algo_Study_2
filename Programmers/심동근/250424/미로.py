'''
2에서 3으로 도착할 수 있는지
0으로 되어있는 곳은 방문 가능
방문하고 방문한 곳은 1로 바꾸는 작업 필요(중복 방지)
'''
from collections import deque


def toFindStartIndex(map, N):
    for y in range(N):
        for x in range(N):
            if(map[y][x]=="2"):
                return y, x

def solution(map, N):
    y, x= toFindStartIndex(map, N)
    dx= [0, 1, 0, -1] # 북 동 남 서
    dy= [-1, 0, 1, 0]

    queue= deque()
    queue.append((y, x))

    while(queue):
        current_y, current_x= queue.popleft()

        for i in range(4):
            temp_y= current_y+dy[i]
            temp_x= current_x+dx[i]
            if(0<=temp_y and temp_y<N and 0<=temp_x and temp_x<N):
                if(map[temp_y][temp_x]=="0"):
                    queue.append((temp_y, temp_x))
                    map[temp_y][temp_x]= 1
                elif(map[temp_y][temp_x]=="3"):
                    return 1
    return 0

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    map= []
    for i in range(N):
        temp = list(input().strip())
        map.append(temp)
    print(f"#{test_case} {solution(map, N)}")