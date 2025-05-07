from collections import deque

def solution(N, K, solved):
    lst= []
    solved= deque(sorted(solved))
    # print(solved)

    for i in range(1, N+1):
        if(len(solved)!=0 and solved[0]==i):
            solved.popleft()
        else:
            lst.append(i)


    result= " ".join(map(str, lst))
    return result




## main ##
T = int(input())
for test_case in range(1, T + 1):
    N, K= map(int, input().split())
    solved= list(map(int, input().split()))
    print(f"#{test_case} {solution(N,K,solved)}")


# N= 7
# K= 2
# solved= [4, 6]
# print(solution(N, K, solved))