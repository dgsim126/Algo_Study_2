
def solution(N, lst):
    result= [0]*10

    for i in range(len(lst)):
        temp= int(lst[i])
        result[temp]+=1

    max_val= max(result)
    # print(result)

    for i in range(len(result)-1, -1, -1):
        # print(i)
        if(result[i]==max_val):
            max_val= i
            break # break 없어서 한 번 틀림

    return max_val, result[max_val]

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= input()
    print(f"#{test_case}", *solution(N, lst))
# N= 10
# lst= "01234560990"
# print(solution(N, lst))