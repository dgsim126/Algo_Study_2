from collections import deque

def solution(string):
    number = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    calc = ("+", "*", "/", "-")
    queue = deque([])
    for s in string:
        if s[0] in number:
            queue.append(int(s))
        elif s[0] in calc:
            if len(queue) < 2:
                return "error"
            y = queue.pop()
            x = queue.pop()
            if s == "+":
                queue.append(x+y)
            elif s == "-":
                queue.append(x-y)
            elif s == "*":
                queue.append(x*y)
            else:
                queue.append(x/y)
        elif s == ".":
            answer = int(queue.pop())
            return answer

T = int(input())
for test_case in range(1, T+1):
    string = list(map(str, input().split()))
    answer = solution(string)
    print(f"#{test_case} {answer}")
