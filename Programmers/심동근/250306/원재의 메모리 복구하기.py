'''
초기화 상태에서 주어진 값으로 변경하기 위해 몇 번의 수정이 필요한가?
000 -> 111 -> 100
10101
00000 -> 11111 -> 10000 -> 10111 -> 10100 -> 10101
규칙을 찾으면 된다!
- 주어진 값에서 1이 나오는 시점부터 시작!(cnt+=1)
- 그 다음 인덱스의 값이 바뀌면 cnt+=1
'''
from collections import deque

def solution(value):
    value= deque(value)

    # 앞에 0 지우기
    while(value):
        if(value[0]=="1"):
            break
        else:
            value.popleft()

    # 예외처리
    if(len(value)==0):
        return 0
    if(len(value)==1 and value[0]==1):
        return 1

    result= 1
    before_value= value[0]

    # 값이 바뀌는 지점 count
    for i in range(1, len(value)):
        if(before_value!=value[i]):
            result+=1
            before_value= value[i]

    return result

## main ##
T = int(input())
for test_case in range(1, T + 1):
    value= input()
    result= solution(value)
    print(f"#{test_case} {result}")