# from collections import deque

# def solution(N, M, street):
#     bridge = [[] for _ in range(N)]
#     for i in street:
#         start, end = i
#         bridge[start-1].append(end)
#         bridge[end-1].append(start)

#     print(bridge)
    
#     queue = deque([[1, 0]])
#     count_list = []
#     visited = [False for _ in range(N)]
    

#     while queue:
#         pos, count= queue.popleft()     # 1, 0
#         visited[pos-1] = True       # vistied[0] == True
    
#         if pos == N:
#             count_list.append(count+1)
#             continue

#         next = bridge[pos-1]
#         print(next)
        
#         for i in next:
#             if not visited[i-1]:
#                 queue.append([i, count + 1])
#                 visited[i-1] = True
    
#     return max(count_list)

# print(solution(3, 2, [[1,2], [3,2]]))
# print(solution(1, 0, []))


from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    street = [list(map(int, input().split())) for _ in range(M)]
    bridge = [[] for _ in range(N)]
    for i in street:
        start, end = i
        bridge[start-1].append(end)
        bridge[end-1].append(start)

    
    queue = deque([[1, 0]])
    count_list = []
    visited = [False for _ in range(N)]
    

    while queue:
        pos, count= queue.popleft()     # 1, 0
        visited[pos-1] = True       # vistied[0] == True
    
        if pos == N:
            count_list.append(count+1)
            continue

        next = bridge[pos-1]
        
        for i in next:
            if not visited[i-1]:
                queue.append([i, count + 1])
                visited[i-1] = True
    answer = max(count_list)
    
    print(f"#{test_case} {answer}")

# 1
# 7 8
# 1 2
# 2 3
# 2 4
# 3 4
# 3 7
# 4 7
# 4 5
# 5 6