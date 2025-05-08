import sys
sys.stdin = open("data/pass.txt", "r")

def solution(N, original, M, command):
    i = 0
    while M > 0:
        # print(original)
        M -= 1
        if command[i] == "I":
            to = int(command[i+1])
            num = int(command[i+2])
            original = original[0:to] + command[i+3:i+3+num] + original[to:]
            i += 3 + num
        elif command[i] == "D":    ## x 위치 바로 다음부터...
            to = int(command[i+1])
            num = int(command[i+2])
            if to + num >= len(original):
                original = original[0:to]
            else:
                original = original[0:to] + original[to+num:]
            i += 3
        elif command[i] == "A":
            num = int(command[i+1])
            s = command[i+2:i+2+num]
            original.extend(s)
            i += 2 + num


    return original[:10]

for test_case in range(1, 11):
    N = int(input())
    original = list(map(str, input().split()))
    M = int(input())
    command = list(map(str, input().split()))
    answer = solution(N, original, M, command)
    print(f"#{test_case}", *answer)