'''
간단한 문제
받은 자연수 N을 리스트로 나눠 순열을 구한다.
구한 순열 중 맨 앞이 0으로 시작하는 것들을 제외하고 하나씩 N으로 나눠보며 나머지가 없는지 확읺하면 된다
'''
from itertools import permutations

def solution(N):
    lst= list(str(N))

    for perm in permutations(lst, len(lst)):
        if(perm[0]=="0"):
            continue
        value= int("".join(perm))
        if(value>N and value%N==0):
            return "possible"

    return "impossible"

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    print(f"#{test_case} {solution(N)}")
# N= 1035
# print(solution(N))