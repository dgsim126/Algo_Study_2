def solution(numbers, c):
    c = int(c)
    j = 0
    while c > 0:
        if j >= len(numbers):
            if c % 2 == 0:
                break
            else:
                numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        k = 0
        bigger = False
        max_ = "0"
        for i in range(j + 1, len(numbers)):
            if numbers[j] < numbers[i] and numbers[i] >= max_:
                max_ = numbers[i]
                k = i
                bigger = True
        if bigger:
            numbers[j], numbers[k] = numbers[k], numbers[j]
            c -= 1
        j += 1

    return "".join(numbers)

T = int(input())
for test_case in range(1, T + 1):
    numbers, c = map(str, input().split())
    answer = solution(list(numbers), c)
    print(f"#{test_case} {answer}")