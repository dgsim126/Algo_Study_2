import heapq

def solution(N, lst):
    min_heap= []
    max_heap= []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    for i in range(len(lst)):
        heapq.heappush(min_heap, lst[i])
        heapq.heappush(max_heap, -lst[i])

    return -(heapq.heappop(max_heap))-(heapq.heappop(min_heap))

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, lst)}")