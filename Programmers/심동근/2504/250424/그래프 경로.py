'''
bfs를 응용해서 풀면 될 듯
'''
from collections import deque


def solution(V, E, lst, start, end):
    queue= deque()
    is_used= [0 for _ in range(E)]

    for i in range(E):
        if(lst[i][0]==start):
            queue.append(lst[i])
            is_used[i]= 1

    while(queue):
        current= queue.popleft()

        if(current[1]==end):
            return 1

        for i in range(E):
            if(is_used[i]==0 and lst[i][0]==current[1]):
                queue.append(lst[i])
                is_used[i]= 1
    return 0


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E= map(int, input().split())
    lst= []
    for i in range(E):
        temp= list(map(int, input().split()))
        lst.append(temp)
    start, end= map(int, input().split())
    print(f"#{test_case} {solution(V, E, lst, start, end)}")

# V= 8
# E= 6
# lst= [[1,4],[1,3],[2,3],[2,5],[4,6],[7,8]]
# start= 7
# end= 6
# print(solution(V, E, lst, start, end))