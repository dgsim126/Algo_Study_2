## 너무 어려워요

def factorial(k):
    factoial_n = 1
    for i in range(k, 1, -1):
        factoial_n *= i
    return factoial_n

def solution(N):
    answer = 0
    m = N // 3
    for i in range(m, -1, -1):
        rem = N - 3 * i
        if rem:
            b = rem // 2
            for j in range(b, -1, -1):
                rem_b = rem - 2 * j
                print(i, j, rem_b)
                answer += factorial(i + j + rem_b)
        else:
            answer += 1
        print(answer)
    return answer

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    answer = solution(N)
    print(f"#{test_case} {answer}")