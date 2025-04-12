'''
bfs로 다시 도전
queue에 넣을 때, 공 두개의 인덱스와 몇 번 움직였는지를 함께 저장
queue에서 꺼내서 4방향 전체로 이동하고, 인덱스를 증가시킴
인덱스가 10이 넘으면 탈락
'''
from collections import deque


def move(board, B, R, dx, dy):
    B= B[:]
    R= R[:]
    cnt_B= 0
    cnt_R= 0
    flag= "NOTHING"
    while(board[B[0]+dy][B[1]+dx]!="#"):
        # print(f"B 이동 예정 위치: ({B[0] + dy}, {B[1] + dx}) -> 값: {board[B[0] + dy][B[1] + dx]}")
        if(board[B[0]+dy][B[1]+dx]=="O"):
            return (B, R, "False")
        cnt_B+=1
        B[0]+=dy
        B[1]+=dx

    while(board[R[0]+dy][R[1]+dx]!="#"):
        # print(f"R 이동 예정 위치: ({R[0]+dy}, {R[1]+dx}) -> 값: {board[R[0]+dy][R[1]+dx]}")
        if(board[R[0] + dy][R[1] + dx] == "O"):
            # print("!!!!!!!!!!")
            return (B, R, "SUCCESS")
        cnt_R+=1
        R[0]+=dy
        R[1]+=dx

    if(B[0]==R[0] and B[1]==R[1]):
        if(cnt_B>cnt_R):
            B[0]-=dy
            B[1]-=dx
        else:
            R[0]-=dy
            R[1]-=dx

    return (B, R, flag)



def solution(N, M, board): # 세로, 가로
    B_index= []
    R_index= []
    O_index= []
    cnt= 0

    # 1. 위치 찾기
    for i in range(N):
        for j in range(M):
            if (board[i][j] == "B"):
                B_index.append(i)
                B_index.append(j)
                cnt += 1
            elif (board[i][j] == "R"):
                R_index.append(i)
                R_index.append(j)
                cnt += 1
            elif (board[i][j] == "O"):
                O_index.append(i)
                O_index.append(j)
                cnt += 1
        if (cnt == 3):
            break
    # print(B_index, R_index, O_index)

    queue= deque()
    queue.append([B_index, R_index, 0])

    # [y][x]
    dx= [0, 1, 0, -1] # 북 동 남 서
    dy= [-1, 0, 1, 0]
    current_depth= 0
    result= []
    visited = set()
    visited.add((B_index[0], B_index[1], R_index[0], R_index[1]))

    while(queue):
        temp= queue.popleft()
        B= temp[0]
        R= temp[1]
        depth= temp[2]
        # print(B,R,depth)
        # input()

        if(depth>=10):
            continue

        for i in range(4):
            # print()
            # print()
            # print()
            BB, RR, flag= move(board, B, R, dx[i], dy[i])
            if(flag=="SUCCESS"):
                # print("성공")
                result.append(depth+1)
                # print(result)
            elif(flag=="NOTHING"):
                state = (BB[0], BB[1], RR[0], RR[1])
                if state not in visited:
                    visited.add(state)
                    queue.append([BB[:], RR[:], depth + 1])

    if(len(result)==0):
        return -1
    return min(result)


## main ##
N, M= map(int, input().split())
board= []
for i in range(N):
    board.append(input())
print(solution(N, M ,board))
# N= 5
# M= 5
# board= ["#####",
#         "#..B#",
#         "#.#.#",
#         "#RO.#",
#         "#####"]
# print(solution(N, M))