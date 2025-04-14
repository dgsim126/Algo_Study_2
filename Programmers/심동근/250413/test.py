from collections import deque

def check_outside(a, b, N):
    if(a<0 or a>=N or b<0 or b>=N):
        return False
    else:
        return True

def solution(N, K, lst, move):
    move = deque(move)
    snake = deque([[0,0]]) # 꼬리 ~ 머리
    direction = 1 # 0=북, 1=동, 2=남, 3=서
    current_time = 0

    while(move):
        temp = move.popleft()
        how_many = temp[0]
        change = temp[1]

        if(direction==0): # 북
            for i in range(how_many-current_time):
                a = snake[-1][0]
                b = snake[-1][1]
                na = a - 1
                nb = b
                current_time += 1

                if(check_outside(na, nb, N)==False or [na, nb] in snake):
                    return current_time

                if([na, nb] in lst):
                    lst.remove([na, nb])
                    snake.append([na, nb])
                else:
                    snake.append([na, nb])
                    snake.popleft()

            if(change=="D"):
                direction = 1
            else:
                direction = 3

        elif(direction==1): # 동
            for i in range(how_many-current_time):
                a = snake[-1][0]
                b = snake[-1][1]
                na = a
                nb = b + 1
                current_time += 1

                if(check_outside(na, nb, N)==False or [na, nb] in snake):
                    return current_time

                if([na, nb] in lst):
                    lst.remove([na, nb])
                    snake.append([na, nb])
                else:
                    snake.append([na, nb])
                    snake.popleft()

            if(change=="D"):
                direction = 2
            else:
                direction = 0

        elif(direction==2): # 남
            for i in range(how_many-current_time):
                a = snake[-1][0]
                b = snake[-1][1]
                na = a + 1
                nb = b
                current_time += 1

                if(check_outside(na, nb, N)==False or [na, nb] in snake):
                    return current_time

                if([na, nb] in lst):
                    lst.remove([na, nb])
                    snake.append([na, nb])
                else:
                    snake.append([na, nb])
                    snake.popleft()

            if(change=="D"):
                direction = 3
            else:
                direction = 1

        else: # 서
            for i in range(how_many-current_time):
                a = snake[-1][0]
                b = snake[-1][1]
                na = a
                nb = b - 1
                current_time += 1

                if(check_outside(na, nb, N)==False or [na, nb] in snake):
                    return current_time

                if([na, nb] in lst):
                    lst.remove([na, nb])
                    snake.append([na, nb])
                else:
                    snake.append([na, nb])
                    snake.popleft()

            if(change=="D"):
                direction = 0
            else:
                direction = 2

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
            lst.remove([a, b])
            snake.append([a, b])
        else:
            snake.append([a, b])
            snake.popleft()


## main ##
N = int(input())
K = int(input())
lst = []
move = []
for i in range(K):
    a, b = map(int, input().split())
    lst.append([a-1, b-1])
T = int(input())
for i in range(T):
    a, b = input().split()
    move.append([int(a), b])
print(solution(N, K, lst, move))
