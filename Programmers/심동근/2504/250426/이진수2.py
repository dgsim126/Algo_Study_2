from itertools import combinations

def solution(N):
    lst= [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625]
    flag= 0
    result_lst= []

    for i in range(1, 13):
        if(flag==1):
            break
        for comb in combinations(lst, i):
            if(sum(comb)==N):
                flag= 1
                result_lst= list(comb)
                break

    for i in range(len(lst)):
        if(lst[i] in result_lst):
            lst[i]= "1"
        else:
            lst[i]= "0"

    while(lst):
        if(lst[-1]=="0"):
            lst.pop()
        else:
            break

    if(len(lst)==0):
        return "overflow"
    else:
        return "".join(lst)

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= float(input())
    print(f"#{test_case} {solution(N)}")