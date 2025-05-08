def solution(N):
    if N == 1:
        return 5
    
    piece = 0
    for i in range(N-1, 1, -1):
        for j in range(1, i):
            if (i**2 + j**2) <= N**2:
                piece += 1
            else:
                break
    
    space = 0
    for i in range(1, N):
        if 2 * (i**2) <= N**2:
            space += 1
        else:
            break
    
    return 4 * N + 4 * space + 8 * piece + 1

print(solution(1))
print(solution(10))
print(solution(100))