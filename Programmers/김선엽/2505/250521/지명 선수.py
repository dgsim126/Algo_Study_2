from collections import deque

def solution(N, A, B):
    members = set([i+1 for i in range(N)])
    A_mem = ["A"] * N
    i = 0
    while i < N:
        if i % 2 == 0:
            if A[0] in members:
                A_mem[A[0]-1] = "A"
                members.remove(A[0])
            else:
                A.popleft()
                continue
        else:
            if B[0] in members:
                A_mem[B[0] - 1] = "B"
                members.remove(B[0])
            else:
                B.popleft()
                continue
        i += 1

    return "".join(A_mem)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = deque(list(map(int, input().split())))
    B = deque(list(map(int, input().split())))
    answer = solution(N, A, B)
    print(answer)