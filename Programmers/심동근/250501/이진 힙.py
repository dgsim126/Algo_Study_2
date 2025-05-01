'''
이진 힙을 구현하라는 문제인가?
포인터 없이 이진힙 구현은 불가능하지 않나?
heapq로 되나? heapq로 부모 노드를 확인할 수 있나?
'''

# import heapq
#
# def solution(N, lst):
#     heap= []
#     heapq.heapify(heap)
#
#     for i in range(len(lst)):
#         heapq.heappush(heap, lst[i])
#
#     print(heapq))
#
#
#
# ## main ##
# N= 6
# lst= [7,2,5,3,4,6]
# print(solution(N, lst))

def solution(N, nums):
    def insert(heap, value):
        heap.append(value)
        idx = len(heap) - 1
        while idx > 1 and heap[idx] < heap[idx // 2]:
            heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
            idx //= 2

    def ancestor_sum(heap, index):
        total = 0
        while index > 1:
            index //= 2
            total += heap[index]
        return total

    heap = [0]  # 1번 인덱스부터 시작
    for num in nums:
        insert(heap, num)

    return ancestor_sum(heap, len(heap) - 1)


# 입력 처리
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = solution(N, nums)
    print(f"#{t} {result}")


