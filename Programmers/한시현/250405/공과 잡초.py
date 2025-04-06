from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    ground = deque(input())
    ball = 0
    while ground:
        recent = ground.popleft()
        if recent == '(':
            ball += 1
            ground.popleft()
        elif recent == ')':
            ball += 1

    print(f'#{test_case} {ball}')