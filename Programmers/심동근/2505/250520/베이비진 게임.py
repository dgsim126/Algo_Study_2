'''
run= 연속인 숫자가 3개 이상
triplet= 같은 숫자가 3개 이상

12개의 카드를 모두 확인했을 떄, 둘 다 run, triplet이 없다면 무승부
'''

def check_same(lst):
    if(len(lst)>=3):
        for i in range(0, len(lst) - 2):
            if (lst[i]==lst[i+1] and lst[i]==lst[i+2]):
                return True
    return False

def check_asc(lst):
    lst= set(lst) # 해당 부분 안 넣어서 틀림. 1 1 2 2 3 3 인 경우 asc이 아니라고 판단하는 문제
    lst= list(lst)
    if(len(lst)>=3):
        for i in range(0, len(lst)-2):
            if(lst[i]+1==lst[i+1] and lst[i]+2==lst[i+2]):
                return True
    return False

def solution(cards):
    A= []
    B= []

    for i in range(0, len(cards), 2):
        A.append(cards[i])
        B.append(cards[i+1])

        if(len(A)>=3):
            A.sort()
            B.sort()
            if(check_asc(A)==True):
                return 1
            if(check_same(A)==True):
                return 1
            if(check_asc(B)==True):
                return 2
            if(check_same(B)==True):
                return 2
    return 0

## main ##
T = int(input())
for test_case in range(1, T + 1):
    cards= list(map(int, input().split()))
    print(f"#{test_case} {solution(cards)}")
