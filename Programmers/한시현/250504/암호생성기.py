from collections import deque

for test_case in range(1, 11):
    tc = int(input())
    data = deque(map(int, input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        current = data.popleft()
        if current - i <= 0:
            data.append(0)
            break
        data.append(current - i)
        i += 1

    print(f'#{test_case}', *data)