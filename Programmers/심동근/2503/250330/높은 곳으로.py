
'''
0~1000000000층 건물
i번째에 i만큼 층수를 올라갈지 묻는다.
일단 모든 선택 상황에서 층수를 올라가면 P가 되는지 확인하고 올라가면 될 듯?

'''
def solution(N, P):
    current_floor= 0
    flag= True

    for i in range(1, N+1):
        if(current_floor+i==P):
            flag= False
            continue
        else:
            current_floor+=i

    if(flag==True):
        return current_floor
    return current_floor-1

## main ##
T = int(input())
for test_case in range(1, T + 1):
    N, P= map(int, input().split())
    print(solution(N, P))