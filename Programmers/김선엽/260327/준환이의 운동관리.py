def solution(L, U, X):
    if X < L:
        return (L - X)
    elif L <= X <= U:
        return 0
    else:
        return -1
    
T = int(input())
for test_case in range(1, T+1):
    L, U, X = map(int, input().split())
    answer = solution(L, U, X)

    print(f"#{test_case} {answer}")