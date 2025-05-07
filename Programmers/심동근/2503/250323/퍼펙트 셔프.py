'''
홀수일 때 예외처리 조심
cards를 두 개의 lst로 분리 -> (홀수인 경우 왼쪽이 하나 더 많도록 분리)
왼쪽부터 하나씩 새로운 리스트에 넣기
'''
from collections import deque
def solution(times, cards):
    cards_len= len(cards)
    if(cards_len%2==0):
        slice_point= len(cards)//2
    else:
        slice_point= len(cards)// 2  +1
    result= []

    for _ in range(times):

        left= deque(cards[0:slice_point])
        right= deque(cards[slice_point:])


        temp= []
        for i in range(len(left)):
            temp.append(left.popleft())
            if(right):
                temp.append(right.popleft())

        result= temp

    return " ".join(map(str, result))





## main ##
T = int(input())
for test_case in range(1, T + 1):
    times= int(input())
    cards= list(map(str, input().split()))
    print(f"#{test_case} {solution(times, cards)}")
# times= 6
# cards= ["A", "B", "C", "D", "E", "F"]
# print(solution(times, cards))