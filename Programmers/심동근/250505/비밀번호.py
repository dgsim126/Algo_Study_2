from collections import deque


def solution(N, lst):
    head= deque()
    tail= deque(lst)

    while(tail):
        if(len(head)==0):
            head.append(tail.popleft())
        elif(head[-1]==tail[0]):
            head.pop()
            tail.popleft()
        else:
            head.append(tail.popleft())

    return "".join(head)


## main ##
T = 10
for test_case in range(1, T + 1):
    N, password= input().split()
    N= int(N)
    print(f"#{test_case} {solution(N, password)}")
# N= 16
# lst= "4100112380990844"
# print(solution(N, lst))
