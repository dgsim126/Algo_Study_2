from collections import deque


def solution(lst):
    lst= deque(lst)
    stack= []

    while(lst):
        current= lst.popleft()
        if(current in ["+", "-", "*", "/", "//"]): # ,하나 누락되서 틀림
            if(len(stack)<2):
                return "error"

            first= stack.pop()
            second= stack.pop()

            if(current=="+"):
                stack.append(second+first)
            elif(current=="-"):
                stack.append(second-first)
            elif(current=="*"):
                stack.append(second*first)
            elif(current=="//" or current=="/"):
                # if(first==0): # 이건가 하고 추가했는데 없어도 됨
                #     return "error"
                stack.append(second//first)

        elif(current=="."):
            if(len(stack)!=1):
                return "error"
            else:
                return stack[-1]
        else:
            stack.append(int(current))

    return "error"


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lst= list(input().split())
    print(f"#{test_case} {solution(lst)}")

# # lst= ['1', '5', '8', '10', '3', '4', '+', '+', '3', '+', '*', '2', '+', '+', '+', '.']
# lst= ["10", "2", "+", "3", "4", "+", "."]
# print(solution(lst))