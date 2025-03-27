
def solution(N, lst):
    number= [[0,"ZRO", 0], [0,"ONE", 1], [0,"TWO", 2], [0,"THR",3 ], [0,"FOR", 4], [0,"FIV", 5], [0,"SIX", 6], [0,"SVN", 7], [0,"EGT", 8], [0,"NIN", 9]]

    for i in range(len(number)):

        for j in range(len(lst)):
            if(number[i][1]==lst[j]):
                number[i][0]+=1

    # number= sorted(number, key= lambda x: (-x[0], x[2]))

    # print(number)

    result= []
    for i in range(len(number)):
        for j in range(number[i][0]):
            result.append(number[i][1])

    # print(result)
    return result


## main ##
T = int(input())
for test_case in range(1, T + 1):
    garbage, N= input().split()
    N= int(N)
    lst= list(map(str, input().split()))
    # print(solution(N, lst))
    print(f"#{test_case}")
    result= solution(N, lst)
    print(*result)