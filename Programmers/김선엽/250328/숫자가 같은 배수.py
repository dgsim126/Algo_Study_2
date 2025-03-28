from itertools import permutations

def solution(number):
    num = int(number)
    length = len(number)
    for comb in permutations(number, length):
        cur = int("".join(comb))
        if cur > num and cur % num == 0:
            return 1
    return 0

T = int(input())
for test_case in range(1, T+1):
    number = input()
    answer = solution(number)
    if answer:
        print(f"#{test_case} possible")
    else:
        print(f"#{test_case} impossible")