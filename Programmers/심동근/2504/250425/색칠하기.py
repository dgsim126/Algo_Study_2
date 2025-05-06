'''
10x10 사이즈의 배열을 만들고
- 붉은색은 1
- 파란색은 2
이때, 붉은색(1)은 0이거나 2인 경우에만 더해질 수 있고,
파란색(2)는 0이거나 1인 경우에만 더해질 수 있다.

이렇게 모든 경우를 확인한 후, 3의 개수를 cnt하면 된다.
'''

def solution(N, lst):
    # board= [[0]*10]*10
    board= [[0 for _ in range(10)] for _ in range(10)]
    # print(board)

    for i in range(len(lst)):
        for x in range(lst[i][0], lst[i][2]+1):
            for y in range(lst[i][1], lst[i][3]+1):
                # print(x, y, board[x][y])
                if(board[x][y]==0):
                    board[x][y]+=lst[i][4]
                elif(board[x][y]==1 and lst[i][4]==2):
                    board[x][y]+=lst[i][4]
                elif(board[x][y]==2 and lst[i][4]==1):
                    board[x][y]+=lst[i][4]
        # print(board)


    result= 0
    for i in range(10):
        for j in range(10):
            if(board[i][j]==3):
                result+=1

    return result


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= []
    for i in range(N):
        temp= list(map(int, input().split()))
        lst.append(temp)
    print(f"#{test_case} {solution(N, lst)}")
# N= 2
# lst= [[2,2,4,4,1],
#       [3,3,6,6,2]]
# print(solution(N, lst))