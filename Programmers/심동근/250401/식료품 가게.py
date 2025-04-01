'''
제한시간 3초
맨 앞에서 값을 빼서 정가를 구한 후, 그 정가가 lst안에 있는지 확인하는 방식이 시간 내 가능한가?

lst의 최대 길이==200,
40000번? 연산도 진행하면 80000 절대 3억번 연산까지 도달 x
'''
from collections import deque

def solution(N, lst):
    lst= deque(lst)
    result= []

    len_= len(lst)//2
    cnt= 0
    while(cnt<len_):
        # print(lst, cnt)
        current= lst.popleft()
        if(current==0):
            continue
        cnt+=1
        cal_value= current*4//3
        for i in range(len(lst)):
            if(lst[i]==cal_value):
                lst[i]=0
                result.append(current)
                break # break 안 넣어서 틀림(다른 값들도 0으로 바꾸고 있었음)
                # print(result)
                # print()
    return sorted(result)

## main ##
# N= 3
# lst= [75, 100]
# print(solution(N, lst))
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= list(map(int, input().split()))
    result= solution(N, lst)
    print(f"#{test_case}", *result)
