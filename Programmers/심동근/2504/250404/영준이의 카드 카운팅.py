'''
str에서 문자 3개씩 읽어서 set S,D,H,C에 넣고 13-len(set)
'''
from collections import deque

def solution(cards):
    cards= deque(cards)
    S= []
    D= []
    H= []
    C= []

    while(cards):
        kind= cards.popleft()
        value= int(cards.popleft()+cards.popleft())
        if(kind=="S"):
            S.append(value)
        elif(kind=="D"):
            D.append(value)
        elif(kind=="H"):
            H.append(value)
        else:
            C.append(value)

    if(len(S)!=len(set(S)) or len(D)!=len(set(D)) or len(H)!=len(set(H)) or len(C)!=len(set(C))):
        return "ERROR"

    return [13-len(S), 13-len(D), 13-len(H), 13-len(C)]


    # print(cards.popleft(), cards.popleft()+cards.popleft())


## main ##
T = int(input())
for test_case in range(1, T + 1):
    cards= input()
    result= solution(cards)
    if(result=="ERROR"):
        print(f"#{test_case} ERROR",)
    else:
        print(f"#{test_case}", *solution(cards))
# cards= "H02H10S11H02"
# print(solution(cards))