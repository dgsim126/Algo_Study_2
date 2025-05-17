from collections import deque

def solution(N, M, C):
    oven = deque([])
    C = deque(C)
    for i in range(N):
        oven.append([C.popleft(), i+1])
    # print(oven.count(0))
    index = N + 1
    while oven.count(0) < N - 1:
        for i in range(N):
            oven[i] //= 2
            if oven[i] == 0:
                if C:
                    oven[i] = C.popleft()

    # for i in range(N):
    #     if oven[i] > 0:
    #         return oven[i]


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    answer = solution(N, M, C)
    print(f"#{test_case} {answer}")