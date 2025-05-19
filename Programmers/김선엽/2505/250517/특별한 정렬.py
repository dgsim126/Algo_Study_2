from collections import deque

def solution(N, numbers):
    numbers = deque(sorted(numbers))
    special_sort = []
    for i in range(N):
        if i % 2 == 0:
            special_sort.append(numbers.pop())
        else:
            special_sort.append(numbers.popleft())
    return special_sort[:10]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = solution(N, numbers)
    print(f"#{test_case}", *answer)