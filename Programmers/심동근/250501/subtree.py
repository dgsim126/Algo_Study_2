'''
노드 개수만큼의 리스트 생성
'''
from collections import deque


def solution(E, N, lst):
    # 0번째 인덱스 무시, 1부터 시작
    tree= [[] for _ in range(0, 1002)]

    for i in range(0, len(lst), 2):
        parent= lst[i]
        child= lst[i+1]

        tree[parent].append(child)

    cnt= 0
    queue= deque()
    queue.append(N)
    while(queue):
        parent= queue.popleft()
        cnt+=1
        # print(parent, tree[parent])

        for i in range(len(tree[parent])):
            queue.append(tree[parent][i])

    return cnt

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    E, N= map(int, input().split())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(E, N ,lst)}")
# E= 1 # 간선의 개수
# N= 1 # 해당 노드의 하위 노드 개수 구하기
# lst= [2,1]
# print(solution(E, N, lst))