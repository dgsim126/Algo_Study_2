# from collections import deque

# def solution(dump, boxes):
#     boxes = sorted(boxes, reverse=True)
#     queue = deque(boxes)

#     left = deque([])
#     left_set = set()
#     right = deque([])
#     right_set = set()

#     left.append(queue.popleft())
#     right.append(queue.pop())

#     while dump > 0:
#         if queue[0] < left[-1]:
#             left[-1] -= 1
#             dump -= 1
#             continue
        
#         else:

def solution(dump, box):
    for j in range(dump):
        high = max(box)
        low = min(box)

        high_index = box.index(max(box))
        low_index = box.index(min(box))
        
        box[high_index] -= 1
        box[low_index] += 1

    return max(box) - min(box)


numbers = [
    42, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 
    92, 5, 3, 54, 93, 83, 22, 17, 19, 96, 48, 27, 72, 39, 70, 13, 68, 100, 36, 95, 
    4, 12, 23, 34, 74, 65, 42, 12, 54, 69, 48, 45, 63, 58, 38, 60, 24, 42, 30, 79, 
    17, 36, 91, 43, 89, 7, 41, 43, 65, 49, 47, 6, 91, 30, 71, 51, 7, 2, 94, 49, 30, 
    24, 85, 55, 57, 41, 67, 77, 32, 9, 45, 40, 27, 24, 38, 39, 19, 83, 30, 42
]

print(solution(834, numbers))

