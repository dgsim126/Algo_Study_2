'''
        부모입장: parent(n)                 자식입장: parent(n/2)

child1(n*2)      child2((n*2)+1)      child1(n)       child2(n+1)

현재 내가 찾고자 하는 위치로 접근(해당 위치가 parent)
접근 후 child1, child2 값 접근
만약 해당 위치의 값이 비어 있다면 해당 child를 parent로 두고 그 아래 child1, child2를 재귀적으로 찾아감
child에 값이 있는 지점에 도달할 때까지 쭉 내려가서 만난 모든 child의 값을 더한다.
'''
def recursive(index, graph, N):
    if(graph[index]==0):
        # print(f"index= {index}에 있는 값은 {graph[index]}!!!, {index*2}, {index*2+1}로 내려간다!")
        if((index*2)+1>N): # 오른쪽 자식이 없음
            if(index*2<=N): # 왼쪽 자식이 있음
                print(f"index= {index}에 있는 값은 {graph[index]}!!!, 왼쪽 자식{index * 2}만 내려간다!")
                return recursive(index * 2, graph, N)
            else:
                print(f"index= {index}에 있는 값은 {graph[index]}!!!, 오른쪽, 왼쪽 자식 없다!")
                return graph[index]
        else:
            print(f"index= {index}에 있는 값은 {graph[index]}!!!, {index * 2}, {index * 2 + 1}로 내려간다!")
            return recursive(index*2, graph, N) + recursive((index*2)+1, graph, N)
    else:
        print(f"index= {index}에 있는 값은 {graph[index]}!!! 이건 최종 결과물에 더해진다!")
        return graph[index]

def solution(N, M, L, lst):
    graph= [0]*(N+1) # 0번 인덱스는 무시

    for i in range(len(lst)):
        graph[lst[i][0]]= lst[i][1]

    return recursive(L, graph, N)


## main ##
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N, M, L= map(int, input().split())
#     lst= []
#     for i in range(M):
#         temp= list(map(int, input().split()))
#         lst.append(temp)
#     print(f"#{test_case} {solution(N, M, L, lst)}")
N= 10
M= 5
L= 2
# lst= [[4,1],[5,2],[3,3]]
lst= [[8,42], [9,468],[10, 335],[6,501],[7,170]]
print(solution(N, M, L, lst))