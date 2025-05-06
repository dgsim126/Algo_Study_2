from collections import deque

def solution(string):
    stack = deque([])
    for i in string:
        # print(stack)
        if i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return 0
        elif i == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return 0
        elif i in "({":
            stack.append(i)
    
    if stack:
        return 0
    else:
        return 1
    
T = int(input())
for test_case in range(1, T+1):
    string = input()

    answer = solution(string)

    print(f"#{test_case} {answer}")