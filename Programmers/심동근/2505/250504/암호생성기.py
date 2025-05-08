from collections import deque

def solution(lst):
    lst= deque(lst)

    min_value= min(lst)
    min_= (min_value//15)-1
    for i in range(8):
        lst[i]= lst[i]-(15*min_)

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