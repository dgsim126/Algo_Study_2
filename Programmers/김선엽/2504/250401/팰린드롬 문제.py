from itertools import permutations

def solution(strings):
    for i in range(len(strings), 0, -1):
        for comb in permutations(strings, i):
            string = "".join(comb)
            if string == string[::-1]:
                return i
    return 0

T = int(input())
for test_case in range(1, T+1):
    N, P = map(int, input().split())
    strings= []
    for _ in range(N):
        strings.append(input())
    
    answer = solution(strings)

    print(f"#{test_case} {answer}")