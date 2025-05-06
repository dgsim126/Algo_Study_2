import sys
sys.stdin = open("data/GNS_test_input (1).txt", "r")

def solution(M, numbers):
    answer = []
    sorted_num = {
        "ZRO": 0,
        "ONE": 0,
        "TWO": 0,
        "THR": 0,
        "FOR": 0,
        "FIV": 0,
        "SIX": 0,
        "SVN": 0,
        "EGT": 0,
        "NIN": 0
    }
    for number in numbers:
        sorted_num[number] += 1
    for key, value in sorted_num.items():
        answer.extend([key] * value)
    # print(answer)
    return answer

T = int(input())
for test_case in range(1, T+1):
    N, M = map(str, input().split())
    numbers = list(map(str, input().split()))
    answer = solution(int(M), numbers)

    print(f"{N}", *answer)