from collections import deque

for test_case in range(1, 11):
    n, num = map(int, input().split())
    pw = deque(map(int, str(num)))
    new_pw = []
    while pw:
        check = pw.popleft()
        if not new_pw or new_pw[-1] != check:
            new_pw.append(check)
        elif new_pw[-1] == check:
            new_pw.pop()
    answer = int(''.join(map(str, new_pw)))

    print(f'#{test_case} {answer}')