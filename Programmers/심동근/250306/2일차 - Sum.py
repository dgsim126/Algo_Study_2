'''
그냥 다 구해서 비교하는 문제인가?
공간복잡도를 엄청 높이면 시간복잡도를 줄일 수 있는데 별로 의미 없어 보임
그냥 다 구하는걸로
'''

def solution(board):
    max_sum= 0

    # 가로합 구하기
    for i in range(100):
        temp= sum(board[i])
        if(temp>max_sum):
            max_sum= temp

    # 세로합 구하기
    for i in range(100):
        temp= 0
        for j in range(100):
            temp+=board[j][i]
        if(temp>max_sum):
            max_sum= temp

    # 대각선 1
    temp_1= 0
    temp_2= 0
    for i in range(100):
        temp_1+=board[i][i]
        temp_2+=board[99-i][99-i]

    return max(max_sum, temp_1, temp_2)


## main ##
T = 10
for test_case in range(1, T + 1):
    garbage= input()
    board= []
    for i in range(100):
        temp= list(map(int, input().split()))
        board.append(temp)

    result= solution(board)
    print(f"#{test_case} {result}")