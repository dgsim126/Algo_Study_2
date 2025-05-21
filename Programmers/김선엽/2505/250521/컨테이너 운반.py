from collections import deque

def solution(N, M, w, t):
    answer = 0
    w = deque(sorted(w, reverse=True))
    t = deque(sorted(t, reverse=True))
    for i in range(N):
        for j in range(len(t)):
            if t[0] >= w[i]:
                answer += w[i]
                # print(answer)
                t.popleft()
                break
    return answer

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    answer = solution(N, M, w, t)
    print(f"#{test_case} {answer}")