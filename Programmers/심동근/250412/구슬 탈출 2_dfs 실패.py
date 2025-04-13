'''
빨간 구슬은 구멍에, 파란 구슬은 구멍에 빠지면 안된다.
- 공은 동시에 움직임

bfs 문제인 것 같음
- 먼저 O의 인덱스를 찾는다.
- R, B를 동서남북 방향 전체로 보낸다.

bfs로 어떻게 해야할지 모르겠다. dfs로 변경
- 현 R, B의 위치에서 동서남북 방향 전체로 보냄(depth, board 함께), 왼쪽 방향으로 이동한다면 x인덱스가 더 작은 값 먼저 움직이게
- depth가 10이 넘으면 return -1
'''
def solution(N, M): # 세로, 가로
    B_index= []
    R_index= []
    O_index= []
    cnt= 0

    # 1. 위치 찾기
    for i in range(N):
        for j in range(M):
            if(board[i][j]=="B"):
                B_index.append(i)
                B_index.append(j)
                cnt+=1
            elif(board[i][j]=="R"):
                R_index.append(i)
                R_index.append(j)
                cnt+=1
            elif(board[i][j]=="O"):
                O_index.append(i)
                O_index.append(j)
                cnt+=1
        if(cnt==3):
            break
    #print(B_index, R_index, O_index)

    def dfs(R_index, B_index, depth):

        def up(R_index, B_index, depth):
            if(R_index[0]>=B_index[0]):
                while(board[R_index[0]-1][R_index[1]]!="#"):
                    R_index[0]-=1
                while(board[B_index[0]-1][B_index[1]]!="#"):
                    B_index[0]-=1
            else:
                while (board[B_index[0] - 1][B_index[1]] != "#"):
                    B_index[0] -= 1
                while (board[R_index[0] - 1][R_index[1]] != "#"):
                    R_index[0] -= 1
            dfs(R_index, B_index, depth+1)

        def down(R_index, B_index, depth):
            if (R_index[0] <= B_index[0]):
                while (board[B_index[0] + 1][B_index[1]] != "#"):
                    B_index[0] += 1
                while (board[R_index[0] + 1][R_index[1]] != "#"):
                    R_index[0] += 1
            else:
                while (board[R_index[0] + 1][R_index[1]] != "#"):
                    R_index[0] += 1
                while (board[B_index[0] + 1][B_index[1]] != "#"):
                    B_index[0] += 1
            dfs(R_index, B_index, depth + 1)

        def right(R_index, B_index, depth):
            if(R_index[1]>=B_index[1]):
                while(board[R_index[0]][R_index[1]+1]!="#"):
                    R_index[1]+=1
                while (board[B_index[0]][B_index[1] + 1] != "#"):
                    B_index[1] += 1
            else:
                while (board[B_index[0]][B_index[1] + 1] != "#"):
                    B_index[1] += 1
                while (board[R_index[0]][R_index[1] + 1] != "#"):
                    R_index[1] += 1
            dfs(R_index, B_index, depth + 1)

        def left(R_index, B_index, depth):
            if (R_index[1] >= B_index[1]):
                while (board[B_index[0]][B_index[1] - 1] != "#"):
                    B_index[1] -= 1
                while (board[R_index[0]][R_index[1] - 1] != "#"):
                    R_index[1] -= 1
            else:
                while (board[R_index[0]][R_index[1] - 1] != "#"):
                    R_index[1] -= 1
                while (board[B_index[0]][B_index[1] - 1] != "#"):
                    R_index[1] -= 1
            dfs(R_index, B_index, depth + 1)

        up(R_index, B_index, depth)
        down(R_index, B_index, depth)
        right(R_index, B_index, depth)
        left(R_index, B_index, depth)




## main ##
N= 5
M= 5
board= ["#####",
        "#..B#",
        "#.#.#",
        "#RO.#",
        "#####"]
print(solution(N, M))