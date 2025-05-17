def solution(N, P):
    start = 0
    boom = False
    for i in range(1, N + 1):
        start += i
        if start == P:
            boom = True
    if boom:
        return start - 1
    else:
        return start

T = int(input())
for test_case in range(1, T+1):
    N, P = map(int, input().split())
    answer = solution(N, P)

    print(answer)