'''
# == 검정   . == 흰색   ? == 흰색, 검은색
인접하는 두 칸의 색이 항상 다르게 하는 것이 가능한지(무조건 체스판이 되어야 함)
-> 체스판이 아니고 가능한 경우가 있나???
  없다! 판 안을 전부 무언가로 채우려면 체스판 형태가 아니고서는 불가능!
그렇다면 내가 확인할 것은 안에는 채워넣는 것에 초점을 맞추는 것이 아니라
현재 주어진 상태가 엇갈려 있는 상태인지만 확인하면 된다


73개 중 70개 성공.. 이유 모르겠음
'''
from collections import deque


def solution(N, M, lst):
    sshop= []
    ddot= []
    for i in range(N):
        for j in range(M):
            if(lst[i][j]=="#"):
                sshop.append([i,j])
            elif(lst[i][j]=="."):
                ddot.append([i,j])

    ssshop= sshop[:]
    dddot= ddot[:]

    ## 예외처리
    if(len(sshop)==1 and len(ddot)==0):
        return "possible"
    elif(len(sshop)==0 and len(ddot)==1):
        return "possible"




    '''
    sshop의 유효성 검사
    1. sshop에서 맨 앞 값을 뺀다.
    2. 뺀 값의 인덱스를 저장해둔다. 
    3. 그 다음값을 빼고, 인덱스를 살핀다.
    4. i값이 얼마나 차이나는지 확인한다.
    4-1. i값이 홀수만큼 차이가 나면 j를 %2한 값이 달라야 한다.
    4-2. i값이 짝수만큼 차이가 나면 j를 %2한 값이 같아야 한다.   
    '''
    sshop= deque(sshop)
    first_index= sshop.popleft()
    first_index_i= first_index[0]%2
    first_index_j= first_index[1]%2

    while(sshop):
        next_index= sshop.popleft()
        diff= next_index[0]-first_index[0]
        if(diff%2==0):
            if(first_index_j!=next_index[1]%2):
                return "impossible"
        else:
            if(first_index_j==next_index[1]%2):
                return "impossible"

    '''
    ddot의 유효성 검사
    1. ddot에서 맨 앞 값을 뺀다.
    2. 뺀 값의 인덱스를 저장해둔다. 
    3. 그 다음값을 빼고, 인덱스를 살핀다.
    4. i값이 얼마나 차이나는지 확인한다.
    4-1. i값이 홀수만큼 차이가 나면 j를 %2한 값이 달라야 한다.
    4-2. i값이 짝수만큼 차이가 나면 j를 %2한 값이 같아야 한다.   
    '''
    ddot = deque(ddot)
    first_index = ddot.popleft()
    first_index_i = first_index[0] % 2
    first_index_j = first_index[1] % 2

    while (ddot):
        next_index = ddot.popleft()
        diff = next_index[0] - first_index[0]
        if (diff % 2 == 0):
            if (first_index_j != next_index[1] % 2):
                return "impossible"
        else:
            if (first_index_j == next_index[1] % 2):
                return "impossible"

    # 예외처리
    if(len(sshop)==0 or len(ddot)==0):
        return "possible"

    '''
    sshop과 ddot이 다른 위치에 있는지 검사
    1. 둘 다 맨 앞에서 값을 꺼낸다.
    2. i값을 비교한다. 
    - i값이 같다면 j_1%2, j_2%2는 달라야 한다.
    - i값이 다르면 i_1%2, i_2%2의 값을 확인한다.
    - 두 값이 같다면 j_1%2, j_2%2는 같아야 하고, 다르다면 j_1%2, j_2%2는 다른 값이어야 한다.
    '''

    if (ssshop[0][0] == dddot[0][0]):
        if (ssshop[0][1] % 2 == dddot[0][1] % 2):
            return "impossible"
    else:
        if (ssshop[0][0] % 2 == dddot[0][0] % 2):
            if (ssshop[0][1] % 2 != dddot[0][1] % 2):
                return "impossible"
        else:
            if (ssshop[0][1] % 2 == dddot[0][1] % 2):
                return "impossible"

    return "possible"

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    lst= []
    for i in range(N):
        lst.append(input())
    print(f"#{test_case} {solution(N, M, lst)}")
# N= 1 # 높이
# M= 6 # 길이
# lst= ["##????"]
# print(solution(N, M, lst))