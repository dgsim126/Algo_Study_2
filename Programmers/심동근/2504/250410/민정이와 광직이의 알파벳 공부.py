'''
모든 조합을 전부 만들어본다.(N의 최대는 15이기에)
각 조합마다 모든 알파벳을 set에 넣어 set의 size가 26인지 확인
'''

from itertools import combinations

def solution(N, lst):
    result= 0

    for i in range(1, N+1):
        for comb in combinations(lst, i):
            set_= set()
            for word in comb:
                set_.update(word)
            if(len(set_)==26):
                result+=1

    return result

## main ##
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N= int(input())
#     lst= []
#     for i in range(N):
#         lst.append(input())
#     print(f"#{test_case} {solution(N, lst)}")

# N= 10
# lst= ["cozy","lummox","gives","smart","squid","who","asks","for","job","pen"]
# print(solution(N, lst))