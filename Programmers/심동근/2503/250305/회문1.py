'''
가로 한 번 확인하고, 세로 한 번 확인하면 될 듯
예를 들어 가로 먼저 한 줄씩 확인한다고 가정한다면 n개씩 슬라이싱해서 가져온 후(앞에 n만큼 더미 값 넣자!)
가져온 리스트를 큐에 넣고 넣을 때 이전 값과 같다면 제거하는 방식. 그렇게 해서 리스트를 순회한 후
길이가 n과 같다면(처음에 넣은 더미값만 남았다면) 값을 증가.

-- aacc인 경우도 회문으로 인식하는 문제가 발생, aacaa도 마찬가지
어떻게 해결해야 할까?
넣으면서 확인하지 말고 일단 다 넣은 후, 확인하자!
짝수일 경우는 큰 문제 없음! 홀수인 경우 탈출조건을 n+1로 설정하면 될 듯!

아니 테스트 케이스 10개를 다 돌려도 문제가 없는데 왜 도대체 왜 런타임 에러가 발생하는지 도저히 이해가
'''
from collections import deque

def solution(n, board):
    if(n==1):
        return 64
    width= 0
    length= 0

    # 가로 확인
    for i in range(8):
        # print("i:", i)
        for j in range(0, 8-n+1):
            temp= board[i][j:j+n]
            sliced= deque(temp)
            flag= True

            for k in range(n//2):
                if (len(sliced) < 2):
                    return
                left= sliced.popleft()
                right= sliced.pop()

                if(left!=right):
                    flag= False
                    break

            if(flag==True):
                width+=1

    # print(width)

    # 세로 확인
    for i in range(8):
        # print("i:", i)
        for j in range(0, 8 - n + 1):
            temp= []
            for l in range(j, j+n):
                temp.append(board[l][i])

            sliced= deque(temp)
            flag= True

            for k in range(n//2):
                if(len(sliced)<2):
                    return
                left= sliced.popleft()
                right= sliced.pop()

                if(left!=right):
                    flag= False
                    break

            if (flag==True):
                length+=1

    return width+length

## main ##
T = int(input())
for test_case in range(1, T + 1):
    n= int(input())
    board= []
    for i in range(8):
        temp= input().strip()
        board.append(temp)
    result= solution(n, board)
    print(f"#{test_case} {result}")

# main ##
# n= 4
# board= ["CBBCBAAB",
#         "CCCBABCB",
#         "CAAAACAB",
#         "BACCCCAC",
#         "AABCBBAC",
#         "ACAACABC",
#         "BCCBAABC",
#         "ABBBCCAA"]
# board = [
#     "BCBBCACA",
#     "BCAAACAC",
#     "ABACBCCB",
#     "AACBCBCA",
#     "ACACBAAA",
#     "ACCACCCB",
#     "AACAAABA",
#     "CACCABCB"
# ]
#
# print(solution(n, board))
'''
C:\Users\dgsim\AppData\Local\Programs\Python\Python312\python.exe C:\mybox\repository\pycharm\Algo_Study_2\Programmers\심동근\250305\회문1.py 
2
8
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
#1 16
1
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
#2 64
'''