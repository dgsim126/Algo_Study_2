from collections import deque

def who_win(first, second):
    if first == second:
        return 1
    elif (first == 1 and second == 3) or (first == 2 and second == 1) or (first == 3 and second == 2):
        return 1
    else:
        return 2

def solution(N, lst):
    while len(lst) > 2:
        lst = deque(lst)
        new_lst = []
        while len(lst) > 1:
            first = lst.popleft()
            second = lst.popleft()
            result = who_win(first[0], second[0])
            if result == 1:
                new_lst.append(first)
            else:
                new_lst.append(second)
        if len(lst) != 0:
            new_lst.append(lst.popleft())
        lst = new_lst[:]
    return lst[who_win(lst[0][0], lst[1][0])-1][1]

## main ##
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = []
    temp = list(map(int, input().split()))
    for i in range(N):
        lst.append([temp[i], i+1])

    print(f"#{test_case} {solution(N, lst)}")
