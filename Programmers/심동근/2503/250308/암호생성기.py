'''
설마 그냥 구현 문제인가?
40을 기준으로 한 사이클이 반복된다
lst= [100,100,100,100,100,100,100,100] 일때 사이클 8번(pop, append가 40번) 일 때
기존의 값과 같은 값이 된다! -> 모든 값이 15씩 사라진 상태
0 deque([100, 100, 100, 100, 100, 100, 100, 100])
40 deque([85, 85, 85, 85, 85, 85, 85, 85])
80 deque([70, 70, 70, 70, 70, 70, 70, 70])
120 deque([55, 55, 55, 55, 55, 55, 55, 55])
160 deque([40, 40, 40, 40, 40, 40, 40, 40])
...
240 deque([10, 10, 10, 10, 10, 10, 10, 10]) 위와 같은 규칙을 발견할 수 있다!
'''
from collections import deque


def solution(lst):
    lst= deque(lst)

    min_value= min(lst)
    min_= (min_value//15)-1
    for i in range(8):
        lst[i]= lst[i]-(15*min_)
    # print(lst)



    plus= 1
    i= 1
    while(True):
        temp= lst.popleft()
        if(plus==6):
            plus=1
        temp-=plus
        if(temp<=0):
            lst.append(0)
            return (" ".join(map(str, lst)))
            # return list(lst)
        plus+=1
        lst.append(temp)
        # print(i, lst)
        i+=1


## main ##
for test_case in range(10):
    n= input()
    temp= list(map(int, input().split()))
    result= solution(temp)
    print(f"#{test_case+1} {result}")



#
# lst= [2419, 2418, 2423, 2415, 2422, 2419, 2420, 2415]
# print(solution(lst))