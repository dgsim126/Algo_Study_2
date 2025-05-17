from collections import deque

def winner(queue):
    if len(queue) > 2:
        lst1 = queue[:int(len(queue)+1/2)]
        lst2 = queue[int(len(queue)+1/2):]

    elif len(queue) == 1:
        return queue
    
    else:
        if queue[0][1] == queue[1][1]:
            return queue[0]
        elif queue[0][1] == queue[1][1] + 1:



# def solution(cards):
#     queue = deque([])
#     for i in range(len(cards)):
#         queue.append([i, cards[i]])
    
#     winner(queue)

        



T = int(input())
for test_case in range(1, T+1):
    cards = list(map(int, input().split()))
    answer = solution(cards)

    print(f"#{test_case} {answer}")