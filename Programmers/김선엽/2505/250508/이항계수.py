from collections import deque

def solution(n, a, b):
    queue = deque([[1, 1]])
    if n == 0 or n == 1:
        return 1
    else:
        while n > 1:
            n -= 1
            cur = queue.popleft()
            # print(cur)
            len_n = len(cur)
            new = []
            new.append(1)
            for i in range(len_n-1):
                new.append(cur[i] + cur[i+1])
            new.append(1)
            queue.append(new)
    return queue[0][b]

T = int(input())
for test_case in range(1, T+1):
    n, a, b = map(int, input().split())
    answer = solution(n, a, b)
    print(f"#{test_case} {answer}")