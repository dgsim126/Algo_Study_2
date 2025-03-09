from collections import deque

def solution(password):
    min_num = min(password)
    minus = (min_num // 15) * 15

    password = deque(password)

    is_end = False
    for i in range(len(password)):
        password[i] -= minus

    num = 1
    index = 0
    while not is_end:
        cur = password.popleft()
        cur -= num

        if num >= 5:
            num = 1
        else:
            num += 1
        
        if cur <= 0:
            cur = 0
            is_end = True

        password.append(cur)
    

    print(*password)


solution([9550,9556,9550,9553,9558,9551,9551,9551])

from collections import deque

for test_case in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))
    
    min_num = min(password)
    minus = (min_num // 15) * 15

    if min_num == minus:
        minus = minus - 15

    password = deque(password)

    is_end = False
    for i in range(len(password)):
        password[i] -= minus

    num = 1
    index = 0
    while not is_end:
        cur = password.popleft()
        cur -= num

        if num >= 5:
            num = 1
        else:
            num += 1
        
        if cur <= 0:
            cur = 0
            is_end = True

        password.append(cur)

    print(f"#{test_case}", *password)