from collections import deque


def isTrue(lst):
    lst= deque(lst)

    while(len(lst)>1):
        if(lst.pop()!=lst.popleft()):
            return 0

    if(len(lst)==0 or len(lst)==1):
        return 1
    return 0

def solution(N, M, lst):
    # 가로 체크
    for i in range(N):
        for j in range(0, N-M+1):
            if(isTrue(lst[i][j:j+M])==1):
                return "".join(lst[i][j:j+M])

    # 세로 체크
    for i in range(N):
        for j in range(0, N-M+1):
            temp = []
            for k in range(M):  # M칸 만큼 아래로 가면서
                temp.append(lst[j+k][i])
            if(isTrue(temp)==1):
                return "".join(temp)

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    lst= []
    for i in range(N):
        lst.append(list(input()))
    print(f"#{test_case} {solution(N, M, lst)}")
# N= 20
# M= 13
# lst= [['E', 'C', 'F', 'Q', 'B', 'K', 'S', 'Y', 'B', 'B', 'O', 'S', 'Z', 'Q', 'S', 'F', 'B', 'X', 'K', 'I'],
#       ['V', 'B', 'O', 'A', 'I', 'D', 'L', 'Y', 'E', 'X', 'Y', 'M', 'N', 'G', 'L', 'L', 'I', 'O', 'P', 'P'],
#       ['A', 'I', 'Z', 'M', 'T', 'V', 'J', 'B', 'Z', 'A', 'W', 'S', 'J', 'E', 'I', 'G', 'A', 'K', 'W', 'B'],
#       ['C', 'A', 'B', 'L', 'Q', 'K', 'M', 'R', 'F', 'N', 'B', 'I', 'N', 'N', 'Z', 'S', 'O', 'G', 'N', 'T'],
#       ['N', 'Q', 'L', 'M', 'H', 'Y', 'U', 'M', 'B', 'O', 'C', 'S', 'Z', 'W', 'I', 'O', 'B', 'I', 'N', 'M'],
#       ['Q', 'J', 'Z', 'Q', 'P', 'S', 'O', 'M', 'N', 'Q', 'E', 'L', 'B', 'P', 'L', 'V', 'X', 'N', 'R', 'N'],
#       ['R', 'H', 'M', 'D', 'W', 'P', 'B', 'H', 'D', 'A', 'M', 'W', 'R', 'O', 'U', 'F', 'T', 'P', 'Y', 'H'],
#       ['F', 'N', 'E', 'R', 'U', 'G', 'I', 'F', 'Z', 'N', 'L', 'J', 'S', 'S', 'A', 'T', 'G', 'F', 'H', 'F'],
#       ['T', 'U', 'I', 'A', 'X', 'P', 'M', 'H', 'F', 'K', 'D', 'L', 'Q', 'L', 'N', 'Y', 'Q', 'B', 'P', 'W'],
#       ['O', 'P', 'I', 'R', 'A', 'D', 'J', 'U', 'R', 'R', 'D', 'L', 'T', 'D', 'K', 'Z', 'G', 'O', 'G', 'A'],
#       ['J', 'H', 'Y', 'X', 'H', 'B', 'Q', 'T', 'L', 'M', 'M', 'H', 'O', 'O', 'O', 'H', 'M', 'M', 'L', 'T'],
#       ['X', 'X', 'C', 'N', 'J', 'G', 'T', 'X', 'X', 'K', 'U', 'C', 'V', 'O', 'U', 'Y', 'N', 'X', 'Z', 'R'],
#       ['R', 'M', 'W', 'T', 'Q', 'Q', 'F', 'H', 'Z', 'U', 'I', 'G', 'C', 'J', 'B', 'A', 'S', 'N', 'O', 'X'],
#       ['C', 'V', 'O', 'D', 'F', 'K', 'W', 'M', 'J', 'S', 'G', 'M', 'F', 'T', 'C', 'S', 'L', 'L', 'W', 'O'],
#       ['E', 'J', 'I', 'S', 'Q', 'C', 'X', 'L', 'N', 'Q', 'H', 'E', 'I', 'X', 'X', 'Z', 'S', 'G', 'K', 'G'],
#       ['K', 'G', 'V', 'F', 'J', 'L', 'N', 'N', 'B', 'T', 'V', 'X', 'J', 'L', 'F', 'X', 'P', 'O', 'Z', 'A'],
#       ['Y', 'U', 'N', 'D', 'J', 'D', 'S', 'S', 'O', 'P', 'R', 'V', 'S', 'L', 'L', 'H', 'G', 'K', 'G', 'Z'],
#       ['O', 'Z', 'V', 'T', 'W', 'R', 'Y', 'W', 'R', 'F', 'I', 'A', 'I', 'P', 'E', 'Y', 'R', 'F', 'F', 'G'],
#       ['E', 'R', 'A', 'P', 'U', 'W', 'P', 'S', 'H', 'H', 'K', 'S', 'W', 'C', 'T', 'B', 'A', 'P', 'X', 'R'],
#       ['F', 'I', 'K', 'Q', 'J', 'T', 'Q', 'D', 'Y', 'L', 'G', 'M', 'M', 'W', 'M', 'E', 'G', 'R', 'U', 'Z']]
# print(solution(N, M, lst))
