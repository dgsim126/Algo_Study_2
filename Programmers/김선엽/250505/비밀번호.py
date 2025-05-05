from collections import deque

def solution(n, password):
    stack = deque([])
    password = deque(password)

    while password:
        cur = password.popleft()
        if stack:
            if cur == stack[-1]:
                stack.pop()
            else:
                stack.append(cur)
        else:
            stack.append(cur)

    return "".join(stack)

for test_case in range(1, 11):
    n, password = map(str, input().split())
    answer = solution(int(n), password)
    print(f"#{test_case} {answer}")