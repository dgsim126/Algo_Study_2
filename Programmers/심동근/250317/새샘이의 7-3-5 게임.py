'''
5번째로 큰 수 만들기
모든 경우의 수를 다 구하면 35?

'''

from itertools import combinations

def solution(lst):
    result= []

    for comb in combinations(lst,3):
        result.append(sum(comb))

    result= list(set(result))
    result.sort(reverse=True)

    return result[4]





## main ##
T = int(input())
for test_case in range(1, T + 1):
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(lst)}")


# lst= [1,2,3,4,5,6,7]
# print(solution(lst))