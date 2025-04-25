'''
두 가지 종류의 괄호
괄호가 하나라면 하나의 스택을 생성하여 간단하게 해결 가능
괄호가 두개라도 스택으로 해결 가능할 것 같음
'''

def solution(word):
    stack= []

    for i in range(len(word)):
        if(word[i]=="("):
            stack.append("(")
        elif(word[i]=="{"):
            stack.append("{")
        elif(word[i]==")"):
            if(len(stack)==0):
                return 0
            if(stack.pop()!="("):
                return 0
        elif(word[i]=="}"):
            if(len(stack)==0):
                return 0
            if(stack.pop()!="{"):
                return 0

    if(len(stack)>0):
        return 0

    return 1

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word= input()
    print(f"#{test_case} {solution(word)}")

