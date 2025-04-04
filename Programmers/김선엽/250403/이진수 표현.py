def solution(N, M):
    binary_ = bin(M)[2:]
    length = len(binary_)

    if N > length:
        return False
    
    binary_ = list(binary_)[-N:]

    if "1" not in binary_:
        return False
    else:
        if len(set(binary_)) != 1:
            return False
    
    return True

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    if solution(N, M):
        print(f"#{test_case} ON")
    else:
        print(f"#{test_case} OFF")