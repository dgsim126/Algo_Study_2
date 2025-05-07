from collections import deque


def solution(word):
    head= deque()
    tail= deque(word)
    head.append(tail.popleft())

    while(tail):
        if(len(head)>0 and head[-1]==tail[0]):
            head.pop()
            tail.popleft()
        else:
            head.append(tail.popleft())

    return len(head)

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word= input()
    print(f"#{test_case} {solution(word)}")

# word= "AAAA"
# print(solution(word))