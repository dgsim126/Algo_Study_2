def solution(a, b):
    answer = 0
    for i in range(a+1, b):
        if i <= 3:
            answer += i
            continue
        else:
            is_prime = True
            if i % 2 == 0:
                continue
            for j in range(2, int(i**(1/2)) + 1):
                if i % j == 0:
                    is_prime = False
                    break   ## ㅇㅇ
            if is_prime:
                answer += i

    return answer

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    answer = solution(a, b)
    print(f"#{test_case} {answer}")