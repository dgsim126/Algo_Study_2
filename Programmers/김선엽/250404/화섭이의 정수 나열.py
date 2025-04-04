def solution(n, numbers):
    for i in range(1, n+1):
        num = set()
        for j in range(n-i+1):
            cur = int("".join(numbers[j:j+i]))
            num.add(cur)

        start = 10 ** (i-1)
        if start == 1:
            start = 0
        end = int("9" * i)

        for k in range(start, end + 1):
            if k not in num:
                return k
    

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    numbers = []
    while len(numbers) < n:
        numbers += list(map(str, input().split()))

    answer = solution(n, numbers)
    
    print(f"#{test_case} {answer}")