def solution(n, m):
    a, b = 0, 0
    if n % 2 == 0:
        b = n // 2
    else:
        a = 1
        b = (n-1) // 2
    
    while a + b != m:
        b -= 1
        a += 2
    
    return a, b

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    a, b = solution(n, m)

    print(f"#{test_case} {a} {b}")