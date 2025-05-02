# from collections import deque
#
# def solution(c, numbers):
#     numbers = sorted(numbers)
#     start = deque([])
#     end = deque([])
#     while c > 0:
#         if not start:
#             s = numbers.popleft()
#
def solution(dump, box):
    for j in range(dump):
        high = max(box)
        low = min(box)

        high_index = box.index(max(box))
        low_index = box.index(min(box))

        box[high_index] -= 1
        box[low_index] += 1

    return max(box) - min(box)

for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    answer = solution(dump, box)
    print(f"#{test_case} {answer}")

