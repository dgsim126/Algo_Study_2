def solution(N, Q, tasks):
    result = [0] * N
    for i in range(Q):
        for j in range(tasks[i][0]-1, tasks[i][1]):
            result[j] = i + 1
    
    return result

T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    tasks = []
    for i in range(Q):
        tasks.append(list(map(int, input().split())))
    
    answer = solution(N, Q, tasks)

    print(f"#{test_case}", *answer)