from collections import deque

def solution(N, original, M, command):
    i = 0
    while M > 0:
        M -= 1
        to = int(command[i+1])
        num = int(command[i+2])
        original = original[0:to] + command[i+3:i+3+num] + original[to:]
        i += 3 + int(num)

    return original[:10]

for test_case in range(1, 11):
    N = int(input())
    original = list(map(str, input().split()))
    M = int(input())
    command = list(map(str, input().split()))

    modified = solution(N, original, M, command)

    print(f"#{test_case}", *modified)