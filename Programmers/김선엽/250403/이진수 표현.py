def solution(N, M):
    binary_ = bin(M)[2:]
    length = len(binary_)

    print(binary_)

    if N > length:
        return False
    
    binary_ = list(binary_)[-N:]

    print(binary_)

    if "1" not in binary_:
        print(1)
        return False
    else:
        if len(set(binary_)) != 1:
            print(2)
            return False
    
    return True

print(solution(5, 62))