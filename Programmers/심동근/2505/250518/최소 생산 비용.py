'''
N-Queen 문제
'''


def solution(N, board):
    global result
    result = 2147483647
    is_used= [False]*len(board[0])
    # temp= [-1]*len(board[0])

    def dfs(current, is_used, depth, max_depth, board):
        global result

        if(current>result):
            return

        # 탈출조건
        if(depth==max_depth):
            if(current<result):
                result= current
            # print(temp)
            return

        for i in range(max_depth):
            if(is_used[i]==False):
                is_used[i]= True
                # temp[depth]= i

                dfs(current+board[depth][i], is_used, depth+1, max_depth, board)

                is_used[i]= False
                # temp[depth]= -1

    dfs(0, is_used, 0, len(board[0]), board)

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    board= []
    for i in range(N):
        board.append(list(map(int, input().split())))
    print(f"#{test_case} {solution(N, board)}")


# N= 3
# board=[[73, 21, 21],
#        [11, 59, 40],
#        [24, 31, 83]]
# print(solution(N, board))
