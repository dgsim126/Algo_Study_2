def solution(A):
    if A == 1 or A == 2 or A == 3:
        return A
    
    root_A = A ** (1/2)
    if root_A == int(root_A):
        return 1
    else:
        min = 1000000000
        for i in range(2, int(A**(1/2))+1):
            if A % i == 0:
                k = A // i
                root_k = k ** (1/2)
                root_i = i ** (1/2)
                if root_i == int(root_i):
                    if k < min:
                        min = k
                if root_k == int(root_k):
                    if i < min:
                        min = i
        if min != 1000000000:
            return min
    return A

T = int(input())
for test_case in range(1, T+1):
    A = int(input())
    answer = solution(A)
    print(f"#{test_case} {answer}")