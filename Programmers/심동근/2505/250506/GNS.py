def solution(N, lst):
    order= ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dic= {}

    for i in range(len(order)):
        dic[order[i]]= 0

    for i in range(len(lst)):
        dic[lst[i]]+=1

    result= ""

    for i in range(len(order)):
        for key, value in dic.items():
            if(order[i]==key):
                result+= (" "+order[i])*value

    return result[1:]


## main ##
T = int(input())
for test_case in range(1, T + 1):
    garbage, N= input().split()
    N= int(N)
    lst= list(map(str, input().split()))
    # print(solution(N, lst))
    print(f"#{test_case}")
    result= solution(N, lst)
    print(result)
