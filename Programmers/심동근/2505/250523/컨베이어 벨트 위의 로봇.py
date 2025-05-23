'''
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
'''
from collections import deque

def print_C(head, tail, robot):
    print(robot)
    print(head)
    print(tail)
    print()

def first(head, tail, robot):
    tail.append(head.pop())
    head.appendleft(tail.popleft())
    robot.pop()
    robot.appendleft(0)
    robot[-1]= 0
    # print("first: 컨베이어 벨트 회전")
    # print_C(head, tail, robot)

def second(head, tail, robot):
    for i in range(len(robot)-2, -1, -1):
        if(robot[i]==1 and robot[i+1]==0 and head[i+1]!=0):
            robot[i+1]= 1
            robot[i]= 0
            head[i+1]-=1
    robot[-1]= 0
    # print("second: 이미 올라간 로봇들 한 칸씩 이동")
    # print_C(head, tail, robot)

def third(head, tail, robot):
    if(head[0]!=0 and robot[0]==0):
        head[0]-=1
        robot[0]= 1
    # print("third: 로봇 맨 앞에 배치(내구도 0이면 못 올림!")
    # print_C(head, tail, robot)

def check(head, tail, K):
    result= 0
    for i in range(len(head)):
        if(head[i]==0):
            result+=1
        if(tail[i]==0):
            result+=1

    if(result>=K):
        return 1
    else:
        return 0

def solution(N, K, life):

    head= deque(life[0:N])
    tail= deque(life[-1:N-1:-1])
    # print(head, tail)
    robot= [0]*N
    robot= deque(robot)
    answer= 1

    while(True):
        # print(robot)
        # print(head)
        # print(tail)
        # print()

        first(head, tail, robot)
        # if (check(head, tail, K) == 1):
        #     return answer

        second(head, tail, robot)
        # if (check(head, tail, K) == 1):
        #     return answer

        third(head, tail, robot)
        # if (check(head, tail, K) == 1):
        #     return answer

        if(check(head,tail,K)==1):
            return answer
        answer+=1


## main ##
# N= 4 # 컨베이어 벨트의 길이
# K= 5 # 내구도가 0인 칸의 개수가 K 이상이라면 종료
# life= [10, 1, 10, 6, 3, 4, 8, 2] # 벨트 밑 칸의 내구도
N, K= map(int, input().split())
life= list(map(int, input().split()))
print(solution(N, K, life))