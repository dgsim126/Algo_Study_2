'''
일반적인 좌표와 다르게 x축이 세로, y축이 가로
이거 파악 못해서 거꾸로 해서 틀림
3트 성공
'''

'''
주사위 굴리는 매커니즘을 만드는게 핵심
 0 1 2 3 4 5
[2,4,1,3,5,6]
[2,6,4,1,5,3] 왼쪽
[2,1,3,6,5,4] 오른쪽
[6,4,2,3,1,5] 위쪽
[1,4,5,3,6,2] 아래쪽
    위     아래
'''
def left(dice):
    new_dice= [dice[0], dice[5], dice[1], dice[2], dice[4], dice[3]]
    return new_dice

def right(dice):
    new_dice= [dice[0], dice[2], dice[3], dice[5], dice[4], dice[1]]
    return new_dice

def up(dice):
    new_dice= [dice[5], dice[1], dice[0], dice[3], dice[2], dice[4]]
    return new_dice

def down(dice):
    new_dice= [dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]]
    return new_dice

# 1:동, 2:서, 3:북, 4:남
# N=y  M=x
def solution(N, M, x, y, K, map, order):
    dice= [0, 0, 0, 0, 0, 0]

    for i in range(K):
        current_order= order[i]
        if(current_order==1): # 동
            if(y<M-1):
                y+=1
                dice= right(dice)
                if(map[x][y]==0):
                    map[x][y]= dice[5]
                else:
                    dice[5]= map[x][y]
                    map[x][y]= 0
                print(dice[2])

        elif(current_order==2): # 서
            if(y>0):
                y-=1
                dice= left(dice)
                if (map[x][y] == 0):
                    map[x][y] = dice[5]
                else:
                    dice[5] = map[x][y]
                    map[x][y] = 0
                print(dice[2])

        elif(current_order==3): # 북
            if(x>0):
                x-=1
                dice= up(dice)
                if (map[x][y] == 0):
                    map[x][y] = dice[5]
                else:
                    dice[5] = map[x][y]
                    map[x][y] = 0
                print(dice[2])

        elif(current_order==4): # 남
            if(x<N-1):
                x+=1
                dice= down(dice)
                if (map[x][y] == 0):
                    map[x][y] = dice[5]
                else:
                    dice[5] = map[x][y]
                    map[x][y] = 0
                print(dice[2])



## main ##
N, M, x, y, K= map(int, input().split())
maps= []
for i in range(N):
    maps.append(list(map(int, input().split())))
order= list(map(int, input().split()))
solution(N, M, x, y, K, maps, order)
# N= 4 # 지도의 세로
# M= 2 # 지도의 가로
# x= 0 # 주사위 x 좌표
# y= 0 # 주사위 y 좌표
# K= 8# 명령의 개수
# map= [[0, 2],
#       [3, 4],
#       [5, 6],
#       [7, 8]]
# order= [4,4,4,1,3,3,3,2]

# N= 3 # 지도의 세로
# M= 3 # 지도의 가로
# x= 1 # 주사위 x 좌표
# y= 1 # 주사위 y 좌표
# K= 9 # 명령의 개수
# map= [[1,2,3],
#       [4,0,5],
#       [6,7,8]]
# order= [1,3,2,2,4,4,1,1,3]
