def solution(N, A, B, C):
    count = 0
    for i in range(N):
        students = A[i]
        students -= B
        count += 1
        if students > 0:
            if students % C > 0:
                count += (students // C) + 1
            else:
                count += (students // C)

    return count

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
print(solution(N, A, B, C))