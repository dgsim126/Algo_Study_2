# 1. 주사위 모양에 따른 동 <-> 서, 남 <-> 북 리스트를 모두 구현?
# 2. 주사위를 동서남북으로 굴렸을 때 위치가 변경되는 방법을 구현
# 2번 채택

def east(dice):
    new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    return new_dice

def west(dice):
    new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    return new_dice

def south(dice):
    new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    return new_dice

def north(dice):
    new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    return new_dice

def solution(N, M, x, y, K, maps, orders):
    location = 1
    dice = [1, 2, 3, 4, 5, 6]
    number = [0] * 6

    for i in range(0, len(orders)):
        if orders[i] == 1:
            if y + 1 < M:
                y += 1
                dice = east(dice)
                if maps[x][y] > 0:
                    number[dice[5]-1] = maps[x][y]
                    maps[x][y] = 0
                else:
                    maps[x][y] = number[dice[5]-1]
            else:
                continue
            
            print(number[dice[0]-1])

        elif orders[i] == 2:
            if 0 <= y - 1:
                y -= 1
                dice = west(dice)
                if maps[x][y] > 0:
                    number[dice[5]-1] = maps[x][y]
                    maps[x][y] = 0
                else:
                    maps[x][y] = number[dice[5]-1]
            else:
                continue
                
            print(number[dice[0]-1])

        elif orders[i] == 3:
            if 0 <= x - 1:
                x -= 1
                dice = north(dice)
                if maps[x][y] > 0:
                    number[dice[5]-1] = maps[x][y]
                    maps[x][y] = 0
                else:
                    maps[x][y] = number[dice[5]-1]
            else:
                continue
            
            print(number[dice[0]-1])

        elif orders[i] == 4:
            if x + 1 < N:
                x += 1
                dice = south(dice)
                if maps[x][y] > 0:
                    number[dice[5]-1] = maps[x][y]
                    maps[x][y] = 0
                else:
                    maps[x][y] = number[dice[5]-1]
            else:
                continue
            
            print(number[dice[0]-1])

maps = []
N, M, x, y, K = map(int, input().split())
for _ in range(N):
    maps.append(list(map(int, input().split())))
orders = list(map(int, input().split()))

solution(N, M, x, y, K, maps, orders)