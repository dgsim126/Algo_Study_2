from itertools import combinations

def solution(n, lst):
    lst= list(lst)

    result= 0

    for comb in combinations(lst, 2):
        temp= comb[0]*comb[1]
        temp= str(temp)
        flag= True

        for i in range(len(temp)-1):
            if(int(temp[i])>int(temp[i+1])):
                # print(temp[i], temp[i+1])
                flag= False
                break

        if(flag==True):
            temp= int(temp)
            if(temp>result):
                result= temp

    if(result== 0):
        return -1

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n= int(input())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(n, lst)}")


# n= 4
# lst= [10,10,10,10]
# print(solution(n, lst))