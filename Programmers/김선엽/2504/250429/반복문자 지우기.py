from collections import deque

def solution(string):
    queue = deque([])
    string = deque(string)
    while string:
        str_ = string.popleft()
        if queue and queue[-1] == str_:
            queue.pop()
            continue
        else:
            queue.append(str_)
    
    return len(queue)

T = int(input())
for test_case in range(1, T+1):
    string = list(input())
    answer = solution(string)
    print(f"#{test_case} {answer}")