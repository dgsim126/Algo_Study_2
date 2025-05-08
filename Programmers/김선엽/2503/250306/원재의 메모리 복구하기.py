# 풀이
# 앞에부터 시작, 앞 index와 값이 달라지면 변경
from collections import deque

def solution(bit):
    answer = 0
    queue = deque([])
    for i in range(len(bit)):
        if not queue and bit[i] == "1":
            answer += 1
            queue.append("1")
        elif queue:
            left = queue.popleft()
            if bit[i] == left:
                queue.append(bit[i])
            else:
                answer += 1
                queue.append(bit[i])
    
    return answer

print(solution("0011")) ## 1
print(solution("100"))  ## 2

## 제출

T = int(input())
for test_case in range(1, T + 1):
    bit = str(input())
    answer = 0
    queue = deque([])
    for i in range(len(bit)):
        if not queue and bit[i] == "1":
            answer += 1
            queue.append("1")
        elif queue:
            left = queue.popleft()
            if bit[i] == left:
                queue.append(bit[i])
            else:
                answer += 1
                queue.append(bit[i])
    
    print(f"#{test_case} {answer}")