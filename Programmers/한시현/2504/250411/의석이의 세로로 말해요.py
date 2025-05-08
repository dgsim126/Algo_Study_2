from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    words = [deque(input()) for _ in range(5)]
    answer = []
    while words[0] or words[1] or words[2] or words[3] or words[4]:
        new = []
        for i in range(5):
            if words[i]:
                new.extend(words[i].popleft())
        answer.extend((''.join(new)))

    print(f'#{test_case} {"".join(answer)}')