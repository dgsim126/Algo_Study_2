'''
password의 앞에서부터 값을 하나씩 빼서 stack에 삽입
stack에서 마지막 두 개의 값이 같으면 제거(while문으로 같지 않을 때까지 반복)
이때, 스택값 확인할 때 인덱스 밖으로 나가는 것을 방지하기 위해 맨 앞에 a, b 삽입
'''
from collections import deque

def solution(N, password):
    stack= ["a", "b"]
    password= deque(password)

    for i in range(N):
        stack.append(password.popleft())
        while(stack[-1]==stack[-2]):
            stack.pop()
            stack.pop()

    stack= stack[2:]
    result= "".join(stack)

    return result



## main ##
T = 10
for test_case in range(1, T + 1):
    N, password= input().split()
    N= int(N)
    print(f"#{test_case} {solution(N, password)}")


# N= 16
# password= "4100112380990844"
# print(solution(N, password))
