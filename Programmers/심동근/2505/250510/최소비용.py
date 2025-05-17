'''
bfs? 무조건 시간초과 is_visited 방문처리 힘듦
다익스트라- gpt 참고
'''

import heapq

def solution(N, map):
    fuel= [([2147483647]*N) for _ in range(N)]
    fuel[0][0]= 0
    heap= []
    heapq.heappush(heap, (0, 0, 0))

    dx= [0, 1, 0, -1] # 북 동 남 서
    dy= [-1, 0, 1, 0]

    while(heap):
        x, y, cost= heapq.heappop(heap)

        # 탈출조건
        if(x==(N-1) and y==(N-1)):
            return cost

        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]

            if(0<=nx<N and 0<=ny<N):
                add_cost= 1

                if(map[ny][nx]>map[y][x]): # 새로 이동할 곳이 더 높은 경우
                    add_cost+=(map[ny][nx]-map[y][x])

                new_cost= cost+add_cost

                if(fuel[ny][nx]>new_cost): # 왔던 길을 돌아가지 않기 위해(새롭게 구한 값이 더 작은 경우에만 갱신)
                    fuel[ny][nx]= new_cost
                    heapq.heappush(heap, (nx, ny, new_cost))

    return -1


## main ##
N= 5
map= [[0, 0, 0, 0, 0], [0, 1, 2, 3, 0], [0, 2, 3, 4, 0], [0, 3, 4, 5, 0], [0, 0, 0, 0, 0]]
print(solution(N, map))