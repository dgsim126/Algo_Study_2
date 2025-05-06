'''
단순 구현
i=1부터 시작하는 것만 조심할 것
'''
from collections import deque

def solution(N, Q, lefts, rights):
    lefts= deque(lefts)
    rights= deque(rights)
    box= [0 for _ in range(N)]

    for i in range(1, Q+1):
        left= lefts.popleft()
        right= rights.popleft()
        for j in range(left-1, right):
            box[j]= i
        # print(box)

    return box


## main ##
T = int(input())
for test_case in range(1, T + 1):
    lefts= []
    rights= []
    N, Q= map(int, input().split())
    for i in range(Q):
        left, right= map(int, input().split())
        lefts.append(left)
        rights.append(right)
    print(f"#{test_case}",*solution(N, Q, lefts, rights))


# N= 5 # 상자의 개수
# Q= 2 # 변경 횟수
# left= [1, 2]
# right= [3, 4]
# print(solution(N, Q, left, right))