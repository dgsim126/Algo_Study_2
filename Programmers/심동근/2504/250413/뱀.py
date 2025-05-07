'''
lst에서 꺼내
'''
from collections import deque

def check_outside(a, b, N):
    if(a<0 or a>=N or b<0 or b>=N):
        return False
    else:
        return True

def solution(N, K, lst, move):
    move= deque(move)
    snake= deque([[0,0]]) # 꼬리 ~ 머리
    direction= 1 # 0=북, 1=동, 2=남, 3=서
    current_k= 0
    current_time= 0
    index= 0
    while(move):
        # print(snake)
        temp= move.popleft()
        how_many= temp[0]
        change= temp[1]
        # print(direction)
        # print(current_time)
        # print()

        if(direction==0): # 북
            for i in range(how_many-current_time):
                a= snake[-1][0]
                b= snake[-1][1]
                if(check_outside(a-1, b, N)==False):
                    return current_time+i+1
                if([a-1, b] in snake):
                    return current_time+i+1
                if([a-1, b] in lst):
                    snake.append([a - 1, b])
                    current_k+=1
                    # if(current_k==K):
                    #     return current_time+i+1
                else:
                    snake.append([a-1, b])
                    snake.popleft()

            if(change=="D"):
                direction= 1
            else:
                direction= 3

        elif(direction==1): # 동
            for i in range(how_many-current_time):
                a= snake[-1][0]
                b= snake[-1][1]
                if(check_outside(a, b+1, N)==False):
                    return current_time+i+1
                if([a, b+1] in snake):
                    return current_time+i+1
                if([a, b+1] in lst):
                    snake.append([a, b+1])
                    current_k += 1
                    # if (current_k == K):
                    #     return current_time + i+1
                else:
                    snake.append([a, b+1])
                    snake.popleft()

            if(change=="D"):
                direction= 2
            else:
                direction= 0

        elif(direction==2): # 남
            for i in range(how_many-current_time):
                # print("!")
                a= snake[-1][0]
                b= snake[-1][1]
                if(check_outside(a+1, b, N)==False):
                    return current_time+i+1
                if([a+1, b] in snake):
                    return current_time+i+1
                if([a+1, b] in lst):
                    snake.append([a+1, b])
                    current_k += 1
                    # if (current_k == K):
                    #     return current_time + i+1
                else:
                    snake.append([a+1, b])
                    snake.popleft()

            if(change=="D"):
                direction= 3
            else:
                direction= 1
        else: # 서
            for i in range(how_many-current_time):
                a= snake[-1][0]
                b= snake[-1][1]
                if(check_outside(a, b-1, N)==False):
                    return current_time+i+1
                if([a, b-1] in snake):
                    return current_time+i+1
                if([a, b-1] in lst):
                    snake.append([a, b-1])
                    current_k += 1
                    # if (current_k == K):
                    #     return current_time + i+1
                else:
                    snake.append([a, b-1])
                    snake.popleft()

            if(change=="D"):
                direction= 0
            else:
                direction= 2
        current_time= how_many

    # 끝까지 이동
    while(True):
        a = snake[-1][0]
        b = snake[-1][1]
        if direction == 0: a -= 1
        elif direction == 1: b += 1
        elif direction == 2: a += 1
        else: b -= 1
        current_time += 1
        if not check_outside(a, b, N) or [a, b] in snake:
            return current_time
        if [a, b] in lst:
            snake.append([a, b])
            current_k += 1
            # if current_k == K:
            #     return current_time
        else:
            snake.append([a, b])
            snake.popleft()


## main ##
N= int(input())
K= int(input())
lst= []
move= []
for i in range(K):
    a, b= map(int, input().split())
    lst.append([a-1, b-1])
T= int(input())
for i in range(T):
    a, b= input().split()
    move.append([int(a), b])
# print(f"solution({N}, {K}, {lst}, {move})")
print(solution(N, K, lst, move))
# N= 10 # board의 크기
# K= 4 # 사과의 개수
# lst= [[1,2],[1,3],[1,4],[1,5]]
# move= [[8, "D"], [10, "D"], [11, "D"], [13, "L"]]
# print(solution(N, K, lst, move))