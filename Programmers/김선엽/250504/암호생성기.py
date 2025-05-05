from collections import deque

def cycle(password):
    i = 0
    while i < 5:
        cur = password.popleft()
        cur -= (i + 1)
        if cur <= 0:
            cur = 0
            password.append(cur)
            return password
        else:
            password.append(cur)
            i += 1
    return password

def solution(data):
    data = deque(data)
    while data[-1] != 0:
        cycle(data)
    return data

for i in range(10):
    T = int(input())
    data = list(map(int, input().split())) # 0?
    answer = solution(data)
    print(f"#{T}", *answer)