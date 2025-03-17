'''
어디서부터 시작할지 판단해야 함(요일 중)
- 1을 처음 마주한 위치부터, 마지막 1까지 가장 적은 요일을 찾자!(기각 - 잘못된 접근)

그냥 모든 위치에서 시작해서 수학식으로 계산하고 나머지만 계산하는 방식으로 구현해보자!
'''
from collections import deque


def solution(n, week):
    # 가능한 요일이 하루일 때(예외 처리)
    if(sum(week)==1):
        return ((n-1)*7)+1

    # 가능한 요일이 하루 이상일 때(모든 경우를 순회)
    week= deque(week)
    answer= 2147483647

    for i in range(7):
        print(week)
        one_week= sum(week)
        if(n>sum(week)):
            result= (n//one_week)*7
            left = n % one_week
        else:
            result=(n//one_week)
            left= one_week

        print(result, left)

        for j in range(7):
            if(left==0):
                break
            if(week[j]==1):
                left-=1
                result+=1
        print(result)
        print()

        if(answer>result):
            answer= result

        # 요일 변경
        week.append(week.popleft())
    return answer


## main ##
# T = int(input())
# for test_case in range(1, T + 1):
#     n= int(input())
#     week= list(map(int, input().split()))
#     # print(n, week)
#     print(f"#{test_case} {solution(n, week)}")

n= 2
week= [1,0,0,0,0,0,1]
print(solution(n, week))