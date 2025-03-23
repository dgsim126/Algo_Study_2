# from collections import deque

# def solution(num, cards):
#     queue = deque([])
#     if num % 2 == 0:
#         range_ = num // 2
#         for i in range(range_):
#             queue.append(cards[i])
#             queue.append(cards[i+range_])
#     else:
#         range_ = num // 2
#         for i in range(range_):
#             queue.append(cards[i])
#             queue.append(cards[i+range_+1])
#         queue.append(cards[range_])

#     return list(queue)

# list_ = ["ALA", "ALEX", "DR", "LORD", "AVI"]
# print(solution(6, ["A","B","C","D","E","F"]))
# print(solution(5,list_))


from collections import deque

def solution(num, cards):
    queue = deque([])
    if num % 2 == 0:
        range_ = num // 2
        for i in range(range_):
            queue.append(cards[i])
            queue.append(cards[i+range_])
    else:
        range_ = num // 2
        for i in range(range_):
            queue.append(cards[i])
            queue.append(cards[i+range_+1])
        queue.append(cards[range_])

    return list(queue)

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    cards = list(map(str, input().split()))
    answer = solution(num, cards)
    
    print(f"#{test_case}", *answer)
