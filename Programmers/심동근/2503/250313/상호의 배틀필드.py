'''
특별한 것이 없는 단순 구현 문제
'''

def find_first(height, width, map):
    for i in range(height):
        for j in range(width):
            if(map[i][j]=="<"):
                return i, j, "<"
            elif(map[i][j]=="^"):
                return i, j, "^"
            elif(map[i][j]==">"):
                return i, j, ">"
            elif(map[i][j]=="v"):
                return i, j, "v"


def solution(height, width, map, moves):
    y, x, direction= find_first(height, width, map)
    #print(y, x, direction)

    for i in range(len(moves)):
        #print(f"i={i}, moves[i]= {moves[i]}")
        #print(map)
        if(moves[i]=="S"): # Shoot
            if(direction==">"):
                k= 1
                while(x+k<width):
                    if(map[y][x+k]=="#"):
                        break
                    if(map[y][x+k]=="*"):
                        map[y][x+k]="."
                        break
                    k+=1

            elif(direction=="<"):
                k= 1
                while(x-k>=0):
                    if(map[y][x-k]=="#"):
                        break
                    if(map[y][x-k]=="*"):
                        map[y][x-k]="."
                        break
                    k+=1

            elif(direction=="^"):
                k= 1
                while(y-k>=0):
                    if(map[y-k][x]=="#"):
                        break
                    if(map[y-k][x]=="*"):
                        map[y-k][x]="."
                        break
                    k+=1

            elif(direction=="v"):
                k= 1
                while(y+k<height):
                    if(map[y+k][x]=="#"):
                        break
                    if(map[y+k][x]=="*"):
                        map[y+k][x]="."
                        break
                    k+=1

            else:
                return "invalid direction"

        elif(moves[i]=="R"): # Right
            direction= ">"
            if(x+1<width and map[y][x+1]=="."):
                map[y][x]= "."
                map[y][x+1]= direction
                x+=1
            else:
                map[y][x]= direction

        elif(moves[i]=="L"): # Left
            direction= "<"
            if(x-1>=0 and map[y][x-1]=="."):
                map[y][x]= "."
                map[y][x-1]= direction
                x-=1
            else:
                map[y][x]= direction

        elif(moves[i]=="U"): # Up
            direction= "^"
            if(y-1>=0 and map[y-1][x]=="."):
                map[y][x]= "."
                map[y-1][x]= direction
                y-=1
            else:
                map[y][x]= direction

        elif(moves[i]=="D"): # Down
            direction= "v"
            if(y+1<height and map[y+1][x]=="."):
                map[y][x]= "."
                map[y+1][x]= direction
                y+=1
            else:
                map[y][x]= direction

        else:
            return "invalid operation"
        #print(map)
        # print()

    return map



## main ##
T = int(input())
for test_case in range(1, T + 1):
    height, width= input().split()
    map= []
    for i in range(int(height)):
        temp= list(input())
        map.append(temp)
    len_= input()
    moves= input()
    # print(height, width, map, moves)
    result= solution(int(height), int(width), map, moves)
    # print(f"#{test_case} {result}")
    print(f"#{test_case}", end=" ")
    for row in result:
        print("".join(row))  # 리스트를 문자열로 변환하여 한 줄씩 출력





# height= 3
# width= 7
# map= [['*', '*', '*', '.', '.', '.', '.'],
#       ['*', '-', '.', '.', '#', '*', '*'],
#       ['#', '<', '.', '*', '*', '*', '*']]
#
# moves= "SURSSSSUSLSRSSSURRDSRDS"
# print(solution(height, width, map, moves))