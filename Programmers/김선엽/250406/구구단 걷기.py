def solution(number):
    is_prime = True
    for i in range(int(number**(1/2)) + 1, 1, -1):
        if number % i == 0:
            is_prime = False
            n = i
            m = number // i
            break

    if is_prime:
        return number - 1
    else:
        return (n - 1) + (m - 1)

T = int(input())
for test_case in range(1, T+1):
    number = int(input())
    answer = solution(number)

    print(f"#{test_case} {answer}")