'''
100개의 문자들을 조합 100C100 ~ 100C1까지
팰린드롬인지 확인할 때, 홀수 짝수를 주의해야함(양 끝부터 중간으로 모이는 방식이 더 효율적)

- 제한시간 초과

'''
from itertools import permutations


# def same(value):
#     for i in range(len(value)//2):
#         if(value[i]!=value[len(value)-1-i]):
#             return False
#     return True
#
# def solution(N, M, lst):
#     for i in range(N, 0, -1):
#         for perm in permutations(lst, i):
#             current= "".join(perm)
#             if(same(current)==True):
#                 return len(current)
#     return 0

'''
주어진 글자들의 반대가 존재하는지 확인하자!
반대가 존재한다는 말은 펠린드롬이 가능하다는 의미!

'''

from collections import deque


def same(value):
    for i in range(len(value)//2):
        if(value[i]!=value[len(value)-1-i]):
            return False
    return True

def solution(N, M, lst):
    lst= deque(lst)
    result= 0
    flag= False

    while(lst):
        value= lst.popleft()
        if(value == 0):
            continue
        reversed_value= value[::-1]


        if(flag==False):
            if(same(value)==True):
                result+=len(value)
                flag= True

        if(reversed_value in lst):
            result+=(len(value)*2)
            for i in range(len(lst)):
                if(lst[i] == reversed_value):
                    lst[i]= 0
                    break

    return result


## main ##
T = int(input())
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    lst= []
    for i in range(N):
        lst.append(input())
    print(f"#{test_case} {solution(N, M, lst)}")

# N= 3
# M= 3
# lst= ["abc",
# "ded",
# "cba"]
# print(solution(N, M, lst))