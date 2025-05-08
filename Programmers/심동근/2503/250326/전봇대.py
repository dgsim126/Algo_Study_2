'''
 전선의 개수가 1000개까지 가능
 전선의 높이는 10000까지, 2초 내

 A가 작은 순서대로 정렬하고, 현 위치에서 뒤에 위치들을 확인하며 내 범위 내 포함되는지 확인
 이때, [1,10]의 범위에 [1,n], [n,10]은 포함되지 않는다는 것을 기억할 것
'''

def solution(N, lst):
    result= 0

    lst= sorted(lst, key= lambda x : x[0])
    print(lst)

    for i in range(N):
        for j in range(i+1, N):
            print(lst[i][0], lst[i][1], lst[j][0], lst[j][1])
            # if(lst[i][1]<lst[j][0]): # 문제 조건 좀 잘 읽자 (1 ≤ Ai, Bi ≤ 10000)
                # break
            if(lst[i][1]>lst[j][1]):
                result+=1

    return result



## main ##
T = int(input())
for test_case in range(1, T + 1):
    N= int(input())
    lst= []
    for i in range(N):
        left, right= map(int, input().split())
        lst.append([left, right])
    print(f"#{test_case} {solution(N, lst)}")


# N= 4
# lst= [[1, 10], [1, 10], [1, 10], [1, 10]]
# print(solution(N, lst))