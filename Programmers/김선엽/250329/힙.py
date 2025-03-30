import heapq

def solution(n, heap):
    values = [1, 2, 3, 4, 5]
    heap = []
    max_heap = []

    for value in heap:
        if len(value) == 2:
            heapq.heappush(heap, -value)
        else:
            if heap:
                return -heapq.heappop(heap)
            else:
                return -1