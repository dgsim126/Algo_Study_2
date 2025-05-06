'''
bfs 응용
'''
from collections import deque


def solution(V, E, lst, start, end):
    reversed_lst= []
    for i in range(E):
        reversed_lst.append([lst[i][1], lst[i][0]])
    lst= lst+reversed_lst

    is_used= [0 for _ in range(len(lst))]
    queue= deque()

    for i in range(E):
        if(lst[i][0]==start):
            queue.append([lst[i][0], lst[i][1], 1])
            is_used[i]= 1

    while(queue):
        current= queue.popleft()

        if(current[1]==end):
            return current[2]

        for i in range(len(lst)):
            if(is_used[i]==0 and current[1]==lst[i][0]):
                queue.append([lst[i][0], lst[i][1], current[2]+1])
                is_used[i]= 1 # 이거 안 넣어서 한 번 틀림

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
# V= 6
# E= 5
# lst= [[1,4],[1,3],[2,3],[2,5],[4,6]]
# start= 1
# end= 6
# print(solution(V, E, lst, start, end))